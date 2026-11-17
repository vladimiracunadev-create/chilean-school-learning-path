"""Geografía, territorio y desafíos socioambientales (electivo HC, 3.º y 4.º medio): OAC-01 (espacio geográfico como construcción social), OAC-02 (dinámicas físico-naturales del territorio nacional) y OAC-03 (decisiones sobre los espacios geográficos), 13 clases. Lugares, casos y cifras ficticios o de ejemplo."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz, goma y papel o cuaderno; si quieres, lápices de colores para dibujar los croquis. No se necesita computador ni internet: cada mapa, tabla o texto se describe por escrito en el enunciado. "
             "Los lugares (Valle del Sauce, Bahía Serena, etc.), los grupos y las cifras son ficticios o de ejemplo y sirven para practicar el método de la geografía, no para aprender datos de un territorio real. "
             "Cuando un tema toque los territorios de los pueblos originarios, la información propia la entregan el educador o la educadora tradicional y la comunidad. "
             "Las posturas se presentan con sus razones y sin tomar partido: tu tarea es analizar y evaluar. Trabaja siempre en un lugar seguro; si algo te preocupa, conversa con una persona adulta de confianza.")
build = make_build(MATERIALS)

O1 = "HI-GTYD-3y4-OAC-01"
O2 = "HI-GTYD-3y4-OAC-02"
O3 = "HI-GTYD-3y4-OAC-03"

# ============================================================ OAC-01, clase 1
F = ("Ficha 1 (caso ficticio). El Valle del Sauce, rodeado de cerros y de clima seco, era hace un tiempo un terreno de pastoreo con pocas familias. Hoy tiene un canal de riego, huertas de hortalizas, una escuela, un camino pavimentado y un mercado semanal. "
     "Los actores principales son las familias regantes (usan el agua del canal), una cooperativa agrícola que vende la producción y la municipalidad, que construyó el camino. Cada grupo usa el valle de un modo distinto y le da un valor distinto.")
build(
    O1, 1, F,
    use="Aprenderé a explicar por qué el espacio geográfico es una construcción social: resultado de lo que los grupos humanos hacen en el medio y del significado que le dan, con efectos en varias dimensiones de la vida.",
    prior=["Sé que un mapa representa un lugar.", "Distingo elementos naturales de elementos construidos.", "He estudiado la organización del territorio de Chile en la Formación General."],
    explain=[
        "El espacio geográfico es el espacio que las sociedades ocupan, usan y transforman. No es solo un paisaje natural ni un simple dibujo en un mapa: es el resultado de lo que los grupos humanos hacen sobre el medio (relieve, clima, agua, suelo, vegetación) y de los significados que le dan. Por eso se dice que es una construcción social: un mismo valle puede ser pastizal, huerta, lugar de descanso o motivo de conflicto según quiénes lo usen y para qué.",
        "Para estudiarlo se contextualiza: se pregunta qué actores intervienen (personas, grupos, empresas, instituciones), en qué tiempo ocurre el proceso y a qué escala se observa (el barrio, la comuna, la región o el país). Las interacciones entre los grupos y el medio influyen en varias dimensiones de la vida en sociedad: la económica (trabajo y producción), la social (convivencia y servicios), la cultural (costumbres y valores), la política (decisiones y poder) y la ambiental (agua, suelo y seres vivos).",
        "Un territorio es un espacio que un grupo se apropia: lo usa, lo gestiona y lo siente suyo. Por eso puede haber tensiones cuando varios actores quieren usar un mismo espacio de maneras distintas. En esta clase no se juzga si un uso es bueno o malo: se describe quién transforma el medio, cómo lo hace y qué dimensiones de la vida social se ven afectadas.",
    ],
    vocab=[("espacio geográfico", "espacio que las sociedades ocupan, usan y transforman"), ("construcción social", "resultado de la acción y de los significados de los grupos humanos"), ("territorio", "espacio que un grupo se apropia, usa y siente suyo"), ("actor", "persona, grupo o institución que interviene en un proceso"), ("dimensión", "aspecto de la vida en sociedad: económico, social, cultural, político o ambiental")],
    worked=[
        ("Separar el medio de la obra social", "Una caleta ficticia tiene una bahía abrigada, un muelle de madera construido por los pescadores, un taller de redes y una escuela. ¿Qué es del medio y qué es obra de la sociedad?",
         ["Pregunta si el elemento existía sin intervención humana: la bahía abrigada sí.", "El muelle, el taller y la escuela los construyó un grupo humano."],
         "Medio: la bahía abrigada; obra social: muelle, taller y escuela"),
        ("Reconocer una dimensión", "La cooperativa de la caleta decide vender los mariscos en conjunto para conseguir un mejor precio. ¿Qué dimensión destaca?",
         ["Pregunta qué cambia: la forma de producir y vender.", "Eso corresponde al trabajo y la producción."],
         "La dimensión económica (con un componente social, porque se organizan juntos)"),
    ],
    mistakes=[("Pensar que el espacio geográfico es solo el paisaje natural.", "Se olvida que las sociedades lo transforman y le dan significado.", "Incluye siempre el medio, la acción de los grupos humanos y los significados que le dan."),
              ("Creer que un territorio tiene un único significado para todos.", "Se supone que todos los actores lo ven igual.", "Pregunta qué uso y qué valor le da cada actor al mismo espacio.")],
    T=[
        ("abc", "{F} ¿Cuál de estos elementos del Valle del Sauce es obra de la sociedad y no del medio natural?", "El canal de riego", "El clima seco", "Los cerros que lo rodean", "El canal fue construido por personas, mientras que el clima y los cerros pertenecen al medio natural."),
        ("En Geografía: ¿cómo se llama el espacio que un grupo se apropia, usa, gestiona y siente suyo?", "Territorio", "Esa es la definición de territorio que entrega la explicación de esta clase."),
        ("abc", "{F} ¿Qué actor construyó el camino pavimentado?", "La municipalidad", "La cooperativa agrícola", "Las familias regantes", "La ficha atribuye el camino a la municipalidad y no a los otros dos grupos."),
        ("abc", "¿Qué significa que el espacio geográfico sea una construcción social?", "Que resulta de lo que los grupos hacen en el medio y del significado que le dan", "Que las personas lo crearon desde cero, sin usar el medio natural", "Que solo existe en los mapas que dibuja la sociedad", "Se construye socialmente porque la acción y los significados de los grupos humanos lo transforman sobre un medio ya existente."),
        ("abc", "{F} La cooperativa vende la producción de las huertas. ¿Qué dimensión de la vida en sociedad destaca más esa acción?", "La económica", "La política", "La ambiental", "Vender producción es una actividad de trabajo y comercio, propia de la dimensión económica."),
        ("ab", "{F} Las familias regantes y la cooperativa usan el valle de modos distintos. Esto muestra que", "un mismo espacio puede tener usos y significados distintos para cada actor", "uno de los dos grupos se equivoca al usar el valle", "Cada actor usa y valora el espacio según sus necesidades, de modo que no hay un solo uso posible."),
        ("Un pueblo minero ficticio tiene un cerro con cobre, una quebrada seca, un campamento de viviendas, una planta de procesamiento y un camino de acceso. ¿Cuántos de estos cinco elementos son obra de la sociedad?", "3", "El campamento, la planta y el camino fueron construidos; el cerro y la quebrada son parte del medio."),
        ("abc", "La junta de vecinos del Valle del Sauce organiza cada año una fiesta con comidas y bailes de la zona. ¿Qué dimensión de la vida en sociedad destaca más?", "La cultural", "La económica", "La política", "Las comidas y los bailes tradicionales expresan costumbres y valores, es decir, la dimensión cultural."),
        ("abc", "¿Cuál de estas preguntas ayuda a contextualizar el caso del Valle del Sauce?", "¿Quiénes usan el valle, desde cuándo y a qué escala lo estudiamos?", "¿Cuál es el valle más grande de todos los países?", "¿Qué opina de la zona alguien que nunca la ha visitado?", "Contextualizar es preguntar por actores, tiempo y escala del proceso que se estudia."),
        ("{F} Una vecina dice que el valle «es solo tierra de cultivo» y un joven dice que «es su hogar y su lugar de encuentro». Explica por qué ambas frases pueden ser verdaderas a la vez.", "Porque cada actor le da al mismo espacio un significado distinto según cómo lo usa y lo siente", "El espacio geográfico se construye con usos y significados diversos, que pueden convivir."),
        ("abc", "{F} Un compañero afirma: «El Valle del Sauce es naturaleza pura, porque tiene cerros y agua». ¿Qué observación de la ficha lo contradice?", "Que hay canal, huertas, camino y mercado construidos por la sociedad", "Que el clima del valle es seco", "Que la municipalidad es uno de los actores", "El canal, las huertas y el camino muestran que el valle fue transformado y no es naturaleza intacta."),
        ("abc", "{F} Cinco años después, la cooperativa propone ampliar las huertas con más agua del canal y un grupo de pastores quiere mantener el pastoreo. ¿Qué situación describe el caso?", "Una posible tensión territorial entre actores que quieren usar el espacio de modos distintos", "Un cambio natural del clima del valle", "Una situación sin efectos en ninguna dimensión social", "Dos usos distintos del mismo territorio pueden generar una tensión entre los actores que lo reclaman."),
        ("abc", "Un estudio dice: «Con el canal se transformó el medio y también cambió la vida en sociedad». {F} ¿Qué dato de la ficha respalda la segunda parte de la frase?", "Que se abrieron un mercado semanal y una escuela", "Que el valle está rodeado de cerros", "Que el clima es seco", "El mercado y la escuela son servicios sociales que aparecieron con el cambio, así que muestran efectos en la vida en sociedad."),
    ],
    ctx=("abc", "Un colegio de una comuna ficticia debe decidir cómo presentar su territorio en una feria escolar. ¿Qué presentación muestra mejor el espacio geográfico como construcción social?", "El paisaje junto a lo que las personas hacen y significan en él", "Solo una foto del paisaje, porque no cambia", "Solo la lista de organizaciones, sin mencionar el medio", "Un espacio geográfico incluye el medio y también las acciones y los significados de quienes lo habitan."),
    sc=[
        ("En Geografía: ¿qué es el espacio geográfico?", "El espacio que las sociedades ocupan, usan y transforman en interacción con el medio", "Reúne el medio natural y la acción y los significados de los grupos humanos."),
        ("¿Qué dimensión de la vida en sociedad se refiere al trabajo y la producción?", "La económica", "La dimensión económica trata de cómo se produce, se trabaja y se vende."),
        ("¿Qué tres preguntas ayudan a contextualizar un proceso espacial?", "Qué actores intervienen, en qué tiempo ocurre y a qué escala se observa", "Esos tres elementos permiten ubicar el proceso antes de explicarlo."),
    ],
    op=("Elige uno de estos lugares ficticios: (1) una caleta con muelle, taller de redes y sede de pescadores; (2) un barrio con plaza, feria libre y sede vecinal. Haz una ficha que indique qué elementos son del medio y cuáles son obra de la sociedad, dos actores, una dimensión de la vida en sociedad afectada y una pregunta de contexto sobre el tiempo o la escala.",
        "Barrio. Medio: la ladera donde está. Obra social: plaza, feria y sede. Actores: junta de vecinos y comerciantes de la feria. Dimensión: social, por la convivencia. Pregunta: ¿desde cuándo funciona la feria?",
        ["separa correctamente medio y obra social", "nombra dos actores del lugar elegido", "relaciona un elemento con una dimensión", "formula una pregunta de tiempo o de escala"],
        ["ficha con medio, obra social, actores, dimensión y pregunta"],
        ["llamar «medio» a algo construido", "nombrar un solo actor", "escribir una pregunta que se responde con sí o no"],
        "Pregunta: «¿cómo sabes que ese elemento fue construido y no existía antes?». Si no puede explicarlo, pídele que revise el criterio de la explicación."),
    reinforce="Describe en cinco líneas un lugar de tu barrio: qué elementos son del medio, cuáles fueron construidos y quiénes lo usan.",
    extend="Conversa con una persona mayor de tu entorno sobre cómo era un lugar de tu comuna hace décadas, anota qué actores lo cambiaron y qué dimensiones de la vida social cambiaron.",
)

# ============================================================ OAC-01, clase 2
F = ("Ficha 2 (datos de ejemplo, ficticios). Tabla del Valle del Sauce en tres cortes en el tiempo. Corte 1: población 600 personas, superficie regada 40 hectáreas, 1 escuela. Corte 2: población 900, superficie regada 90 hectáreas, 1 escuela. Corte 3: población 1.500, superficie regada 150 hectáreas, 2 escuelas. "
     "Fuentes: (P) censo municipal de ejemplo, levantado por funcionarios en las tres fechas; (R) relato de una regante que dice «el valle se llenó de gente desde que llegó el agua»; (M) folleto de la cooperativa que afirma «el valle es el más próspero de la zona».")
build(
    O1, 2, F,
    use="Aprenderé a interrogar fuentes (quién las produjo, cuándo y para qué) y a leer indicadores con sus límites, para explicar cómo cambia un espacio sin tratar una fuente como neutral y completa.",
    prior=["Sé que el espacio geográfico se construye socialmente.", "Sé leer una tabla de datos.", "Calculo porcentajes sencillos."],
    explain=[
        "Una fuente es el origen de la información que usamos: un censo, un mapa, una fotografía aérea, un folleto, una entrevista o un relato. Toda fuente fue producida por alguien, en un momento y con un propósito. Por eso se la interroga: ¿quién la produjo?, ¿cuándo?, ¿para qué?, ¿qué muestra y qué deja fuera? Una fuente no es neutral ni completa por el solo hecho de tener cifras, ni inútil por tener un interés: se usa sabiendo desde qué perspectiva habla.",
        "Un indicador es un dato que mide un aspecto de un proceso, como la población, las hectáreas regadas o el número de escuelas. Sirve para comparar cortes en el tiempo o lugares distintos, pero tiene límites: el número de escuelas no dice cuántos estudiantes hay, y la población no dice si las personas viven bien. Conviene leer varios indicadores y contrastarlos con otras fuentes, como los testimonios.",
        "Para medir un cambio relativo se calcula el porcentaje de aumento: se divide el aumento por el valor inicial y se multiplica por 100. Si algo pasa de 50 a 75, el aumento es 25, y 25 dividido por 50 por 100 da un 50 %. Un porcentaje permite comparar cambios en cosas de tamaños muy distintos, siempre que se diga cuál es el valor inicial.",
    ],
    vocab=[("fuente", "origen de la información: censo, mapa, fotografía, relato"), ("indicador", "dato que mide un aspecto de un proceso"), ("perspectiva", "lugar desde el cual una fuente o una persona mira un hecho"), ("corte en el tiempo", "momento fijo en que se toman los datos para comparar"), ("porcentaje de aumento", "aumento dividido por el valor inicial y multiplicado por 100")],
    worked=[
        ("Interrogar una fuente", "Un folleto de una empresa turística ficticia dice que su costa es «la más hermosa». Interroga la fuente.",
         ["Quién la produjo: una empresa; para qué: atraer visitantes.", "Qué deja fuera: opiniones de los vecinos y datos que se puedan comprobar."],
         "Es una fuente con interés comercial: sirve para saber cómo se promociona el lugar, pero hay que contrastarla con otras"),
        ("Leer un indicador con sus límites", "Una comuna ficticia pasó de 2 centros de salud y 8.000 habitantes a 3 centros y 12.000 habitantes. ¿Mejoró la atención?",
         ["Calcula habitantes por centro antes: 8.000 ÷ 2 = 4.000.", "Después: 12.000 ÷ 3 = 4.000."],
         "Hay más centros, pero cada uno atiende a los mismos 4.000 habitantes; el indicador no prueba una mejora por sí solo"),
    ],
    mistakes=[("Usar un solo indicador como prueba de que un lugar está mejor.", "Se olvida que cada indicador mide un aspecto y deja otros fuera.", "Lee varios indicadores y contrástalos con testimonios u otras fuentes."),
              ("Descartar una fuente porque tiene un interés.", "Se confunde interés con falsedad.", "Úsala sabiendo quién la produjo y para qué, y contrástala con otras fuentes.")],
    T=[
        ("=", "{F} ¿Cuántas personas más había en el corte 3 que en el corte 1?", "1500-600", "Se resta la población del corte 1 a la del corte 3 para hallar el aumento.", " personas"),
        ("abc", "{F} ¿Qué fuente de la ficha fue levantada por funcionarios en tres fechas distintas?", "El censo municipal (P)", "El relato de la regante (R)", "El folleto de la cooperativa (M)", "La ficha dice que el censo lo levantaron funcionarios en las tres fechas."),
        ("En Geografía: ¿cómo se llama el dato que mide un aspecto de un proceso, como la población o las hectáreas regadas?", "Indicador", "Un indicador es el dato que mide un aspecto de un proceso."),
        ("abc", "{F} ¿Por qué hay que mirar con cuidado el folleto de la cooperativa (M)?", "Porque lo escribe un actor que tiene interés en mostrar bien el valle", "Porque es una fuente muy antigua", "Porque no contiene ningún dato numérico", "Una fuente se interroga según quién la produjo y para qué, y el folleto lo escribe un actor interesado."),
        ("abc", "{F} El relato (R) dice que el valle «se llenó de gente». ¿Qué indicador de la tabla permite comprobarlo?", "La población en cada corte", "El número de escuelas", "La superficie regada", "La población mide cuánta gente vive en el valle, que es lo que afirma el relato."),
        ("abc", "¿Qué aporta una fuente de testimonio, como el relato de la regante?", "La experiencia de quien vivió el cambio, que los números no muestran", "Una cifra exacta y neutral", "La prueba definitiva de lo ocurrido", "Un testimonio da una mirada vivida, pero es una perspectiva y no una prueba definitiva."),
        ("=", "{F} ¿En cuántas hectáreas aumentó la superficie regada entre el corte 1 y el corte 3?", "150-40", "Se resta la superficie del corte 1 a la del corte 3.", " hectáreas"),
        ("=", "{F} ¿En qué porcentaje aumentó la superficie regada entre el corte 1 y el corte 2? El aumento se divide por el valor inicial y se multiplica por 100.", "(90-40)*100//40", "El aumento es 50 hectáreas y el valor inicial es 40: 50 dividido por 40 por 100 da 125.", " %"),
        ("abc", "Un municipio ficticio dice: «Hay 3 escuelas, así que todos los niños estudian». ¿Qué limita esa conclusión?", "El número de escuelas no dice cuántos niños hay ni cuántos asisten", "Tres es un número demasiado pequeño para medir", "Las escuelas no pueden ser un indicador", "Un indicador mide un solo aspecto: tener escuelas no prueba que todos los niños estén matriculados."),
        ("abc", "{F} ¿Qué conclusión se puede sostener con los datos de la tabla?", "La población y la superficie regada crecieron en cada corte", "Todas las familias viven mejor en el corte 3", "El agua fue la única causa del aumento de población", "La tabla muestra crecimiento de dos indicadores, pero no mide bienestar ni prueba una causa única."),
        ("abc", "{F} ¿Qué pregunta ayuda más a evaluar el folleto (M)?", "¿Con qué datos comprueba que el valle es «el más próspero» y comparado con cuáles?", "¿Está de acuerdo con la opinión de la mayoría?", "¿Es más corto que las otras fuentes?", "Evaluar una afirmación exige pedir la evidencia y el punto de comparación que la sostienen."),
        ("abc", "{F} Si el censo (P) hubiera contado solo a los hombres adultos, ¿qué problema tendría el indicador de población?", "Subestimaría la población y sesgaría las conclusiones", "Ninguno, porque igual sería un censo", "Solo cambiaría el año de los datos", "Un indicador que deja fuera a parte de la población no la representa y sesga lo que se concluye."),
        ("abc", "{F} Para contrastar las tres fuentes sobre un mismo cambio del valle, ¿qué estrategia es más sólida?", "Comparar qué dice cada una, quién la produjo y si los datos coinciden", "Quedarse con la más reciente", "Quedarse con la que tiene más números", "Contrastar fuentes es compararlas por su productor, su propósito y la coincidencia de sus datos."),
    ],
    ctx=("abc", "Un diario escolar ficticio quiere publicar «El barrio mejoró mucho». Tiene dos datos: las áreas verdes subieron de 2 a 4 y los robos denunciados subieron de 10 a 14. ¿Qué conviene hacer?", "Informar ambos indicadores y explicar qué mide cada uno", "Publicar solo el de áreas verdes, porque es positivo", "Publicar solo el de robos, porque es más importante", "Cada indicador muestra un aspecto distinto; ocultar uno entregaría una imagen incompleta."),
    sc=[
        ("En Geografía, territorio y desafíos socioambientales: En Geografía: ¿qué es un indicador?", "Un dato que mide un aspecto de un proceso", "Mide, por ejemplo, población, superficie o servicios."),
        ("¿Qué dos preguntas básicas se hacen a una fuente sobre su producción?", "Quién la produjo y para qué", "Saber quién la hizo y con qué propósito permite entender su perspectiva."),
        ("Para calcular un porcentaje de aumento, ¿qué se divide por el valor inicial?", "El aumento", "El aumento dividido por el valor inicial y multiplicado por 100 da el porcentaje."),
    ],
    op=("Elige un caso ficticio. Caso 1 (caleta): pescadores inscritos 30, 45 y 60 en tres cortes; muelles 1, 1 y 2; fuentes: registro municipal y un afiche de la cooperativa que dice «la mejor caleta del litoral». Caso 2 (barrio): vecinos 400, 520 y 700 en tres cortes; áreas verdes 1, 1 y 2; fuentes: censo vecinal y una nota de un negocio que dice «el barrio ideal». "
        "Interroga las dos fuentes (quién, para qué, qué deja fuera), calcula el porcentaje de aumento entre los cortes 1 y 2 de un indicador y escribe una conclusión prudente.",
        "Caso 2. El censo vecinal lo hacen vecinos para planificar; la nota la escribe un negocio que quiere atraer clientes. Vecinos: de 400 a 520, aumento 120, 120 ÷ 400 × 100 = 30 %. Conclusión: la población creció, pero no sabemos si el barrio es «ideal».",
        ["interroga a las dos fuentes con quién, para qué y qué deja fuera", "calcula bien el porcentaje de aumento", "no presenta la fuente interesada como prueba", "escribe una conclusión prudente"],
        ["ficha con interrogación de fuentes, cálculo y conclusión"],
        ["dividir por el valor final en vez del inicial", "aceptar el afiche como dato neutral", "concluir bienestar solo con la población"],
        "Pregunta: «¿qué indicador usarías además de este para saber si las personas viven mejor?». Si no propone otro, pídele que lea de nuevo los límites de un indicador."),
    reinforce="Elige un anuncio o un afiche que hayas visto sobre tu comuna y escribe quién lo produjo, para qué y qué datos faltarían para comprobar lo que dice.",
    extend="Busca dos fuentes distintas sobre un mismo cambio en tu barrio (por ejemplo, un relato de una persona mayor y una noticia) y anota en qué coinciden y en qué se diferencian.",
)

# ============================================================ OAC-01, clase 3
F = ("Ficha 3 (relatos ficticios). Tres explicaciones de por qué creció el Valle del Sauce. Regante: «Creció porque se construyó el canal: sin agua no hay huertas ni trabajo.» "
     "Concejala: «Creció porque la municipalidad pavimentó el camino y el mercado llegó a la zona.» Ambientalista: «Creció, pero a costa de bajar el nivel del pozo que abastece al pueblo; el crecimiento no es gratis.»")
build(
    O1, 3, F,
    use="Aprenderé a comparar las causas que explican un cambio en el espacio y las perspectivas de distintos actores, sin buscar una causa única ni suponer que una perspectiva es la correcta.",
    prior=["Sé interrogar una fuente.", "Sé leer indicadores con sus límites.", "Reconozco actores y dimensiones en un caso."],
    explain=[
        "La causalidad es la relación entre un hecho y aquello que lo provocó. En geografía casi nunca hay una sola causa: los cambios en un territorio suelen tener varias causas que actúan juntas, de distinto tipo (económicas, políticas, naturales, culturales). Se distingue la causa próxima, la más cercana al hecho, de la causa de fondo, que crea las condiciones desde antes. Que dos hechos ocurran a la vez no prueba que uno cause al otro.",
        "Una perspectiva es el lugar desde el cual un actor mira un proceso, según su experiencia, sus intereses y sus valores. La regante destaca el agua, la concejala destaca el camino y el mercado, el ambientalista destaca el costo sobre el pozo. Ninguna de las tres necesariamente miente: cada una ilumina una parte de la explicación. Comparar perspectivas significa ver qué causa subraya cada una, qué deja fuera y con qué evidencia podría comprobarse.",
        "Para comparar se hace una tabla con tres columnas: actor, causa que destaca y consecuencia que valora. Luego se pregunta qué evidencia falta para decidir cuánto pesa cada causa. Una buena explicación geográfica suele combinar varias causas y reconocer que algunas perspectivas ven costos que otras no ven.",
    ],
    vocab=[("causalidad", "relación entre un hecho y lo que lo provocó"), ("causa próxima", "causa más cercana al hecho"), ("causa de fondo", "condición que crea las bases del hecho desde antes"), ("perspectiva", "lugar desde el cual un actor mira un proceso"), ("multicausalidad", "existencia de varias causas que actúan juntas")],
    worked=[
        ("Distinguir causa de consecuencia", "En una comuna ficticia se construyó una nueva carretera y, después, llegaron más empresas de transporte. ¿Cuál es la causa y cuál la consecuencia?",
         ["Pregunta qué ocurrió primero y qué lo hizo posible: la carretera.", "Lo que vino después y depende de ella son las empresas."],
         "Causa: la carretera; consecuencia: la llegada de empresas (aunque pueden existir otras causas)"),
        ("Comparar dos perspectivas", "Sobre una feria libre ficticia, una comerciante dice «trae empleo» y una vecina dice «trae ruido y basura». ¿Qué destaca cada una?",
         ["La comerciante destaca el efecto económico.", "La vecina destaca el efecto sobre la convivencia y el ambiente."],
         "Ambas ven efectos reales pero distintos; se necesita evidencia para ver cuánto pesa cada uno"),
    ],
    mistakes=[("Buscar «la» causa de un cambio y descartar las demás.", "Se supone que un hecho espacial tiene una sola explicación.", "Reconoce que varias causas pueden actuar juntas y evalúa cuánto pesa cada una."),
              ("Pensar que si dos hechos ocurren a la vez, uno es causa del otro.", "Se confunde coincidencia con causalidad.", "Busca evidencia de cómo un hecho produce al otro antes de afirmarlo.")],
    T=[
        ("abc", "{F} ¿Qué causa destaca la regante para explicar el crecimiento del valle?", "La construcción del canal de riego", "El pavimento del camino", "La baja del pozo", "La regante dice que sin el canal no hay agua, huertas ni trabajo."),
        ("abc", "{F} ¿Qué actor destaca un costo ambiental del crecimiento?", "El ambientalista", "La concejala", "La regante", "El ambientalista menciona que bajó el nivel del pozo que abastece al pueblo."),
        ("En Geografía: ¿cómo se llama la relación entre un hecho y lo que lo provocó?", "Causalidad", "La causalidad es la relación entre un hecho y su causa."),
        ("abc", "{F} Las tres explicaciones del crecimiento del valle son distintas porque", "cada actor mira el proceso desde su experiencia y sus intereses", "solo una de ellas puede ser verdadera", "ninguna tiene relación con el valle", "Cada actor destaca una parte del proceso desde su perspectiva, sin que necesariamente mienta."),
        ("abc", "¿Qué es la multicausalidad?", "Que varias causas actúan juntas para producir un cambio", "Que un cambio siempre tiene la misma causa en todos los lugares", "Que las causas de un cambio no se pueden conocer", "Según la explicación, los cambios en un territorio suelen tener varias causas combinadas."),
        ("abc", "{F} ¿Qué causa de tipo político aparece en las explicaciones?", "La decisión de la municipalidad de pavimentar el camino", "La construcción del canal por las familias", "La baja del nivel del pozo", "La decisión de una institución pública es una causa política, como la del camino."),
        ("Una comuna ficticia construyó un puerto y, el mismo año, subió la temperatura media. Un estudiante concluye que el puerto causó el alza. ¿Qué error comete?", "Confundir coincidencia con causalidad", "Que dos hechos ocurran a la vez no prueba que uno cause al otro."),
        ("abc", "{F} Un vecino dice: «La concejala y la regante se contradicen». ¿Qué respuesta es más sólida?", "No necesariamente: el canal y el camino pueden ser causas que actuaron juntas", "Sí, porque solo una de las dos puede tener razón", "No, porque ninguna de las dos habla del valle", "Si ambas causas son compatibles, el crecimiento pudo explicarse por varias causas combinadas."),
        ("abc", "{F} ¿Qué evidencia ayudaría a decidir cuánto pesó el camino en el crecimiento del valle?", "Datos de cuántas familias llegaron después de pavimentar el camino y por qué vinieron", "La opinión del actor que más habla", "La fecha en que se fundó la municipalidad", "Para pesar una causa hacen falta datos que muestren cómo se relaciona con el cambio estudiado."),
        ("{F} ¿Qué consecuencia del crecimiento valora el ambientalista que los otros dos relatos no mencionan?", "El descenso del nivel del pozo de agua potable", "Es el único relato que habla de un costo para el abastecimiento de agua."),
        ("abc", "{F} Una estudiante escribe: «El ambientalista está en contra del crecimiento». Con lo que dice la ficha, ¿qué es más preciso?", "Reconoce que el valle creció, pero advierte un costo sobre el pozo", "Quiere que el valle vuelva a ser un terreno de pastoreo", "No tiene ninguna evidencia", "El relato dice «creció, pero...»: acepta el crecimiento y señala un costo que se debe considerar."),
        ("abc", "{F} Para comparar las tres explicaciones, ¿qué columnas sirven mejor en la tabla?", "Actor, causa que destaca y consecuencia que valora", "Actor, edad y color favorito", "Fecha de publicación, largo del texto y autor", "La comparación se centra en la causa y la consecuencia que cada actor subraya."),
        ("abc", "{F} ¿Cuál es una buena explicación geográfica del crecimiento del valle?", "Un conjunto de causas (canal, camino, mercado) con costos y beneficios distintos para cada actor", "El canal, porque fue lo primero que se construyó", "Una causa elegida al azar", "Combinar varias causas y reconocer sus costos desiguales es lo que pide una explicación geográfica."),
    ],
    ctx=("abc", "Dos vecinos de una población ficticia discuten por qué subió el precio de las casas. Uno dice que fue por una nueva línea de buses; la otra, por la llegada de una universidad. ¿Qué conviene hacer?", "Reunir datos para ver si ambas causas actuaron y cuánto pesó cada una", "Elegir la causa del vecino que habla más fuerte", "Decir que no se puede saber nada", "Frente a causas posibles se busca evidencia, sin elegir por autoridad ni renunciar a explicar."),
    sc=[
        ("En Geografía: ¿qué es una perspectiva?", "El lugar desde el cual un actor mira un proceso, según su experiencia e intereses", "Cada actor ve el proceso desde su experiencia, sus intereses y sus valores."),
        ("¿Cómo se llama la causa que crea las condiciones de un hecho desde antes?", "Causa de fondo", "La causa de fondo prepara las condiciones, a diferencia de la próxima, que está cerca del hecho."),
        ("¿Prueba la coincidencia de dos hechos que uno cause al otro?", "No", "Hace falta evidencia de cómo uno produce el otro."),
    ],
    op=("Lee estas dos versiones ficticias sobre un nuevo mercado cercano a una población. Vecina A: «Trajo empleo y precios más bajos.» Vecino B: «Trajo tránsito, ruido y menos espacio para los niños.» Haz una tabla de tres columnas (actor, causa o efecto que destaca, dimensión de la vida en sociedad) y escribe una explicación que combine ambas, más una evidencia que pedirías para saber cuál efecto pesa más.",
        "Vecina A: efecto económico, dimensión económica. Vecino B: efectos sobre convivencia y ambiente, dimensión social. Explicación: el mercado tiene beneficios y costos que no sienten igual todos. Evidencia: encuesta de empleos creados y medición del tránsito en horas punta.",
        ["completa la tabla con actor, efecto y dimensión", "combina las dos versiones sin descartar ninguna", "propone una evidencia comprobable", "evita afirmar una causa única"],
        ["tabla de tres columnas, explicación de dos o tres líneas y evidencia propuesta"],
        ["decidir que una versión es falsa sin evidencia", "mezclar causas con consecuencias", "proponer una evidencia que no se puede comprobar"],
        "Pregunta: «¿qué efecto ve cada persona y cuál no ve?». Si responde con una sola versión, pídele que relea las dos columnas."),
    reinforce="Elige un cambio reciente de tu barrio (por ejemplo, una nueva ciclovía o un local nuevo) y escribe dos causas posibles y dos perspectivas distintas sobre él.",
    extend="Entrevista a dos personas de edades distintas sobre un mismo cambio de tu comuna y compara qué causas destaca cada una y qué dimensiones menciona.",
)

# ============================================================ OAC-01, clase 4
F = ("Ficha 4 (cadena de cambios ficticia en el Valle del Sauce). (1) Llega el canal de riego. (2) Crecen las huertas. (3) Hay más trabajo y llegan nuevas familias. (4) La escuela se llena y se abre un segundo curso. (5) Aumenta el consumo de agua y baja el nivel del pozo del pueblo. "
     "Continuidad: la fiesta de la cosecha se sigue celebrando cada año con las mismas comidas. Consecuencias desiguales: para las familias recién llegadas hay trabajo; para los pastores hay menos espacio de pastoreo.")
build(
    O1, 4, F,
    use="Aprenderé a explicar las relaciones entre dimensiones y las consecuencias de un cambio espacial, distinguiendo continuidad y cambio, y reconociendo que las consecuencias no son iguales para todos los actores.",
    prior=["Reconozco actores, dimensiones y escalas.", "Comparo causas y perspectivas.", "Sé que las fuentes tienen límites."],
    explain=[
        "Un cambio en el espacio rara vez se queda en una sola dimensión. Una obra económica, como un canal, altera lo social (llegan familias y se llenan las escuelas), lo ambiental (se usa más agua), lo cultural (cambian las costumbres) y lo político (se toman nuevas decisiones). Explicar las relaciones es seguir esa cadena de cambios: qué provocó qué, y hasta dónde llega el efecto. Una consecuencia es lo que resulta de un proceso, y puede aparecer a corto plazo, a mediano o a largo plazo.",
        "Las consecuencias casi nunca son iguales para todos. El mismo cambio da trabajo a unas familias y quita espacio a otras. Por eso se pregunta quién gana y quién pierde, y en qué escala: lo que beneficia al valle puede perjudicar al pozo del pueblo. Las consecuencias también pueden retroalimentar el proceso: si baja el agua, tal vez se limiten las huertas, y el ciclo cambia.",
        "La continuidad es lo que permanece mientras otras cosas cambian, como una fiesta o una forma de organizarse. Al explicar un territorio se necesita ver los dos: qué cambió, qué siguió igual y qué relaciones unen ambos. Una explicación completa nombra los actores, ordena los cambios en el tiempo y no esconde las consecuencias desiguales.",
    ],
    vocab=[("consecuencia", "resultado de un proceso o cambio"), ("cadena de cambios", "serie de hechos en que cada uno provoca el siguiente"), ("continuidad", "lo que permanece mientras otras cosas cambian"), ("retroalimentación", "efecto que vuelve sobre su propia causa"), ("corto y largo plazo", "efectos que aparecen pronto o después de mucho tiempo")],
    worked=[
        ("Seguir una cadena de cambios", "En una población ficticia se instala un mercado, llegan más compradores y el tránsito aumenta. ¿Qué relación hay entre las dimensiones?",
         ["Lo económico (mercado) provoca lo social (más personas en el sector).", "Eso provoca lo ambiental y de convivencia (ruido, tránsito)."],
         "Un cambio económico produce cambios sociales y ambientales encadenados"),
        ("Distinguir continuidad y cambio", "Un puerto ficticio incorporó grúas modernas, pero la fiesta anual de la caleta se celebra igual. ¿Qué es cambio y qué es continuidad?",
         ["Las grúas son una transformación del espacio productivo.", "La fiesta permanece igual."],
         "Cambio: las grúas; continuidad: la fiesta anual"),
    ],
    mistakes=[("Explicar un cambio solo en una dimensión.", "Se olvida que las dimensiones de la vida en sociedad están conectadas.", "Pregunta qué otras dimensiones se ven afectadas y en qué orden."),
              ("Suponer que las consecuencias son iguales para todos los actores.", "Se mira el proceso solo desde un grupo.", "Pregunta quién gana, quién pierde y en qué escala.")],
    T=[
        ("abc", "{F} ¿Qué ocurre justo después de que crecen las huertas en la cadena de cambios?", "Hay más trabajo y llegan nuevas familias", "Se abre un segundo curso en la escuela", "Baja el nivel del pozo", "En la ficha, el paso (3) sigue al (2): más trabajo y llegada de nuevas familias."),
        ("abc", "{F} ¿Cuál es un ejemplo de continuidad en el valle?", "La fiesta de la cosecha, que se celebra igual cada año", "La escuela con un segundo curso", "El aumento del consumo de agua", "La fiesta permanece igual mientras otras cosas cambian, lo que define la continuidad."),
        ("En Geografía: ¿cómo se llama el resultado de un proceso o cambio?", "Consecuencia", "Una consecuencia es lo que resulta de un proceso o cambio."),
        ("abc", "{F} ¿Qué dimensión se ve afectada cuando baja el nivel del pozo?", "La ambiental", "La cultural", "La política", "El pozo es un recurso de agua: su descenso afecta directamente el ambiente."),
        ("abc", "{F} La escuela abre un segundo curso por la llegada de nuevas familias. ¿Qué relación muestra?", "Un cambio económico produce un cambio social", "Un cambio cultural produce uno económico", "No hay relación entre ambos", "La llegada de familias por el trabajo agrícola aumenta la demanda de servicios sociales."),
        ("abc", "¿Qué es la retroalimentación en un proceso?", "Un efecto que vuelve sobre su propia causa", "Una causa que se olvida con el tiempo", "Una consecuencia que no tiene explicación", "La retroalimentación ocurre cuando una consecuencia modifica lo que la originó."),
        ("{F} Para los pastores del valle, ¿qué consecuencia tuvo el cambio?", "Menos espacio de pastoreo", "La ficha dice que para los pastores hay menos espacio de pastoreo."),
        ("abc", "{F} ¿Qué consecuencia a largo plazo podría tener que el pozo baje cada año?", "Una limitación futura de las huertas si falta agua", "Una celebración más grande de la fiesta", "Menos familias interesadas en el trabajo agrícola a corto plazo", "Si el recurso se agota, se limita la actividad que lo usa, lo que retroalimenta el proceso."),
        ("abc", "Una comuna ficticia construye un parque. ¿Qué cadena de relaciones entre dimensiones es más coherente?", "Parque (ambiental), más encuentros vecinales (social), nuevos comercios cercanos (económica)", "Nuevos comercios cercanos (económica), luego el parque (ambiental), luego más encuentros vecinales (social)", "Parque (ambiental), más encuentros vecinales (social), y esos encuentros explican por qué se construyó el parque (ambiental)", "La primera cadena sigue el orden del cambio: el parque provoca los encuentros y estos atraen comercios; las otras invierten causa y consecuencia."),
        ("{F} Una estudiante dice: «El canal fue positivo para todos». Con la ficha, explica por qué esa afirmación no es exacta.", "Porque para los pastores significó menos espacio y para el pozo, más presión", "Los efectos del cambio no son iguales para todos los actores ni todos los recursos."),
        ("abc", "{F} ¿Qué dato falta para evaluar a largo plazo las consecuencias del consumo de agua?", "Cuánta agua entra al pozo cada año comparada con la que se extrae", "Cuántas comidas se preparan en la fiesta", "Cuántos años tiene la escuela", "Para saber si el pozo se agota hay que comparar entrada y extracción de agua."),
        ("abc", "{F} Un informe propone: «Cuidemos solo el pozo y olvidemos a los pastores». ¿Qué problema tiene?", "Ignora una consecuencia desigual que afecta a otro actor", "No incluye ninguna cifra", "Habla de un lugar equivocado", "Una explicación completa considera todas las consecuencias y a todos los actores afectados."),
        ("abc", "{F} Para un informe completo del valle, ¿qué estructura es más adecuada?", "Cambios en orden, continuidades, consecuencias para cada actor y evidencia de apoyo", "Una lista de cerros y quebradas", "Una opinión sin datos", "Un informe completo ordena cambios, continuidades y consecuencias desiguales, y los respalda con evidencia."),
    ],
    ctx=("abc", "Una comuna costera ficticia planea un nuevo paseo frente al mar. Los comerciantes esperan más clientes; los pescadores temen perder acceso a la playa. ¿Qué enfoque explica mejor el caso?", "Describir las consecuencias para cada actor y las relaciones entre dimensiones", "Anotar solo los beneficios para los comerciantes", "Anotar solo el acceso de los pescadores", "Un enfoque completo analiza consecuencias y relaciones para todos los actores involucrados."),
    sc=[
        ("En Geografía: ¿qué es la continuidad en un proceso espacial?", "Lo que permanece mientras otras cosas cambian", "Es lo que sigue igual en medio de las transformaciones."),
        ("¿Son iguales las consecuencias de un cambio para todos los actores?", "No", "Un mismo cambio puede beneficiar a unos y perjudicar a otros."),
        ("¿Qué es una cadena de cambios?", "Una serie de hechos en que cada uno provoca el siguiente", "Permite seguir cómo un cambio se propaga a otras dimensiones."),
    ],
    op=("Elige uno de estos cambios ficticios: (1) se abre una ciclovía que atraviesa un barrio; (2) se cierra la única panadería de un pueblo pequeño. Arma una cadena de al menos cuatro cambios que conecte dimensiones distintas, señala una continuidad posible y describe una consecuencia distinta para dos actores.",
        "Ciclovía. Cadena: nueva ciclovía (política), más personas en bicicleta (social), menos autos en la calle (ambiental), más ventas en cafés cercanos (económica). Continuidad: la feria de los sábados. Consecuencias: ciclistas ganan seguridad; automovilistas pierden estacionamiento.",
        ["la cadena tiene al menos cuatro pasos en orden", "conecta al menos tres dimensiones distintas", "indica una continuidad", "muestra consecuencias distintas para dos actores"],
        ["cadena de cambios, continuidad y dos consecuencias para dos actores"],
        ["listar hechos sueltos sin relación", "describir las consecuencias de un solo actor", "olvidar la continuidad"],
        "Pregunta: «¿por qué el paso 2 ocurre después del paso 1?». Si no hay razón, pídele que reordene la cadena."),
    reinforce="Elige una obra reciente de tu barrio y escribe cuatro consecuencias en dimensiones distintas, con un actor beneficiado y otro perjudicado.",
    extend="Compara por escrito cómo cambiaron dos barrios de tu comuna tras una obra importante y qué continuidades se mantuvieron en cada uno.",
)

# ============================================================ OAC-02, clase 1
F = ("Ficha 1 (corte esquemático ficticio, solo para practicar). Una franja de la zona central de Chile vista de oeste a este: (1) océano Pacífico; (2) playas y terrazas costeras; (3) cordillera de la Costa, cerros bajos; (4) depresión intermedia, valle plano con ríos y suelos fértiles; (5) cordillera de los Andes, alta, con nieve en invierno. "
     "Una corriente marina fría recorre la costa hacia el norte. Bajo el océano, una placa tectónica se hunde bajo la placa sobre la que está el continente.")
build(
    O2, 1, F,
    use="Aprenderé a ubicar las grandes unidades del relieve y del clima de Chile y a nombrar las dinámicas físico-naturales (tectónica, clima, aguas, vegetación) que configuran el territorio, con sus escalas y sus tiempos.",
    prior=["Reconozco que el espacio se construye socialmente.", "Sé leer un corte o perfil esquemático.", "Conozco la ubicación de Chile entre los Andes y el Pacífico."],
    explain=[
        "Las dinámicas físico-naturales son los procesos del medio que cambian el territorio: el movimiento de las placas tectónicas, la erosión, el clima, el ciclo del agua, el crecimiento de la vegetación. Configuran el relieve (montañas, valles, costa), el clima, las aguas y los ambientes en que viven las sociedades. Actúan a escalas de tiempo muy distintas: un temblor dura segundos, la formación de una cordillera toma millones de años.",
        "Chile es un país largo y angosto entre la cordillera de los Andes, al este, y el océano Pacífico, al oeste. En la zona central se distinguen, de oeste a este, la costa, la cordillera de la Costa, la depresión intermedia y la cordillera de los Andes. La placa de Nazca se hunde bajo la placa Sudamericana (subducción), lo que explica la alta frecuencia de terremotos y la presencia de volcanes, y también el alzamiento de los Andes.",
        "El clima cambia con la latitud y con el relieve: es muy seco en el norte, de tipo mediterráneo en el centro y lluvioso y frío hacia el sur. La corriente marina fría de Humboldt, que sube por la costa, influye en el clima costero. Los ambientes dependen unos de otros (interdependencia): la nieve alimenta los ríos, los ríos riegan los valles y los valles sostienen la vida en sociedad. Esa relación puede ser frágil si uno de sus eslabones se altera.",
    ],
    vocab=[("dinámica físico-natural", "proceso del medio que cambia el territorio"), ("placa tectónica", "gran bloque de la corteza terrestre que se mueve lentamente"), ("subducción", "hundimiento de una placa bajo otra"), ("depresión intermedia", "valle plano que se extiende entre la cordillera de la Costa y los Andes"), ("interdependencia", "relación en que cada elemento depende de otros")],
    worked=[
        ("Ubicar las unidades en el corte", "En el corte esquemático oeste-este, ¿qué unidad se encuentra entre la cordillera de la Costa y los Andes?",
         ["Recorre el corte de oeste a este: océano, playas, cordillera de la Costa.", "Sigue un valle plano con ríos y, después, los Andes."],
         "La depresión intermedia"),
        ("Relacionar causa físico-natural y consecuencia", "Un barrio ficticio de la costa sufre temblores frecuentes. ¿Qué dinámica físico-natural lo explica?",
         ["Chile está en un borde donde una placa se hunde bajo otra.", "Ese movimiento acumula tensión que se libera como sismos."],
         "La subducción de la placa de Nazca bajo la placa Sudamericana"),
    ],
    mistakes=[("Pensar que las dinámicas físico-naturales actúan siempre rápido.", "Se confunde un terremoto con el proceso que forma una cordillera.", "Distingue procesos de segundos de procesos de millones de años."),
              ("Decir que el clima de Chile es igual de norte a sur.", "Se ignora el efecto de la latitud y del relieve.", "Compara norte, centro y sur y explica qué cambia en cada zona.")],
    T=[
        ("abc", "{F} ¿Qué unidad del relieve se encuentra más al este en el corte?", "La cordillera de los Andes", "La cordillera de la Costa", "La depresión intermedia", "El corte se recorre de oeste a este y termina en los Andes."),
        ("En Geografía: ¿cómo se llama el hundimiento de una placa tectónica bajo otra?", "Subducción", "La explicación define subducción como el hundimiento de una placa bajo otra."),
        ("abc", "{F} ¿Hacia dónde recorre la costa la corriente marina fría?", "Hacia el norte", "Hacia el sur", "Hacia el este", "La ficha dice que la corriente fría recorre la costa hacia el norte."),
        ("abc", "¿Qué explica la alta frecuencia de terremotos y la presencia de volcanes en Chile?", "La placa de Nazca que se hunde bajo la Sudamericana", "Los vientos que soplan desde el océano", "Los ríos que bajan de los Andes", "La subducción acumula tensión que se libera en sismos y sostiene el vulcanismo."),
        ("abc", "{F} ¿Qué ambiente del corte sostiene la vida agrícola con ríos y suelos fértiles?", "La depresión intermedia", "Las playas y terrazas costeras", "La cima de los Andes", "El valle plano con ríos y suelos fértiles es la depresión intermedia."),
        ("ab", "Según la explicación, el clima de Chile", "cambia con la latitud y con el relieve", "depende solo de la distancia al mar", "Es seco en el norte, mediterráneo en el centro y lluvioso hacia el sur, por latitud y relieve."),
        ("abc", "Un temblor dura segundos y la formación de una cordillera toma millones de años. ¿Qué muestra esto?", "Que las dinámicas físico-naturales actúan a escalas de tiempo muy distintas", "Que la cordillera se formó con un solo temblor", "Que el tiempo no influye en el relieve", "Las dinámicas tienen duraciones muy diferentes, desde segundos hasta millones de años."),
        ("abc", "{F} Una familia vive en la playa y otra en el valle plano. ¿Qué relación de interdependencia explica que el agua del valle venga de los Andes?", "La nieve de los Andes alimenta los ríos que riegan el valle", "El océano trae agua dulce al valle", "La cordillera de la Costa produce los ríos", "La nieve se derrite y alimenta ríos que riegan los valles, un eslabón de la cadena."),
        ("abc", "¿Qué elemento de un territorio cambia más lentamente?", "El relieve de una cordillera", "El caudal de un río tras una lluvia", "El estado de la vegetación en una estación", "Una cordillera se forma en millones de años, mucho más lento que los otros cambios."),
        ("{F} Si desaparecieran las nieves de los Andes, explica qué pasaría con el valle según la interdependencia de la cadena.", "Los ríos tendrían menos agua y el valle tendría menos riego para sus cultivos y su población", "La nieve alimenta los ríos, los ríos riegan el valle y el valle sostiene la vida en sociedad."),
        ("abc", "{F} Un estudiante dice: «Los terremotos son un problema solo de la costa». ¿Qué corrección es más acertada?", "Los sismos se sienten también en valles y montañas, aunque la placa se hunda bajo el océano", "Tiene razón, porque la placa de Nazca está solo bajo la costa", "Tiene razón, porque las cordilleras detienen los sismos", "Las ondas de un sismo viajan por el territorio, por lo que se sienten también lejos de la costa."),
        ("abc", "{F} Un colegio quiere explicar por qué el centro de Chile tiene un valle largo y plano entre dos cordilleras. ¿Qué ubicación aparece en el corte?", "Entre la cordillera de la Costa y los Andes", "Entre el océano y las playas", "Dentro del océano Pacífico", "El corte muestra que la depresión intermedia queda entre las dos cordilleras."),
        ("abc", "Una sociedad que dependiera solo de un río alimentado por nieve, ¿qué fragilidad tendría?", "Si disminuyera la nieve, bajaría el agua disponible", "Que el río corre hacia el este", "Que el valle tiene suelos fértiles", "Depender de un solo eslabón vuelve frágil a la sociedad si ese eslabón se altera."),
    ],
    ctx=("abc", "Un municipio ficticio de la costa prepara una guía escolar sobre su territorio. Quiere explicar por qué hay sismos, un valle fértil y un clima de lluvias en invierno. ¿Qué enfoque conviene?", "Relacionar placas, relieve y clima como dinámicas físico-naturales conectadas", "Describir solo el clima", "Explicar solo los sismos", "Las dinámicas del medio se explican en conjunto, porque el relieve, el clima y los sismos están conectados."),
    sc=[
        ("En Geografía: ¿qué es una dinámica físico-natural?", "Un proceso del medio que cambia el territorio", "Por ejemplo, el movimiento de las placas o la erosión."),
        ("¿Qué placa se hunde bajo la placa Sudamericana frente a Chile?", "La placa de Nazca", "La explicación nombra a la placa de Nazca como la que se hunde."),
        ("¿Qué es la interdependencia entre ambientes?", "Que cada elemento depende de otros, como la nieve, el río y el valle", "Una alteración en un eslabón afecta a los demás."),
    ],
    op=("Dibuja un corte esquemático de oeste a este de la zona central de Chile con las cinco unidades de la ficha y escribe una frase en cada una sobre su importancia para la vida en sociedad (por ejemplo, puerto, cultivo, agua, riesgo sísmico). Agrega una flecha que muestre una relación de interdependencia.",
        "Océano: pesca y puerto. Playas: turismo. Cordillera de la Costa: bosque y suelo. Depresión intermedia: cultivos y ciudades. Andes: nieve y agua. Flecha: nieve alimenta ríos que riegan el valle.",
        ["dibuja las cinco unidades en el orden correcto", "relaciona cada unidad con la vida en sociedad", "incluye una flecha de interdependencia", "usa términos geográficos con precisión"],
        ["corte esquemático con cinco unidades, cinco frases y una flecha"],
        ["invertir el orden oeste-este", "olvidar la depresión intermedia", "no explicar la relación"],
        "Pregunta: «¿qué pasaría en tu esquema si faltara la nieve de los Andes?». Si no puede responder, pídele que revise la flecha."),
    reinforce="Copia en tu cuaderno el corte de la ficha y escribe un riesgo y un recurso posibles en cada unidad.",
    extend="Pregunta a una persona de tu entorno qué temblor o fenómeno natural recuerda y anota qué dinámica del medio lo explica.",
)

# ============================================================ OAC-02, clase 2
F = ("Ficha 2 (datos de ejemplo, ficticios). Precipitación anual de tres ciudades: Ciudad N (zona norte), 5 mm; Ciudad C (zona central), 350 mm; Ciudad S (zona sur), 1.800 mm. "
     "Caudal medio mensual del río Claro (de ejemplo, en metros cúbicos por segundo): junio 25; agosto 40; octubre 70; diciembre 120; febrero 90; abril 35. "
     "Fuentes: (E) estación meteorológica de ejemplo con instrumentos calibrados; (V) relato de un agricultor que dice «este año llovió poquísimo»; (P) nota de prensa sin autor que dice «el río está más seco que nunca».")
build(
    O2, 2, F,
    use="Aprenderé a interrogar datos y fuentes del medio físico (precipitación, caudal, temperatura) para describir el clima y el régimen de un río, reconociendo sus límites y su escala.",
    prior=["Sé leer tablas y calcular diferencias.", "Conozco las grandes unidades del relieve de Chile.", "Sé que una fuente tiene productor y propósito."],
    explain=[
        "Para estudiar las dinámicas del medio se usan indicadores medibles: la precipitación (cuánta agua cae, en milímetros), la temperatura (en grados Celsius) y el caudal de un río (cuánta agua pasa por segundo, en metros cúbicos por segundo). Un indicador de un solo día no describe un clima: se necesitan promedios de muchos años. Un año muy seco o muy lluvioso es una variación, no un cambio de clima.",
        "El régimen de un río es la forma en que su caudal cambia durante el año. Si el caudal máximo ocurre en primavera o verano, cuando se derrite la nieve, el régimen es nival. Si el máximo ocurre en invierno, cuando llueve más, el régimen es pluvial. Si combina ambos, es mixto. Esto importa para la sociedad: define cuándo hay agua para regar y cuánta se puede guardar.",
        "Una fuente instrumental, como una estación meteorológica, mide con aparatos y registra en el tiempo. Un relato o una nota de prensa pueden decir lo que sienten las personas, pero no entregan una medición. Se usan juntos: el instrumento dice cuánto, el testimonio dice cómo se vive. Y siempre se pregunta por la escala: los datos de una ciudad no describen toda la región.",
    ],
    vocab=[("precipitación", "agua que cae del cielo como lluvia o nieve, en milímetros"), ("caudal", "cantidad de agua que pasa por un río en un tiempo"), ("régimen de un río", "forma en que cambia su caudal durante el año"), ("régimen nival", "caudal máximo en primavera o verano por el deshielo"), ("variación climática", "diferencia de un año respecto del clima habitual")],
    worked=[
        ("Calcular una diferencia entre dos ciudades", "Ciudad X de ejemplo recibe 600 mm al año y ciudad Y recibe 150 mm. ¿Cuántos milímetros más recibe X?",
         ["Resta el valor menor del mayor.", "600 − 150 = 450."],
         "450 mm más"),
        ("Identificar un régimen", "Un río ficticio tiene su caudal máximo en enero y el mínimo en junio. ¿Qué régimen tiene?",
         ["El máximo ocurre en verano.", "En verano se derrite la nieve de la montaña."],
         "Régimen nival"),
    ],
    mistakes=[("Concluir el clima de una zona a partir de un solo año.", "Se confunde una variación con un cambio de clima.", "El clima se describe con promedios de muchos años."),
              ("Tomar un relato o una nota de prensa como si fueran mediciones.", "Se confunde la opinión con un registro con aparatos.", "Contrasta con una fuente instrumental y cita sus datos.")],
    T=[
        ("abc", "{F} ¿Qué ciudad recibe la menor precipitación anual?", "Ciudad N", "Ciudad C", "Ciudad S", "5 mm es el valor más bajo de las tres ciudades."),
        ("En Geografía: ¿cómo se llama la forma en que cambia el caudal de un río durante el año?", "Régimen", "El régimen de un río describe cómo cambia su caudal durante el año."),
        ("abc", "{F} ¿Qué fuente de la ficha mide con instrumentos calibrados?", "La estación meteorológica (E)", "El relato del agricultor (V)", "La nota de prensa (P)", "La ficha dice que la estación tiene instrumentos calibrados."),
        ("=", "{F} ¿Cuántos milímetros más recibe la Ciudad C que la Ciudad N?", "350-5", "Se resta la precipitación de la Ciudad N a la de la Ciudad C.", " mm"),
        ("abc", "{F} ¿En qué mes ocurre el caudal máximo del río Claro?", "Diciembre", "Junio", "Abril", "Diciembre tiene el valor más alto, 120 metros cúbicos por segundo."),
        ("abc", "{F} Dado el mes del caudal máximo, ¿qué régimen tiene el río Claro?", "Nival, por el deshielo de primavera y verano", "Pluvial, por las lluvias de invierno", "Ninguno, porque su caudal cambia", "El máximo en diciembre coincide con el deshielo, según la explicación."),
        ("=", "{F} ¿Cuántos metros cúbicos por segundo aumentó el caudal entre junio y diciembre?", "120-25", "Se resta el caudal de junio al de diciembre.", " metros cúbicos por segundo"),
        ("abc", "{F} El agricultor dice que «llovió poquísimo». ¿Qué sirve para comprobar su relato?", "Comparar la precipitación de ese año con el promedio de muchos años", "Preguntarle a otro agricultor sin datos", "Esperar un año más sin medir", "Un relato se contrasta con mediciones y promedios de muchos años."),
        ("abc", "{F} ¿Qué problema tiene la nota de prensa (P)?", "No tiene autor ni datos que permitan verificar su afirmación", "Es demasiado larga", "Solo habla de un río", "Sin autor ni cifras no se pueden comprobar su origen ni su afirmación."),
        ("abc", "{F} Un estudiante concluye: «El clima de la zona central es seco, porque este año llovió poco». ¿Qué falla?", "Usa un solo año para describir el clima", "Usa una ciudad del sur", "Habla de caudales", "El clima se describe con promedios de muchos años, no con un solo año."),
        ("abc", "{F} La Ciudad C recibe 350 mm y el río Claro baja su caudal a 35 en abril. ¿Qué relación es razonable proponer?", "Que el caudal se alimenta del deshielo y de la lluvia, y baja cuando ambos disminuyen", "Que el caudal depende solo del número de habitantes", "Que no hay relación posible", "El caudal responde a lluvia y nieve, así que baja cuando ambas fuentes disminuyen."),
        ("{F} Explica por qué los datos de la Ciudad S no describen todo el sur del país.", "Porque son de una sola ciudad y la escala regional exige más estaciones", "Los datos de un punto no describen una región: hay que revisar la escala de los datos."),
        ("abc", "{F} Una comunidad agrícola ficticia quiere guardar agua para el verano. Según el caudal de la ficha, ¿cuándo conviene acumular más?", "En diciembre, cuando el caudal es más alto, para usarla cuando baje", "En abril, cuando el caudal es bajo", "En junio, cuando el caudal es el menor del año", "Se guarda agua cuando abunda para tenerla cuando el caudal baja."),
    ],
    ctx=("abc", "Una escuela ficticia instala un pluviómetro (instrumento para medir lluvia) en su patio y anota los milímetros de lluvia por mes durante dos años. ¿Qué conclusión sería prudente?", "Describir los datos de dos años y no generalizar a todo el clima de la región", "Afirmar que el clima de toda la región cambió", "Descartar los datos por ser pocos", "Dos años de un punto son una variación, no un clima, pero sí un dato útil."),
    sc=[
        ("En Geografía: ¿qué es el caudal de un río?", "La cantidad de agua que pasa por el río en un tiempo", "Se mide en metros cúbicos por segundo."),
        ("¿Qué régimen tiene un río con su máximo en primavera o verano?", "Nival", "El máximo en esas estaciones se debe al deshielo."),
        ("¿Por qué un solo año no describe un clima?", "Porque el clima se describe con promedios de muchos años", "Un año aislado es una variación."),
    ],
    op=("Usa los datos de ejemplo de esta tabla de una ciudad ficticia: temperatura media (en grados Celsius) por mes: enero 22, abril 16, julio 9, octubre 15; precipitación mensual (en milímetros): enero 2, abril 20, julio 90, octubre 25. "
        "Describe el clima: cuándo llueve más, cuándo hace más calor, cuál es la diferencia de temperatura entre enero y julio y una pregunta sobre qué otras fuentes necesitarías para decir que el clima es así todos los años.",
        "Llueve más en julio (90 mm). Más calor en enero (22 grados). Diferencia: 22 − 9 = 13 grados. Pregunta: ¿qué promedios hay de diez años o más? Con un solo año no puedo afirmar el clima.",
        ["identifica el mes de más lluvia y el de más calor", "calcula bien la diferencia de temperatura", "advierte el límite de un solo año de datos", "formula una pregunta sobre otras fuentes"],
        ["descripción de cuatro líneas con un cálculo y una pregunta"],
        ["tomar los datos como promedio de muchos años", "restar mal las temperaturas", "confundir temperatura con precipitación"],
        "Pregunta: «¿qué dato te falta para decir que el clima es así todos los años?». Si no lo identifica, pídele que relea la explicación sobre promedios."),
    reinforce="Anota durante una semana la temperatura que dice el pronóstico para tu comuna y escribe la diferencia entre el día más cálido y el más frío.",
    extend="Compara un relato de una persona mayor sobre cómo eran las lluvias antes con un dato de precipitación de ejemplo y explica qué falta para concluir algo.",
)

# ============================================================ OAC-02, clase 3
F = ("Ficha 3 (explicaciones de estudiantes, ficticias). Pregunta: ¿por qué el norte de Chile es muy seco y el sur es lluvioso? Estudiante 1: «Solo por la latitud: más al sur llueve más.» "
     "Estudiante 2: «Porque la corriente marina fría y las condiciones estables del aire sobre el Pacífico dejan poca lluvia en el norte, y en el sur llegan con más frecuencia sistemas de lluvia desde el océano.» "
     "Estudiante 3: «Porque los Andes bloquean la humedad que viene de más al este, y por eso el norte queda seco.»")
build(
    O2, 3, F,
    use="Aprenderé a comparar las causas que explican el clima y el relieve de Chile y a distinguir una explicación de una sola causa de una explicación de varias causas que actúan juntas.",
    prior=["Sé leer indicadores de clima y caudal.", "Distingo causa de consecuencia.", "Sé que muchos cambios tienen varias causas."],
    explain=[
        "Explicar por qué el clima del norte de Chile es seco no se resuelve con una sola causa. Intervienen varias dinámicas físico-naturales a la vez: la corriente marina fría enfría el aire cerca de la costa y deja poca humedad disponible; las condiciones estables del aire sobre el Pacífico dificultan la formación de lluvia; y la cordillera de los Andes impide el paso de la humedad desde el este. Cada una explica una parte; juntas explican el resultado.",
        "La latitud también importa: hacia el sur, el clima se vuelve más frío y llegan con más frecuencia sistemas de lluvia que vienen del océano. Pero la latitud, por sí sola, no explica todo, porque a la misma latitud el relieve y el mar crean climas diferentes entre la costa y la cordillera. Por eso se dice que una explicación de una sola causa es incompleta, aunque no sea falsa.",
        "Comparar explicaciones es evaluar cuántas dinámicas consideran, si se apoyan en evidencia y qué dejan fuera. También hay perspectivas: un agricultor, una geóloga y una comunidad costera pueden destacar causas distintas porque les importan cosas distintas. En esta asignatura se valora la explicación que reúne varias causas, reconoce sus escalas y no presenta una causa como la única.",
    ],
    vocab=[("corriente marina fría", "flujo de agua fría en el mar que enfría el aire cercano"), ("estabilidad del aire", "condición que dificulta que se formen nubes y lluvia"), ("efecto barrera", "bloqueo del paso de humedad por una cordillera"), ("explicación completa", "la que reúne varias causas y reconoce su escala"), ("latitud", "distancia al ecuador, medida en grados")],
    worked=[
        ("Evaluar una explicación de una sola causa", "Un estudiante dice: «El desierto del norte es seco solo porque hace calor». ¿Qué falla?",
         ["Es una sola causa, la temperatura.", "Se omiten la corriente fría, la estabilidad del aire y el efecto barrera de los Andes."],
         "Es incompleta: faltan otras causas físico-naturales"),
        ("Reconocer una perspectiva", "Una dirigente de una caleta destaca que la corriente fría trae peces; un ingeniero destaca que la falta de lluvia exige llevar agua desde lejos. ¿Qué hay en común?",
         ["Ambos hablan de la misma dinámica del medio.", "Cada uno mira desde lo que necesita: pesca o agua."],
         "Una misma dinámica físico-natural vista desde dos perspectivas"),
    ],
    mistakes=[("Elegir una sola causa para explicar el clima de una zona.", "Se supone que una dinámica del medio actúa sola.", "Combina varias causas y explica qué papel cumple cada una."),
              ("Creer que una explicación incompleta es falsa.", "Se confunde incompleta con equivocada.", "Reconoce qué parte explica y qué le falta.")],
    T=[
        ("abc", "{F} ¿Qué estudiante propone una sola causa, la latitud?", "El estudiante 1", "El estudiante 2", "El estudiante 3", "El estudiante 1 dice «solo por la latitud»."),
        ("abc", "{F} ¿Qué estudiante menciona la cordillera de los Andes?", "El estudiante 3", "El estudiante 1", "El estudiante 2", "El estudiante 3 dice que los Andes bloquean la humedad."),
        ("En Geografía: ¿cómo se llama el bloqueo del paso de humedad por una cordillera?", "Efecto barrera", "La explicación llama efecto barrera al bloqueo de la humedad por una cordillera."),
        ("abc", "{F} ¿Qué estudiante reúne más de una causa físico-natural?", "El estudiante 2", "El estudiante 1", "El estudiante 3", "Menciona la corriente fría y las condiciones estables del aire sobre el Pacífico, más los sistemas de lluvia del sur."),
        ("abc", "¿Por qué la latitud sola no explica el clima?", "Porque a la misma latitud el relieve y el mar crean climas diferentes", "Porque la latitud no influye en nada", "Porque todos los lugares tienen la misma latitud", "El relieve y el mar modifican el clima a una misma latitud."),
        ("abc", "{F} Una explicación incompleta, ¿es lo mismo que una falsa?", "No: explica una parte, pero le faltan otras causas", "Sí: toda explicación incompleta es falsa", "Sí, porque la ciencia no admite causas parciales", "Una explicación incompleta puede ser verdadera en lo que dice y limitada en lo que omite."),
        ("abc", "Una comunidad pesquera ficticia valora la corriente fría porque atrae peces. ¿Qué tipo de perspectiva es?", "Una perspectiva basada en lo que necesita la comunidad", "Una perspectiva basada en una sola latitud", "Una perspectiva sin relación con el medio", "Cada actor destaca la dinámica del medio que le resulta útil o relevante."),
        ("{F} ¿Cuál de las tres explicaciones incluye tanto una causa del mar como una del aire?", "La del estudiante 2", "Menciona la corriente marina fría y las condiciones estables del aire."),
        ("abc", "{F} ¿Cómo se pueden combinar las explicaciones de los estudiantes 2 y 3?", "Sumando la corriente fría, el aire estable y el efecto barrera de los Andes", "Descartando una de las dos", "Quedándose con la más corta", "Las causas son compatibles y juntas explican el resultado de forma más completa."),
        ("abc", "{F} Un estudiante dice que el 1 «se equivoca». ¿Qué es más preciso?", "El 1 acierta en que la latitud influye, pero omite otras causas", "El 1 miente sobre el clima", "El 1 no habla del clima", "La latitud sí influye; el problema es que lo presenta como la única causa."),
        ("abc", "{F} Si solo existiera el efecto barrera de los Andes, ¿qué explicaría?", "Parte de la sequedad del norte, pero no el efecto de la corriente fría", "Toda la lluvia del sur", "La temperatura del mar", "El efecto barrera explica un bloqueo de humedad, no el papel del mar ni del aire estable."),
        ("{F} Explica por qué es mejor una explicación que considera varias causas.", "Porque los fenómenos del medio dependen de varias dinámicas que actúan juntas", "Una sola causa deja fuera dinámicas que también influyen en el clima."),
        ("abc", "{F} ¿Qué evidencia ayudaría a comparar la importancia de la corriente fría y de la cordillera?", "Comparar zonas con y sin corriente fría o con distinta altura de cordillera", "Contar cuántos estudiantes hay en la clase", "Anotar la fecha de la explicación", "Para pesar una causa se comparan casos que difieren en esa causa."),
    ],
    ctx=("abc", "Un programa de radio escolar ficticio quiere explicar a la comunidad por qué un valle recibe poca lluvia aunque está cerca del mar. ¿Qué explicación es más completa?", "Combinar corriente fría, aire estable y cordilleras que bloquean la humedad", "Decir que el valle está mal ubicado", "Indicar solo que el mar está cerca", "Varias dinámicas actúan juntas; mencionar solo el mar deja fuera otras causas."),
    sc=[
        ("En Geografía: ¿qué significa que una explicación sea completa?", "Que reúne varias causas y reconoce su escala", "Reúne todas las dinámicas relevantes y reconoce su escala."),
        ("¿Qué es el efecto barrera?", "El bloqueo del paso de humedad por una cordillera", "Una cordillera puede impedir que la lluvia pase al otro lado."),
        ("¿Es falsa una explicación de una sola causa?", "No necesariamente: puede ser verdadera pero incompleta", "La causa puede ser real, aunque no sea la única."),
    ],
    op=("Lee estas dos explicaciones ficticias sobre por qué los valles de una zona de montaña tienen más lluvia en un lado que en el otro. Explicación A: «Por la altura de los cerros.» Explicación B: «Por la altura de los cerros y por la dirección de los vientos que traen la humedad.» "
        "Escribe cuál explicación es más completa y por qué, qué causa falta en cada una y qué dato pedirías para comprobar la explicación B.",
        "B es más completa porque reúne dos causas. A omite el viento. B podría omitir la cercanía al mar. Dato: dirección habitual del viento y lluvia a ambos lados.",
        ["compara las dos explicaciones por la cantidad de causas", "indica una causa que falta en cada una", "propone un dato que se pueda obtener", "no declara falsa a ninguna sin razón"],
        ["texto de cuatro líneas con comparación, causas faltantes y un dato"],
        ["decir que A es falsa", "no proponer ningún dato", "repetir lo que dice el texto"],
        "Pregunta: «¿qué causa agrega B respecto de A?». Si no la nombra, pídele que subraye en el texto."),
    reinforce="Elige un fenómeno de tu comuna (por ejemplo, la niebla de la mañana) y escribe dos causas posibles y qué dato necesitarías.",
    extend="Compara por escrito la explicación de una persona que trabaja en agricultura con la de otra que trabaja en pesca sobre el clima de una misma zona.",
)

# ============================================================ OAC-02, clase 4
F = ("Ficha 4 (cuenca ficticia del río Ancho). Cabecera: alta cordillera con nieve y glaciares pequeños. Curso medio: laderas con bosque nativo y matorral. Valle: huertas, un pueblo y dos pozos de agua potable. Desembocadura: un humedal costero con aves migratorias. "
     "Año de ejemplo muy seco: baja la nieve y el caudal; algunos agricultores bombean más agua de los pozos. Otro año se talan las laderas para leña: llega más barro y piedras al río con las lluvias.")
build(
    O2, 4, F,
    use="Aprenderé a explicar la interdependencia y la fragilidad de los ambientes dentro de una cuenca y a relacionarlas con su importancia para la vida en sociedad (agua, alimento, riesgos).",
    prior=["Sé que las dinámicas del medio tienen varias causas.", "Conozco el régimen de un río.", "Reconozco consecuencias a corto y largo plazo."],
    explain=[
        "Una cuenca hidrográfica es el territorio cuyas aguas drenan hacia un mismo río. Tiene una cabecera en la parte alta, un curso medio y una desembocadura en el mar o en un lago. Sus ambientes dependen unos de otros: la nieve y los glaciares alimentan el río, la vegetación de las laderas sostiene el suelo y regula el agua, el río riega el valle y los sedimentos que arrastra alimentan el humedal de la desembocadura.",
        "Esa interdependencia hace que los ambientes sean frágiles: si se altera un eslabón, se afectan los demás. Si disminuye la nieve, baja el caudal y los pozos se usan más. Si se talan las laderas, el suelo queda sin protección y la lluvia arrastra barro y piedras al río, lo que puede dañar el valle. Un ambiente es frágil cuando se altera con facilidad y se recupera con lentitud.",
        "Para la sociedad, estos ambientes tienen importancia concreta: entregan agua potable y de riego, alimento, energía, protección frente a riesgos y lugares de valor cultural y recreativo. Por eso decidir sobre ellos es una cuestión social: se pregunta quién usa el agua, quién cuida la ladera y quién sufre las consecuencias cuando el ambiente se altera. Las consecuencias también aparecen en el tiempo: algunas se notan en una temporada, otras tardan décadas.",
    ],
    vocab=[("cuenca hidrográfica", "territorio cuyas aguas drenan hacia un mismo río"), ("cabecera", "parte alta de una cuenca, donde nace el río"), ("desembocadura", "lugar donde el río llega al mar o a un lago"), ("fragilidad", "facilidad con que un ambiente se altera y lo lenta que es su recuperación"), ("sedimentos", "partículas de suelo y rocas que arrastra el agua")],
    worked=[
        ("Seguir una cadena de dependencia", "En otra cuenca ficticia disminuyen los glaciares. ¿Qué eslabones se afectan?",
         ["Primero baja el aporte de agua de la cabecera.", "Luego baja el caudal del río y, con él, el riego del valle."],
         "Glaciares, caudal, riego del valle: la alteración de la cabecera llega hasta los usuarios"),
        ("Reconocer fragilidad", "Un humedal ficticio tarda muchos años en recuperarse si se seca. ¿Qué indica?",
         ["Se altera con facilidad si falta agua.", "Su recuperación es lenta."],
         "Que es un ambiente frágil"),
    ],
    mistakes=[("Estudiar la ladera, el valle y el humedal como lugares separados.", "Se olvida que están conectados por el agua.", "Sigue el recorrido del agua desde la cabecera hasta la desembocadura."),
              ("Pensar que un daño ambiental se nota siempre de inmediato.", "Se ignoran los tiempos largos de algunas consecuencias.", "Distingue consecuencias de corto y de largo plazo.")],
    T=[
        ("abc", "{F} ¿Qué ambiente está en la cabecera de la cuenca del río Ancho?", "La alta cordillera con nieve y glaciares", "El humedal costero", "El valle con huertas", "La ficha ubica la cordillera con nieve y glaciares en la parte alta."),
        ("En Geografía: ¿cómo se llama el territorio cuyas aguas drenan hacia un mismo río?", "Cuenca hidrográfica", "Esa es la definición de cuenca hidrográfica."),
        ("abc", "{F} ¿Dónde está el humedal con aves migratorias?", "En la desembocadura", "En la cabecera", "En el curso medio", "La ficha ubica el humedal costero en la desembocadura."),
        ("abc", "{F} Según la ficha, ¿qué pasa en un año muy seco?", "Baja la nieve y el caudal, y se bombea más agua de los pozos", "Aumenta la nieve y el caudal", "Se llenan los humedales", "La ficha describe menos nieve, menos caudal y más bombeo de pozos."),
        ("abc", "¿Qué función cumple la vegetación de las laderas?", "Sostiene el suelo y regula el agua", "Aumenta la cantidad de nieve", "Hace que el río corra más lento en todos los lugares", "La vegetación protege el suelo de la erosión y regula el agua que baja."),
        ("abc", "{F} ¿Qué ocurre cuando se talan las laderas, según la ficha?", "La lluvia arrastra barro y piedras al río", "Aumenta la nieve en la cabecera", "El humedal se llena de aves", "La ficha dice que llega más barro y piedras al río con las lluvias."),
        ("abc", "{F} Si el caudal baja por falta de nieve, ¿qué consecuencia afecta directamente a la sociedad?", "Menos agua para riego y para los pozos del pueblo", "Más aves migratorias", "Más vegetación en la cabecera", "El agua de riego y de los pozos depende del caudal."),
        ("abc", "{F} Un estudiante dice que la tala de laderas solo afecta a las laderas. ¿Qué respuesta muestra la interdependencia?", "Afecta también al río, al valle y al humedal, porque el barro viaja con el agua", "No afecta a nadie más", "Solo afecta a la cabecera", "Los sedimentos viajan río abajo y dañan los ambientes siguientes."),
        ("abc", "Un ambiente que se altera con facilidad y se recupera lentamente es", "frágil", "resistente", "inalterable", "Fragilidad es justamente alterarse con facilidad y recuperarse con lentitud."),
        ("{F} Explica por qué la importancia de la cuenca para la vida en sociedad va más allá del agua para beber.", "Porque también entrega riego, alimento, protección frente a riesgos y lugares de valor cultural", "La cuenca sostiene muchas actividades y servicios, no solo el agua potable."),
        ("abc", "{F} Si la tala de laderas sigue por muchos años y el valle recibe cada año coladas de barro y piedras, ¿qué tipo de consecuencia es?", "Una consecuencia de largo plazo que puede afectar a varios actores", "Una consecuencia sin efecto social", "Una causa natural sin relación con la tala", "La pérdida de protección del suelo puede tardar años en mostrar su daño pleno."),
        ("abc", "{F} Los agricultores bombean más agua de los pozos por la sequía. ¿Qué pregunta de interdependencia surge?", "¿Qué pasará con el agua potable del pueblo si los pozos bajan?", "¿Cuántas aves tiene el humedal?", "¿Cuántas huertas hay en el cerro más alto?", "Los pozos abastecen al pueblo, así que usarlos más afecta a otro actor."),
        ("abc", "{F} ¿Qué actor sufriría primero el daño en el humedal si el río trae más barro?", "Las aves migratorias que dependen del humedal", "Los glaciares de la cabecera", "El bosque nativo de las laderas", "Los sedimentos llegan a la desembocadura y afectan al ambiente del humedal."),
    ],
    ctx=("abc", "Una municipalidad ficticia debe decidir si autoriza una cantera cerca de la ladera de una cuenca. ¿Qué pregunta ayuda mejor a evaluar la fragilidad del ambiente?", "¿Qué pasaría con el suelo, el agua y el valle si se remueve la ladera?", "¿Cuántos camiones llegan por día?", "¿Qué color tiene la roca?", "Evaluar fragilidad es preguntar cómo se alteraría cada eslabón de la cuenca y cuánto tardaría en recuperarse."),
    sc=[
        ("En Geografía: ¿qué es la cabecera de una cuenca?", "La parte alta, donde nace el río", "Suele ser una cordillera con nieve que alimenta el río."),
        ("¿Qué es la fragilidad de un ambiente?", "La facilidad con que se altera y lo lenta que es su recuperación", "Un ambiente frágil se daña fácil y se recupera despacio."),
        ("¿Por qué las laderas con vegetación protegen al valle?", "Porque sostienen el suelo y regulan el agua", "Sin vegetación el suelo se arrastra con la lluvia."),
    ],
    op=("Dibuja un esquema de una cuenca ficticia con cabecera, curso medio, valle y desembocadura. Escribe en cada parte un ambiente, un uso de la sociedad (por ejemplo, riego o pesca) y un riesgo de alteración. Une las partes con flechas que muestren cómo se afectan unas a otras y escribe una consecuencia de corto plazo y otra de largo plazo.",
        "Cabecera: nieve, agua; riesgo: poca nieve. Curso medio: bosque, leña; riesgo: tala. Valle: huertas; riesgo: poco caudal. Desembocadura: humedal; riesgo: barro. Corto plazo: menos riego. Largo plazo: pérdida del humedal.",
        ["incluye las cuatro partes de la cuenca", "relaciona ambiente, uso y riesgo en cada parte", "usa flechas que muestran interdependencia", "distingue consecuencias de corto y largo plazo"],
        ["esquema con cuatro partes, flechas y dos consecuencias"],
        ["no dibujar la conexión entre partes", "confundir uso con riesgo", "olvidar los plazos"],
        "Pregunta: «¿qué le pasa al humedal si se altera la ladera?». Si no puede responder, pídele que siga las flechas."),
    reinforce="Dibuja el recorrido del agua que pasa por tu casa o tu colegio, desde donde nace hasta donde desemboca, con tres ambientes que atraviesa.",
    extend="Averigua con una persona de tu entorno cómo se obtiene el agua potable en tu comuna y qué ambientes la sostienen.",
)


# ============================================================ OAC-03, clase 1
F = ("Ficha 1 (caso ficticio). Bahía Serena es una comuna costera con un humedal de 80 hectáreas junto a la playa, usado por aves, por recolectores de orilla y por vecinos que pasean. Una inmobiliaria propone construir 300 viviendas en terrenos que bordean el humedal. "
     "Actores: la inmobiliaria (empresa); la municipalidad, que decide el plan regulador comunal (el instrumento que define los usos del suelo); el gobierno regional, que financia caminos; el servicio público que evalúa el impacto ambiental; la junta de vecinos; el sindicato de recolectores de orilla; y una organización ambiental. "
     "Una norma nacional exige evaluar el impacto ambiental de ciertos proyectos antes de aprobarlos.")
build(
    O3, 1, F,
    use="Aprenderé a identificar las decisiones políticas, económicas y sociales que se toman sobre un espacio local, quiénes las toman, a qué escala y qué impacto pueden tener en el entorno natural.",
    prior=["Reconozco actores, dimensiones y escalas.", "Sé que el espacio se construye socialmente.", "Conozco la fragilidad de los ambientes en una cuenca."],
    explain=[
        "Los espacios geográficos no cambian solos: se transforman por decisiones. Una decisión política la toman autoridades o instituciones, mediante leyes, planes o permisos (por ejemplo, definir en un plan regulador dónde se puede construir). Una decisión económica trata de inversión, costos, precios y empleo (por ejemplo, una empresa que decide construir viviendas). Una decisión social surge de la organización de las personas: vecinos que se reúnen, firman, protestan o proponen alternativas.",
        "Esas decisiones se toman a escalas distintas. La municipalidad decide a escala comunal, el gobierno regional a escala regional y las leyes nacionales fijan reglas para todo el país. Los actores no tienen el mismo poder: una empresa puede tener recursos y asesores, una junta de vecinos tiene la voz de la comunidad, y una autoridad tiene facultades legales. Por eso se pregunta quién decide, quién es consultado y quién queda fuera.",
        "Todas las decisiones tienen un impacto en el entorno natural: cambian el uso del suelo, el agua, la vegetación y los hábitats de otros seres vivos. Contextualizar significa identificar los actores, el tiempo y la escala de una decisión antes de evaluarla. En esta clase todavía no se decide si la propuesta es buena o mala: se ordena quién hace qué, desde dónde y con qué efectos posibles.",
    ],
    vocab=[("decisión política", "la que toman autoridades o instituciones mediante leyes, planes o permisos"), ("decisión económica", "la que se refiere a inversión, costos, precios y empleo"), ("decisión social", "la que surge de la organización de las personas"), ("plan regulador comunal", "instrumento que define los usos del suelo de una comuna"), ("impacto ambiental", "cambio en el entorno natural causado por una actividad o proyecto")],
    worked=[
        ("Clasificar una decisión", "Una empresa ficticia decide invertir en un puerto nuevo en una caleta. ¿Qué tipo de decisión es?",
         ["Pregunta quién decide y sobre qué: una empresa sobre una inversión.", "Eso corresponde a costos, inversión y empleo."],
         "Una decisión económica (con impactos sociales y ambientales)"),
        ("Ubicar la escala de una decisión", "Un consejo comunal ficticio aprueba un parque en un barrio. ¿A qué escala se toma y quiénes pueden participar?",
         ["Lo decide un consejo comunal, es decir, un organismo de la comuna.", "Pueden participar vecinos y organizaciones de ese barrio."],
         "Escala comunal; participan actores locales"),
    ],
    mistakes=[("Pensar que las decisiones sobre un espacio las toma un solo actor.", "Se olvida que intervienen autoridades, empresas y organizaciones sociales.", "Identifica todos los actores y qué decide cada uno."),
              ("Creer que un proyecto solo afecta a su terreno.", "Se ignora el impacto sobre el entorno cercano.", "Pregunta qué cambia en el suelo, el agua y los seres vivos del entorno.")],
    T=[
        ("abc", "{F} ¿Qué actor decide en el plan regulador comunal dónde se puede construir?", "La municipalidad", "La inmobiliaria", "La junta de vecinos", "La ficha dice que la municipalidad decide el plan regulador comunal."),
        ("abc", "{F} ¿Qué actor propone construir 300 viviendas?", "La inmobiliaria", "El gobierno regional", "El sindicato de recolectores", "La propuesta de las 300 viviendas viene de la empresa inmobiliaria."),
        ("En Geografía: ¿cómo se llama el instrumento que define los usos del suelo de una comuna?", "Plan regulador comunal", "La ficha y la explicación nombran así al instrumento que define los usos del suelo."),
        ("abc", "{F} La inmobiliaria decide invertir en las viviendas. ¿Qué tipo de decisión es?", "Económica", "Política", "Social", "Invertir y construir son decisiones sobre costos, inversión y empleo, es decir, económicas."),
        ("abc", "{F} Los vecinos firman una carta pidiendo proteger el humedal. ¿Qué tipo de decisión toman?", "Social", "Económica", "Política", "Organizarse y firmar una petición son decisiones sociales surgidas de la comunidad."),
        ("abc", "{F} El gobierno regional financia un camino costero. ¿A qué escala actúa?", "Regional", "Del barrio", "Internacional", "El gobierno regional decide a escala de la región."),
        ("abc", "{F} ¿Qué impacto ambiental es probable si se construyen viviendas sobre el borde del humedal?", "Cambios en el uso del suelo, del agua y del hábitat de las aves", "Un aumento de las nevadas en la zona", "Ningún cambio, porque el humedal está lejos", "Construir sobre el borde de un humedal altera su suelo, su agua y a los seres vivos que dependen de él."),
        ("abc", "Un plan regulador antiguo permite construir en una zona que hoy se valora como frágil. ¿Qué pregunta ayuda a contextualizar la decisión?", "¿Quién lo aprobó, cuándo y con qué información?", "¿Qué decisión le gusta hoy a la mayoría de las personas?", "¿Cuánto cuesta construir una casa en esa zona?", "Contextualizar es identificar actores, tiempo y escala de la decisión."),
        ("abc", "{F} ¿Qué actor está fuera de la lista de decisores formales, pero tiene un interés directo en el humedal?", "El sindicato de recolectores de orilla", "El servicio público ambiental", "El gobierno regional", "El sindicato usa el humedal para trabajar, pero la ficha no lo menciona como decisor formal."),
        ("{F} Explica por qué es importante incluir a los vecinos y a los recolectores en la evaluación del proyecto.", "Porque usan el humedal y sufrirían o aprovecharían las consecuencias del proyecto", "Quienes viven de un espacio conocen sus usos y pueden ser afectados por las decisiones."),
        ("abc", "{F} Un estudiante dice: «La decisión es solo de la inmobiliaria». ¿Qué corrección es más acertada?", "La municipalidad, el servicio ambiental y otros actores también participan", "Tiene razón: solo ella decide", "Solo decide el sindicato", "La ficha muestra varios actores con distintas facultades, no un solo decisor."),
        ("abc", "{F} Si una ley nacional exige evaluar el impacto antes de aprobar el proyecto, ¿qué escala interviene además de la comunal?", "La nacional, porque la norma fija reglas para todo el país", "Solo la de la inmobiliaria", "Ninguna, porque es una decisión local", "Las leyes nacionales ponen condiciones a las decisiones locales."),
        ("abc", "{F} ¿Qué combinación de preguntas contextualiza mejor la decisión?", "¿Quiénes deciden?, ¿cuándo se decide?, ¿a qué escala? y ¿qué entorno natural afecta?", "¿Cuántas viviendas caben y cuánto cuestan?", "¿Qué opina la mayoría sin ver datos?", "Contextualizar es identificar actores, tiempo, escala y entorno afectado."),
    ],
    ctx=("abc", "En otra comuna ficticia una empresa quiere abrir una planta de áridos (arena y gravilla) cerca de un río. ¿Qué paso corresponde primero para analizar la decisión?", "Identificar quién decide, a qué escala y qué ambiente podría verse afectado", "Decidir si el proyecto es bueno o malo", "Pedir a la empresa que explique su plan, sin consultar a nadie más", "Antes de evaluar hay que ordenar actores, escala y entorno afectado."),
    sc=[
        ("En Geografía: ¿qué es una decisión política sobre un espacio?", "La que toman autoridades o instituciones con leyes, planes o permisos", "Es una decisión con facultades legales sobre el uso del espacio."),
        ("¿Qué tres elementos conviene identificar al contextualizar una decisión?", "Actores, tiempo y escala", "Sirven para ubicar la decisión antes de evaluarla."),
        ("¿Qué es el impacto ambiental?", "El cambio en el entorno natural causado por una actividad o proyecto", "Se mide en suelo, agua, aire y seres vivos."),
    ],
    op=("Elige uno de estos casos ficticios: (1) una comuna de montaña autoriza un nuevo camino hacia una laguna; (2) una comuna de valle permite agrandar un basural. Haz una tabla con al menos cuatro actores, qué tipo de decisión toma cada uno (política, económica o social), a qué escala actúa y un impacto posible en el entorno natural.",
        "Camino a la laguna. Municipalidad: decisión política, comunal. Empresa de turismo: económica, local. Junta de vecinos: social, local. Servicio ambiental: política, nacional. Impacto: más personas en la orilla de la laguna y pérdida de vegetación.",
        ["nombra al menos cuatro actores del caso", "clasifica bien el tipo de decisión de cada uno", "indica la escala", "identifica un impacto ambiental posible"],
        ["tabla de cuatro filas con actor, tipo de decisión, escala e impacto"],
        ["clasificar una decisión social como política", "olvidar un actor con interés directo", "describir un impacto sin relación con el caso"],
        "Pregunta: «¿quién queda fuera de esta tabla y podría verse afectado?». Si no lo identifica, pídele que relea los actores."),
    reinforce="Elige una decisión reciente de tu comuna (por ejemplo, un nuevo paradero) y escribe quién la tomó, de qué tipo es y a qué escala.",
    extend="Averigua con tu junta de vecinos o con tu colegio cómo se participa en las decisiones sobre un espacio de tu barrio y anota los pasos.",
)

# ============================================================ OAC-03, clase 2
F = ("Ficha 2 (datos y fuentes de ejemplo, ficticios). Proyecto de Bahía Serena. Informe de la inmobiliaria (I): promete 120 empleos mientras dura la construcción y 15 empleos permanentes; afirma que el humedal «seguirá existiendo». "
     "Informe de la organización ambiental (O): en 10 años las especies de aves registradas bajaron de 52 a 41, y el proyecto ocuparía 20 de las 80 hectáreas del humedal y su borde. Registro municipal (M): 220 familias inscritas en lista de espera de vivienda en la comuna.")
build(
    O3, 2, F,
    use="Aprenderé a interrogar fuentes e indicadores económicos, sociales y ambientales de una decisión territorial, distinguiendo lo que miden, lo que dejan fuera y desde qué interés fueron producidos.",
    prior=["Sé interrogar una fuente y leer un indicador.", "Identifico actores y decisiones.", "Calculo diferencias y porcentajes sencillos."],
    explain=[
        "Para analizar una decisión sobre un territorio se usan indicadores de tres tipos. Los económicos miden empleo, inversión o costos. Los sociales miden necesidades, como el número de familias sin vivienda. Los ambientales miden el estado del entorno natural, como las especies de aves o la superficie de humedal. Cada tipo ilumina un aspecto distinto, y ninguno basta por sí solo para decidir.",
        "Los informes también tienen autor, propósito e interés. Un informe de una empresa suele destacar beneficios económicos; uno de una organización ambiental, riesgos para el entorno; un registro municipal, necesidades de la comunidad. Esto no los vuelve falsos, pero obliga a leerlos con cuidado: ¿qué miden?, ¿qué omiten?, ¿en qué plazo? Un empleo temporal no es lo mismo que un empleo permanente, aunque ambos sean «empleos».",
        "Al comparar indicadores conviene usar las mismas unidades y el mismo período. El porcentaje de superficie ocupada se calcula dividiendo la parte entre el total y multiplicando por 100. Una afirmación como «el humedal seguirá existiendo» necesita una cifra que la respalde: ¿qué parte seguirá existiendo y en qué estado? Lo que no está medido en una fuente no significa que no importe: puede ser la pregunta que falta.",
    ],
    vocab=[("indicador económico", "dato que mide empleo, inversión o costos"), ("indicador social", "dato que mide necesidades o condiciones de las personas"), ("indicador ambiental", "dato que mide el estado del entorno natural"), ("empleo temporal", "empleo que dura solo mientras dura una obra"), ("interés", "aquello que un actor quiere lograr o proteger")],
    worked=[
        ("Leer un indicador ambiental", "Un humedal ficticio tenía 30 especies de aves y hoy tiene 24. ¿Cuánto bajó y qué porcentaje es?",
         ["Resta: 30 − 24 = 6 especies.", "Divide entre el valor inicial: 6 ÷ 30 × 100 = 20 %."],
         "Bajó 6 especies, un 20 %"),
        ("Distinguir temporal de permanente", "Un informe ficticio dice que una obra crea 100 empleos, pero 90 duran solo un año. ¿Qué conviene preguntar?",
         ["Hay 100 empleos en total y 10 duran más de un año.", "Cambia la valoración si se considera la duración."],
         "Cuántos empleos son permanentes y por cuánto tiempo"),
    ],
    mistakes=[("Comparar indicadores de períodos o unidades distintas.", "Se mezclan datos que no son comparables.", "Usa el mismo período y las mismas unidades."),
              ("Tomar «empleos» como un solo número sin mirar su duración.", "Se omite que hay trabajos temporales y permanentes.", "Pregunta cuántos son permanentes y de qué duran.")],
    T=[
        ("abc", "{F} ¿Qué fuente de la ficha es un informe de la organización ambiental?", "El informe (O)", "El informe (I)", "El registro (M)", "La ficha rotula con (O) el informe de la organización ambiental."),
        ("=", "{F} ¿Cuántas especies de aves menos se registraron en el humedal tras 10 años?", "52-41", "Se resta el valor actual al valor inicial.", " especies"),
        ("En Geografía: ¿cómo se llama el dato que mide el estado del entorno natural, como las especies de aves?", "Indicador ambiental", "Mide el estado del entorno natural."),
        ("abc", "{F} ¿Qué indicador social aparece en la ficha?", "Las 220 familias en lista de espera de vivienda", "Las especies de aves registradas", "Los 15 empleos permanentes", "Las familias sin vivienda miden una necesidad de las personas, es decir, un indicador social."),
        ("abc", "{F} ¿Qué diferencia hay entre los 120 empleos y los 15 empleos del informe (I)?", "Los 120 duran lo que dura la obra y los 15 son permanentes", "Los 120 son permanentes y los 15 son temporales", "No hay diferencia entre ellos", "El informe dice que 120 son durante la construcción y 15 permanentes."),
        ("abc", "{F} ¿Qué necesita la afirmación «el humedal seguirá existiendo» del informe (I)?", "Una cifra de qué parte seguirá existiendo y en qué estado", "Un color de portada más llamativo", "Una opinión de otra empresa", "Una afirmación general se respalda con datos concretos."),
        ("=", "{F} ¿Qué porcentaje de las 80 hectáreas ocuparía el proyecto? Divide la parte entre el total y multiplica por 100.", "20*100//80", "El proyecto ocuparía 20 de las 80 hectáreas.", " %"),
        ("abc", "{F} Una estudiante dice: «Como el informe (I) promete empleos, el proyecto es beneficioso». ¿Qué falla?", "Mira solo un indicador económico y no el social ni el ambiental", "El informe no habla de empleos", "Los empleos nunca son un indicador", "Un solo tipo de indicador no basta para valorar una decisión."),
        ("abc", "{F} ¿Por qué hay que leer con cuidado el informe (O)?", "Porque lo escribe un actor con interés en proteger el humedal", "Porque tiene demasiados datos", "Porque es muy antiguo", "Como todo informe, tiene autor e interés, aunque sus datos puedan ser correctos."),
        ("abc", "{F} Si el proyecto construye 300 viviendas y hay 220 familias en lista de espera, ¿qué se puede afirmar con esos datos?", "Que la oferta sería mayor que las familias en lista, pero no se sabe si esas familias podrían comprar", "Que todas las familias de la lista tendrían casa", "Que no hace falta ninguna vivienda", "Los números se comparan, pero no dicen quién podría pagar ni quién viviría allí."),
        ("{F} Propón un dato que falta en el informe (I) para evaluar el impacto ambiental.", "Cuántas hectáreas del humedal se rellenarían o se alterarían y en qué estado quedarían", "El informe no entrega datos ambientales sobre la superficie afectada ni su estado."),
        ("abc", "{F} Las 52 especies de hace 10 años y las 41 de hoy, ¿qué permiten hacer?", "Comparar el estado del humedal en dos cortes de tiempo", "Probar que el proyecto causará la baja", "Calcular los empleos futuros", "Dos cortes permiten comparar, pero no prueban por sí solos la causa de la baja."),
        ("abc", "{F} ¿Qué estrategia es más sólida para evaluar la situación?", "Combinar indicadores económicos, sociales y ambientales y contrastar las fuentes", "Quedarse con el informe más largo", "Elegir la fuente que dice lo que ya pensaba", "Se integran los tres tipos de indicador y se contrastan las fuentes por su interés."),
    ],
    ctx=("abc", "Un concejo comunal ficticio debe resolver si permite un nuevo puerto deportivo. Recibe un informe de la empresa que destaca empleos y un informe de pescadores que destaca la pérdida de sitios de pesca. ¿Qué conviene hacer?", "Leer ambos con sus intereses y pedir datos de cada tipo de indicador", "Descartar el informe de los pescadores por ser interesado", "Aceptar solo el informe de la empresa porque tiene más cifras", "Ambos informes tienen interés; la decisión se apoya en el contraste de ambos y en nuevos datos."),
    sc=[
        ("En Geografía: ¿qué es un indicador social?", "Un dato que mide necesidades o condiciones de las personas", "Por ejemplo, las familias sin vivienda."),
        ("¿Por qué es distinto un empleo temporal de uno permanente?", "Porque el temporal dura solo lo que dura la obra", "La duración cambia la valoración de la oferta de empleo."),
        ("¿Qué se divide para obtener el porcentaje de superficie ocupada?", "La parte ocupada entre el total", "Luego ese cociente se multiplica por 100."),
    ],
    op=("Elige un caso ficticio. Caso 1: un pueblo costero discute instalar una piscicultura (criadero de peces); el informe de la empresa dice que crea 40 empleos permanentes y el de los pescadores dice que el agua de la bahía tiene hoy 12 especies y podría perder 3. Caso 2: un valle discute una nueva planta solar; el informe de la empresa dice que usa 50 de 200 hectáreas y el de una cooperativa agrícola dice que perderían 30 hectáreas regadas. "
        "Para cada informe escribe qué tipo de indicador usa, quién lo produce y qué deja fuera; calcula un porcentaje con los datos y escribe dos preguntas que harías antes de decidir.",
        "Caso 2. La empresa usa un indicador de superficie y la cooperativa uno económico y ambiental. Porcentaje: 50 ÷ 200 × 100 = 25 %. La empresa omite qué hectáreas son regadas. Preguntas: ¿qué pasa con el agua de riego? ¿Cuántos empleos agrícolas hay hoy?",
        ["clasifica los indicadores y el interés de cada fuente", "calcula bien el porcentaje", "señala lo que cada informe deja fuera", "formula dos preguntas útiles"],
        ["ficha con clasificación de indicadores, un cálculo y dos preguntas"],
        ["dividir por la parte y no por el total", "tratar un informe como neutral", "hacer preguntas que se responden con sí o no"],
        "Pregunta: «¿qué diría el otro actor sobre este mismo dato?». Si no lo imagina, pídele que relea la fuente contraria."),
    reinforce="Elige una noticia sobre un proyecto en una ciudad (describe sus datos en tres líneas) y escribe qué tipo de indicador usa y qué falta.",
    extend="Compara dos informes ficticios o reales sobre un mismo proyecto y anota por escrito sus intereses y los datos que no coinciden.",
)

# ============================================================ OAC-03, clase 3
F = ("Ficha 3 (versiones ficticias). ¿Por qué se propuso construir junto al humedal de Bahía Serena? Inmobiliaria: «Hay demanda de viviendas y ese terreno es el más barato y plano de la comuna.» "
     "Municipio: «El plan regulador vigente permite construir allí, porque se aprobó hace años sin considerar el humedal.» Organización ambiental: «El humedal no tiene protección formal y el suelo cercano se valora solo por su precio.» "
     "Junta de vecinos: «Necesitamos viviendas, pero también el humedal, que es donde juegan los niños.»")
build(
    O3, 3, F,
    use="Aprenderé a comparar las causas de una decisión territorial (económicas, políticas y sociales) y las perspectivas de distintos actores, distinguiendo sus posiciones de sus intereses y valores.",
    prior=["Sé interrogar informes e indicadores.", "Identifico tipos de decisión y escalas.", "Reconozco la multicausalidad."],
    explain=[
        "Una decisión territorial rara vez tiene una sola causa. En el caso de Bahía Serena se combinan causas económicas (suelo barato, interés en construir), políticas (un plan regulador antiguo que permite construir y la falta de protección formal del humedal) y sociales (la necesidad real de viviendas). La causa de fondo suele estar en las reglas y las condiciones previas; la causa próxima es la decisión que se toma hoy.",
        "Cada actor tiene una posición (lo que pide) y un interés (lo que necesita o quiere proteger). La posición de la inmobiliaria es construir; su interés es obtener ganancias. La posición de la organización ambiental es no construir; su interés es proteger el humedal. A veces las posiciones chocan, pero los intereses pueden ser compatibles, como tener viviendas y conservar un espacio de juego. Los valores (lo que cada actor considera importante) también cuentan.",
        "Comparar perspectivas es leer cada versión según su actor, su causa destacada, su interés y lo que deja fuera. No se trata de decidir quién tiene la razón, sino de entender por qué cada uno ve el problema así y qué evidencia haría falta para resolverlo. También se pregunta quién tiene más poder para decidir y quién queda con menos voz.",
    ],
    vocab=[("posición", "lo que un actor pide o defiende en un conflicto"), ("interés", "lo que un actor necesita o quiere proteger"), ("valor", "lo que un actor considera importante"), ("causa próxima", "decisión o hecho más cercano al resultado"), ("causa de fondo", "regla o condición previa que hace posible la decisión")],
    worked=[
        ("Separar posición e interés", "Un sindicato ficticio exige que no se cierre un muelle. Su interés es poder trabajar y mantener sus ingresos. ¿Qué es la posición y qué es el interés?",
         ["La posición es lo que pide: que no se cierre el muelle.", "El interés es lo que necesita: trabajo e ingresos."],
         "Posición: no cerrar el muelle; interés: trabajo e ingresos"),
        ("Clasificar causas", "Una comuna ficticia permite viviendas en un cerro porque el suelo es barato y el plan regulador lo autoriza. ¿Qué tipo de causas son?",
         ["Que el suelo sea barato es una causa económica.", "Que el plan lo autorice es una causa política."],
         "Una económica y una política"),
    ],
    mistakes=[("Confundir la posición de un actor con su interés.", "Se supone que lo que pide es lo mismo que lo que necesita.", "Pregunta qué necesita o qué quiere proteger detrás de lo que pide."),
              ("Buscar quién tiene la razón en vez de entender las perspectivas.", "Se trata de un debate que se gana o se pierde.", "Entiende la causa, el interés y la evidencia de cada actor.")],
    T=[
        ("abc", "{F} ¿Qué causa de tipo económico menciona la inmobiliaria?", "El suelo más barato y plano de la comuna", "El plan regulador antiguo", "La falta de protección formal", "Un suelo barato reduce los costos, una causa económica."),
        ("abc", "{F} ¿Qué causa de tipo político menciona el municipio?", "Un plan regulador antiguo que permite construir allí", "La demanda de viviendas", "El valor del suelo", "El plan regulador es un instrumento político que permite construir."),
        ("En Geografía: ¿cómo se llama lo que un actor pide o defiende en un conflicto?", "Posición", "La posición es lo que un actor pide o defiende."),
        ("abc", "{F} ¿Qué actor destaca la necesidad social de viviendas, pero también el valor del humedal?", "La junta de vecinos", "La inmobiliaria", "La organización ambiental", "La junta dice que necesita viviendas y también el humedal."),
        ("abc", "{F} ¿Cuál es el interés de la organización ambiental?", "Proteger el humedal", "Obtener ganancias por las viviendas", "Reducir los impuestos", "La organización busca la protección del humedal."),
        ("abc", "{F} ¿Qué es una causa de fondo en el caso?", "Un plan regulador antiguo y un humedal sin protección formal", "La decisión de la inmobiliaria de presentar un proyecto el año pasado", "La conversación de la junta de vecinos", "Las reglas y condiciones previas hacen posible la decisión."),
        ("abc", "Dos grupos ficticios discuten por un terreno: uno pide construir una cancha y otro pide dejarlo sin construir. Sus intereses son tener un lugar para jugar y conservar el pasto. ¿Qué se puede proponer?", "Una cancha pequeña y un área de pasto protegida", "Dar la razón al primero sin consultar", "Cerrar el terreno para siempre", "Los intereses pueden ser compatibles aunque las posiciones choquen."),
        ("abc", "{F} ¿Por qué no se trata de «decidir quién tiene la razón» en la ficha?", "Porque cada actor ilumina una parte del problema desde su perspectiva", "Porque ninguno tiene datos", "Porque todos dicen lo mismo", "Se compara para entender, no para ganar el debate."),
        ("abc", "{F} Un estudiante afirma que la causa del proyecto es «solo la demanda de viviendas». ¿Qué respuesta es mejor?", "También influyen el suelo barato y las reglas que permiten construir", "Esa es la única causa posible", "La demanda no influye", "Las decisiones territoriales tienen varias causas combinadas."),
        ("{F} Explica por qué la organización ambiental no es necesariamente enemiga de la vivienda.", "Porque su interés es proteger el humedal y podría aceptar viviendas en otros terrenos", "Posición e interés no son lo mismo: puede haber alternativas compatibles."),
        ("abc", "{F} ¿Qué actor tiene probablemente menos poder para decidir y más para opinar?", "La junta de vecinos", "El municipio, que aprueba el plan regulador", "La inmobiliaria, que presenta el proyecto", "Los vecinos opinan y se organizan, pero no aprueban planes ni proyectos."),
        ("abc", "{F} ¿Qué evidencia ayudaría a decidir entre construir en el borde o en otro terreno?", "Un estudio comparado de terrenos alternativos por costo, riesgo y efecto ambiental", "La opinión del actor más fuerte", "El color de los terrenos", "Para comparar alternativas se necesita información de cada terreno con los mismos criterios."),
        ("abc", "{F} ¿Qué respuesta integra mejor las cuatro versiones?", "Hay necesidad de viviendas, suelo barato, reglas antiguas y un humedal sin protección: todas son causas del conflicto", "Solo importa la demanda de viviendas", "Solo importa el humedal", "Las versiones señalan causas complementarias que, juntas, explican el conflicto."),
    ],
    ctx=("abc", "En una comuna ficticia, una cooperativa pide ampliar un muelle y un grupo de turismo pide mantenerlo pequeño para cuidar una playa de anidación. ¿Qué paso ayuda más a entender el conflicto?", "Separar posiciones de intereses y buscar si hay alternativas que satisfagan a ambos", "Decir quién tiene la razón", "Ignorar al grupo con menos poder", "Entender los intereses abre opciones que las posiciones cierran."),
    sc=[
        ("En Geografía: ¿qué es un interés en un conflicto territorial?", "Lo que un actor necesita o quiere proteger", "Es lo que hay detrás de lo que el actor pide."),
        ("¿Qué es una causa de fondo?", "Una regla o condición previa que hace posible la decisión", "Está en las condiciones previas, no en la decisión de hoy."),
        ("¿Pueden ser compatibles dos intereses aunque las posiciones choquen?", "Sí", "Los intereses suelen admitir soluciones compartidas."),
    ],
    op=("Lee este caso ficticio: una comuna de montaña decide ampliar su camino principal. El comercio local quiere el camino para recibir más turistas; los pastores temen que pase el ganado por zonas peligrosas; la organización ambiental teme que se pierdan especies de flores. Haz una tabla con actor, posición, interés y causa que destaca, y escribe una propuesta que combine al menos dos intereses.",
        "Comercio: posición, ampliar; interés, ventas; causa: turistas. Pastores: posición, cuidar el ganado; interés, seguridad. Ambiental: posición, proteger flores. Propuesta: ampliar el camino con un paso de ganado y desvío de la zona de flores.",
        ["separa posición e interés de cada actor", "identifica la causa que destaca cada uno", "propone una solución que combina dos intereses", "no declara ganador a ningún actor"],
        ["tabla de tres filas con cuatro columnas y una propuesta de dos líneas"],
        ["repetir la posición como interés", "proponer algo que solo satisface a un actor", "ignorar a un actor"],
        "Pregunta: «¿qué necesita cada actor detrás de lo que pide?». Si no lo distingue, pídele que reescriba la columna de interés."),
    reinforce="Elige un desacuerdo de tu entorno (por ejemplo, el uso de una cancha) y escribe la posición y el interés de cada parte.",
    extend="Conversa con dos personas con puntos de vista distintos sobre un lugar de tu barrio y anota en qué intereses podrían ponerse de acuerdo.",
)

# ============================================================ OAC-03, clase 4
F = ("Ficha 4 (cadena de efectos ficticia en Bahía Serena). Si se construye junto al humedal: (1) se rellena parte del terreno; (2) el suelo pavimentado absorbe menos lluvia; (3) en invierno el agua se acumula más rápido en las calles bajas; (4) cambia el hábitat de las aves; (5) los recolectores de orilla tienen menos zona de trabajo. "
     "Beneficios: viviendas y empleos de construcción. Quién recibe cada efecto: nuevas familias (vivienda), vecinos de calles bajas (más anegamiento), recolectores (menos trabajo), municipalidad (más ingresos por impuestos).")
build(
    O3, 4, F,
    use="Aprenderé a explicar las relaciones entre decisiones y sus consecuencias para el entorno natural y para distintos actores, distinguiendo costos y beneficios y su distribución desigual.",
    prior=["Comparo causas y perspectivas.", "Sé que las consecuencias no son iguales para todos.", "Distingo corto y largo plazo."],
    explain=[
        "Una decisión sobre el territorio tiene efectos en cadena. En el caso de Bahía Serena, rellenar el humedal cambia el suelo, el suelo cambia el agua de lluvia, el agua cambia la vida en las calles bajas y el hábitat de las aves. Cada efecto puede ser una causa del siguiente. Explicar las relaciones es seguir esa cadena y decir cómo conecta lo ambiental con lo social y lo económico.",
        "Todo proyecto tiene beneficios y costos, y no se reparten por igual. Las nuevas familias ganan vivienda, los vecinos de calles bajas podrían perder seguridad frente a las lluvias, los recolectores pierden zona de trabajo y la municipalidad recibe ingresos. Un beneficio puede ser inmediato, y un costo puede aparecer años después. Por eso se pregunta quién gana, quién pierde, cuándo y de qué modo.",
        "Algunas consecuencias son reversibles, es decir, se pueden corregir; otras son difíciles de revertir, como rellenar un humedal. Cuando una consecuencia es irreversible o muy lenta de recuperar, la prudencia pide más cuidado antes de decidir. Una explicación completa nombra la cadena de efectos, los actores que reciben cada efecto, el plazo y si el daño se puede corregir.",
    ],
    vocab=[("efecto en cadena", "serie de cambios en que cada uno provoca el siguiente"), ("costo", "pérdida o daño que sufre un actor o el ambiente por una decisión"), ("beneficio", "ganancia que recibe un actor por una decisión"), ("reversible", "que se puede corregir o volver al estado anterior"), ("distribución desigual", "reparto no equivalente de beneficios y costos")],
    worked=[
        ("Seguir un efecto en cadena", "Una comuna ficticia pavimenta un cerro. Llueve y el agua baja más rápido. ¿Qué cadena se forma?",
         ["Pavimento: el suelo absorbe menos agua.", "El agua baja más rápido y llega a las calles bajas."],
         "Pavimento, menos absorción, más escurrimiento hacia las calles bajas"),
        ("Distribuir costos y beneficios", "Un puerto ficticio da empleo a 50 personas, pero ensucia la playa donde pescan 30 familias. ¿Quién recibe qué?",
         ["Los trabajadores reciben el beneficio del empleo.", "Las familias pescadoras reciben el costo de la playa más sucia."],
         "Beneficio para los trabajadores y costo para las familias pescadoras"),
    ],
    mistakes=[("Contar solo los beneficios de un proyecto.", "Se mira la decisión desde el actor que gana.", "Anota también los costos y quién los asume."),
              ("Tratar todas las consecuencias como si se pudieran corregir.", "Se ignora que algunas son irreversibles.", "Pregunta si el daño se puede revertir y en cuánto tiempo.")],
    T=[
        ("abc", "{F} ¿Qué ocurre primero en la cadena de efectos?", "Se rellena parte del terreno", "Cambia el hábitat de las aves", "Se acumula agua en las calles bajas", "El paso (1) de la ficha es el relleno del terreno."),
        ("abc", "{F} ¿Qué actor recibe el beneficio de la vivienda?", "Las nuevas familias", "Los recolectores de orilla", "Los vecinos de calles bajas", "Según la ficha, las nuevas familias reciben la vivienda."),
        ("En Geografía: ¿cómo se llama la serie de cambios en que cada uno provoca el siguiente?", "Efecto en cadena", "La explicación llama así a esa serie de cambios."),
        ("abc", "{F} ¿Por qué se acumula más agua en las calles bajas?", "Porque el suelo pavimentado absorbe menos lluvia", "Porque llueve más en el humedal", "Porque hay más aves", "El paso (2) explica que el pavimento absorbe menos lluvia."),
        ("abc", "{F} ¿Qué costo reciben los recolectores de orilla?", "Menos zona de trabajo", "Más ingresos por impuestos", "Más viviendas", "La ficha dice que tienen menos zona de trabajo."),
        ("abc", "¿Qué significa que una consecuencia sea reversible?", "Que se puede corregir o volver al estado anterior", "Que ocurre solo en verano", "Que afecta a una sola persona", "Reversible es lo que puede corregirse."),
        ("abc", "{F} La municipalidad recibe más ingresos por impuestos. ¿Qué dimensión destaca?", "La económica", "La cultural", "La ambiental", "Los ingresos municipales son un efecto económico."),
        ("abc", "{F} ¿Qué consecuencia del proyecto sería más difícil de revertir?", "Rellenar y pavimentar parte del humedal", "Que se abra un mercado nuevo", "Que cambie un horario de buses", "Alterar el suelo de un humedal tarda muchísimo en recuperarse."),
        ("=", "{F} Si se pierden 20 de las 80 hectáreas del humedal, ¿cuántas hectáreas quedarían?", "80-20", "Se resta lo que se pierde al total del humedal.", " hectáreas"),
        ("{F} Explica por qué se dice que los costos y los beneficios del proyecto se reparten de forma desigual.", "Porque unos actores reciben vivienda e ingresos y otros pierden trabajo o seguridad", "Los efectos recaen de modo distinto sobre cada actor."),
        ("abc", "{F} Un estudiante dice: «El proyecto es bueno porque da viviendas». ¿Qué le falta a su análisis?", "Los costos y quién los asume", "Nada, porque las viviendas bastan", "Más viviendas", "Un análisis completo incluye costos, beneficios y su reparto."),
        ("abc", "{F} Para evaluar el riesgo de anegamiento a largo plazo, ¿qué dato ayudaría?", "Cuántas hectáreas absorbentes se perderían y qué pasa con el agua de lluvia", "Cuántas viviendas se construirán en total", "Cuántos recolectores hay inscritos en el sindicato", "El agua que no se absorbe se acumula; hay que saber cuánta superficie se pierde."),
        ("abc", "{F} Si la consecuencia es irreversible y afecta a muchos actores, ¿qué actitud pide la prudencia?", "Revisar alternativas y reunir más evidencia antes de decidir", "Aprobar rápido", "Ignorar la consecuencia", "Cuanto mayor y más difícil de revertir es el daño, más cuidado se necesita."),
    ],
    ctx=("abc", "Una comuna ficticia estudia convertir una laguna en un balneario con restaurantes. Los comerciantes ganan clientes, pero la laguna recibe más basura. ¿Qué paso es adecuado?", "Anotar beneficios y costos para cada actor y el plazo de cada efecto", "Aprobar el balneario porque da trabajo", "Rechazarlo sin leer datos", "El análisis se apoya en una lista de efectos, actores y plazos."),
    sc=[
        ("En Geografía: ¿qué es un costo de un proyecto?", "Una pérdida o daño que sufre un actor o el ambiente", "Puede ser ambiental, social o económico."),
        ("¿Se reparten por igual los beneficios y costos de un proyecto?", "No", "Suelen recaer de modo distinto en cada actor."),
        ("¿Qué consecuencia pide más prudencia?", "La irreversible", "No se puede corregir si resulta dañina."),
    ],
    op=("Elige un proyecto ficticio: (1) una ciclovía costera sobre una duna; (2) una ampliación de una mina de arena junto a un río. Dibuja una cadena de al menos cuatro efectos, indica un beneficio y un costo para tres actores distintos, y señala una consecuencia reversible y una difícil de revertir.",
        "Ciclovía sobre duna: se afirma el suelo, se pierde vegetación de la duna, cambia el hábitat de insectos, la duna se erosiona más rápido. Beneficio: ciclistas. Costo: guardaparques. Reversible: letreros. Irreversible: pérdida de la duna.",
        ["la cadena tiene al menos cuatro efectos coherentes", "indica beneficio y costo para tres actores", "distingue una consecuencia reversible y otra irreversible", "usa un lenguaje preciso sobre el entorno natural"],
        ["cadena de cuatro pasos con tabla de actores y dos consecuencias"],
        ["listar solo beneficios", "mezclar el orden de la cadena", "decir que todo se puede corregir"],
        "Pregunta: «¿qué se podría hacer para corregir esta consecuencia?». Si no hay respuesta, pídele que la reclasifique como difícil de revertir."),
    reinforce="Elige una obra de tu entorno y escribe una cadena de tres efectos, un beneficio y un costo.",
    extend="Entrevista a alguien que haya vivido un cambio fuerte en su barrio (una obra, una feria nueva) y anota sus beneficios, costos y plazos.",
)

# ============================================================ OAC-03, clase 5
F = ("Ficha 5 (matriz de ejemplo, ficticia). Tres alternativas para Bahía Serena: 1) construir las 300 viviendas como se propuso; 2) construir 150 viviendas lejos del borde y proteger una franja de 40 hectáreas del humedal; 3) no construir allí y destinar el terreno a un parque con protección total, buscando otro terreno para viviendas. "
     "Puntajes de 1 (bajo) a 3 (alto), de ejemplo. Vivienda: 3, 2, 1. Empleo: 3, 2, 1. Conservación del humedal: 1, 3, 3. Seguridad frente al anegamiento (3 = menor riesgo): 1, 2, 3. Bajo costo público (3 = menor costo): 2, 2, 1. Las columnas son las alternativas 1, 2 y 3 en ese orden.")
build(
    O3, 5, F,
    use="Aprenderé a evaluar alternativas de decisión sobre un espacio con criterios explícitos, ponderaciones y consecuencias, reconociendo que el puntaje no reemplaza la deliberación con los actores.",
    prior=["Comparo costos y beneficios.", "Separo posición e interés.", "Calculo sumas y productos."],
    explain=[
        "Evaluar alternativas es comparar posibles decisiones usando criterios explícitos. Un criterio es un aspecto que se considera importante, como la vivienda, el empleo, la conservación, la seguridad o el costo. Una matriz de decisión pone las alternativas en columnas, los criterios en filas y asigna un puntaje a cada celda. Sumar los puntajes da una primera comparación, que debe leerse con cuidado.",
        "No todos los criterios pesan igual. La ponderación es multiplicar el puntaje de un criterio por un peso. Si un criterio vale el doble, su puntaje se multiplica por 2. Cambiar los pesos puede cambiar la alternativa ganadora, lo que se llama sensibilidad. Por eso se muestra qué pesos se usaron y quién los eligió: elegir pesos es también una decisión de valores.",
        "El puntaje ayuda a ordenar la discusión, pero no reemplaza la deliberación con los actores. Una buena evaluación declara los criterios, muestra las ponderaciones, indica qué evidencia respalda los puntajes y reconoce lo que no se pudo medir. También considera medidas de mitigación (reducir el daño), compensación (reparar de otro modo) y seguimiento posterior a la decisión.",
    ],
    vocab=[("criterio", "aspecto que se considera importante para comparar alternativas"), ("matriz de decisión", "tabla con alternativas, criterios y puntajes"), ("ponderación", "multiplicar el puntaje de un criterio por un peso"), ("sensibilidad", "cambio del resultado cuando cambian los pesos"), ("mitigación", "medida que reduce el daño de una decisión")],
    worked=[
        ("Sumar puntajes", "Una alternativa ficticia obtiene 3 en seguridad, 2 en costo y 1 en conservación. ¿Cuál es su puntaje total?",
         ["Suma los tres puntajes.", "3 + 2 + 1 = 6."],
         "6 puntos"),
        ("Ponderar un criterio", "En un caso ficticio, la conservación vale el doble. Una alternativa tiene 3 en conservación y 2 en costo. ¿Cuál es su puntaje con esa ponderación?",
         ["Multiplica la conservación por 2: 3 × 2 = 6.", "Suma el costo sin ponderar: 6 + 2 = 8."],
         "8 puntos"),
    ],
    mistakes=[("Decidir solo con la suma simple de puntajes.", "Se olvida que los pesos cambian el resultado.", "Prueba al menos dos juegos de pesos y explica por qué elegiste uno."),
              ("Creer que el puntaje reemplaza a la discusión con los actores.", "Se confunde cálculo con legitimidad.", "Usa la matriz para ordenar la deliberación, no para evitarla.")],
    T=[
        ("abc", "{F} ¿Qué alternativa obtiene el mayor puntaje en conservación del humedal?", "Las alternativas 2 y 3, con 3 puntos cada una", "La alternativa 1, con 3 puntos", "Ninguna, porque todas tienen 1 punto", "La ficha asigna 1, 3 y 3, así que dos alternativas tienen el máximo."),
        ("En Geografía: ¿cómo se llama la tabla con alternativas, criterios y puntajes?", "Matriz de decisión", "Esa es la definición de matriz de decisión dada en la explicación."),
        ("=", "{F} ¿Cuál es el puntaje total de la alternativa 1 sumando los cinco criterios sin ponderar?", "3+3+1+1+2", "Se suman vivienda 3, empleo 3, conservación 1, anegamiento 1 y costo 2.", " puntos"),
        ("=", "{F} ¿Cuál es el puntaje total de la alternativa 2 sin ponderar?", "2+2+3+2+2", "Se suman vivienda 2, empleo 2, conservación 3, anegamiento 2 y costo 2.", " puntos"),
        ("=", "{F} ¿Cuál es el puntaje total de la alternativa 3 sin ponderar?", "1+1+3+3+1", "Se suman vivienda 1, empleo 1, conservación 3, anegamiento 3 y costo 1.", " puntos"),
        ("abc", "{F} Sin ponderar, ¿qué alternativa suma más puntos?", "La alternativa 2", "La alternativa 1", "La alternativa 3", "Los totales son 10, 11 y 9, y el mayor es el de la alternativa 2."),
        ("=", "{F} Si conservación y anegamiento valen el doble, ¿cuál es el puntaje de la alternativa 2? Multiplica por 2 los puntajes de esos dos criterios y suma los cinco.", "2+2+3*2+2*2+2", "Se duplican conservación (3 × 2) y anegamiento (2 × 2) y se suman los demás.", " puntos"),
        ("=", "{F} Con esa misma ponderación (conservación y anegamiento valen el doble), ¿cuál es el puntaje de la alternativa 3? Multiplica por 2 los puntajes de esos dos criterios y suma los cinco.", "1+1+3*2+3*2+1", "Se duplican conservación y anegamiento y se suman los demás criterios.", " puntos"),
        ("=", "{F} Con esa ponderación, ¿cuál es el puntaje de la alternativa 1? Multiplica por 2 los puntajes de esos dos criterios y suma los cinco.", "3+3+1*2+1*2+2", "Se duplican conservación y anegamiento y se suman los demás.", " puntos"),
        ("abc", "{F} Con la ponderación de conservación y anegamiento dobles, ¿cuál alternativa gana?", "La alternativa 2, con 16 puntos", "La alternativa 3, con 15 puntos", "La alternativa 1, con 12 puntos", "Con los pesos dobles los totales son 12, 16 y 15, y el mayor es 16."),
        ("abc", "{F} Si en cambio vivienda y empleo valieran el doble, la alternativa 1 sumaría 16 y la alternativa 2 sumaría 15. ¿Qué muestra esto?", "Que el resultado cambia según los pesos elegidos", "Que el puntaje no importa", "Que la alternativa 2 siempre gana", "Cambiar los pesos cambia el ganador: es la sensibilidad."),
        ("abc", "{F} ¿Qué pregunta es más útil antes de decidir con la matriz?", "¿Quién eligió los pesos y con qué evidencia se asignaron los puntajes?", "¿Qué alternativa tiene el número más grande?", "¿Cuántas páginas tiene el informe?", "Los pesos y la evidencia determinan la validez de la matriz."),
        ("abc", "{F} La alternativa 2 reduce el daño al humedal al dejar una franja protegida. ¿Cómo se llama una medida que reduce el daño?", "Mitigación", "Sensibilidad", "Ponderación", "La mitigación es la medida que reduce el daño de una decisión."),
    ],
    ctx=("abc", "Un consejo comunal ficticio debe decidir dónde instalar un relleno sanitario entre tres terrenos. Con una matriz da el mismo total a dos terrenos. ¿Qué paso conviene?", "Revisar los pesos, buscar más evidencia y escuchar a los actores afectados", "Elegir al azar", "Cerrar la discusión porque no hay ganador claro", "Un empate invita a revisar pesos y evidencia y a deliberar con los actores."),
    sc=[
        ("En Geografía: ¿qué es un criterio de evaluación?", "Un aspecto que se considera importante para comparar alternativas", "Por ejemplo, el costo o la conservación."),
        ("¿Qué significa ponderar un criterio?", "Multiplicar su puntaje por un peso", "Un criterio que vale el doble multiplica su puntaje por 2."),
        ("¿Reemplaza el puntaje a la deliberación con los actores?", "No", "Solo ayuda a ordenar la discusión."),
    ],
    op=("Usa esta matriz ficticia para decidir cómo usar un terreno junto a un río. Alternativas: 1) estacionamiento; 2) plaza con árboles; 3) bodega. Criterios con puntajes 1 a 3: Costo bajo: 3, 2, 3; Áreas verdes: 1, 3, 1; Seguridad frente a crecidas (3 = menor riesgo): 1, 3, 1; Uso por vecinos: 2, 3, 1. "
        "Calcula los totales sin ponderar y luego con el doble en áreas verdes y seguridad; escribe la alternativa que elegirías, qué medida de mitigación agregarías y qué evidencia o actor consultarías antes de decidir.",
        "Sin ponderar: 1) 3+1+1+2 = 7; 2) 2+3+3+3 = 11; 3) 3+1+1+1 = 6. Con doble: 1) 3+2+2+2 = 9; 2) 2+6+6+3 = 17; 3) 3+2+2+1 = 8. Elijo la plaza. Mitigación: árboles nativos. Consultaría a la junta de vecinos.",
        ["calcula correctamente los totales sin ponderar y ponderados", "elige una alternativa y justifica con los datos", "propone una medida de mitigación", "indica qué evidencia o actor consultaría"],
        ["tabla con totales, una elección justificada y una propuesta de mitigación"],
        ["no duplicar los dos criterios al ponderar", "elegir sin mirar los totales", "olvidar consultar a los actores"],
        "Pregunta: «¿cambiaría tu elección si el costo valiera el doble?». Si no lo prueba, pídele que recalcule."),
    reinforce="Haz una matriz con tres alternativas para usar un espacio de tu colegio y tres criterios, con puntajes del 1 al 3.",
    extend="Repite tu matriz con dos juegos de pesos distintos y anota si la alternativa ganadora cambia.",
)
