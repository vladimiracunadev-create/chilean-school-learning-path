"""Historia, Geografía y Ciencias Sociales EPJA Media N1, módulo 3 (parte 1): OAD-09, comparar perspectivas de pueblos indígenas y de mujeres sobre procesos de Chile del siglo XIX y la primera mitad del siglo XX. Todas las fuentes son textos de ejemplo inventados para este cuaderno y se leen en papel."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz, goma y cuaderno. Todas las fuentes de esta clase son extractos inventados «de ejemplo», escritos en cada ejercicio: no son citas de personas reales y no necesitas internet, mapas ni libros. "
             "Los hechos generales que se mencionan son los que se enseñan en los programas escolares. Tu experiencia de vida es bienvenida, pero nadie te pide contar datos personales ni de tu familia. "
             "Si un tema te trae recuerdos difíciles, puedes trabajar solo con los casos del cuaderno.")
build = make_build(MATERIALS)

O = "EPJA-HGCS-NM1-OAD-09"

# ======================================================= clase 1
F1 = ("Ficha 1 (de ejemplo). Dos textos inventados sobre un mismo hecho: la entrega de un terreno a una comunidad mapuche ficticia, la comunidad Lof Rayén, a fines del siglo XIX. "
      "Texto A (informe de un funcionario del Estado, de ejemplo): «Se asignó a la comunidad un terreno de menor tamaño que el que ocupaba antes, y el Estado considera cumplida su obligación.» "
      "Texto B (relato de una descendiente de la comunidad, de ejemplo): «Mis abuelos contaban que antes la familia usaba tierras para sembrar, criar animales y recolectar; después quedaron en un terreno más pequeño.»")
build(
    O, 1, F1,
    use="Hoy reconozco que un mismo hecho del pasado puede contarse desde perspectivas distintas y aprendo a leer dos textos con empatía y respeto.",
    prior=["Sé que una fuente entrega información sobre el pasado.", "Distingo quién escribe un texto.", "He escuchado dos versiones distintas de un mismo suceso en el trabajo o en el barrio."],
    explain=[
        "Una perspectiva es el punto de vista desde el que alguien mira un hecho. Depende de quién es, de lo que vivió y de lo que le importa. Tú ya lo sabes por experiencia: el dueño de un local y quien trabaja en él pueden contar de forma distinta un mismo cambio de horario.",
        "En la historia de Chile del siglo XIX y de la primera mitad del siglo XX ocurrieron procesos que afectaron a muchos grupos. Por ejemplo, el Estado extendió su control sobre el territorio de la Araucanía y el pueblo mapuche perdió gran parte de sus tierras. Los documentos oficiales y los relatos de las comunidades suelen contarlo de manera diferente.",
        "Comparar perspectivas no es decidir quién nos cae mejor. Es leer cada texto con respeto, preguntarse quién habla y desde dónde, y anotar en qué coinciden y en qué se distinguen. Así entendemos mejor el proceso completo y no solo una parte.",
    ],
    vocab=[("perspectiva", "punto de vista desde el que alguien mira un hecho"), ("actor", "persona o grupo que participa en un proceso"), ("pueblo indígena", "pueblo que vivía en el territorio antes de la formación del Estado actual"), ("empatía", "esfuerzo por comprender cómo vio un hecho otra persona"), ("coincidir", "decir lo mismo sobre un dato")],
    worked=[
        ("Quién habla en cada texto", "{F} Identifica quién escribe cada texto.", ["El texto A es un informe de un funcionario del Estado.", "El texto B es el relato de una descendiente de la comunidad."], "A: funcionario del Estado; B: descendiente de la comunidad"),
        ("En qué coinciden", "{F} ¿Hay un dato en el que ambos textos coinciden?", ["El texto A dice que el terreno asignado era de menor tamaño que el anterior.", "El texto B dice que quedaron en un terreno más pequeño."], "Sí: ambos dicen que el terreno nuevo era más pequeño"),
    ],
    mistakes=[("Pensar que solo una de las dos versiones es «la verdad» y la otra se descarta.", "Cada texto muestra una parte del proceso desde un lugar distinto.", "Anota qué dice cada uno y en qué coinciden antes de sacar una conclusión."),
              ("Juzgar el pasado solo con los valores de hoy, sin preguntar por el contexto del autor.", "Se pierde de vista desde dónde hablaba cada persona en su época.", "Pregunta quién escribe, para quién y en qué situación, y luego opina con respeto.")],
    T=[
        ("abc", "En HGCS: ¿qué es una perspectiva?", "El punto de vista desde el que se mira un hecho", "Un dato que se comprueba con un documento", "La fecha exacta en que ocurrió el hecho", "La perspectiva depende de quién mira, no es un dato comprobable."),
        ("abc", "{F} ¿Qué texto cuenta el hecho desde la experiencia de la comunidad que recibió el terreno?", "El texto B", "El texto A", "Ninguno de los dos", "El relato de la descendiente habla desde la comunidad; el informe habla desde el Estado."),
        ("{F} Según el texto B, ¿para qué usaba la tierra la familia antes?", "Para sembrar, criar animales y recolectar", "El relato lo enumera con esas tres actividades."),
        ("abc", "{F} ¿Qué diferencia hay entre lo que destacan A y B?", "A destaca que el Estado cumplió su obligación y B destaca los usos de la tierra que se perdieron", "A habla de un terreno y B de una ciudad", "A y B destacan lo mismo con otras palabras", "Cada texto pone el acento en algo distinto del mismo hecho."),
        ("ab", "{F} ¿Qué texto dice que el Estado considera cumplida su obligación?", "El texto A", "El texto B", "Esa frase aparece en el informe del funcionario."),
        ("abc", "{F} ¿Por qué los dos textos cuentan el hecho de manera distinta?", "Porque cada autor lo mira desde su lugar y su experiencia", "Porque uno de los dos está inventando todo", "Porque ocurrió dos veces en lugares distintos", "La perspectiva cambia según quién habla y qué vivió."),
        ("=", "Dato de ejemplo: antes la comunidad usaba 500 hectáreas y el terreno asignado tiene 120. ¿Cuántas hectáreas menos tiene ahora?", "500-120", "Se resta el terreno nuevo al terreno anterior para ver cuánto se perdió.", " hectáreas"),
        ("abc", "Un texto de ejemplo dice: «Para el Estado el asunto quedó cerrado». ¿Desde qué perspectiva parece escrito?", "Desde la de la autoridad que asignó el terreno", "Desde la de la comunidad que lo recibió", "Desde la de nadie, sin punto de vista", "Esa frase muestra cómo valoraba el asunto quien tomaba la decisión."),
        ("abc", "Dos frases de ejemplo: «El terreno nuevo mide 120 hectáreas» y «Fue una injusticia». ¿Cuál se puede comprobar con un documento?", "La primera, porque da una medida", "La segunda, porque es más fuerte", "Ambas, porque las dos hablan del terreno", "Una medida se verifica con documentos; «injusticia» es un juicio de valor."),
        ("abc", "Alguien dice: «Solo sirve el informe del funcionario porque es oficial». ¿Qué falla en esa idea?", "Deja fuera lo que vivió la comunidad y muestra solo una parte", "Los informes nunca sirven", "Los relatos orales siempre son más exactos", "Un documento oficial muestra la mirada del Estado, pero no toda la historia."),
        ("ab", "Para trabajar con empatía y respeto, ¿qué conviene hacer al leer el texto B?", "Preguntar qué quiso decir y desde dónde lo cuenta", "Descartarlo por ser un recuerdo familiar", "La empatía parte por intentar comprender el punto de vista de quien habla."),
        ("abc", "{F} Se quiere saber cuántas hectáreas ocupaba la comunidad antes. ¿Qué conviene hacer?", "Buscar otra fuente que traiga la medida, porque estos textos no la dan", "Inventar una cifra parecida", "Suponer que eran muchas", "Ninguno de los textos indica la medida, así que hace falta otra fuente."),
        ("abc", "{F} ¿Cuál es una buena conclusión de la comparación?", "Ambos textos reconocen un terreno menor, pero valoran de forma distinta lo ocurrido", "El texto A miente y el B dice la verdad", "Los dos textos dicen exactamente lo mismo", "Resume lo que coincide y lo que difiere sin descartar ningún texto."),
    ],
    ctx=("abc", "En un taller de la biblioteca municipal, dos personas leen los textos de la ficha y una dice: «Entonces el Estado quedó conforme y la comunidad no». ¿Qué respuesta es más exacta?", "El texto A dice que el Estado considera cumplida su obligación; el B muestra otra mirada, pero no habla de conformidad", "Ambos textos dicen que hubo acuerdo", "No se puede saber nada de ninguno de los dos", "Hay que apoyarse en lo que dicen: el B habla de un terreno más pequeño, no de conformidad."),
    sc=[("En HGCS: ¿qué es una perspectiva?", "El punto de vista desde el que alguien mira un hecho", "Depende de quién habla y de su experiencia."),
        ("¿Qué hago antes de comparar dos textos?", "Preguntar quién habla y desde dónde", "Saber quién escribe ayuda a entender su mirada."),
        ("¿Es lo mismo comparar que decidir quién tiene la razón?", "No: comparar es ver en qué se coincide y se difiere", "El objetivo es comprender mejor el proceso.")],
    op=("Ficha de ejemplo: «Texto 1 (nota de un diario de ejemplo): la nueva línea del tren acercó el pueblo a la ciudad. Texto 2 (relato de ejemplo de una mujer mapuche del lugar): el tren cruzó el camino por donde la comunidad llevaba sus animales.» "
        "Escribe quién habla en cada texto, una cosa que cada uno destaca y una pregunta que le harías a cada autor.",
        "Texto 1: diario; destaca que el pueblo quedó más cerca de la ciudad; pregunta: ¿para quién fue más cómodo el tren? Texto 2: mujer mapuche; destaca que el camino de los animales quedó cortado; pregunta: ¿qué ruta nueva usaron?",
        ["identifica quién habla en cada texto", "señala lo que cada texto destaca", "formula preguntas respetuosas"],
        ["una tabla de dos filas con autor, lo que destaca y una pregunta"], ["decir que uno de los textos es falso", "inventar datos que no están"],
        "Pregunta: «¿Desde dónde habla esta persona y qué le importa?»."),
    reinforce="Piensa en un cambio reciente de tu barrio o trabajo y escribe cómo lo contaría alguien a quien le convino y alguien a quien no.",
    extend="Explica con un ejemplo por qué la perspectiva de un grupo no reemplaza a la de otro, sino que la completa.",
)

# ======================================================= clase 2
F2 = ("Ficha 2 (de ejemplo). Resumen escrito para este cuaderno sobre Chile entre el siglo XIX y mediados del siglo XX. "
      "Política: la república se organiza con la Constitución de 1833 y más tarde con la de 1925. "
      "Económica: crecen la minería (plata, cobre y salitre) y la agricultura de exportación; en 1939 se crea la CORFO para impulsar la industria. "
      "Social: las ciudades crecen, aparecen la pobreza urbana y el reclamo por derechos del trabajo y de las mujeres. "
      "Medioambiental: la minería y la ampliación de tierras agrícolas transforman bosques, suelos y aguas. "
      "Actores: pueblos indígenas, mujeres, trabajadores, empresarios, funcionarios.")
build(
    O, 2, F2,
    use="Hoy conozco las cuatro dimensiones de un proceso (política, económica, social y medioambiental) y el vocabulario para comparar perspectivas.",
    prior=["Sé que una perspectiva es un punto de vista.", "Distingo fuente primaria de secundaria.", "Reconozco palabras como «ley», «ciudad» y «trabajo»."],
    explain=[
        "Un proceso histórico es un conjunto de cambios que se desarrollan durante años. Para entenderlo miramos cuatro dimensiones: la política (leyes, gobierno, poder), la económica (producción, trabajo, comercio), la social (cómo viven y se organizan las personas) y la medioambiental (cómo se usa y cambia el territorio).",
        "En el siglo XIX y la primera mitad del siglo XX participaron muchos actores: los pueblos indígenas, las mujeres, los trabajadores, los empresarios y el Estado. No todos tuvieron las mismas oportunidades ni fueron escuchados de igual manera. Por eso conviene buscar fuentes de distintos actores.",
        "Una fuente primaria viene de la época estudiada (una carta, un acta); una secundaria la explica después (un libro, un artículo). Ambas sirven: la primaria muestra la mirada de entonces y la secundaria ordena y relaciona muchas fuentes.",
    ],
    vocab=[("proceso", "conjunto de cambios que ocurren durante muchos años"), ("dimensión", "aspecto desde el que se mira un proceso: político, económico, social o medioambiental"), ("fuente primaria", "viene de la época que se estudia"), ("fuente secundaria", "trabajo posterior que explica lo ocurrido"), ("medioambiental", "relativo a la naturaleza y al territorio")],
    worked=[
        ("Clasificar por dimensión", "{F} ¿A qué dimensión pertenece la frase «se crea la CORFO para impulsar la industria»?", ["Habla de producción e industria.", "La producción y el trabajo son parte de la dimensión económica."], "Dimensión económica"),
        ("Primaria o secundaria", "Una carta de 1915 de una trabajadora textil (de ejemplo) cuenta cómo eran los turnos. ¿Qué tipo de fuente es para estudiar 1915?", ["La carta fue escrita en la misma época que se estudia.", "Una fuente de la época es primaria."], "Fuente primaria"),
    ],
    mistakes=[("Estudiar solo la dimensión política y olvidar cómo vivía la gente.", "Un proceso tiene varias dimensiones que se influyen entre sí.", "Pregunta por la economía, la vida social y el territorio, además de las leyes."),
              ("Creer que una fuente secundaria vale menos que una primaria.", "Cumplen funciones distintas: una muestra la época y la otra la explica.", "Usa las secundarias para el panorama y las primarias para comprobar detalles.")],
    T=[
        ("abc", "{F} ¿A qué dimensión pertenece que la minería y la ampliación de tierras agrícolas transformen bosques y aguas?", "A la medioambiental", "A la política", "A la social", "Se refiere a cambios en el territorio y la naturaleza."),
        ("ab", "En HGCS: ¿qué es una fuente primaria?", "Una que viene de la época que se estudia", "Una escrita muchos años después", "Primaria significa que nace en la época estudiada."),
        ("{F} ¿Qué constituciones se nombran en la ficha y de qué años?", "La de 1833 y la de 1925", "La ficha nombra esas dos fechas en la dimensión política."),
        ("abc", "{F} ¿Cuál de estos actores aparece en la lista de la ficha?", "Las mujeres", "Los turistas", "Los banqueros extranjeros", "La ficha nombra a las mujeres entre los actores del proceso."),
        ("ab", "{F} La frase «crecen las ciudades y aparece la pobreza urbana» corresponde a la dimensión:", "Social", "Política", "Habla de cómo viven las personas, es decir, lo social."),
        ("abc", "¿Por qué conviene buscar fuentes de distintos actores?", "Porque cada grupo vivió el proceso de manera distinta", "Porque así hay más páginas que leer", "Porque todos los actores dicen lo mismo", "Distintos actores aportan miradas que se complementan."),
        ("=", "{F} Entre la Constitución de 1833 y la de 1925, ¿cuántos años pasaron?", "1925-1833", "Se restan los dos años para saber el tiempo entre ambas.", " años"),
        ("abc", "{F} Una investigadora quiere saber cómo cambió el trabajo de las personas con la minería. ¿Qué dimensión priorizará?", "La económica, junto con la social", "Solo la política", "Solo la medioambiental", "Trabajo y producción son temas económicos y sociales."),
        ("abc", "Un libro de 2015 sobre la minería del siglo XIX, ¿qué tipo de fuente es para estudiar ese siglo?", "Secundaria", "Primaria", "Ninguna de las dos", "Fue escrito mucho después para explicar lo ocurrido."),
        ("abc", "Un vecino dice: «La historia solo trata de presidentes y leyes». ¿Qué le responderías?", "Que también incluye cómo vivían las personas, el trabajo y el territorio", "Que tiene toda la razón", "Que la historia solo trata de fechas", "Las otras dimensiones muestran la vida de los distintos actores."),
        ("ab", "{F} Un proceso como el uso de tierras agrícolas, ¿se explica bien con una sola dimensión?", "No, porque se mezclan lo económico, lo social y lo ambiental", "Sí, solo con la política", "Los procesos reales suelen involucrar varias dimensiones al mismo tiempo."),
        ("abc", "{F} Se quiere conocer la perspectiva de las mujeres trabajadoras. ¿Qué fuente primaria serviría?", "Una carta de ejemplo escrita por una trabajadora de la época", "Un mapa de ejemplo de las minas", "Un libro actual sobre el salitre", "Una carta propia de la época muestra directamente su mirada."),
        ("abc", "{F} ¿Qué combinación de fuentes ayuda más a comparar perspectivas?", "Un documento oficial, un relato de una comunidad y un texto de una historiadora", "Tres documentos oficiales iguales", "Solo un libro actual", "Combinar actores y tipos de fuente muestra distintos lados del proceso."),
    ],
    ctx=("abc", "En un centro comunitario preparan una exposición sobre cómo cambió la vida de las mujeres entre 1900 y 1950. Tienen un reglamento de una fábrica de 1920 (de ejemplo), una entrevista grabada en 2018 y un texto de una historiadora. ¿Cuál es la fuente primaria?", "El reglamento de la fábrica de 1920", "La entrevista grabada en 2018", "El texto de la historiadora", "Solo el reglamento viene de la época que se estudia."),
    sc=[("En HGCS: ¿cuáles son las cuatro dimensiones de un proceso?", "Política, económica, social y medioambiental", "Permiten mirar un proceso desde varios lados."),
        ("¿Qué diferencia hay entre fuente primaria y secundaria?", "La primaria es de la época y la secundaria la explica después", "Se distinguen por su relación con la época estudiada."),
        ("¿Por qué buscar varios actores?", "Porque cada uno vivió el proceso de forma distinta", "Los actores aportan perspectivas que se complementan.")],
    op=("Ficha de ejemplo: «a) acta de 1930 de un sindicato de costureras; b) informe de 1930 de una empresa; c) libro de 2010 sobre las fábricas de la época; d) cuaderno de cuentas de una costurera, de 1930.» "
        "Clasifica cada fuente en primaria o secundaria, anota qué actor habla en cada una y una dimensión (política, económica, social o medioambiental) sobre la que informaría.",
        "a) primaria, sindicato, social y económica; b) primaria, empresa, económica; c) secundaria, historiadora, social y económica; d) primaria, costurera, económica y social.",
        ["clasifica correctamente las cuatro fuentes", "identifica el actor de cada una", "asocia una dimensión con razón"],
        ["una tabla de cuatro filas y tres columnas"], ["llamar secundaria a todo lo antiguo", "no indicar quién habla"],
        "Pregunta: «¿Qué actor habla en esta fuente y de qué dimensión?»."),
    reinforce="Elige un objeto de tu casa (una boleta antigua, una herramienta) y di si sería fuente primaria o secundaria y qué dimensión podría informar.",
    extend="Escribe una pregunta sobre cada una de las cuatro dimensiones para un mismo lugar de tu comuna.",
)

# ======================================================= clase 3
F3 = ("Ficha 3 (de ejemplo). En 1877 un decreto permitió a las mujeres rendir los exámenes para ingresar a la universidad en Chile. Tres textos inventados sobre esa medida. "
      "Fuente A (editorial de un diario de ejemplo, 1877): «La medida abre a las mujeres un camino que antes se les negaba; la nación necesita ciudadanas instruidas.» "
      "Fuente B (carta de un lector de ejemplo, 1877): «Los estudios universitarios apartarán a las mujeres de sus deberes en el hogar.» "
      "Fuente C (diario íntimo de una joven de ejemplo, 1880): «Quiero estudiar medicina; mi familia duda, pero mi profesora me apoya.»")
build(
    O, 3, F3,
    use="Hoy aprendo a comparar fuentes con una tabla de cuatro columnas: quién habla, qué dice, qué valora o teme y qué no dice.",
    prior=["Sé que una perspectiva depende de quién habla.", "Distingo hecho de opinión.", "Conozco las dimensiones de un proceso."],
    explain=[
        "Para comparar perspectivas sobre un proceso conviene seguir pasos. Paso 1: identifica quién habla, cuándo y desde qué lugar. Paso 2: anota qué dice la fuente con claridad. Paso 3: pregunta qué valora o qué teme el autor. Paso 4: observa qué no dice y qué actores quedan fuera. Paso 5: compara coincidencias y diferencias.",
        "En el siglo XIX las mujeres tenían pocos derechos: no votaban y su educación estaba muy limitada. Cuando se abrió la universidad a las mujeres, hubo quienes lo celebraron y quienes lo rechazaron. Escuchar a ambos lados y a las propias mujeres permite entender mejor lo que ocurrió.",
        "Trabajar con empatía y respeto significa entender por qué alguien pensaba así en su época sin dejar de reconocer los derechos de hoy. Podemos explicar una opinión del pasado sin compartirla, y tampoco sirve burlarse de ella.",
    ],
    vocab=[("valorar", "considerar que algo es bueno o importante"), ("temer", "preocuparse por una consecuencia negativa"), ("contexto", "situación de la época en que se escribió una fuente"), ("silencio de la fuente", "lo que la fuente no dice o los actores que no menciona"), ("contrastar", "comparar para ver coincidencias y diferencias")],
    worked=[
        ("Qué valora cada fuente", "{F} ¿Qué valora la fuente A y qué teme la fuente B?", ["La fuente A valora la instrucción de las mujeres y la considera útil para la nación.", "La fuente B teme que las mujeres abandonen sus deberes en el hogar."], "A valora la instrucción de las mujeres; B teme que dejen sus deberes del hogar"),
        ("Qué no dice", "{F} ¿Qué actor habla en la fuente C que no habla en la A ni en la B?", ["La fuente C es el diario de una joven.", "Las otras dos fuentes hablan sobre las mujeres, pero no escriben desde su experiencia."], "Una joven que quiere estudiar, es decir, una mujer protagonista"),
    ],
    mistakes=[("Quedarse con la primera fuente que se lee y tomarla como la única visión.", "Se pierde el contraste y el proceso queda a medias.", "Lee al menos dos fuentes de actores distintos antes de concluir."),
              ("Burlarse de una opinión del pasado en lugar de explicar por qué se pensaba así.", "No se logra comprender ni la época ni el cambio posterior.", "Pregunta qué valoraba esa persona y qué contexto la rodeaba.")],
    T=[
        ("abc", "{F} ¿Qué permitió el decreto de 1877 según la ficha?", "Que las mujeres rindieran los exámenes para ingresar a la universidad", "Que las mujeres votaran", "Que las mujeres trabajaran en minas", "La ficha lo dice en su primera frase."),
        ("abc", "{F} ¿Quién escribe la fuente C?", "Una joven de ejemplo, en su diario", "Un diario de la capital", "Un lector molesto", "La fuente C es un diario íntimo."),
        ("ab", "En HGCS: ¿qué significa «valorar» algo?", "Considerar que es bueno o importante", "Dudar de que algo sea cierto", "Valorar es darle importancia a algo según lo que nos importa."),
        ("abc", "{F} ¿Qué cuenta la fuente C sobre la familia de la joven?", "Que duda de su deseo de estudiar", "Que la apoya sin dudas", "Que ya la inscribió en la universidad", "La joven escribe que su familia duda y que su profesora la apoya."),
        ("ab", "{F} ¿Qué fuente celebra la medida?", "La fuente A", "La fuente B", "El editorial dice que abre un camino que antes se negaba."),
        ("abc", "{F} ¿En qué se diferencian las fuentes A y B?", "A valora la medida y B teme sus consecuencias", "A habla de 1877 y B de 1880", "A y B dicen lo mismo con otras palabras", "Evalúan de manera opuesta la misma medida."),
        ("=", "{F} Entre el decreto de 1877 y el diario de la fuente C hay una diferencia de años. ¿Cuántos?", "1880-1877", "Se restan las dos fechas para saber el tiempo entre ambas.", " años"),
        ("abc", "{F} ¿Qué no dice la fuente A?", "Cuántas mujeres podrían estudiar en la práctica", "Que la medida es de 1877", "Que la nación necesita ciudadanas instruidas", "La editorial opina sobre la medida, pero no entrega cifras ni habla de cuántas mujeres podrían ingresar."),
        ("abc", "Una compañera dice: «El lector de la carta era tonto». ¿Cuál es una respuesta con empatía y respeto?", "Pensaba según las ideas de su época; veamos qué temía y por qué", "Tiene razón, es una burla justa", "Hay que borrar su carta", "Se puede explicar una opinión sin compartirla ni burlarse de ella."),
        ("abc", "{F} ¿Qué conviene hacer para completar la comparación?", "Buscar la perspectiva de una mujer que ya estudiaba, de otra fuente", "Dar por cierto que todas pensaban igual", "Dejar solo la fuente B", "Sumar nuevas voces ayuda a no quedarse con una sola mirada."),
        ("ab", "{F} Alguien afirma: «Con A, B y C sabemos qué pensaban todas las personas de 1877». ¿Es correcta?", "No, porque son solo tres textos", "Sí, porque hay tres opiniones", "Tres textos de ejemplo muestran algunas voces, no a toda la sociedad."),
        ("abc", "{F} ¿Cuál de estas es una buena comparación escrita?", "A valora la medida, B teme que afecte al hogar y C muestra a una joven con apoyo y dudas familiares", "A es la correcta y las otras no valen", "Los tres textos dicen lo mismo", "Resume lo que dice cada fuente sin descartarlas."),
        ("abc", "{F} Para evitar juzgar solo con valores de hoy, ¿qué pregunta conviene hacerle a la fuente B?", "¿Qué ideas sobre las mujeres eran comunes en su época y quién tenía poder para opinar?", "¿Por qué pensaba mal?", "¿Por qué no pensó como yo?", "La pregunta contextual ayuda a entender sin aprobar."),
    ],
    ctx=("abc", "En una charla de un centro de educación de adultos, se lee una carta de ejemplo de 1900: «Mi hija debería aprender a leer, pero no necesita más que eso». ¿Qué se obtiene al aplicar el paso 3 (qué valora o teme)?", "Que el autor valoraba que las mujeres supieran leer, pero no pensaba en estudios mayores", "Que el autor odiaba la lectura", "Que todas las personas pensaban igual", "El texto muestra una valoración limitada, no una opinión universal."),
    sc=[("¿Cuáles son los cinco pasos para comparar fuentes?", "Quién habla, qué dice, qué valora, qué no dice y comparar", "Siguen un orden que facilita la comparación."),
        ("¿Qué es el silencio de una fuente?", "Lo que no dice o los actores que no menciona", "Notarlo ayuda a buscar otras voces."),
        ("¿Se puede explicar una opinión del pasado sin compartirla?", "Sí, explicando su contexto y lo que valoraba", "Explicar una opinión del pasado no es aprobarla.")],
    op=("Ficha de ejemplo: «Fuente 1 (aviso de un colegio de niñas, 1895): ofrece clases de bordado, lectura y buenas costumbres. Fuente 2 (carta de una profesora, 1895): pide que también se enseñe matemática y ciencias a las niñas.» "
        "Completa una tabla de cuatro columnas (quién habla, qué dice, qué valora, qué no dice) y escribe dos frases que comparen las fuentes.",
        "Fuente 1: colegio; ofrece bordado y buenas costumbres; valora la formación para el hogar; no dice nada sobre estudios superiores. Fuente 2: profesora; pide matemática y ciencias; valora un saber más amplio; no dice cómo se pagaría. Comparación: ambas se ocupan de la educación de las niñas, pero una limita y la otra pide ampliar.",
        ["completa las cuatro columnas con datos del texto", "compara sin descartar ninguna fuente", "usa lenguaje respetuoso"],
        ["una tabla de dos filas y dos frases"], ["inventar datos", "burlarse de una de las fuentes"],
        "Pregunta: «¿Qué valora esta persona y qué no está diciendo?»."),
    reinforce="Lee un aviso o un cartel de tu barrio y anota quién habla, qué valora y qué no dice.",
    extend="Explica por qué el silencio de una fuente también entrega información.",
)

# ======================================================= clase 4
F4 = ("Ficha 4 (de ejemplo). El voto de las mujeres en Chile: en 1934 una ley les permitió votar en elecciones municipales y en 1949 otra ley les reconoció el voto en todas las elecciones. Tres textos inventados. "
      "Fuente A (acta de una asociación de mujeres, 1946, de ejemplo): «Exigimos el voto en todas las elecciones: trabajamos, pagamos cuentas y criamos a la nación.» "
      "Fuente B (discurso de un parlamentario, 1946, de ejemplo): «Las mujeres aún no están preparadas para decidir en política.» "
      "Fuente C (relato de una profesora, década de 1950, de ejemplo): «La primera vez que voté hice la fila con mi madre y mis vecinas, y sentimos que nuestra voz contaba.»")
build(
    O, 4, F4,
    use="Hoy practico con apoyo cómo comparar tres fuentes sobre el voto de las mujeres, separando hechos, opiniones y perspectivas.",
    prior=["Uso los cinco pasos para comparar fuentes.", "Distingo hecho de opinión.", "Sé que las mujeres no siempre pudieron votar."],
    explain=[
        "En Chile las mujeres lograron votar en etapas. Una ley de 1934 les permitió participar en elecciones municipales y una ley de 1949 les reconoció el voto en todas las elecciones. Antes hubo años de organización, reuniones y peticiones de muchas mujeres de distintos lugares y oficios.",
        "Al comparar fuentes sobre este proceso conviene separar tres cosas: los hechos (qué ley hubo y cuándo), las opiniones (qué pensaba cada autor) y las perspectivas (desde qué lugar hablaba). Por ejemplo, una asociación de mujeres pide un derecho y un parlamentario defiende una restricción; los dos hablan de política, pero desde posiciones distintas.",
        "Una buena práctica es escribir una frase por fuente y luego una frase final que las relacione. Así se ve la dimensión política (leyes y derechos), la social (vida de las mujeres) y la económica (trabajo) del mismo proceso.",
    ],
    vocab=[("derecho", "algo que una persona puede exigir y ejercer por ser parte de la sociedad"), ("sufragio", "derecho a votar"), ("asociación", "grupo organizado de personas con un fin común"), ("restricción", "límite que impide hacer algo"), ("ciudadanía", "condición de quien participa en las decisiones de su país")],
    worked=[
        ("Hecho, opinión o perspectiva", "{F} Clasifica la frase de la fuente B: «Las mujeres aún no están preparadas para decidir en política».", ["No se puede comprobar con un documento: expresa lo que piensa el parlamentario.", "Muestra la posición de quien defendía una restricción."], "Es una opinión que refleja una perspectiva contraria al voto femenino"),
        ("Relacionar las fuentes", "{F} ¿Qué relación hay entre la fuente A y la fuente C?", ["La fuente A pide el derecho en 1946.", "La fuente C cuenta, años después, cómo se vivió votar."], "La A exige el derecho y la C muestra cómo se ejerció después"),
    ],
    mistakes=[("Presentar la opinión de la fuente B como si fuera un hecho.", "Se confunde lo que alguien piensa con lo que se puede comprobar.", "Escribe «el parlamentario opinaba que…» y no «las mujeres no estaban preparadas»."),
              ("Contar el voto de las mujeres como un regalo único de una ley.", "Se olvidan los años de organización de las propias mujeres.", "Menciona a las asociaciones y a las personas que lo pidieron.")],
    T=[
        ("abc", "{F} ¿Qué dice la ficha que ocurrió en 1949?", "Una ley reconoció el voto de las mujeres en todas las elecciones", "Se creó el primer partido político", "Se terminó el voto municipal", "La ficha lo indica en la primera frase."),
        ("abc", "{F} ¿Quién escribió la fuente A?", "Una asociación de mujeres", "Un parlamentario", "Una profesora", "El encabezado de la fuente dice que es un acta de una asociación."),
        ("ab", "En HGCS: ¿qué es el sufragio?", "El derecho a votar", "El pago de impuestos", "Sufragio es el derecho a participar en una elección con el voto."),
        ("abc", "{F} ¿Qué pide la fuente A?", "El voto en todas las elecciones", "Más feriados", "Menos impuestos", "Lo dice con esas palabras en su primera frase."),
        ("ab", "Una frase de ejemplo dice: «En 1934 una ley permitió votar a las mujeres en elecciones municipales». Esa frase es:", "Un hecho que se puede comprobar con la ley", "Una opinión que no se puede comprobar", "Nombra una ley y una fecha, que se verifican en un documento."),
        ("abc", "{F} ¿Qué muestra la fuente C?", "Cómo se vivió votar años después, con la fila y las vecinas", "Una discusión del Congreso", "Un reglamento de fábrica", "Cuenta una experiencia posterior al derecho."),
        ("=", "{F} Entre la ley de 1934 y la de 1949, ¿cuántos años pasaron?", "1949-1934", "Se restan los años para saber cuánto tardó el reconocimiento completo.", " años"),
        ("abc", "{F} ¿Qué dimensión del proceso muestra mejor la fuente A?", "La política y la económica, porque habla de derechos y de trabajo", "La medioambiental", "Ninguna", "Reclama un derecho político y menciona trabajo y cuentas."),
        ("abc", "{F} Un estudiante escribe: «Las mujeres no estaban preparadas para votar, según las fuentes». ¿Qué falla?", "Presenta como hecho una opinión de un solo parlamentario", "No usa fechas", "Cita una ley equivocada", "Esa frase es una opinión de un autor, no un hecho."),
        ("abc", "{F} ¿Cuál es una buena frase que relaciona A y B?", "A exige el voto femenino y B defiende que las mujeres no voten, aunque ambos hablan de política", "A y B apoyan lo mismo", "B es la correcta porque es un parlamentario", "Muestra posiciones opuestas sobre un mismo asunto."),
        ("ab", "{F} Para entender mejor el proceso, ¿qué fuente nueva ayudaría?", "Una carta de una mujer del campo sobre su vida y su trabajo", "Otro discurso igual al de B", "Se necesita una perspectiva distinta, no repetir la misma."),
        ("abc", "{F} ¿Por qué sería incompleto decir que el voto fue solo «un regalo» de la ley?", "Porque hubo años de organización y peticiones de mujeres", "Porque la ley no existió", "Porque nadie quiso votar", "Las asociaciones del acta muestran el trabajo previo."),
        ("abc", "{F} Una conclusión bien comparada y respetuosa es:", "Las mujeres pidieron el voto, un parlamentario lo cuestionó y años después votar fue una experiencia compartida", "El debate nunca existió", "Solo importa la fuente C", "Resume las tres perspectivas sin descartar ninguna."),
    ],
    ctx=("abc", "En un taller de la junta de vecinos se leen fragmentos de ejemplo: una mujer pide el voto en una asamblea de 1945 y un vecino dice que «no es cosa de mujeres». ¿Cómo se registra la frase del vecino en una tabla de perspectivas?", "Como una opinión de un actor que se oponía", "Como un hecho comprobado", "Se descarta sin anotarla", "Anotarla permite ver una perspectiva contraria al cambio."),
    sc=[("En HGCS: ¿Qué diferencia hay entre hecho y opinión?", "El hecho se comprueba y la opinión expresa lo que se piensa", "Separarlos evita sacar conclusiones erradas sobre las fuentes."),
        ("¿En qué año se reconoció el voto femenino en todas las elecciones?", "En 1949", "Una ley de ese año lo dispuso."),
        ("¿Quién participó del proceso además de las leyes?", "Las asociaciones y las mujeres que lo pidieron", "Hubo una organización previa de muchas personas.")],
    op=("Ficha de ejemplo: «Fuente 1 (afiche de ejemplo, 1948): ‘Mujer chilena, tu voto vale’. Fuente 2 (editorial de ejemplo, 1948): ‘El voto femenino dividiría a las familias’. Fuente 3 (carta de una obrera, 1948): ‘Trabajo diez horas y aún no puedo opinar con mi voto’.» "
        "Haz una tabla con quién habla, qué dice y qué valora cada fuente. Escribe una frase de comparación y una pregunta que te quedó.",
        "1: quien hace el afiche; dice que el voto vale; valora la participación. 2: un editorialista; dice que dividiría a las familias; valora la unidad familiar. 3: una obrera; dice que trabaja diez horas y no vota; valora la voz de las trabajadoras. Comparación: pedir el voto se enfrenta al temor por la familia. Pregunta: ¿qué respondían las mujeres de las asociaciones?",
        ["identifica quién habla y qué valora", "compara sin descartar ninguna fuente", "plantea una pregunta pertinente"],
        ["una tabla de tres filas, una frase y una pregunta"], ["tratar el editorial como hecho", "no mencionar la fuente de la obrera"],
        "Pregunta: «¿Qué fuente falta para tener una visión más completa?»."),
    reinforce="Escribe dos frases sobre un derecho que hoy ejerces y qué personas lo pidieron antes.",
    extend="Explica por qué una ley y un grupo organizado de personas se influyen mutuamente.",
)

# ======================================================= clase 5
F5 = ("Ficha 5 (de ejemplo). A mediados y fines del siglo XIX se despejaron grandes superficies de bosque en el sur de Chile para sembrar y levantar pueblos. Cuatro textos inventados sobre ese proceso. "
      "Fuente A (informe de un agente colonizador, hacia 1880, de ejemplo): «Se despejaron terrenos con fuego para sembrar trigo y levantar pueblos; el progreso avanza.» "
      "Fuente B (relato de una comunidad mapuche, de ejemplo): «El bosque nos daba leña, alimentos y plantas medicinales; cuando lo quemaron, perdimos más que árboles.» "
      "Fuente C (cuaderno de una mujer de una familia colona, de ejemplo): «Mi madre cocinaba con leña y lavaba en el río; el humo de los campos cubría el cielo por días.» "
      "Fuente D (informe de un científico de la época, de ejemplo): «La tala sin control erosionará los suelos y secará las vertientes.»")
build(
    O, 5, F5,
    use="Hoy aplico la comparación de perspectivas a un proceso con dimensión medioambiental: el uso del bosque y de la tierra en el sur de Chile.",
    prior=["Comparo fuentes con una tabla.", "Reconozco las cuatro dimensiones.", "Escucho distintas voces sin descartarlas."],
    explain=[
        "En el siglo XIX el sur de Chile fue ocupado por el Estado y por familias colonas, y se ampliaron las tierras agrícolas. Para eso se despejaron bosques, muchas veces con fuego. Fue un proceso político (el Estado extendió su control), económico (se buscaba producir trigo), social (llegaron colonos y cambiaron las comunidades) y medioambiental (cambió el paisaje).",
        "Cada actor miró el cambio desde su lugar. Para quien impulsaba la colonización era progreso; para las comunidades mapuche, el bosque era fuente de alimentos, leña y plantas medicinales; para las familias que llegaron, el trabajo diario con el fuego y el río marcaba su vida; y un científico de la época advertía riesgos para los suelos.",
        "Aplicar la comparación a un caso nuevo es usar los mismos pasos: quién habla, qué dice, qué valora, qué no dice y qué cambia en cada dimensión. Al final conviene escribir una conclusión que reconozca varias voces sin ocultar las diferencias.",
    ],
    vocab=[("colono", "persona que llega a vivir y trabajar a un territorio nuevo para ella"), ("erosión", "desgaste del suelo por el agua o el viento"), ("vertiente", "agua que brota de la tierra"), ("territorio", "espacio que habita un grupo y usa para vivir"), ("progreso", "idea de avance material; no todos lo vieron como una mejora")],
    worked=[
        ("Dimensión de cada fuente", "{F} ¿Qué dimensión destaca la fuente D?", ["La fuente D habla de suelos y vertientes.", "Los suelos y el agua pertenecen a lo medioambiental."], "La dimensión medioambiental"),
        ("Qué valora cada actor", "{F} ¿Qué valora la fuente A y qué valora la fuente B?", ["La fuente A valora el avance de las tierras sembradas y los pueblos.", "La fuente B valora lo que el bosque daba a la comunidad."], "A valora el progreso agrícola; B valora los usos del bosque para la vida de la comunidad"),
    ],
    mistakes=[("Quedarse solo con la mirada del que «progresa» y no ver lo que otros perdieron.", "Se pierde parte del proceso si no se miran todos los actores.", "Anota qué ganó y qué perdió cada actor."),
              ("Creer que las advertencias de un científico no sirven por ser de otra época.", "Las advertencias muestran que ya había miradas críticas en ese tiempo.", "Úsalas como una perspectiva más sobre el medio ambiente.")],
    T=[
        ("abc", "{F} ¿Qué se despejó, según la ficha, para sembrar y levantar pueblos?", "Grandes superficies de bosque", "Grandes ciudades", "Minas de salitre", "La ficha lo indica en su primera frase."),
        ("abc", "{F} ¿Quién escribe la fuente B?", "Una comunidad mapuche", "Un agente colonizador", "Un científico", "Es el relato de la comunidad."),
        ("ab", "En HGCS: ¿qué es la erosión?", "El desgaste del suelo por el agua o el viento", "El crecimiento de un bosque", "La erosión desgasta y empobrece los suelos."),
        ("abc", "{F} ¿Qué advierte la fuente D?", "Que la tala sin control erosionará los suelos", "Que sobrará el trigo", "Que subirán los precios", "Habla de riesgos para suelos y vertientes."),
        ("ab", "{F} ¿Qué fuente muestra la vida diaria de una mujer de familia colona?", "La fuente C", "La fuente A", "El cuaderno de una mujer cuenta cocina con leña y lavado en el río."),
        ("abc", "{F} ¿Qué pierde la comunidad según B?", "Más que árboles: alimentos, leña y plantas medicinales", "Solo dinero", "Solo animales de granja", "Lo dice expresamente en su relato."),
        ("abc", "{F} Si el bosque aportaba leña, alimentos y plantas medicinales, ¿cuántos tipos de recursos nombra la fuente B?", "Tres", "Dos", "Cuatro", "Se cuentan leña, alimentos y plantas medicinales."),
        ("abc", "{F} ¿Qué dimensión se ve en la frase «llegaron colonos y cambiaron las comunidades»?", "La social", "La medioambiental", "La política", "Habla de cómo cambia la vida de las personas."),
        ("abc", "{F} Una compañera dice: «A y D se contradicen». ¿Qué respuesta es más exacta?", "A destaca el avance agrícola y D advierte riesgos ambientales; miran distintos efectos del mismo proceso", "A y D dicen exactamente lo mismo", "D no puede ser comparado con A", "Ambos hablan de la tala, con valoraciones diferentes."),
        ("abc", "{F} ¿Qué silencio tiene la fuente A?", "No dice qué pasó con las comunidades que usaban el bosque", "No dice qué es el trigo", "No nombra ningún año", "El informe habla del progreso, pero no de quienes perdieron el bosque."),
        ("ab", "{F} ¿Qué muestra la fuente C que las otras no?", "La vida cotidiana de una familia colona y el humo de los campos", "Las ganancias del comercio de trigo", "Es el único texto que cuenta el trabajo diario con leña y río."),
        ("abc", "{F} ¿Cuál es una conclusión bien comparada?", "El despeje del bosque fue visto como progreso por unos, como pérdida por otros y como riesgo por un científico", "Todos celebraron el cambio", "Solo importa la fuente A", "Reúne las perspectivas sin ocultar diferencias."),
        ("abc", "{F} ¿Qué fuente agregarías para una visión más completa del medio ambiente de la época?", "Un registro de ejemplo de lluvias y cosechas de esos años", "Un manual de cocina actual", "Otro informe igual al de A", "Datos del ambiente permiten comprobar lo que advierte la fuente D."),
    ],
    ctx=("abc", "Una biblioteca rural prepara una muestra con las cuatro fuentes de la ficha. Quieren una frase para el letrero que no tome partido y respete a todas las voces. ¿Cuál sirve más?", "Para unos fue progreso, para otros una pérdida, y un científico advirtió riesgos para el suelo", "El bosque no tenía importancia", "Todo salió bien para todos", "El letrero muestra varias perspectivas sin descartar ninguna."),
    sc=[("¿Qué dimensión destaca hablar de suelos y vertientes?", "La medioambiental", "Son elementos del territorio y la naturaleza."),
        ("¿Qué valoraba la comunidad en el bosque?", "Leña, alimentos y plantas medicinales", "Eran recursos que la comunidad usaba para su vida."),
        ("¿Para qué sirve preguntar «qué no dice» una fuente?", "Para notar actores y efectos que quedan fuera", "El silencio muestra lo que falta.")],
    op=("Ficha de ejemplo: «Fuente 1 (carta de un comerciante, 1890): el ferrocarril trajo trabajo al valle. Fuente 2 (relato de una comunidad, de ejemplo): el ferrocarril dividió nuestros campos. Fuente 3 (nota de una vecina, de ejemplo): el tren permitió que mi hija llegara a la escuela.» "
        "Compara las tres fuentes en una tabla (quién habla, qué dice, qué valora, dimensión) y escribe una conclusión de tres líneas sin descartar ninguna voz.",
        "1: comerciante; trabajo; valora lo económico. 2: comunidad; campos divididos; valora su territorio. 3: vecina; acceso a escuela; valora la educación. Conclusión: el ferrocarril trajo empleo y acceso a escuela, pero también dividió campos; hay ventajas y pérdidas según el actor.",
        ["completa la tabla con datos del texto", "relaciona dimensión con cada fuente", "escribe una conclusión que incluye todas las voces"],
        ["una tabla de tres filas y una conclusión"], ["quedarse con la voz del comerciante", "inventar datos"],
        "Pregunta: «¿Qué ganó y qué perdió cada actor?»."),
    reinforce="Piensa en una obra de tu barrio (una calle, una plaza) y escribe qué ganó y qué perdió cada grupo.",
    extend="Explica por qué un mismo cambio del territorio puede ser progreso para un actor y pérdida para otro.",
)

# ======================================================= clase 6
F6 = ("Ficha 6 (de ejemplo). Cuatro textos inventados sobre la ocupación de la Araucanía en la segunda mitad del siglo XIX, proceso en que el Estado extendió su control sobre ese territorio y el pueblo mapuche perdió gran parte de sus tierras. "
      "Texto A (memoria de un ministerio, de ejemplo): «Se ocupó el territorio para extender la autoridad del Estado y habilitar tierras para la agricultura.» "
      "Texto B (relato de una comunidad mapuche, de ejemplo): «Perdimos tierras y quedamos en terrenos pequeños; nuestras familias se dispersaron.» "
      "Texto C (diario de una mujer de una familia colona, de ejemplo): «Llegamos a una tierra nueva, con miedo y con esperanza; el primer invierno fue duro.» "
      "Texto D (artículo de una historiadora, de ejemplo): «El proceso combinó razones económicas, políticas y de ideas de la época, y tuvo consecuencias duraderas para el pueblo mapuche.»")
build(
    O, 6, F6,
    use="Hoy reviso lo logrado: comparo cuatro perspectivas sobre un proceso, evalúo mi trabajo y decido qué falta para comunicar mi conclusión.",
    prior=["Comparo fuentes con una tabla.", "Reconozco hechos, opiniones y perspectivas.", "Relaciono las cuatro dimensiones."],
    explain=[
        "Revisar lo logrado es comprobar si una comparación cumple criterios. Una buena comparación identifica quién habla, qué dice cada texto, en qué coinciden y en qué se diferencian, y lo hace con respeto. Además reconoce lo que no se sabe y qué fuente falta.",
        "En el caso de la ocupación de la Araucanía hay perspectivas del Estado, de una comunidad mapuche, de una mujer colona y de una historiadora que explica después. Ninguna reemplaza a las otras; juntas muestran un proceso político, económico y social con consecuencias que llegan hasta hoy.",
        "Al cerrar, resume en dos o tres frases lo central, nombra una pregunta que aún queda y decide un paso siguiente: buscar una fuente más, practicar el contraste o explicar tu conclusión a otra persona.",
    ],
    vocab=[("criterio", "regla que usamos para evaluar un trabajo"), ("consecuencia", "efecto que sigue a un hecho"), ("síntesis", "resumen de lo más importante"), ("fuente secundaria", "texto posterior que explica lo ocurrido"), ("decisión posterior", "paso que decido dar después de evaluar")],
    worked=[
        ("Aplicar un criterio", "{F} Revisa la afirmación: «Los cuatro textos dicen lo mismo». ¿Cumple el criterio «reconoce diferencias»?", ["El texto A habla de extender el Estado.", "El texto B habla de pérdida de tierras: son miradas distintas."], "No cumple: hay diferencias claras entre los textos"),
        ("Escribir una síntesis", "{F} Redacta una frase que relacione B y D.", ["B cuenta la pérdida de tierras desde la comunidad.", "D explica el proceso con razones económicas, políticas y de ideas."], "B muestra la experiencia de la pérdida y D explica sus causas generales"),
    ],
    mistakes=[("Dar la conclusión sin mencionar de qué fuentes sale.", "No se puede comprobar el trabajo ni reconocer las voces.", "Cita la fuente con una letra o un nombre en cada afirmación."),
              ("Cerrar la comparación con una sola mirada «ganadora».", "Se pierde el objetivo de comprender distintas perspectivas.", "Resume lo que aporta cada una y lo que falta.")],
    T=[
        ("abc", "{F} ¿Quién escribe el texto C?", "Una mujer de una familia colona", "Una historiadora", "Un ministerio", "La ficha lo indica en la presentación del texto."),
        ("abc", "{F} ¿Qué tipo de fuente es el texto D?", "Secundaria", "Primaria", "Ninguna de las dos", "Es un artículo posterior que explica el proceso."),
        ("ab", "En HGCS: ¿qué es una síntesis?", "Un resumen de lo más importante", "Una copia completa del texto", "Una síntesis recoge lo esencial con pocas palabras."),
        ("abc", "{F} ¿Qué valora el texto A?", "Extender la autoridad del Estado y habilitar tierras", "Recuperar el bosque", "Mantener las tierras de la comunidad", "El texto A lo dice con esas palabras."),
        ("ab", "{F} ¿Qué dice el texto B sobre las familias?", "Que se dispersaron", "Que se reunieron más", "El relato menciona esa consecuencia directamente."),
        ("abc", "{F} ¿Cuál de estas es una consecuencia nombrada en el texto D?", "Efectos duraderos para el pueblo mapuche", "El fin del trigo", "La creación de un puerto", "Lo dice en su última parte."),
        ("=", "Dato de ejemplo: una comunidad tenía 300 hectáreas y después de la ocupación le quedaron 80. ¿Cuántas hectáreas perdió?", "300-80", "Se resta lo que quedó a lo que tenía.", " hectáreas"),
        ("abc", "{F} Una persona afirma que el texto C «justifica» la ocupación. ¿Qué se puede responder con exactitud?", "El texto C cuenta cómo una familia vivió su llegada, sin evaluar el proceso político", "El texto C lo justifica totalmente", "El texto C lo rechaza totalmente", "El diario habla de miedo, esperanza e invierno duro, no de una evaluación."),
        ("abc", "{F} Se evalúa esta comparación: «A dice una cosa, B dice otra». ¿Qué le falta?", "Explicar en qué consisten las diferencias y citar datos de cada texto", "Más adjetivos", "Descartar uno", "Una comparación necesita datos y relación entre las fuentes."),
        ("ab", "{F} Para ser honestos con el trabajo, ¿qué conviene escribir?", "Qué fuentes usamos y qué no sabemos", "Solo la conclusión", "La honestidad exige indicar fuentes y límites."),
        ("abc", "{F} ¿Qué pregunta nueva sirve para continuar?", "¿Qué fuentes de otras mujeres de la época podrían ampliar esta visión?", "¿Cuál texto es más lindo?", "¿Quién escribió más palabras?", "Plantea buscar las voces que aún faltan."),
        ("abc", "{F} ¿Cuál es una buena síntesis final?", "El Estado extendió su control, la comunidad mapuche perdió tierras, familias colonas llegaron con dificultades y la historiadora explica causas variadas", "Solo el Estado importa", "Todos ganaron", "Reúne las cuatro perspectivas con precisión."),
        ("abc", "{F} Tras evaluar tu comparación, notas que no explicaste qué dimensión muestra cada texto. ¿Qué decisión conviene?", "Agregar una columna con la dimensión y volver a revisar", "Dejarlo así", "Borrar la tabla", "Corregir lo faltante mejora la comparación."),
    ],
    ctx=("abc", "En un taller comunitario una persona facilita la lectura de los cuatro textos y pide una conclusión que no ofenda a nadie ni oculte lo ocurrido. ¿Qué enfoque sirve?", "Presentar cada perspectiva con sus datos y decir que juntas permiten entender mejor el proceso", "Elegir solo la visión oficial", "Evitar hablar del tema", "Las perspectivas se exponen con respeto y precisión."),
    sc=[("En HGCS: ¿qué es una consecuencia?", "El efecto que sigue a un hecho", "Una consecuencia se produce por una causa previa."),
        ("¿Qué incluye una buena comparación?", "Quién habla, qué dice, coincidencias y diferencias", "Esos elementos permiten comprender las perspectivas."),
        ("¿Para qué sirve una decisión posterior?", "Para saber qué hacer tras evaluar", "Guía el siguiente paso de aprendizaje.")],
    op=("Elige uno de los procesos que trabajaste (ocupación de la Araucanía, voto de las mujeres o despeje del bosque). Con las fuentes de ejemplo de las clases, escribe una comparación de tres perspectivas en un párrafo de seis líneas. "
        "Marca con una letra qué fuente sostiene cada idea y termina con una pregunta que te quedó y un paso siguiente.",
        "Voto de las mujeres: la asociación pide el voto (A); el parlamentario lo cuestiona (B); la profesora cuenta cómo se vivió votar (C). Coinciden en que era un asunto político; difieren en lo que valoran. Pregunta: ¿cómo era la vida de las mujeres del campo? Paso siguiente: buscar una carta de ejemplo de una campesina.",
        ["identifica tres perspectivas con sus fuentes", "usa datos del texto sin inventar", "cierra con pregunta y paso siguiente"],
        ["un párrafo de seis líneas con letras de fuente y una pregunta"], ["no citar la fuente", "dar una sola mirada como ganadora"],
        "Pregunta: «¿Cada afirmación tiene una fuente que la sostenga?»."),
    reinforce="Vuelve a tu tabla de la clase 3 y agrega una columna que diga qué dimensión muestra cada fuente.",
    extend="Explica a otra persona, con tus palabras, por qué comparar perspectivas ayuda a entender mejor un proceso histórico.",
)
