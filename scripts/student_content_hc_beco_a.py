"""Biología de los ecosistemas (electivo 3.º y 4.º medio HC): OAC-01 (estado de la biodiversidad, clases 1 a 4) y OAC-02 (biodiversidad, funcionamiento y servicios, clases 1 a 5)."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz y cuaderno. Todos los datos, tablas y casos son de ejemplo (rotulados así) y están escritos completos en el enunciado: no necesitas salida a terreno, laboratorio ni internet. "
             "Este cuaderno no propone recolectar, manipular ni capturar seres vivos: las observaciones que se analizan se entregan ya escritas. Si quieres observar un ecosistema real, hazlo solo desde un sendero o una plaza, sin tocar ni sacar organismos, con una persona adulta y respetando la normativa del lugar. "
             "Las cifras son inventadas para practicar el razonamiento y no describen un lugar real; las fechas se dan solo cuando son bien conocidas.")
build = make_build(MATERIALS)

O1 = "CN-BECO-3y4-OAC-01"
O2 = "CN-BECO-3y4-OAC-02"

# ============================================================ OAC-01, clase 1
F = ("Ficha 1 (datos de ejemplo). Dos terrenos de igual tamaño. Terreno A, un bosque: 30 especies de plantas y 12 de aves; las aves de una de esas especies forman dos poblaciones con variantes genéticas distintas entre sí. "
     "Terreno B, un cultivo de un solo tipo de planta: 1 especie de planta y 3 de aves.")
build(
    O1, 1, F,
    use="Aprenderé a delimitar una pregunta sobre el estado de la biodiversidad: qué se mide, en qué lugar y a qué nivel. Sirve para que una afirmación sobre «pérdida de biodiversidad» se pueda comprobar con datos.",
    prior=["Sé qué es una especie y qué es un ecosistema.", "Sé leer una tabla o una lista de datos.", "Distingo una observación de una conclusión."],
    explain=[
        "La biodiversidad es la variedad de la vida y se estudia en tres niveles. La diversidad genética es la variación de genes dentro de una especie. La diversidad de especies es cuántas especies distintas hay en un lugar, a lo que se llama riqueza de especies. La diversidad de ecosistemas es la variedad de ambientes, como bosques, humedales o desiertos, y de las relaciones entre sus seres vivos y su entorno.",
        "Para decir cuál es el «estado» de la biodiversidad hay que medirla. Para eso se delimita el sistema, es decir, la parte de la realidad que se estudia: un lugar concreto, un grupo de organismos y un período. Sin esos límites, una frase como «la biodiversidad está bien» o «está mal» no se puede comprobar, porque no dice de qué lugar, de qué grupo ni de qué fecha habla.",
        "Una buena pregunta nombra el nivel, el grupo, el lugar y el tiempo. Por ejemplo: «¿cambió el número de especies de aves de un valle entre dos conteos hechos con el mismo método?». Con datos de ejemplo se puede responder; en cambio, «¿qué pasa con la naturaleza?» es demasiado amplia. Además, hay que separar lo que los datos muestran de lo que se supone: un solo conteo no permite hablar de una tendencia.",
    ],
    vocab=[("biodiversidad", "variedad de la vida en sus niveles de genes, especies y ecosistemas"), ("riqueza de especies", "número de especies distintas de un lugar"), ("diversidad genética", "variación de genes dentro de una especie"), ("sistema", "parte de la realidad que se delimita para estudiarla"), ("tendencia", "dirección en que cambia un dato al comparar varios momentos")],
    worked=[
        ("Identificar el nivel", "Un equipo cuenta cuántas especies de mariposas hay en una quebrada de ejemplo. ¿Qué nivel de biodiversidad mide?",
         ["Pregunta: ¿cuenta genes, especies o ambientes?", "Cuenta especies distintas de un grupo, las mariposas.", "Eso es riqueza de especies."],
         "Diversidad de especies"),
        ("Delimitar una pregunta", "¿Cuál pregunta está mejor delimitada: «¿cómo está la naturaleza?» o «¿cambió la riqueza de especies de anfibios de una laguna entre el primer y el segundo conteo?»",
         ["La primera no nombra nivel, grupo, lugar ni tiempo.", "La segunda nombra el nivel (especies), el grupo (anfibios), el lugar (la laguna) y dos momentos.", "La segunda se puede responder con dos conteos."],
         "La segunda pregunta"),
    ],
    mistakes=[("Creer que biodiversidad es solo «muchos animales».", "La biodiversidad incluye plantas, hongos, microorganismos y también la variación genética y la de ecosistemas.", "Nombra siempre el nivel que mides: genes, especies o ecosistemas."),
              ("Concluir sobre un lugar entero a partir de un solo conteo en un día.", "Un conteo es una foto de un momento y no muestra una tendencia.", "Pide al menos dos conteos hechos con el mismo método para hablar de cambio.")],
    T=[
        ("abc", "En Biología de los ecosistemas: ¿qué incluye la biodiversidad?", "La variedad de la vida en sus niveles de genes, especies y ecosistemas", "Solo el número de animales de un lugar", "Solo las especies que están en peligro", "La biodiversidad abarca tres niveles y no se reduce a contar animales ni a las especies amenazadas."),
        ("{F} ¿Qué terreno, A o B, tiene mayor riqueza de especies de plantas?", "A", "El terreno A tiene 30 especies de plantas y el B solo 1, así que A tiene mayor riqueza."),
        ("=", "{F} ¿Cuántas especies de plantas y aves hay en total en el terreno A?", "30+12", "La riqueza total suma las 30 especies de plantas y las 12 de aves del terreno A.", " especies"),
        ("abc", "{F} Las dos poblaciones de aves del terreno A con variantes genéticas distintas son un ejemplo de diversidad…", "genética", "de especies", "de ecosistemas", "Es variación de genes dentro de una misma especie, lo que se llama diversidad genética."),
        ("ab", "{F} ¿Por qué el terreno B tiene menos biodiversidad que el A?", "Porque tiene muchas menos especies de plantas y de aves", "Porque sus especies son menos útiles para las personas", "La comparación de la ficha se basa en el número de especies, no en su utilidad."),
        ("abc", "Se compara un humedal con un bosque de una misma región. ¿Qué nivel de biodiversidad se está comparando?", "La diversidad de ecosistemas", "La diversidad genética", "El tamaño de una población", "Comparar ambientes distintos corresponde al nivel de ecosistemas."),
        ("=", "{F} ¿Cuántas especies de plantas más tiene el terreno A que el B?", "30-1", "La diferencia se obtiene restando las especies de B a las de A.", " especies"),
        ("abc", "¿Cuál pregunta está mejor delimitada para estudiar el estado de la biodiversidad?", "¿Cambió el número de especies de aves de un valle entre dos conteos hechos con el mismo método?", "¿Qué pasa con la naturaleza?", "¿Es importante la biodiversidad para el planeta?", "Solo la primera nombra grupo, lugar, método y dos momentos que se pueden comparar con datos."),
        ("abc", "Un grupo quiere saber si una especie exótica cambió la biodiversidad de un humedal. ¿Qué debe delimitar primero?", "El humedal concreto, el grupo de organismos y el período de estudio", "Todos los humedales del mundo", "Solo la opinión de los vecinos", "Delimitar es acotar lugar, grupo y tiempo para poder medir y comparar."),
        ("abc", "Un equipo cuenta especies y otro compara genes de una sola especie. ¿Por qué no deberían mezclar sus resultados como si midieran lo mismo?", "Porque miden niveles distintos de la biodiversidad: especies y genes", "Porque uno de los dos equipos se equivoca siempre", "Porque los genes no forman parte de la biodiversidad", "Cada nivel responde una pregunta distinta y sus datos no son intercambiables."),
        ("ab", "{F} Una estudiante dice: «con estos datos A siempre será más biodiverso que B». ¿Qué es lo más prudente?", "Decir que, con estos datos de ejemplo, A tiene hoy mayor riqueza y que faltan otros conteos para hablar de tendencia", "Afirmar que A mantendrá siempre su ventaja", "Los datos son de un momento y solo permiten comparar ese momento."),
        ("abc", "Se quiere responder «¿cómo cambió la biodiversidad de un valle?». ¿Qué mejora más esa pregunta?", "Precisar el nivel, el grupo, la zona y los años que se comparan", "Agregar la palabra «urgente»", "Cambiar «valle» por «mundo»", "Una pregunta mejora cuando se puede responder con datos concretos."),
        ("Ordena de menor a mayor alcance: (a) una población de una especie de ave de un bosque, (b) el bosque completo con todos sus seres vivos, (c) un gen de esa ave. Escribe las letras separadas por comas.", "c, a, b", "Un gen es parte de un individuo, la población reúne individuos de una especie y el bosque reúne muchas especies y su ambiente."),
    ],
    ctx=("abc", "Contexto: en tu liceo se discute si el humedal cercano «ha perdido biodiversidad». Te piden proponer cómo averiguarlo. ¿Cuál propuesta es mejor?", "Contar las especies de aves del humedal en dos fechas con el mismo método y comparar", "Preguntar a cada persona si cree que hay menos aves", "Buscar una sola fotografía del humedal", "Dos conteos con el mismo método permiten comparar con datos y no con impresiones."),
    sc=[
        ("En Biología de los ecosistemas: ¿qué es la riqueza de especies?", "El número de especies distintas de un lugar", "La riqueza cuenta especies distintas y no individuos."),
        ("ab", "Para hablar de una tendencia hacen falta:", "Al menos dos mediciones comparables", "Una sola medición muy cuidadosa", "Una tendencia es un cambio en el tiempo y exige comparar momentos."),
        ("ab", "Una pregunta bien delimitada:", "Nombra el nivel, el grupo, el lugar y el tiempo", "Es tan amplia que sirve para todo", "Al acotar se puede responder con datos concretos."),
    ],
    op=("Con los datos de la ficha {F}: (1) escribe una pregunta bien delimitada que se pueda responder con esos datos; (2) indica qué nivel de biodiversidad mide; (3) escribe una limitación de los datos, es decir, algo que no permiten concluir.",
        "(1) ¿Tiene el terreno A mayor riqueza de especies de plantas que el B? (2) Diversidad de especies. (3) Son datos de un solo conteo, así que no muestran si la riqueza cambia en el tiempo.",
        ["pregunta con nivel, grupo y lugar", "nivel de biodiversidad correcto", "limitación coherente con los datos"],
        ["tres respuestas numeradas"],
        ["hacer una pregunta demasiado amplia", "confundir especies con genes", "no reconocer que es un solo conteo"],
        "Pregunta: «¿qué dato nuevo necesitarías para hablar de una tendencia?»."),
    reinforce="Escribe tres ejemplos, uno por cada nivel de biodiversidad (genes, especies y ecosistemas), con tus propias palabras.",
    extend="Redacta dos preguntas sobre biodiversidad, una mal delimitada y otra bien delimitada, y explica qué corregiste.",
)

# ============================================================ OAC-01, clase 2
F = ("Ficha 2 (fuentes de ejemplo sobre la evolución). Fuente 1: artículo de una revista científica con revisión de otros especialistas, sobre fósiles de un grupo de vertebrados, con el método descrito. "
     "Fuente 2: publicación anónima de una red social que dice «la evolución es solo una opinión» y no cita datos. "
     "Fuente 3: libro de texto escolar que resume la comparación del ADN de varias especies y remite a los estudios originales. "
     "Tabla de ejemplo con las diferencias entre una secuencia corta de ADN de la especie X y la misma secuencia en otras tres especies: especie P: 2 diferencias; especie Q: 9 diferencias; especie R: 15 diferencias.")
build(
    O1, 2, F,
    use="Aprenderé a evaluar fuentes y variables en la evidencia sobre el origen de la vida y la evolución. Sirve para distinguir qué fuentes son confiables y qué conclusiones permiten realmente los datos.",
    prior=["Sé qué es el ADN y que se hereda.", "Sé que las especies cambian a lo largo de muchas generaciones.", "Sé leer una tabla de ejemplo."],
    explain=[
        "La evolución es el cambio de las características hereditarias de las poblaciones a lo largo de las generaciones. Se apoya en varias líneas de evidencia: los fósiles, que muestran formas de vida del pasado; la anatomía comparada, que halla estructuras parecidas por un origen común; la biogeografía, que estudia dónde viven las especies; y la comparación del ADN y de las proteínas, donde más parecido indica un ancestro común más cercano.",
        "Sobre el origen de la vida se habla de hipótesis, porque ocurrió hace muchísimo tiempo y solo quedan pruebas indirectas, como rocas antiguas, fósiles de microorganismos y experimentos que simulan condiciones primitivas. La hipótesis de la evolución química propone que moléculas simples formaron moléculas más complejas y que, en algún momento, aparecieron sistemas capaces de copiarse. Aún quedan preguntas abiertas, y la ciencia lo reconoce.",
        "Para evaluar una fuente se revisa quién la escribe, si cita datos y método, si otros especialistas la revisaron y qué tan reciente es. Para evaluar una variable se pregunta qué se midió, con qué unidad y con qué método. Una cifra sin método ni fuente no es evidencia. Una diferencia de ADN, por ejemplo, es una variable medida; de ella se infiere el parentesco, y esa inferencia debe declararse como tal.",
    ],
    vocab=[("evolución", "cambio hereditario de las poblaciones a lo largo de las generaciones"), ("fósil", "resto o huella de un ser vivo del pasado conservado en una roca"), ("anatomía comparada", "comparación de estructuras corporales entre especies"), ("hipótesis", "explicación provisoria que se puede poner a prueba"), ("ancestro común", "especie de la que descienden dos o más especies actuales")],
    worked=[
        ("Elegir la fuente más confiable", "Con la ficha, entre la Fuente 1 y la Fuente 2, ¿cuál es más confiable para estudiar la evolución de los vertebrados y por qué?",
         ["Se revisa si cada fuente cita datos y método.", "La Fuente 1 describe su método y fue revisada por otros especialistas.", "La Fuente 2 es anónima y no cita datos."],
         "La Fuente 1, porque entrega datos y método revisables"),
        ("Inferir con cuidado", "En una tabla de ejemplo, la especie M tiene 4 diferencias de ADN con la especie X y la especie N tiene 11. ¿Con cuál se infiere un ancestro común más cercano?",
         ["Menos diferencias de ADN indican mayor parecido.", "Mayor parecido sugiere un ancestro común más cercano.", "4 es menor que 11, así que corresponde a la especie M."],
         "La especie M"),
    ],
    mistakes=[("Pensar que «hipótesis» significa «idea sin respaldo».", "En ciencia una hipótesis es una explicación provisoria que se pone a prueba con evidencia.", "Di «hipótesis apoyada por evidencia indirecta», no «adivinanza»."),
              ("Dar por probado un parentesco con una sola secuencia corta de ADN.", "Una secuencia pequeña entrega un indicio; las conclusiones sólidas combinan varias líneas de evidencia.", "Cruza ADN con fósiles, anatomía y distribución geográfica.")],
    T=[
        ("abc", "En Biología de los ecosistemas: ¿qué es un fósil?", "Un resto o huella de un ser vivo del pasado conservado en una roca", "Un animal actual muy parecido a otro extinguido", "Una roca con forma de animal sin relación con la vida", "Un fósil es evidencia directa de vida pasada, no un animal actual ni una roca cualquiera."),
        ("{F} ¿Cuál fuente (1, 2 o 3) no cita datos?", "La Fuente 2", "La Fuente 2 es una publicación anónima que no presenta datos ni método."),
        ("{F} ¿Qué especie (P, Q o R) tiene menos diferencias de ADN con la especie X?", "P", "La especie P tiene solo 2 diferencias, menos que Q con 9 y R con 15."),
        ("abc", "{F} Comparada con la especie Q, ¿cómo se parece la especie R a la especie X en esa secuencia de ADN?", "Se parece menos, porque tiene más diferencias (15 contra 9)", "Se parece más, porque 15 es un número mayor", "Se parece igual, porque ambas son distintas de X", "Más diferencias en la secuencia significa menor parecido."),
        ("ab", "{F} ¿Por qué la Fuente 1 es más confiable que la Fuente 2?", "Porque describe su método y fue revisada por otros especialistas", "Porque es más larga que la otra", "Lo que da confiabilidad es el método revisable y los datos citados, no la extensión."),
        ("abc", "¿Qué tipo de evidencia es comparar los huesos de la extremidad delantera de varias especies de vertebrados?", "Anatomía comparada", "Biogeografía", "Datación de rocas", "Comparar estructuras corporales entre especies es anatomía comparada."),
        ("=", "{F} ¿Cuántas diferencias de ADN suman en total las tres especies comparadas?", "2+9+15", "El total suma las diferencias de P, Q y R respecto de la especie X.", " diferencias"),
        ("=", "{F} ¿Cuántas diferencias más tiene la especie R que la especie Q respecto de X?", "15-9", "Se resta lo que tiene Q a lo que tiene R para obtener la diferencia entre ambas.", " diferencias"),
        ("abc", "Un grupo estudia las especies que viven en dos islas lejanas y halla especies parecidas que no viven en el continente. ¿Qué línea de evidencia usa?", "La biogeografía, que estudia dónde viven las especies", "La anatomía comparada", "El estudio de proteínas de la sangre", "Relacionar especies con los lugares donde viven es biogeografía."),
        ("abc", "¿Por qué el origen de la vida se presenta como hipótesis y no como hecho cerrado?", "Porque ocurrió hace muchísimo tiempo y solo hay evidencia indirecta", "Porque a nadie le interesa investigarlo", "Porque ya se probó que fue imposible", "Las pruebas indirectas sostienen la hipótesis pero no la cierran del todo."),
        ("ab", "{F} Una compañera afirma: «la tabla prueba por sí sola todo el parentesco entre X, P, Q y R». ¿Qué respondes?", "Es un indicio sobre una secuencia corta; faltan otras líneas de evidencia para concluir con más fuerza", "Tiene razón, porque los números no mienten", "Una sola secuencia entrega un indicio y debe cruzarse con fósiles y anatomía."),
        ("abc", "{F} ¿Qué es lo más importante revisar de la Fuente 3 antes de usarla como evidencia?", "A qué estudios originales remite y si presenta los datos que resume", "Si tiene muchas imágenes", "Si el título está en letras grandes", "Un resumen es útil si remite a datos y estudios que se puedan revisar."),
        ("abc", "En un estudio de ejemplo se mide el ADN de dos especies con métodos distintos, uno informa 8 diferencias en una secuencia de 400 letras y otro informa 8 diferencias por cada cien letras. ¿Qué problema hay para compararlos?", "Las variables vienen en unidades distintas y hay que expresarlas igual", "Que 8 es un número demasiado pequeño", "Que se midió ADN y no proteínas", "Para comparar variables hay que usar la misma unidad y el mismo método."),
    ],
    ctx=("abc", "Contexto: un compañero te muestra un video que dice «los científicos mienten sobre la evolución» y no muestra datos. Preparas una respuesta breve. ¿Cuál es la más adecuada?", "Pedir las fuentes y los datos, y compararlos con estudios revisados por especialistas", "Aceptar el video porque tiene muchas visitas", "Descartarlo sin leer, solo porque no te gusta", "Evaluar la fuente por sus datos y método es lo que distingue evidencia de opinión."),
    sc=[
        ("En Biología de los ecosistemas: ¿qué es un ancestro común?", "Una especie de la que descienden dos o más especies actuales", "Un ancestro común explica el parecido entre especies emparentadas."),
        ("ab", "Una cifra sin método ni fuente:", "No es evidencia suficiente", "Es la mejor evidencia posible", "Sin fuente ni método no se puede revisar ni repetir."),
        ("ab", "Una hipótesis científica es:", "Una explicación provisoria que se pone a prueba", "Una idea sin ningún respaldo", "Se prueba con datos y se corrige si la evidencia lo exige."),
    ],
    op=("Con la ficha {F}: (1) ordena las tres fuentes de más a menos confiable; (2) justifica el orden con un criterio para cada una; (3) explica qué conclusión permite la tabla de ADN y qué conclusión no permite.",
        "(1) Fuente 1, Fuente 3, Fuente 2. (2) La 1 describe método y fue revisada; la 3 resume estudios; la 2 no cita datos. (3) Permite decir que P se parece más a X en esa secuencia; no permite afirmar el parentesco completo con una sola secuencia.",
        ["orden coherente con criterios", "criterio explícito por fuente", "conclusión permitida y no permitida"],
        ["tres respuestas numeradas"],
        ["ordenar sin criterio", "concluir más que lo que dicen los datos", "tratar la fuente anónima como válida"],
        "Pregunta: «¿qué otra línea de evidencia reforzaría esa conclusión?»."),
    reinforce="Haz una tabla con cuatro líneas de evidencia de la evolución (fósiles, anatomía comparada, biogeografía y ADN) y, para cada una, una frase de lo que muestra.",
    extend="Explica con un ejemplo por qué la ciencia puede decir «no lo sabemos del todo» sobre el origen de la vida y aun así tener evidencia.",
)

# ============================================================ OAC-01, clase 3
F = ("Ficha 3 (datos de ejemplo, modelo de selección). Una población de insectos de ejemplo vive en un bosque de troncos oscuros. El color es hereditario y hay insectos claros y oscuros. "
     "Generación 1: 100 insectos, 20 claros y 80 oscuros. Cada generación, las aves comen más insectos claros porque se ven más. "
     "Generación 2: 100 insectos, 10 claros y 90 oscuros. Generación 3: 100 insectos, 5 claros y 95 oscuros.")
build(
    O1, 3, F,
    use="Aprenderé a interpretar un modelo de selección natural con datos de ejemplo. Sirve para explicar cómo cambian las poblaciones y por qué la evolución no es una decisión de los individuos.",
    prior=["Sé que los rasgos se heredan.", "Sé calcular porcentajes sencillos.", "Sé qué es una población."],
    explain=[
        "La selección natural es un modelo que explica cómo cambian las poblaciones. Tiene cuatro ideas: hay variación entre los individuos; parte de esa variación es hereditaria; no todos los individuos sobreviven y se reproducen por igual; y quienes dejan más descendientes con un rasgo hacen que ese rasgo sea más frecuente en la siguiente generación. La variación nueva surge por mutaciones, que son cambios en el ADN.",
        "Un punto clave: cambia la población, no el individuo. Un insecto claro no se vuelve oscuro por necesitarlo. Lo que cambia es la proporción de insectos claros y oscuros entre generaciones, porque los claros dejan menos descendientes en ese ambiente. Un rasgo que ayuda a sobrevivir y reproducirse en un ambiente se llama adaptación. Si el ambiente cambia, el mismo rasgo puede dejar de ser ventajoso.",
        "Un modelo se evalúa por lo que supone y por cómo se compara con datos. Este supone que el color se hereda, que la presión de las aves se mantiene y que no llegan insectos de afuera. Si alguno de esos supuestos falla, la predicción cambia. Además, la selección natural no es la única causa de cambio: el azar, la llegada de individuos de otras poblaciones y las mutaciones también influyen.",
    ],
    vocab=[("selección natural", "proceso por el que los rasgos hereditarios que mejoran la supervivencia y la reproducción se hacen más frecuentes"), ("adaptación", "rasgo hereditario que ayuda a sobrevivir y reproducirse en un ambiente"), ("mutación", "cambio en el ADN que puede generar variación nueva"), ("frecuencia", "proporción de individuos que tienen un rasgo"), ("supuesto", "condición que el modelo da por cierta para funcionar")],
    worked=[
        ("Calcular una frecuencia", "En una generación de ejemplo hay 100 escarabajos, 30 con un rasgo. ¿Qué porcentaje tiene el rasgo?",
         ["Frecuencia = individuos con el rasgo ÷ total.", "30 ÷ 100 = 0,30, es decir 30 %."],
         "30 %"),
        ("Aplicar el modelo", "En un bosque de ejemplo las aves ven más fácil a los insectos verdes que a los pardos. ¿Qué se espera de la frecuencia de insectos pardos en las generaciones siguientes, si el color es hereditario?",
         ["Los pardos dejan más descendientes porque son menos comidos.", "Los descendientes heredan el color de sus padres.", "La proporción de pardos aumenta."],
         "Aumenta"),
    ],
    mistakes=[("Decir que «los insectos claros se volvieron oscuros porque lo necesitaban».", "El rasgo no cambia en el individuo; cambia la proporción en la población por reproducción diferencial.", "Explica con variación, herencia y descendencia desigual."),
              ("Creer que la selección natural «mejora» a las especies hacia un fin.", "Una adaptación es útil en un ambiente determinado y puede dejar de serlo si el ambiente cambia.", "Habla de «mejor ajustado a este ambiente», no de «más perfecto».")],
    T=[
        ("abc", "En Biología de los ecosistemas: ¿qué es una adaptación?", "Un rasgo hereditario que ayuda a sobrevivir y reproducirse en un ambiente", "Un cambio que un individuo logra esforzándose", "Un rasgo que no se hereda", "Una adaptación es hereditaria y favorece la supervivencia y reproducción en un ambiente dado."),
        ("{F} ¿Cuántos insectos claros hay en la generación 3?", "5", "La ficha indica 5 claros y 95 oscuros en la generación 3."),
        ("=", "{F} ¿Qué porcentaje de insectos claros hay en la generación 1?", "20/100*100", "El porcentaje se obtiene dividiendo los claros por el total y multiplicando por cien.", " %"),
        ("abc", "{F} ¿Qué pasó con la proporción de insectos claros entre las generaciones 1 y 3?", "Disminuyó", "Aumentó", "Se mantuvo igual", "Pasó de 20 a 5 insectos claros por cada cien, así que disminuyó."),
        ("ab", "{F} ¿Por qué los insectos claros dejan menos descendientes en este bosque?", "Porque las aves los ven más fácil y los comen antes de que se reproduzcan", "Porque los insectos claros no quieren reproducirse", "En el modelo, el color afecta la probabilidad de ser comido y de reproducirse."),
        ("=", "{F} ¿Qué porcentaje de insectos oscuros hay en la generación 2?", "90/100*100", "Es la cantidad de oscuros dividida por el total de la generación, expresada en porcentaje.", " %"),
        ("=", "{F} ¿Cuántos puntos porcentuales bajó el porcentaje de claros entre la generación 1 y la 3?", "20-5", "Se restan los porcentajes de claros de las generaciones comparadas, que coinciden con las cantidades porque el total es 100.", " puntos"),
        ("abc", "{F} Una estudiante dice que los insectos claros «se pintaron de oscuro» para sobrevivir. ¿Qué explicación del modelo corrige su idea?", "Los claros dejaron menos descendientes, así que la población tiene proporcionalmente más oscuros", "Los claros se transformaron individualmente en oscuros", "Las aves cambiaron el color de los insectos", "El modelo explica cambios en la proporción de la población, no cambios en cada individuo."),
        ("abc", "Un criadero de ejemplo hace crecer sus aves más altas con una dieta especial; sus crías no heredan esa altura. ¿Se trata de selección natural de un rasgo hereditario?", "No, porque el efecto de la dieta no es hereditario", "Sí, porque cambió la altura", "Sí, porque hubo aves más altas", "La selección natural actúa sobre rasgos hereditarios y no sobre cambios provocados por la dieta."),
        ("abc", "{F} Si de pronto los troncos del bosque se volvieran claros, ¿qué esperarías para las generaciones siguientes, según el modelo?", "Que los insectos claros dejen más descendientes que antes", "Que los insectos claros desaparezcan igual", "Que nada cambie por ser hereditario", "Si el ambiente cambia, la ventaja de un rasgo puede cambiar también."),
        ("ab", "{F} ¿Cuál es un supuesto del modelo de la ficha?", "Que la presión de las aves se mantiene igual en las tres generaciones", "Que los insectos claros no existen", "El modelo da por cierto que la presión de depredación no cambia entre generaciones."),
        ("abc", "¿Qué fuente de variación nueva entre individuos se menciona en el modelo?", "Las mutaciones", "Las aves", "El color del tronco", "Las mutaciones cambian el ADN y generan variantes nuevas heredables."),
        ("abc", "{F} En la generación 4, el recuento de ejemplo fue de 20 claros, porque llegaron insectos claros desde otro bosque. ¿Qué supuesto del modelo falló?", "Que no llegan individuos de fuera de la población", "Que el color es hereditario", "Que las aves comen insectos", "La llegada de individuos desde otra población rompe el supuesto de población cerrada."),
    ],
    ctx=("abc", "Contexto: en una exposición escolar debes explicar con un cartel por qué las bacterias de un cultivo de ejemplo llegaron a ser resistentes a un antibiótico. ¿Qué explicación elegirías?", "Algunas bacterias ya tenían una variante que les permitía sobrevivir, sobrevivieron y dejaron descendientes, y la variante se hizo más frecuente", "Las bacterias decidieron volverse resistentes", "El antibiótico transformó a todas las bacterias en resistentes", "La explicación correcta usa variación previa, supervivencia diferencial y herencia."),
    sc=[
        ("En Biología de los ecosistemas: ¿qué es una mutación?", "Un cambio en el ADN que puede generar variación nueva", "Una mutación modifica el ADN y es fuente de variación."),
        ("ab", "La selección natural cambia:", "La proporción de rasgos en la población", "El rasgo de un individuo mientras vive", "Lo que cambia entre generaciones es la proporción en la población."),
        ("ab", "Un modelo debe declarar:", "Sus supuestos", "Que siempre acierta", "Declarar supuestos permite saber cuándo falla."),
    ],
    op=("Con los datos de la ficha {F}: (1) calcula el porcentaje de insectos claros en cada generación; (2) explica en dos oraciones la tendencia usando variación, herencia y descendencia desigual; (3) indica un supuesto del modelo y qué pasaría si dejara de cumplirse.",
        "(1) 20 %, 10 % y 5 %. (2) Había insectos claros y oscuros y el color se hereda; los claros eran más comidos y dejaron menos descendientes, por eso bajó su proporción. (3) Supone que la presión de las aves es constante; si las aves dejaran de comerlos, los claros dejarían de disminuir.",
        ["tres porcentajes correctos", "explicación con variación, herencia y descendencia desigual", "supuesto y consecuencia coherentes"],
        ["tres respuestas numeradas"],
        ["decir que los individuos cambian de color", "omitir la herencia", "no relacionar el supuesto con una consecuencia"],
        "Pregunta: «¿cómo sabrías si el supuesto de la presión de las aves sigue siendo válido?»."),
    reinforce="Escribe las cuatro ideas del modelo de selección natural con un ejemplo inventado, distinto del de los insectos.",
    extend="Explica por qué «el más fuerte sobrevive» resume mal la selección natural y reescribe esa frase de forma correcta.",
)

# ============================================================ OAC-01, clase 4
F = ("Ficha 4 (datos de ejemplo de un valle ficticio). Año 1: 8 especies de aves nativas, 0 especies exóticas y 50 % de la superficie cubierta por bosque nativo. "
     "Año 20: 5 especies de aves nativas, 2 especies exóticas y 30 % de la superficie cubierta por bosque nativo. "
     "Hechos registrados en el valle: tala para ampliar cultivos, introducción de una especie exótica y contaminación de un río.")
build(
    O1, 4, F,
    use="Aprenderé a analizar evidencia sobre cómo la actividad humana afecta la biodiversidad y a separar causas de datos. Sirve para explicar el estado actual de la biodiversidad con argumentos y no con frases generales.",
    prior=["Sé qué es una especie nativa y una exótica.", "Sé calcular porcentajes.", "Sé la diferencia entre correlación y causa."],
    explain=[
        "La extinción de especies es un proceso natural, pero la evidencia científica indica que hoy ocurre más rápido de lo esperable sin actividades humanas. Las principales presiones sobre la biodiversidad son la pérdida y fragmentación de hábitat, la introducción de especies exóticas invasoras, la sobreexplotación de recursos, la contaminación y el cambio climático. Casi siempre actúan varias a la vez.",
        "Una especie exótica es la que vive fuera de su área natural por acción humana. Se vuelve invasora cuando se multiplica y desplaza a especies nativas. La fragmentación divide un hábitat grande en parcelas pequeñas y aisladas, donde cada población es menor y tiene menos alimento y pareja. Todo esto disminuye la riqueza de especies y también la diversidad genética de cada población.",
        "Al analizar evidencia hay que cuidar la lógica. Si la riqueza de aves baja mientras el bosque disminuye, hay una asociación, pero la causa se apoya mejor si se comparan lugares con y sin tala, o si se mide el efecto en distintas fechas. Hay que declarar qué se midió, qué no se midió y qué otras causas posibles existen. Y las personas también pueden revertir parte del daño con restauración y protección, por ejemplo conectando parcelas de bosque con corredores, que son franjas de vegetación nativa que las unen.",
    ],
    vocab=[("especie exótica", "especie que vive fuera de su área natural por acción humana"), ("especie invasora", "especie exótica que se multiplica y desplaza a especies nativas"), ("fragmentación del hábitat", "división de un hábitat grande en parcelas pequeñas y aisladas"), ("sobreexplotación", "extracción de un recurso a un ritmo mayor que el de su renovación"), ("correlación", "asociación entre dos variables que no prueba por sí sola una causa")],
    worked=[
        ("Calcular un cambio relativo", "En una laguna de ejemplo había 40 hectáreas de totoral y quedan 30. ¿Qué porcentaje de la superficie original se perdió?",
         ["Pérdida = 40 − 30 = 10 hectáreas.", "Porcentaje = 10 ÷ 40 × 100 = 25."],
         "25 %"),
        ("Distinguir asociación y causa", "En un lago de ejemplo bajó la riqueza de peces después de construir un camino y de introducir una especie de pez exótica. ¿Se puede culpar solo al camino?",
         ["Hay dos hechos que ocurrieron en el mismo período.", "Los datos no separan el efecto de cada uno.", "Se necesitaría comparar lagos con uno y sin el otro."],
         "No, con esos datos no se puede culpar solo al camino"),
    ],
    mistakes=[("Decir «la tala es la única causa» porque coincide con la baja de especies.", "Coincidir en el tiempo no prueba una causa única y puede haber otros factores.", "Habla de «asociación» y propone una comparación que separe causas."),
              ("Creer que una especie exótica siempre es invasora.", "Muchas especies exóticas no se multiplican hasta desplazar a las nativas.", "Es invasora solo si se multiplica y desplaza a otras especies.")],
    T=[
        ("abc", "En Biología de los ecosistemas: ¿qué es una especie exótica?", "Una especie que vive fuera de su área natural por acción humana", "Una especie que solo vive en climas cálidos", "Una especie que está a punto de extinguirse", "Lo definitorio es estar fuera de su área natural por acción humana."),
        ("{F} ¿Cuántas especies de aves nativas había en el año 1?", "8", "La ficha indica 8 especies de aves nativas en el año 1."),
        ("=", "{F} ¿Cuántas especies de aves nativas se perdieron entre el año 1 y el año 20?", "8-5", "Se restan las especies nativas del año 20 a las del año 1.", " especies"),
        ("abc", "{F} ¿Cuál de estos hechos de la ficha es una introducción de especies?", "La introducción de una especie exótica", "La tala para ampliar cultivos", "La contaminación del río", "Introducir una especie fuera de su área natural es el hecho que se relaciona con especies exóticas."),
        ("ab", "{F} ¿Qué presión sobre la biodiversidad se relaciona con la tala para ampliar cultivos?", "La pérdida y fragmentación del hábitat", "La sobreexplotación de una especie", "Talar bosque nativo reduce y divide el hábitat de los organismos."),
        ("=", "{F} ¿Cuántos puntos porcentuales bajó la cobertura de bosque nativo entre el año 1 y el año 20?", "50-30", "Se restan los porcentajes de cobertura de los dos años.", " puntos"),
        ("=", "{F} ¿Qué porcentaje de la cobertura inicial de bosque nativo se perdió? Calcula la pérdida y divídela por la cobertura del año 1.", "(50-30)/50*100", "La pérdida relativa compara lo perdido con la cobertura inicial, no con 100.", " %"),
        ("abc", "{F} Una compañera dice que la baja de aves se debe únicamente a la contaminación del río. ¿Qué respondes?", "Con estos datos no se puede asignar la baja a una sola causa, porque ocurrieron otros hechos al mismo tiempo", "Tiene razón, porque la contaminación es siempre la peor causa", "Tiene razón, porque no se mencionan más hechos", "La ficha registra tres hechos simultáneos y no separa su efecto."),
        ("abc", "Para acercarse a la causa de la baja de aves, ¿qué comparación daría mejor evidencia?", "Comparar valles parecidos, uno con tala y otro sin tala, midiendo aves con el mismo método", "Preguntar a una persona cuántas aves recuerda", "Mirar solo el valle con tala", "Comparar casos con y sin la presión permite acercarse a la causa."),
        ("abc", "{F} Un equipo propone volver a medir el valle a los 40 años, además de los años 1 y 20. ¿Qué ventaja tiene?", "Permite ver si la tendencia continúa o se estabiliza", "Confirma que la tala es la única causa", "Reemplaza la necesidad de comparar con otros valles", "Más puntos en el tiempo permiten ver la tendencia con más claridad."),
        ("ab", "{F} Con estos datos, ¿qué afirmación es correcta?", "La riqueza de aves nativas disminuyó mientras aumentaron las exóticas y se redujo el bosque", "La biodiversidad del valle desapareció", "Los datos muestran bajas en aves nativas y bosque, pero no dicen que no quede biodiversidad."),
        ("abc", "Una especie exótica llega a un humedal de ejemplo, pero tras diez años sigue siendo rara y no desplaza a ninguna especie nativa. ¿Es invasora?", "No, porque no se multiplicó ni desplazó a especies nativas", "Sí, porque es exótica", "Sí, porque llegó por acción humana", "Invasora es la especie exótica que se multiplica y desplaza a las nativas."),
        ("abc", "¿Qué medida se relaciona mejor con reducir la fragmentación del hábitat?", "Conectar parcelas de bosque con corredores de vegetación nativa", "Aumentar las parcelas aisladas", "Sembrar una sola especie exótica", "Los corredores unen parcelas y permiten el paso de organismos."),
    ],
    ctx=("abc", "Contexto: tu municipio propone abrir un camino por un bosque nativo de ejemplo y te piden preguntas para estudiar su efecto en las aves. ¿Qué propuesta es más adecuada?", "Contar aves antes y después con el mismo método y comparar con un bosque sin camino", "Opinar sin contar aves", "Contar aves solo después del camino", "Comparar antes y después, y con un sitio sin camino, acerca la respuesta a una causa."),
    sc=[
        ("En Biología de los ecosistemas: ¿qué es una especie invasora?", "Una especie exótica que se multiplica y desplaza a especies nativas", "Una invasora es exótica y además desplaza a las nativas."),
        ("ab", "Una correlación entre dos variables:", "No prueba por sí sola una causa", "Siempre prueba que una variable causa a la otra", "Dos variables pueden asociarse sin que una cause la otra."),
        ("ab", "Las presiones sobre la biodiversidad:", "Suelen actuar varias a la vez", "Siempre actúan una por una", "En un mismo lugar suelen sumarse varias presiones."),
    ],
    op=("Con la ficha {F}: (1) calcula cuántas especies de aves nativas se perdieron y cuántos puntos porcentuales bajó el bosque; (2) escribe una explicación del estado del valle que mencione al menos dos presiones; (3) propone una comparación que permita separar mejor el efecto de cada presión.",
        "(1) 3 especies y 20 puntos. (2) Bajaron las aves nativas mientras se perdió bosque por tala y aparecieron especies exóticas; ambas presiones reducen el hábitat y la competencia. (3) Comparar valles parecidos con tala y sin tala, y con y sin la especie exótica.",
        ["dos cálculos correctos", "al menos dos presiones", "comparación que separa causas"],
        ["tres respuestas numeradas"],
        ["atribuir todo a una sola causa", "confundir puntos porcentuales con especies", "proponer una comparación sin grupo de contraste"],
        "Pregunta: «¿qué solución concreta podría reducir una de esas presiones?»."),
    reinforce="Escribe las cinco presiones sobre la biodiversidad y un ejemplo inventado de cada una.",
    extend="Explica por qué la fragmentación del hábitat reduce también la diversidad genética de una población, con un ejemplo.",
)

# ============================================================ OAC-02, clase 1
F = ("Ficha 5 (beneficios de ejemplo de un humedal costero ficticio). a) Provee peces y mariscos para alimentación. b) Retiene agua y reduce las inundaciones en lluvias fuertes. "
     "c) Es un lugar de paseo y de observación de aves. d) Sus plantas hacen fotosíntesis y reciclan nutrientes que sostienen a todos los organismos del ecosistema. "
     "e) Filtra parte de los contaminantes del agua.")
build(
    O2, 1, F,
    use="Aprenderé a delimitar qué servicios entregan los ecosistemas y cómo se relacionan con la biodiversidad y el bienestar de las personas. Sirve para plantear preguntas concretas sobre lo que perdemos cuando un ecosistema se degrada.",
    prior=["Sé qué es un ecosistema.", "Sé qué es una cadena trófica.", "Distingo un beneficio directo de uno indirecto."],
    explain=[
        "Los servicios ecosistémicos son los beneficios que las personas obtienen de los ecosistemas. Se agrupan en cuatro categorías. Los de aprovisionamiento entregan productos, como alimentos, agua o madera. Los de regulación controlan procesos, como inundaciones, clima o calidad del agua. Los culturales aportan recreación, conocimiento o identidad. Los de soporte son procesos básicos, como el ciclo de nutrientes y la fotosíntesis, que sostienen a los demás servicios.",
        "El funcionamiento de un ecosistema es el conjunto de procesos que ocurren en él: producción de materia orgánica, ciclo de nutrientes, descomposición y flujo de energía. La biodiversidad participa en esos procesos porque cada especie cumple funciones distintas. Cuando se pierden especies o se simplifica el ecosistema, algunos procesos se debilitan, y con ellos los servicios que las personas usan.",
        "Para delimitar una pregunta sobre servicios hay que fijar el ecosistema, el servicio, la forma de medirlo y el grupo de personas que lo recibe. Por ejemplo: «¿cómo cambia la regulación de inundaciones de un humedal al rellenarlo parcialmente, para las viviendas cercanas?». Así se evita hablar de «la naturaleza» en general y se puede medir con datos concretos.",
    ],
    vocab=[("servicio ecosistémico", "beneficio que las personas obtienen de un ecosistema"), ("aprovisionamiento", "servicio que entrega productos como alimento, agua o madera"), ("regulación", "servicio que controla procesos como inundaciones, clima o calidad del agua"), ("servicio cultural", "beneficio de recreación, conocimiento o identidad"), ("servicio de soporte", "proceso básico que sostiene a los demás servicios")],
    worked=[
        ("Clasificar un servicio", "Un bosque de ejemplo da madera a un aserradero. ¿De qué categoría es ese servicio?",
         ["La madera es un producto que se extrae.", "Los servicios que entregan productos son de aprovisionamiento."],
         "Aprovisionamiento"),
        ("Delimitar la pregunta", "Quieres estudiar un servicio de una cuenca de ejemplo. ¿Qué pregunta está mejor delimitada: «¿cuánto vale la naturaleza?» o «¿cuántos metros cúbicos de agua retiene al año el suelo de un bosque de una cuenca y cuántas casas abastece?»",
         ["La primera no nombra ecosistema, servicio ni forma de medir.", "La segunda nombra el ecosistema, el servicio, la unidad y el grupo beneficiado."],
         "La segunda pregunta"),
    ],
    mistakes=[("Pensar que los servicios ecosistémicos son solo los productos que se venden.", "Incluyen también regulación, procesos de soporte y valores culturales, que no siempre tienen precio.", "Revisa las cuatro categorías antes de listar servicios."),
              ("Confundir el funcionamiento del ecosistema con el servicio.", "El funcionamiento es el proceso (por ejemplo, el ciclo de nutrientes); el servicio es el beneficio para las personas.", "Pregunta: ¿es un proceso del ecosistema o un beneficio para las personas?")],
    T=[
        ("abc", "En Biología de los ecosistemas: ¿qué es un servicio ecosistémico?", "Un beneficio que las personas obtienen de un ecosistema", "Un trabajo que las personas hacen en un ecosistema", "Una especie que vive en un ecosistema", "Un servicio ecosistémico es un beneficio del ecosistema para las personas."),
        ("{F} ¿Qué letra (a, b, c, d o e) describe un servicio de aprovisionamiento?", "a", "Proveer peces y mariscos para alimentación es entregar un producto."),
        ("{F} ¿Qué letra (a, b, c, d o e) describe un servicio cultural?", "c", "El paseo y la observación de aves son recreación, un beneficio cultural."),
        ("abc", "{F} El servicio b (reducir las inundaciones) es de…", "regulación", "aprovisionamiento", "soporte", "Controlar inundaciones es regular un proceso."),
        ("abc", "{F} El servicio d (fotosíntesis y reciclaje de nutrientes) es de…", "soporte", "regulación", "aprovisionamiento", "Son procesos básicos que sostienen a los demás servicios."),
        ("ab", "{F} Filtrar contaminantes del agua (e) se clasifica mejor como servicio de…", "regulación, porque controla la calidad del agua", "aprovisionamiento, porque entrega agua", "La definición de regulación incluye controlar la calidad del agua."),
        ("{F} ¿Cuántos de los cinco beneficios son de aprovisionamiento o culturales?", "2", "Solo a (aprovisionamiento) y c (cultural) están en esas categorías; b, d y e son de regulación o soporte."),
        ("abc", "Un hotel de ejemplo cobra por guiar paseos para observar aves en un humedal. ¿Qué servicio ecosistémico aprovecha principalmente?", "Cultural", "De aprovisionamiento, porque obtiene ingresos", "De regulación de inundaciones", "Observar aves es un beneficio recreativo y de conocimiento."),
        ("abc", "¿Qué pregunta delimita mejor un estudio sobre un servicio ecosistémico?", "¿Cuántas toneladas de pescado extrae al año la pesca de una bahía de ejemplo y cuántas familias viven de ella?", "¿Cuánto vale la naturaleza?", "¿Es bueno cuidar el medio ambiente?", "Solo la primera nombra ecosistema, servicio, unidad y beneficiarios."),
        ("abc", "{F} Si se rellenara el humedal para construir, ¿qué beneficio de la ficha se relaciona directamente con el riesgo de inundación de las casas cercanas?", "El b, la retención de agua", "El a, los peces y mariscos", "El c, el paseo y la observación de aves", "Menos humedal retiene menos agua y aumenta el riesgo de inundación cercano."),
        ("ab", "Un equipo dice: «si desaparece una especie del humedal, no cambia ningún servicio». ¿Qué falla?", "Cada especie cumple funciones, y perderlas puede debilitar procesos y servicios", "Nada: las especies se reemplazan sin que cambie ningún proceso", "La biodiversidad participa en los procesos del ecosistema, por lo que perder especies puede afectar servicios."),
        ("abc", "¿Por qué los servicios de soporte suelen pasar desapercibidos para las personas?", "Porque son procesos básicos y no se ven como un beneficio directo", "Porque no existen", "Porque solo están en los océanos", "Sostienen a los otros servicios, pero no se perciben como un beneficio directo."),
        ("abc", "Un grupo debe decidir cuál servicio medir primero en un humedal. ¿Qué criterio es más científico?", "Elegir un servicio que se pueda medir con datos y unidades claras", "Elegir el que parezca más importante, aunque no haya datos", "Elegir el que más guste", "Un servicio medible permite comparar antes y después."),
    ],
    ctx=("abc", "Contexto: una comunidad de ejemplo junto a un río con bosque de ribera quiere saber qué perdería si se talan los árboles de la orilla. ¿Qué pregunta de investigación es mejor?", "¿Cambia la calidad del agua y el riesgo de erosión del río cuando se talan los árboles de la ribera, para las casas cercanas?", "¿Es malo talar?", "¿Qué opina la gente del río?", "La mejor pregunta nombra los servicios de regulación afectados y quiénes los reciben."),
    sc=[
        ("En Biología de los ecosistemas: ¿qué es un servicio de regulación?", "Uno que controla procesos como inundaciones, clima o calidad del agua", "Los servicios de regulación controlan procesos del ambiente."),
        ("ab", "Los servicios de soporte:", "Sostienen a los demás servicios", "Son siempre productos que se venden", "Procesos como la fotosíntesis sostienen todo lo demás."),
        ("ab", "El funcionamiento de un ecosistema es:", "El conjunto de procesos que ocurren en él", "Un beneficio que se vende", "Los procesos son la base de los servicios, pero no son el servicio."),
    ],
    op=("Con la ficha {F}: (1) clasifica los cinco beneficios (a a e) en las cuatro categorías; (2) escribe una pregunta bien delimitada sobre uno de ellos; (3) explica qué pasaría con ese servicio si el humedal perdiera varias especies.",
        "(1) a aprovisionamiento; b y e regulación; c cultural; d soporte. (2) ¿Cuántos metros cúbicos de agua retiene el humedal en lluvias fuertes y cuántas casas protege? (3) Si desaparecieran plantas que retienen suelo y agua, bajaría la retención y subiría el riesgo de inundación.",
        ["clasificación correcta", "pregunta con ecosistema, servicio y medida", "relación entre pérdida de especies y servicio"],
        ["tres respuestas numeradas"],
        ["mezclar proceso y servicio", "hacer una pregunta sin medida", "no relacionar especies con funciones"],
        "Pregunta: «¿qué dato necesitarías para saber cuánto cambió el servicio?»."),
    reinforce="Haz una tabla con las cuatro categorías de servicios y dos ejemplos de cada una para un bosque.",
    extend="Explica con un ejemplo por qué un ecosistema con menos especies puede dar menos servicios, aunque tenga el mismo tamaño.",
)

# ============================================================ OAC-02, clase 2
F = ("Ficha 6 (datos de ejemplo, energía en kJ por metro cuadrado por día). Pastizal 1: energía total fijada por las plantas en la fotosíntesis (producción primaria bruta): 200; energía que las plantas usan en su propia respiración celular: 80. "
     "Pastizal 2, en un año de sequía: producción primaria bruta: 120; respiración de las plantas: 70. "
     "Dato de otro estudio, en unidades distintas: pastizal 3, producción primaria bruta de 35 kJ por metro cuadrado por semana.")
build(
    O2, 2, F,
    use="Aprenderé la bioenergética de un ecosistema: cómo los productores captan energía y cómo la usan. Sirve para evaluar variables y fuentes cuando se comparan ecosistemas.",
    prior=["Sé qué es un productor y un consumidor.", "Sé que las plantas hacen fotosíntesis.", "Sé restar y comparar cantidades con unidades."],
    explain=[
        "La bioenergética estudia cómo los seres vivos obtienen, transforman y usan la energía. En la fotosíntesis, los productores usan la energía de la luz para transformar dióxido de carbono y agua en glucosa y oxígeno. En la respiración celular, que hacen todos los seres vivos, incluidas las plantas, la glucosa y el oxígeno se transforman en dióxido de carbono y agua, y la energía queda disponible en una molécula llamada ATP.",
        "La producción primaria bruta es la energía total que los productores fijan por fotosíntesis. Parte se gasta en su respiración. Lo que queda es la producción primaria neta: producción neta = producción bruta − respiración. Esa energía neta es la que queda disponible para el crecimiento de las plantas y para los consumidores que se alimentan de ellas.",
        "Para comparar ecosistemas hay que cuidar las variables y las unidades. La luz, el agua y los nutrientes limitan la producción. Si dos datos vienen en unidades o períodos distintos, como kJ por día y kJ por semana, hay que llevarlos a la misma unidad antes de compararlos. También se debe revisar la fuente: quién midió, con qué método y en qué fecha.",
    ],
    vocab=[("fotosíntesis", "proceso en que los productores usan la luz para fabricar glucosa"), ("respiración celular", "proceso que libera la energía de la glucosa para el trabajo de la célula"), ("ATP", "molécula que almacena energía útil para la célula"), ("producción primaria neta", "energía que queda para crecer y para los consumidores"), ("factor limitante", "recurso escaso que frena la producción de un ecosistema")],
    worked=[
        ("Calcular la producción neta", "En una pradera de ejemplo la producción bruta es 150 kJ y la respiración de las plantas es 60 kJ. ¿Cuál es la producción neta?",
         ["Neta = bruta − respiración.", "150 − 60 = 90."],
         "90 kJ"),
        ("Cambiar de unidad antes de comparar", "Un dato de ejemplo es 14 kJ por semana. ¿Cuántos kJ por día son, en promedio?",
         ["Una semana tiene 7 días.", "14 ÷ 7 = 2."],
         "2 kJ por día"),
    ],
    mistakes=[("Creer que las plantas solo hacen fotosíntesis y no respiran.", "Las plantas también hacen respiración celular, de día y de noche, y gastan parte de lo que fijan.", "Resta la respiración de la producción bruta para obtener la neta."),
              ("Comparar kJ por día con kJ por semana sin convertir.", "Los períodos son distintos y los números no son comparables directamente.", "Lleva ambos datos a la misma unidad antes de comparar.")],
    T=[
        ("abc", "En Biología de los ecosistemas: ¿qué es la producción primaria neta?", "La energía que queda tras restar la respiración de las plantas", "Toda la energía que llega del Sol", "La energía que gastan los consumidores", "Es producción bruta menos respiración de los productores."),
        ("{F} ¿Cuánta energía fijaron las plantas del pastizal 1 por fotosíntesis, en kJ por metro cuadrado por día?", "200", "La ficha indica una producción primaria bruta de 200 en el pastizal 1."),
        ("=", "{F} ¿Cuál es la producción primaria neta del pastizal 1?", "200-80", "La producción neta se obtiene restando la respiración de las plantas a la producción bruta.", " kJ por metro cuadrado por día"),
        ("=", "{F} ¿Cuál es la producción primaria neta del pastizal 2, el año de sequía?", "120-70", "Se resta la respiración de 70 a la producción bruta de 120.", " kJ por metro cuadrado por día"),
        ("abc", "{F} ¿En cuál pastizal es mayor la producción neta?", "En el pastizal 1", "En el pastizal 2", "Es igual en ambos", "El pastizal 1 tiene una neta de 120 y el 2 una neta de 50."),
        ("abc", "¿Qué molécula almacena energía útil para la célula tras la respiración celular?", "ATP", "ADN", "Celulosa", "El ATP guarda energía que la célula usa para sus procesos."),
        ("=", "{F} ¿Cuántos kJ menos de producción bruta tiene el pastizal 2 que el pastizal 1?", "200-120", "La diferencia entre las producciones brutas muestra cuánto menos fijó el pastizal en sequía.", " kJ"),
        ("abc", "{F} Una explicación posible de la menor producción bruta del pastizal 2 es:", "La sequía limitó la fotosíntesis por falta de agua", "Las plantas dejaron de necesitar luz", "El pastizal tiene más consumidores que productores", "El agua es un factor limitante de la fotosíntesis, y en sequía baja la producción bruta."),
        ("=", "{F} El pastizal 3 tiene 35 kJ por metro cuadrado por semana. ¿Cuántos kJ por metro cuadrado por día son en promedio? Una semana tiene 7 días.", "35/7", "Se divide la producción semanal por los siete días de la semana para tener una unidad diaria.", " kJ por día"),
        ("abc", "{F} Una estudiante compara directamente 120 (pastizal 2) con 35 (pastizal 3) y dice que el 2 produce más de tres veces lo del 3. ¿Qué falla?", "Las unidades son distintas (por día y por semana) y deben igualarse antes", "Nada, el cálculo es correcto", "Los pastizales no se pueden comparar nunca", "Para comparar hay que llevar los datos a la misma unidad y período."),
        ("ab", "¿Por qué una planta en la noche sigue gastando energía aunque no haga fotosíntesis?", "Porque su respiración celular continúa", "Porque la planta se detiene por completo", "Las plantas, como todos los seres vivos, respiran todo el tiempo."),
        ("abc", "¿Qué afirmación sobre la fotosíntesis y la respiración celular es correcta?", "La fotosíntesis fabrica glucosa y la respiración celular la usa para obtener energía", "Ambos procesos son lo mismo", "La respiración celular solo ocurre en animales", "Son procesos complementarios: uno fija energía y el otro la libera."),
        ("abc", "Un informe presenta una cifra de producción sin decir quién la midió ni cómo. ¿Qué haces?", "Buscar la fuente y el método antes de usar la cifra", "Usarla porque parece precisa", "Descartar todas las cifras por igual", "Una cifra sin método ni autor no se puede revisar ni comparar."),
    ],
    ctx=("abc", "Contexto: una región de ejemplo sufre varios años secos y los ganaderos notan menos pasto. Tu curso quiere explicar el fenómeno con bioenergética. ¿Qué explicación elegirías?", "Con menos agua baja la fotosíntesis, baja la producción neta y hay menos energía para los herbívoros", "El pasto dejó de respirar", "Los herbívoros comen menos por voluntad", "La explicación conecta el factor limitante (agua) con la producción neta y los consumidores."),
    sc=[
        ("En Biología de los ecosistemas: ¿qué es un factor limitante?", "Un recurso escaso que frena la producción", "Un factor limitante restringe la fotosíntesis o el crecimiento."),
        ("ab", "Producción neta es:", "Producción bruta menos respiración", "Producción bruta más respiración", "La respiración consume parte de lo fijado, por eso se resta."),
        ("ab", "Para comparar datos con distintos períodos hay que:", "Convertirlos a la misma unidad", "Compararlos directamente", "Las unidades iguales evitan comparaciones engañosas."),
    ],
    op=("Con los datos de la ficha {F}: (1) calcula la producción neta de los pastizales 1 y 2; (2) explica en dos oraciones qué factor pudo causar la diferencia y qué proceso de la planta se afectó; (3) escribe qué haría falta para comparar el pastizal 3 con los otros.",
        "(1) 120 y 50. (2) La sequía pudo limitar la fotosíntesis por falta de agua, lo que bajó la producción bruta y la neta. (3) Convertir los 35 kJ por semana a kJ por día y confirmar el método y la fecha de ese estudio.",
        ["dos cálculos correctos", "factor limitante y proceso", "cambio de unidad antes de comparar"],
        ["tres respuestas numeradas"],
        ["restar mal la respiración", "atribuir la baja a otro proceso sin justificar", "comparar unidades distintas"],
        "Pregunta: «¿qué otra variable podría explicar la diferencia?»."),
    reinforce="Escribe las ecuaciones de la fotosíntesis y de la respiración celular con palabras, y rotula qué entra y qué sale.",
    extend="Explica por qué la producción neta de un ecosistema condiciona cuántos herbívoros puede mantener.",
)

# ============================================================ OAC-02, clase 3
F = ("Ficha 7 (red trófica de ejemplo, energía en kJ disponibles en cada nivel). Productores (pasto): 10.000. Consumidores primarios (conejos, que comen pasto): 1.000. "
     "Consumidores secundarios (zorros, que comen conejos): 100. Consumidores terciarios (águilas, que comen zorros): 10. "
     "En este modelo de ejemplo solo pasa de un nivel al siguiente el 10 % de la energía; el resto se pierde como calor en la respiración. Los descomponedores actúan sobre los restos de todos los niveles.")
build(
    O2, 3, F,
    use="Aprenderé a interpretar un modelo de flujo de materia y energía en una red trófica. Sirve para explicar por qué hay pocos depredadores grandes y por qué la materia se recicla pero la energía no.",
    prior=["Sé qué son productores, consumidores y descomponedores.", "Sé calcular porcentajes sencillos.", "Sé leer un esquema de niveles tróficos."],
    explain=[
        "Un ecosistema funciona gracias a dos flujos. La energía entra casi siempre como luz del Sol, la fijan los productores y pasa de un nivel trófico a otro cuando alguien se come a otro organismo. En cada paso, la mayor parte se pierde como calor por la respiración, por lo que el flujo de energía es en un solo sentido y se agota. En muchos modelos escolares se usa el 10 % de ejemplo como paso de un nivel al siguiente.",
        "La materia, en cambio, se recicla. Los átomos de carbono, nitrógeno y fósforo pasan de los organismos al ambiente y vuelven a los productores gracias a los descomponedores, que son hongos y bacterias que transforman los restos en nutrientes. Por eso se dice que la energía fluye y la materia circula. Sin descomponedores, los nutrientes quedarían atrapados en los restos.",
        "Un modelo como una pirámide de energía permite predecir. Como cada nivel recibe solo una fracción, hay menos energía disponible para los niveles altos y por eso suelen tener menos individuos y cadenas cortas. Un modelo simplifica: las redes reales tienen muchas conexiones, y los porcentajes de paso varían según los organismos. Siempre hay que declarar qué supuestos se usan.",
    ],
    vocab=[("nivel trófico", "posición de un organismo en la cadena alimentaria"), ("descomponedor", "hongo o bacteria que transforma restos en nutrientes"), ("pirámide de energía", "modelo que muestra la energía disponible en cada nivel trófico"), ("ciclo de la materia", "recorrido de los átomos entre los organismos y el ambiente"), ("flujo de energía", "paso de energía de un nivel al siguiente, con pérdidas como calor")],
    worked=[
        ("Aplicar el 10 %", "En una red de ejemplo los productores tienen 5.000 kJ. Con un paso del 10 %, ¿cuántos kJ llegan a los consumidores primarios?",
         ["Se toma el 10 % de 5.000.", "5.000 × 10 ÷ 100 = 500."],
         "500 kJ"),
        ("Distinguir energía y materia", "¿Qué es cíclico: el carbono o la energía que usan los organismos?",
         ["El carbono pasa del ambiente a los organismos y vuelve al ambiente.", "La energía se pierde como calor y no vuelve a ser usada por los productores."],
         "El carbono es cíclico; la energía no"),
    ],
    mistakes=[("Decir que la energía se recicla como los nutrientes.", "La energía se disipa como calor y se necesita luz nueva; los nutrientes sí se reutilizan.", "Escribe «la energía fluye en un sentido y la materia circula»."),
              ("Pensar que los descomponedores son el último nivel y no aportan nada.", "Los descomponedores devuelven nutrientes a los productores y mantienen el ciclo de la materia.", "Dibuja una flecha de los restos hacia los descomponedores y de ahí hacia los productores.")],
    T=[
        ("abc", "En Biología de los ecosistemas: ¿qué hacen los descomponedores?", "Transforman los restos en nutrientes que pueden usar los productores", "Fijan la energía de la luz", "Se alimentan solo de animales vivos", "Los descomponedores reciclan la materia de los restos."),
        ("{F} ¿Quiénes son los productores en la red de la ficha?", "El pasto", "En la ficha, el pasto es el productor, que fija la energía de la luz."),
        ("{F} ¿Cuántos kJ hay en el nivel de los consumidores secundarios?", "100", "La ficha indica 100 kJ para los consumidores secundarios, los zorros."),
        ("abc", "{F} ¿Dónde se pierde la mayor parte de la energía entre un nivel y el siguiente?", "Como calor por la respiración", "Como nutrientes en el suelo", "Como luz que vuelve al Sol", "En el modelo, la mayor parte se disipa como calor."),
        ("=", "{F} Si los productores tuvieran 4.000 kJ, ¿cuántos kJ pasarían a los consumidores primarios con el paso del 10 %?", "4000*10/100", "Se calcula el 10 % de la energía de los productores.", " kJ"),
        ("abc", "{F} Si los conejos tuvieran 2.000 kJ, ¿cuántos kJ pasan a los zorros con el paso del 10 %?", "200", "20", "2.000", "El 10 % de 2.000 son 200 kJ."),
        ("=", "{F} ¿Cuántos kJ de los 10.000 de los productores no llegaron a los consumidores primarios?", "10000-1000", "Se resta lo que llegó al nivel siguiente a lo que había en los productores.", " kJ"),
        ("ab", "{F} ¿Por qué hay muy pocas águilas en la red?", "Porque llega muy poca energía al último nivel", "Porque los consumidores grandes siempre se extinguen primero", "Cada paso pierde energía como calor, y al final queda muy poca para mantener muchos individuos."),
        ("abc", "{F} Si desaparecieran los descomponedores del ecosistema, ¿qué ocurriría a largo plazo?", "Los nutrientes quedarían atrapados en los restos y los productores recibirían menos", "La energía del Sol dejaría de llegar", "Los consumidores se volverían productores", "Los descomponedores devuelven nutrientes al suelo y al agua."),
        ("abc", "¿Qué ocurre con la energía de un ecosistema que no recibe luz nueva durante mucho tiempo?", "Se agota porque se disipa como calor", "Se recicla indefinidamente", "Se acumula en los descomponedores", "Sin nueva energía de entrada, la existente se pierde como calor."),
        ("abc", "{F} Alguien propone agregar un cuarto nivel con otro depredador sobre las águilas. Según el modelo, ¿cuánta energía le llegaría?", "1 kJ, un valor muy bajo para sostener a una población", "100 kJ", "1.000 kJ", "El 10 % de 10 kJ es 1 kJ, insuficiente en el modelo."),
        ("ab", "{F} La red de la ficha es un modelo. ¿Cuál es una limitación?", "Usa el mismo 10 % para todos los pasos, aunque en la realidad varía", "Expresa la energía en kJ", "Los porcentajes reales varían según los organismos, pero el modelo usa un valor único."),
        ("abc", "Una cadena de ejemplo tiene solo tres niveles y otra tiene seis niveles. Con las mismas condiciones, ¿cuál tendrá en el último nivel menos energía disponible?", "La de seis niveles", "La de tres niveles", "Ambas igual", "A más niveles, más pérdidas acumuladas."),
    ],
    ctx=("abc", "Contexto: una escuela quiere instalar un huerto de ejemplo con compostera. Debes explicar por qué la compostera ayuda a cerrar el ciclo de la materia. ¿Qué explicación eliges?", "Los descomponedores transforman los restos en nutrientes que las plantas pueden volver a usar", "La compostera crea energía nueva", "Los restos desaparecen sin dejar nutrientes", "La compostera reproduce el trabajo de los descomponedores y reutiliza la materia."),
    sc=[
        ("En Biología de los ecosistemas: ¿qué es un nivel trófico?", "La posición de un organismo en la cadena alimentaria", "Los niveles ordenan quién come a quién."),
        ("ab", "La energía en un ecosistema:", "Fluye en un sentido y se pierde como calor", "Circula sin pérdidas", "Siempre se pierde calor en cada paso."),
        ("ab", "La materia en un ecosistema:", "Se recicla gracias a los descomponedores", "Se pierde para siempre", "Los átomos se reutilizan en ciclos."),
    ],
    op=("Con la ficha {F}: (1) dibuja con palabras la pirámide de energía con los cuatro valores; (2) explica en dos oraciones por qué hay menos individuos en los niveles altos; (3) escribe qué papel cumplen los descomponedores y qué pasaría sin ellos.",
        "(1) Productores 10.000; primarios 1.000; secundarios 100; terciarios 10. (2) Cada paso pierde alrededor de nueve décimas como calor, así que a los niveles altos llega poca energía. (3) Reciclan la materia de los restos; sin ellos, los nutrientes quedarían atrapados y bajaría la producción.",
        ["cuatro valores bien ordenados", "explicación con pérdida de energía", "papel de los descomponedores"],
        ["tres respuestas numeradas"],
        ["decir que la energía se recicla", "omitir las pérdidas en cada paso", "olvidar a los descomponedores"],
        "Pregunta: «¿qué cambiaría si el paso fuera del 20 % y no del 10 %?»."),
    reinforce="Dibuja una pirámide de energía con tres niveles e inventa valores coherentes con el paso del 10 %.",
    extend="Explica por qué las cadenas alimentarias suelen tener pocos niveles y qué efecto tiene eso en el tamaño de los depredadores finales.",
)

# ============================================================ OAC-02, clase 4
F = ("Ficha 8 (datos de ejemplo). Población de un roedor en una isla ficticia: al comenzar el año 1 hay 200 individuos. Durante el año 1 nacen 80, mueren 50, no llega ni sale ninguno. "
     "Capacidad de carga de la isla (individuos que el ambiente sostiene): 400. "
     "Tamaño de la población al comenzar cada año: año 1: 200; año 2: 230; año 3: 275; año 4: 320; año 5: 360; año 6: 385; año 7: 395.")
build(
    O2, 4, F,
    use="Aprenderé a analizar datos de una población: cómo cambia su tamaño y por qué se acerca a un límite. Sirve para entender cómo la dinámica de poblaciones afecta el funcionamiento de los ecosistemas.",
    prior=["Sé qué es una población.", "Sé sumar y restar con cantidades y calcular porcentajes sencillos.", "Sé leer una serie de datos en el tiempo."],
    explain=[
        "El tamaño de una población cambia por cuatro procesos: natalidad (nacimientos), mortalidad (muertes), inmigración (llegada de individuos) y emigración (salida de individuos). Se resume así: cambio = nacimientos + inmigración − muertes − emigración. Si el cambio es positivo, la población crece; si es negativo, disminuye.",
        "Cuando hay alimento y espacio de sobra, una población puede crecer rápido, a un ritmo que aumenta con el tamaño: crecimiento exponencial. Pero los recursos son limitados. La capacidad de carga es el número máximo de individuos que un ambiente puede sostener. Al acercarse a ese límite, la competencia por alimento, las enfermedades y los depredadores aumentan, el crecimiento se frena y la curva se aplana: crecimiento logístico.",
        "Los factores que dependen de la densidad, como la competencia y las enfermedades, actúan más cuando hay muchos individuos. Los independientes de la densidad, como una helada fuerte, afectan igual sin importar el tamaño. Analizar evidencia es leer la serie de datos, calcular los cambios y decidir qué modelo la describe mejor, declarando también sus límites.",
    ],
    vocab=[("natalidad", "número de nacimientos en un período"), ("mortalidad", "número de muertes en un período"), ("capacidad de carga", "número máximo de individuos que un ambiente puede sostener"), ("crecimiento logístico", "crecimiento que se frena al acercarse a la capacidad de carga"), ("factor dependiente de la densidad", "factor que actúa más cuando hay más individuos")],
    worked=[
        ("Calcular el cambio", "Una población de ejemplo tiene 150 individuos; en el año nacen 40, mueren 30, llegan 10 y salen 5. ¿Cuántos individuos hay al final del año?",
         ["Cambio = 40 + 10 − 30 − 5 = 15.", "150 + 15 = 165."],
         "165 individuos"),
        ("Reconocer el modelo", "Una población de ejemplo crece de 100 a 140, a 190 y a 230, y luego se queda en torno a 250, que es la capacidad de carga. ¿Qué modelo la describe?",
         ["Primero crece rápido.", "Luego se aplana cerca del límite que sostiene el ambiente.", "Eso corresponde al crecimiento logístico."],
         "Crecimiento logístico"),
    ],
    mistakes=[("Olvidar la inmigración y la emigración al calcular el cambio de una población.", "Las poblaciones también cambian por llegadas y salidas, no solo por nacimientos y muertes.", "Usa siempre la fórmula completa con los cuatro términos."),
              ("Creer que la capacidad de carga es un número fijo para siempre.", "Cambia si cambian los recursos, como el alimento, el agua o el espacio.", "Di «en las condiciones actuales», no «siempre».")],
    T=[
        ("abc", "En Biología de los ecosistemas: ¿qué es la capacidad de carga?", "El número máximo de individuos que un ambiente puede sostener", "El número de individuos que nacen cada año", "El peso total de una población", "Es el límite que los recursos del ambiente imponen a una población."),
        ("{F} ¿Cuántos individuos hay al comenzar el año 4?", "320", "La serie de la ficha indica 320 individuos al comenzar el año 4."),
        ("=", "{F} ¿Cuál fue el cambio de la población durante el año 1?", "80-50", "Como no hay inmigración ni emigración, el cambio es nacimientos menos muertes.", " individuos"),
        ("abc", "{F} Según la ficha, la población del año 1 al año 7, ¿qué hace?", "Crece todos los años y, hacia el final, los aumentos son más pequeños", "Disminuye cada año", "Se mantiene igual", "Los valores suben cada año, pero los aumentos del año 5 en adelante son cada vez menores."),
        ("=", "{F} ¿Cuántos individuos aumentó la población entre el año 2 y el año 3?", "275-230", "Se restan los individuos de los dos momentos.", " individuos"),
        ("=", "{F} ¿Cuántos individuos aumentó la población entre el año 6 y el año 7?", "395-385", "Se restan los individuos de los dos momentos para comparar con los aumentos anteriores.", " individuos"),
        ("ab", "{F} ¿Por qué el aumento entre el año 6 y el 7 es menor que entre el año 2 y el 3?", "Porque la población se acerca a la capacidad de carga y los recursos son más escasos", "Porque la isla se hizo más grande", "Al acercarse al límite, la competencia frena el crecimiento."),
        ("=", "{F} ¿Qué porcentaje de crecimiento tuvo la población durante el año 1? Divide el cambio por la población inicial y multiplica por cien.", "30/200*100", "El porcentaje relativo compara el aumento con el tamaño inicial de la población.", " %"),
        ("abc", "Una población de ejemplo tiene 300 individuos; en un año nacen 60, mueren 40, llegan 20 y salen 50. ¿Cuántos hay al final?", "290", "310", "270", "Cambio = 60 + 20 − 40 − 50 = −10, entonces 300 − 10 = 290."),
        ("abc", "{F} Se produce una helada fuerte y mueren 50 roedores al azar. ¿Qué tipo de factor es?", "Independiente de la densidad", "Dependiente de la densidad", "No es un factor ambiental", "Una helada afecta aunque haya pocos o muchos individuos."),
        ("ab", "{F} Un estudiante afirma que, como el año 7 hay 395 y la capacidad es 400, la población no puede cambiar más. ¿Qué respondes?", "Puede seguir cambiando si cambia el alimento, el clima o hay migración", "Tiene razón, porque no puede superar el límite", "La capacidad de carga depende de los recursos y puede variar, por lo que los números pueden moverse."),
        ("abc", "{F} Un incendio en la isla de ejemplo reduce los alimentos a la mitad. ¿Qué esperarías para la capacidad de carga?", "Que baje", "Que suba", "Que no cambie", "Con menos recursos, el ambiente sostiene menos individuos."),
        ("abc", "{F} Una enfermedad que se contagia más cuando hay muchos roedores juntos es un ejemplo de factor…", "dependiente de la densidad", "independiente de la densidad", "ajeno al ambiente", "Su efecto crece al aumentar la densidad."),
    ],
    ctx=("abc", "Contexto: una comunidad de ejemplo observa que los ciervos de una reserva aumentan cada año y el pasto escasea. Tu curso debe explicar qué ocurrirá. ¿Qué explicación elige?", "Si los ciervos superan la capacidad de carga, aumentarán el hambre y la mortalidad y la población se estabilizará o bajará", "Los ciervos seguirán creciendo sin límite", "El pasto crecerá más con más ciervos", "La población se frena cuando los recursos limitan su crecimiento."),
    sc=[
        ("En Biología de los ecosistemas: ¿qué es la natalidad?", "El número de nacimientos en un período", "La natalidad cuenta los nacimientos y es uno de los procesos que cambian una población."),
        ("ab", "El crecimiento logístico:", "Se frena al acercarse a la capacidad de carga", "Es siempre más rápido cada año", "Los recursos limitados frenan la curva."),
        ("ab", "El cambio de una población incluye:", "Nacimientos, muertes, inmigración y emigración", "Solo nacimientos", "Son cuatro procesos los que cambian el tamaño de una población."),
    ],
    op=("Con los datos de la ficha {F}: (1) calcula el aumento de población año a año entre el año 3 y el año 7; (2) describe la tendencia de esos aumentos; (3) explica con un factor del ambiente por qué ocurre y qué otro dato necesitarías para comprobarlo.",
        "(1) Año 3 a 4: 45; 4 a 5: 40; 5 a 6: 25; 6 a 7: 10. (2) Los aumentos son cada vez menores. (3) Al acercarse a 400 aumenta la competencia por alimento; necesitaría datos del alimento disponible y de la mortalidad por año.",
        ["cuatro aumentos correctos", "tendencia descrita", "factor y dato para comprobar"],
        ["tres respuestas numeradas"],
        ["restar mal", "decir que la población ya llegó al límite", "no proponer un dato para comprobar"],
        "Pregunta: «¿qué pasaría si la capacidad de carga bajara a 300?»."),
    reinforce="Escribe la fórmula del cambio de una población y úsala con números inventados distintos a los de la ficha.",
    extend="Explica por qué dos poblaciones de la misma especie pueden tener distinta capacidad de carga en dos islas distintas.",
)

# ============================================================ OAC-02, clase 5
F = ("Ficha 9 (dos opciones de manejo de ejemplo para 100 hectáreas; puntajes de ejemplo de 1 a 5, donde 5 es lo mejor). "
     "Opción X, plantación de un solo tipo de árbol: producción de madera 5, regulación del agua 2, resistencia a plagas 1, hábitat para fauna 1. "
     "Opción Y, bosque mixto con varias especies nativas: producción de madera 3, regulación del agua 4, resistencia a plagas 4, hábitat para fauna 5.")
build(
    O2, 5, F,
    use="Aprenderé a comparar soluciones de manejo según los servicios que entregan y cómo la biodiversidad afecta la estabilidad. Sirve para tomar decisiones con criterios explícitos y no solo por costumbre.",
    prior=["Sé qué son los servicios ecosistémicos.", "Sé sumar puntajes.", "Sé qué es una plaga."],
    explain=[
        "Los ecosistemas con más biodiversidad suelen mantener mejor sus funciones cuando hay cambios. Una razón es que hay especies distintas que cumplen funciones parecidas; si una disminuye por una plaga o una sequía, otra puede compensar. A esta capacidad de volver a funcionar tras una perturbación se la llama resiliencia. En cambio, un sistema con una sola especie depende de que ella resista.",
        "Esto no significa que toda opción con más especies sea la mejor en todo. Una plantación de una especie puede producir más madera por hectárea en poco tiempo, pero entregar menos regulación del agua, hábitat y resistencia a plagas. Elegir exige comparar varios criterios, decidir cuánto importa cada uno y reconocer que hay compromisos o «trade-offs», es decir, ganar en un criterio y perder en otro.",
        "Una matriz de decisión ordena esa comparación: se listan las opciones, los criterios y un puntaje por criterio, que se suman, a veces con pesos. Los puntajes de ejemplo no son hechos medidos; hay que decir quién los asignó y con qué datos. Además, se revisa la sensibilidad de la decisión: si el ganador cambia al cambiar un peso, la decisión es frágil.",
    ],
    vocab=[("resiliencia", "capacidad de un ecosistema de recuperarse tras una perturbación"), ("perturbación", "evento que altera un ecosistema, como una sequía o un incendio"), ("matriz de decisión", "tabla que compara opciones con varios criterios"), ("compromiso (trade-off)", "ganar en un criterio a costa de otro"), ("peso", "importancia que se da a un criterio al sumar puntajes")],
    worked=[
        ("Sumar puntajes", "Una opción de ejemplo tiene puntajes 4, 3 y 2 en tres criterios. ¿Cuál es el total sin pesos?",
         ["Se suman los tres puntajes.", "4 + 3 + 2 = 9."],
         "9 puntos"),
        ("Usar pesos", "En una matriz de ejemplo el criterio A vale doble. Una opción tiene 3 en A y 4 en B. ¿Cuál es su total?",
         ["A vale doble: 3 × 2 = 6.", "B vale una vez: 4.", "6 + 4 = 10."],
         "10 puntos"),
    ],
    mistakes=[("Decir que la opción con más producción es siempre la mejor.", "Un criterio no cubre todo; otras funciones, como regular el agua o resistir plagas, también importan.", "Compara varios criterios y declara cuánto pesa cada uno."),
              ("Tratar los puntajes de la matriz como mediciones exactas.", "Son valoraciones; dependen de quién las asigna y con qué datos.", "Rotula los puntajes como de ejemplo y di de dónde vienen.")],
    T=[
        ("abc", "En Biología de los ecosistemas: ¿qué es la resiliencia?", "La capacidad de recuperarse tras una perturbación", "La capacidad de no cambiar nunca", "El número de especies de un lugar", "La resiliencia es recuperar el funcionamiento después de una alteración."),
        ("{F} ¿Qué puntaje de producción de madera tiene la opción X?", "5", "La ficha da 5 puntos de producción de madera a la opción X."),
        ("=", "{F} ¿Cuál es el total de puntos de la opción X sumando los cuatro criterios?", "5+2+1+1", "El total suma los puntajes de madera, agua, plagas y hábitat de la opción X.", " puntos"),
        ("=", "{F} ¿Cuál es el total de puntos de la opción Y sumando los cuatro criterios?", "3+4+4+5", "El total suma los puntajes de madera, agua, plagas y hábitat de la opción Y.", " puntos"),
        ("abc", "{F} Según la suma simple, ¿qué opción tiene mejor puntaje total?", "La opción Y", "La opción X", "Empatan", "La opción Y suma 16 y la X suma 9, así que Y es mayor."),
        ("abc", "{F} ¿En qué criterio gana la opción X?", "Producción de madera", "Regulación del agua", "Hábitat para fauna", "Solo en madera X supera a Y, con 5 contra 3."),
        ("=", "{F} Si la producción de madera vale el doble, ¿cuál es el total de la opción X?", "5*2+2+1+1", "El puntaje de madera se multiplica por dos y los demás se suman una vez.", " puntos"),
        ("=", "{F} Si la producción de madera vale el doble, ¿cuál es el total de la opción Y?", "3*2+4+4+5", "El puntaje de madera de Y se duplica y se suman los otros tres criterios.", " puntos"),
        ("abc", "{F} Aun con la madera valiendo el doble, ¿qué opción queda mejor?", "La opción Y", "La opción X", "Quedan en empate", "Con el doble, X suma 14 e Y suma 19, por lo que la decisión no cambia."),
        ("abc", "{F} Una plaga ataca la plantación de un solo tipo de árbol. Según el puntaje de resistencia a plagas, ¿qué se espera?", "Que X sea más vulnerable porque tiene solo 1 punto en ese criterio", "Que X sea más resistente que Y", "Que ambas opciones resistan igual", "Menor puntaje en resistencia indica mayor vulnerabilidad."),
        ("ab", "Una compañera dice: «como Y es mejor, elegiría Y sin mirar ningún dato». ¿Qué falla?", "Los puntajes son de ejemplo y hay que revisar quién los asignó y con qué datos", "Nada: los puntajes son hechos medidos", "Una decisión debe apoyarse en puntajes con fuente conocida, no en una suma sin revisar."),
        ("abc", "¿Qué indica una decisión que cambia al modificar un peso?", "Que es frágil y conviene revisar los pesos", "Que la matriz está perfecta", "Que no importa el peso", "Si la elección depende de un peso discutible, hay que revisar cuánto confías en él."),
        ("abc", "Un bosque pierde una especie de ejemplo, pero otras especies parecidas siguen filtrando el agua. ¿Qué idea ilustra?", "Que especies distintas con funciones parecidas dan estabilidad", "Que las especies no importan", "Que el agua no necesita filtrarse", "Si una especie falta, otra puede compensar su función."),
    ],
    ctx=("abc", "Contexto: una municipalidad de ejemplo debe elegir entre una plantación de un solo árbol de rápido crecimiento y un bosque de varias especies nativas para proteger una cuenca. ¿Qué recomendación es más sólida?", "Comparar con una matriz de varios criterios, declarar los pesos y revisar si la decisión cambia", "Elegir la opción más barata sin comparar", "Elegir la opción que prefiere una sola persona", "Una matriz con criterios y pesos explícitos permite justificar la decisión."),
    sc=[
        ("En Biología de los ecosistemas: ¿qué es una perturbación?", "Un evento que altera un ecosistema, como una sequía o un incendio", "Las perturbaciones alteran el funcionamiento y ponen a prueba la resiliencia."),
        ("ab", "Un compromiso (trade-off) es:", "Ganar en un criterio a costa de otro", "Ganar siempre en todos los criterios", "Las decisiones reales suelen tener ganancias y pérdidas."),
        ("ab", "Los puntajes de una matriz de ejemplo:", "Son valoraciones que hay que justificar", "Son siempre hechos medidos", "Cualquier puntaje debe tener una fuente."),
    ],
    op=("Con la ficha {F}: (1) calcula el total sin pesos de X e Y; (2) elige un criterio que tú consideres más importante, dale peso doble y recalcula; (3) escribe una recomendación en tres oraciones con el criterio, el resultado y una limitación.",
        "(1) X = 9 e Y = 16. (2) Elijo regulación del agua con peso doble: X = 11 e Y = 20. (3) Recomiendo Y porque suma más aun cuando el agua pesa doble. Los puntajes son de ejemplo y deberían apoyarse en datos medidos de la cuenca.",
        ["totales correctos", "recálculo coherente con el peso elegido", "recomendación con criterio y limitación"],
        ["tres respuestas numeradas"],
        ["no aplicar bien el peso", "recomendar sin criterio", "no declarar que los puntajes son de ejemplo"],
        "Pregunta: «¿qué dato real te haría cambiar la recomendación?»."),
    reinforce="Haz una matriz de decisión de dos opciones para el patio de tu liceo (árboles nativos o pasto sintético) con tres criterios y puntajes inventados.",
    extend="Explica con un ejemplo cómo la biodiversidad puede aumentar la resiliencia de un ecosistema agrícola.",
)
