"""Material del estudiante de 4.º básico, Historia, Geografía y Ciencias Sociales: OA 05 (pueblos indígenas americanos en el presente) y OA 06 (paralelos, meridianos y localización)."""
from __future__ import annotations

from student_lessons import arith, ex, register
from student_content_hi4_a import task

OA5 = "HI04 OA 05"
OA6 = "HI04 OA 06"

# ================================================================ OA 05 · PRESENTE
# ---------------------------------------------------------------- clase 1
P1 = ("Ficha 1: Los pueblos indígenas americanos no son solo del pasado. Hoy viven personas mayas en México, Guatemala y otros países de Centroamérica. "
      "Personas que hablan náhuatl, lengua de los aztecas, viven en el centro de México. Personas que hablan quechua, lengua de los incas, viven en los Andes de Perú, Bolivia y Ecuador. "
      "Los países actuales, como México, Guatemala y Perú, no existían en tiempos de los mayas, los aztecas o los incas; se formaron a comienzos del siglo XIX. "
      "En Chile también viven pueblos originarios, como el mapuche, el aymara y el rapa nui.")
register(
    OA5, 1,
    materials="Lápiz y papel. La ficha está escrita en cada ejercicio. Un mapa de América ayuda, pero no es necesario.",
    use="Aprenderé dónde viven hoy los descendientes de las civilizaciones que estudié. Sirve para entender que estos pueblos continúan en el presente.",
    prior=["Sé quiénes fueron los mayas, aztecas e incas.", "Sé ubicar países en un mapa de América."],
    explain=[
        "Los mayas, los aztecas y los incas formaron grandes civilizaciones del pasado. Pero sus descendientes siguen viviendo hoy. Hay personas mayas en México, Guatemala y otros países de Centroamérica. Hay personas que hablan náhuatl en el centro de México y personas que hablan quechua en los Andes de Perú, Bolivia y Ecuador.",
        "Los países actuales, como México, Guatemala y Perú, no existían cuando vivieron esas civilizaciones. Se formaron a comienzos del siglo XIX. Por eso hay que ubicar el lugar con cuidado: decimos «en lo que hoy es Perú» y no «en el Perú de los incas». Así evitamos mezclar épocas.",
        "En Chile también viven pueblos originarios, como el mapuche, el aymara y el rapa nui. Sus historias son propias y no son las mismas de mayas, aztecas e incas. Para conocerlas bien conviene escuchar a sus comunidades y a sus educadores tradicionales, que enseñan su lengua y su cultura.",
    ],
    vocab=[("pueblo indígena", "grupo de personas con una historia, lengua y cultura propias, que vivía en América antes de la llegada de los europeos"), ("descendiente", "persona que viene de los antepasados de un pueblo"), ("náhuatl", "lengua de los aztecas, que hoy se sigue hablando"), ("quechua", "lengua de los incas, que hoy se sigue hablando"), ("pueblo originario", "pueblo que vivía en un territorio desde antes de la llegada de otros")],
    worked=[
        {"title": "Ubicar un pueblo hoy", "problem": f"{P1} ¿Dónde viven hoy personas que hablan quechua?", "steps": ["Busco la palabra quechua en la ficha.", "Dice que viven en los Andes de Perú, Bolivia y Ecuador."], "answer": "En los Andes de Perú, Bolivia y Ecuador"},
        {"title": "Evitar un error de época", "problem": f"{P1} ¿Es correcto decir «los incas del Perú»?", "steps": ["Reviso cuándo se formó Perú.", "Se formó a comienzos del siglo XIX, mucho después de los incas."], "answer": "No, es mejor decir «los incas, en lo que hoy es Perú»"},
    ],
    mistakes=[
        {"wrong": "Decir que los mayas, aztecas e incas ya no existen.", "why": "Se confunde el imperio con el pueblo.", "fix": "Recuerda que hoy hay personas mayas, nahuas y quechuas."},
        {"wrong": "Decir que los países actuales ya existían en tiempos de los incas.", "why": "Se mezclan épocas.", "fix": "Los países actuales se formaron a comienzos del siglo XIX."},
    ],
    tiers={
        "recovery": [
            ex(f"{P1} ¿Dónde viven hoy personas mayas?", "en México, Guatemala y otros países de Centroamérica", "La ficha lo indica."),
            ex(f"{P1} ¿Qué lengua hablan personas del centro de México que son descendientes de los aztecas?", "náhuatl", "La ficha lo dice."),
            ex(f"{P1} ¿Qué pueblos originarios nombra la ficha para Chile?", "mapuche, aymara y rapa nui", "La ficha nombra a esos tres."),
        ],
        "understand": [
            ex(f"{P1} ¿Existían México, Guatemala y Perú en tiempos de los mayas, aztecas o incas?", "No", "La ficha dice que se formaron a comienzos del siglo XIX."),
            ex(f"{P1} ¿Qué lengua es hoy la de los incas?", "el quechua", "La ficha lo indica."),
            ex(f"{P1} ¿Los pueblos indígenas son solo del pasado?", "No, siguen viviendo hoy", "La ficha lo dice desde el comienzo."),
        ],
        "apply": [
            ex(f"{P1} En un mapa, ¿dónde ubicarías hoy a las personas que hablan quechua: los Andes o la costa del Caribe?", "los Andes", "La ficha lo ubica en los Andes de Perú, Bolivia y Ecuador."),
            ex(f"{P1} Un cartel dice «Cusco, ciudad de los incas del Perú». ¿Qué frase es más precisa?", "Cusco, ciudad de los incas, en lo que hoy es Perú", "Evita mezclar épocas."),
            ex(f"{P1} Un taller enseña náhuatl en el centro de México. ¿De qué civilización antigua era lengua el náhuatl, según la ficha?", "de los aztecas", "La ficha dice que el náhuatl es la lengua de los aztecas."),
        ],
        "reason": [
            ex(f"{P1} Tomás dice: «Los mayas desaparecieron hace siglos». ¿Qué dato de la ficha lo corrige?", "Hoy viven personas mayas en México, Guatemala y otros países", "La ficha muestra su presencia hoy."),
            ex(f"{P1} Ana dice: «La historia de los mapuche es la misma que la de los incas». ¿Por qué no es correcto?", "Cada pueblo tiene su propia historia, lengua y cultura", "La ficha los nombra como pueblos distintos."),
        ],
        "challenge": [
            ex(f"{P1} Clasifica cada frase como «pasado» o «presente»: a) los incas gobernaban desde Cusco; b) hoy millones hablan quechua; c) los aztecas fundaron Tenochtitlán.", "a: pasado; b: presente; c: pasado", "Las frases a y c hablan de hechos antiguos; b habla de hoy."),
            ex(f"{P1} Marca la frase que evita el error de época. A) «El presidente de los aztecas era el emperador». B) «El emperador azteca gobernaba en lo que hoy es el centro de México».", "B", "B usa el lugar actual sin inventar un país."),
        ],
    },
    context=[ex("En una feria escolar, un afiche dice: «Taller de quechua para niñas y niños». Una compañera pregunta si esa lengua aún se habla. ¿Qué responderías con la ficha?", "Sí, millones de personas hablan quechua hoy en los Andes", "La ficha dice que el quechua se habla en la actualidad.")],
    selfcheck=[
        ex("¿Dónde viven hoy personas mayas?", "en México, Guatemala y otros países de Centroamérica", "Son países actuales donde viven mayas."),
        ex("¿Qué lengua hablan personas nahuas?", "náhuatl", "Es la lengua de los aztecas."),
        ex("¿Por qué conviene decir «en lo que hoy es Perú»?", "porque Perú no existía en tiempos de los incas", "Evita mezclar épocas."),
    ],
    open_task=task(
        f"Dibuja un mapa simple de América con tres manchas de colores: mayas hoy (sur de México y Centroamérica), nahuas hoy (centro de México) y quechuas hoy (Andes). Escribe un rótulo en cada mancha. Después escribe una frase con «en lo que hoy es…» para uno de los pueblos. {P1} Para saber más de los pueblos originarios de Chile, consulta con el educador o educadora tradicional de tu escuela o comunidad.",
        "Mapa con tres manchas rotuladas. Frase: «Los incas gobernaban desde Cusco, en lo que hoy es Perú».",
        ["tres manchas bien ubicadas", "rótulos", "una frase sin error de época"], ["mapa", "una frase"], ["ubicar a los quechuas en México", "decir que ya no existen"],
        "Pregunta cómo se llama hoy un país donde viven mayas. Respuestas posibles: México o Guatemala."),
    reinforce="Nombra tres pueblos indígenas americanos de hoy y dónde viven.",
    extend="Escribe dos preguntas que harías a una persona que habla quechua o náhuatl.",
)

# ---------------------------------------------------------------- clase 2
P2 = ("Ficha 2: Cuatro fuentes para investigar a los pueblos indígenas de hoy. (A) Sitio web de un museo, con nombre de la institución, autor y fecha. (B) Entrada de un blog sin autor ni fecha, que dice que «los mayas ya no existen». "
      "(C) Fotografía de una feria de tejidos, con el pie de foto «Mercado de tejidos de una comunidad quechua, 2019». (D) Gráfico de práctica con datos inventados para ejercitar, no son cifras reales: "
      "Aldea Uno, 40 personas que hablan quechua; Aldea Dos, 25; Aldea Tres, 65.")
register(
    OA5, 2,
    materials="Lápiz y papel. Las fuentes están escritas en cada ejercicio.",
    use="Aprenderé a buscar y evaluar fuentes distintas (sitios web, fotos, gráficos y textos) sobre los pueblos indígenas de hoy. Sirve para investigar sin creer cualquier cosa.",
    prior=["Sé qué es la procedencia de una fuente.", "Sé leer un gráfico de barras sencillo."],
    explain=[
        "Para investigar sobre el presente de los pueblos indígenas podemos usar muchas fuentes: imágenes, videos, páginas web, gráficos y textos. No todas valen lo mismo. Antes de usar una, preguntamos: ¿quién la hizo?, ¿cuándo?, ¿tiene autor o institución?, ¿dice de dónde saca los datos?",
        "Una página de un museo con institución, autor y fecha es más confiable que un blog sin autor ni fecha. Una fotografía con pie de foto que dice dónde y cuándo se tomó nos ayuda más que una foto sin explicación. Si dos fuentes dicen lo contrario, buscamos una tercera para contrastar.",
        "Los gráficos nos ayudan a comparar cantidades. En un gráfico de barras, una barra más alta significa un número mayor. Leemos el título, cada barra y la unidad. Atención: el gráfico de práctica de la ficha tiene datos inventados, y por eso solo sirve para aprender a leer gráficos, no para afirmar nada real.",
    ],
    vocab=[("confiable", "que merece que le creamos porque indica quién, cuándo y de dónde saca los datos"), ("contrastar", "comparar fuentes para ver si dicen lo mismo"), ("pie de foto", "texto breve que explica una fotografía"), ("gráfico de barras", "dibujo que usa barras para comparar cantidades"), ("institución", "organización, como un museo o un ministerio")],
    worked=[
        {"title": "Elegir la fuente más confiable", "problem": f"{P2} ¿Cuál es más confiable, A o B? ¿Por qué?", "steps": ["A tiene institución, autor y fecha.", "B no tiene autor ni fecha."], "answer": "A, porque dice quién la hizo y cuándo"},
        {"title": "Leer un gráfico", "problem": f"{P2} ¿Qué aldea del gráfico de práctica tiene más personas que hablan quechua?", "steps": ["Comparo 40, 25 y 65.", "65 es el mayor."], "answer": "Aldea Tres"},
    ],
    mistakes=[
        {"wrong": "Creer una afirmación solo porque aparece en internet.", "why": "No se revisa quién la escribió.", "fix": "Revisa autor, fecha y de dónde saca los datos."},
        {"wrong": "Usar los datos de práctica como si fueran reales.", "why": "No se lee la aclaración.", "fix": "Lee el aviso: son datos inventados para ejercitar."},
    ],
    tiers={
        "recovery": [
            ex(f"{P2} ¿Qué fuente tiene institución, autor y fecha?", "la fuente A", "Es el sitio web del museo."),
            ex(f"{P2} ¿Qué fuente no tiene autor ni fecha?", "la fuente B", "Es la entrada del blog."),
            ex(f"{P2} ¿Qué aldea tiene 25 personas que hablan quechua en el gráfico de práctica?", "Aldea Dos", "Así lo indica el gráfico."),
        ],
        "understand": [
            ex(f"{P2} ¿Qué dice el pie de foto de la fuente C?", "que es un mercado de tejidos de una comunidad quechua, en 2019", "El pie explica dónde y cuándo se tomó."),
            ex(f"{P2} ¿Por qué no podemos usar el gráfico D para afirmar algo real?", "porque tiene datos inventados", "La ficha lo avisa."),
            ex(f"{P2} ¿Qué significa contrastar fuentes?", "compararlas para ver si dicen lo mismo", "Así se confirma un dato."),
        ],
        "apply": [
            arith(f"{P2} En el gráfico de práctica, ¿cuántas personas hablan quechua en las tres aldeas juntas?", "40+25+65", "Se suman las tres aldeas.", " personas"),
            arith(f"{P2} En el gráfico de práctica, ¿cuántas personas más hay en la Aldea Tres que en la Aldea Dos?", "65-25", "Se resta la cantidad menor de la mayor.", " personas"),
            ex(f"{P2} Quieres saber cómo son los tejidos de una comunidad quechua. ¿Qué fuente te muestra directamente cómo son?", "la fuente C", "Es una fotografía de un mercado de tejidos."),
        ],
        "reason": [
            ex(f"{P2} El blog (fuente B) dice que «los mayas ya no existen». ¿Qué debes hacer antes de creerlo?", "Revisar quién lo escribió y contrastarlo con otras fuentes", "No tiene autor ni fecha y es posible contrastarlo."),
            ex(f"{P2} Luis dice: «El gráfico D prueba que hay 130 personas quechuas en el mundo». ¿Qué error tiene?", "Los datos son inventados y solo sirven para practicar", "No se puede afirmar nada real con ellos."),
        ],
        "challenge": [
            ex(f"{P2} Ordena las fuentes A, B y C de más a menos confiable para saber algo sobre una comunidad quechua, y explica en una frase.", "A, C y B; A tiene institución, autor y fecha, C tiene pie con lugar y año, B no tiene ninguno", "Cuantos más datos de procedencia, más confiable."),
            ex(f"{P2} Se contradicen A y B. ¿Qué es lo más razonable: creer a B, creer a A o buscar una tercera fuente?", "buscar una tercera fuente", "Contrastar ayuda a decidir."),
        ],
    },
    context=[ex("Para una tarea, un compañero encuentra un video sin título ni autor sobre un pueblo indígena. ¿Qué dos preguntas le harías antes de usarlo?", "¿Quién lo hizo? ¿Cuándo y de dónde saca los datos?", "Son las preguntas de procedencia.")],
    selfcheck=[
        ex("¿Qué fuente de la ficha es más confiable: A o B?", "A", "Tiene institución, autor y fecha."),
        ex("¿Qué significa contrastar fuentes?", "compararlas para ver si dicen lo mismo", "Ayuda a confirmar los datos."),
        ex("En un gráfico de barras, ¿qué indica una barra más alta?", "un número mayor", "La altura representa la cantidad."),
    ],
    open_task=task(
        f"Haz una tabla con las fuentes A, B y C y estas columnas: «¿Tiene autor o institución?», «¿Tiene fecha?», «¿La usaría? Sí o no». Completa cada fila con los datos de la ficha. Escribe una frase que explique tu decisión sobre la fuente B. {P2}",
        "A: sí, sí, sí. B: no, no, no. C: sí (pie de foto), sí, sí. B no, porque no tiene autor ni fecha.",
        ["tres filas completas", "decisiones coherentes", "una explicación"], ["tabla", "una frase"], ["usar la fuente B sin explicar", "dejar columnas vacías"],
        "Pregunta qué haría si solo tuviera la fuente B. La respuesta esperada es buscar otras fuentes."),
    reinforce="Nombra tres preguntas que hay que hacer a una fuente antes de usarla.",
    extend="Diseña un pequeño gráfico de barras con datos inventados de tu curso y escribe su título.",
)

# ---------------------------------------------------------------- clase 3
P3 = ("Ficha 3: Palabras y alimentos que usamos hoy y vienen de pueblos indígenas de América. "
      "Del quechua: papa, palta, choclo, poroto, zapallo, guagua. Del náhuatl: tomate, chocolate, chile. "
      "Alimentos de origen americano que hoy se comen en muchos países: maíz, papa, tomate, cacao, zapallo, quinua. "
      "Palabras de otro origen, para comparar: mesa, ventana, camino.")
register(
    OA5, 3,
    materials="Lápiz y papel. La ficha está escrita en cada ejercicio.",
    use="Aprenderé qué palabras y alimentos que usamos hoy vienen de lenguas y cultivos indígenas. Sirve para ver la influencia de estos pueblos en nuestra vida diaria.",
    prior=["Sé qué lengua hablaban los aztecas y los incas.", "Sé qué cultivaban los mayas, aztecas e incas."],
    explain=[
        "Los pueblos indígenas dejaron una gran herencia. Muchas palabras que usamos cada día vienen del quechua, como papa, palta, choclo, poroto, zapallo y guagua. Otras vienen del náhuatl, como tomate, chocolate y chile. Cuando las decimos, usamos palabras que vienen de lenguas americanas.",
        "También heredamos alimentos. El maíz, la papa, el tomate, el cacao, el zapallo y la quinua se cultivaban en América mucho antes de que llegaran los europeos. Hoy se comen en muchos países del mundo. Piensa en una ensalada con tomate, unas papas fritas o un chocolate: todos tienen origen americano.",
        "No todas las palabras vienen de lenguas indígenas. Mesa, ventana y camino tienen otro origen. Para saber de dónde viene una palabra, se consulta un diccionario o a una persona que conozca la lengua. Es importante aprender con respeto, porque las lenguas indígenas siguen vivas y tienen hablantes hoy.",
    ],
    vocab=[("herencia", "lo que una cultura deja a las que vienen después"), ("origen", "lugar o pueblo de donde viene algo"), ("quechua", "lengua de los Andes, hablada por los incas"), ("náhuatl", "lengua de los aztecas"), ("alimento americano", "alimento que se cultivaba en América antes de que llegaran los europeos")],
    worked=[
        {"title": "Reconocer el origen de una palabra", "problem": f"{P3} ¿De qué lengua viene la palabra «poroto»?", "steps": ["Busco poroto en las listas.", "Está entre las palabras del quechua."], "answer": "Del quechua"},
        {"title": "Distinguir lo que no es indígena", "problem": f"{P3} ¿Cuál de estas palabras no viene del quechua ni del náhuatl: papa o mesa?", "steps": ["Papa está en la lista del quechua.", "Mesa está entre las palabras de otro origen."], "answer": "Mesa"},
    ],
    mistakes=[
        {"wrong": "Pensar que todas las palabras vienen del español.", "why": "No se conoce la influencia de otras lenguas.", "fix": "Revisa las listas: muchas vienen del quechua y del náhuatl."},
        {"wrong": "Pensar que el tomate o la papa vinieron de Europa.", "why": "Se piensa en cómo los conocemos hoy.", "fix": "Son alimentos americanos que se cultivaban antes de la llegada de los europeos."},
    ],
    tiers={
        "recovery": [
            ex(f"{P3} ¿De qué lengua viene la palabra «palta»?", "del quechua", "Está en la lista del quechua."),
            ex(f"{P3} ¿De qué lengua viene la palabra «tomate»?", "del náhuatl", "Está en la lista del náhuatl."),
            ex(f"{P3} ¿De qué lengua viene la palabra «guagua»?", "del quechua", "Está en la lista del quechua."),
        ],
        "understand": [
            ex(f"{P3} ¿Cuál de estos alimentos es de origen americano según la ficha: el maíz o el trigo?", "el maíz", "El trigo no está en la lista de alimentos americanos."),
            ex(f"{P3} ¿Qué palabra de la lista viene del náhuatl y es un dulce?", "chocolate", "Chocolate está en la lista del náhuatl."),
            ex(f"{P3} ¿Las lenguas indígenas siguen vivas hoy?", "Sí", "La ficha dice que tienen hablantes hoy."),
        ],
        "apply": [
            arith(f"{P3} La lista del quechua tiene seis palabras y la del náhuatl tiene tres. ¿Cuántas palabras indígenas hay entre las dos listas?", "6+3", "Se suman las palabras de ambas listas.", " palabras"),
            ex(f"{P3} Una ensalada lleva tomate, choclo y palta. ¿Cuántas palabras de ese menú vienen del quechua?", "2", "Choclo y palta son del quechua; tomate es del náhuatl."),
            ex(f"{P3} Clasifica las palabras como «de lengua indígena» o «de otro origen»: papa, ventana, chile, camino.", "papa: indígena; ventana: otro origen; chile: indígena; camino: otro origen", "Papa es quechua, chile es náhuatl y las otras dos están en la lista de otro origen."),
        ],
        "reason": [
            ex(f"{P3} Tomás dice: «El tomate es un alimento europeo». ¿Qué dato de la ficha lo contradice?", "El tomate es un alimento americano y su nombre viene del náhuatl", "La ficha lo muestra en dos listas."),
            ex(f"{P3} Ana dice: «Al decir poroto uso una palabra indígena». ¿Tiene razón?", "Sí", "Poroto viene del quechua."),
        ],
        "challenge": [
            ex(f"{P3} Elige las dos palabras que vienen del quechua: tomate, choclo, chocolate, poroto.", "choclo y poroto", "Tomate y chocolate están en la lista del náhuatl."),
            ex(f"{P3} Elige la afirmación mejor sostenida. A) Todos los alimentos de hoy vinieron de América. B) Varios alimentos y palabras de hoy vienen de pueblos indígenas de América.", "B", "B no exagera: se apoya en las listas."),
        ],
    },
    context=[ex("En un almuerzo hay porotos, choclo, zapallo y palta. ¿Qué lengua indígena aportó los nombres de esos cuatro alimentos?", "el quechua", "Las cuatro palabras están en la lista del quechua.")],
    selfcheck=[
        ex("¿De qué lengua viene «choclo»?", "del quechua", "Está en la lista del quechua."),
        ex("¿Qué palabra de la lista viene del náhuatl: tomate o zapallo?", "tomate", "Zapallo es del quechua."),
        ex("¿Qué alimento americano se cultivaba para hacer tortillas?", "el maíz", "Las civilizaciones lo cultivaban."),
    ],
    open_task=task(
        f"Dibuja un plato de comida con cinco alimentos americanos de la ficha y escribe el nombre de cada uno. Debajo escribe una frase: «De estos alimentos, las palabras … vienen del quechua y la palabra … viene del náhuatl». {P3}",
        "Plato con maíz, papa, tomate, zapallo y cacao. Palabras del quechua: papa y zapallo. Palabra del náhuatl: tomate.",
        ["cinco alimentos de la ficha", "origen de al menos dos palabras"], ["dibujo", "una frase"], ["incluir alimentos no americanos", "confundir quechua y náhuatl"],
        "Pregunta qué alimento del plato comes más seguido. Es una conversación, no una respuesta única."),
    reinforce="Nombra cinco palabras de origen indígena que uses en tu casa o escuela.",
    extend="Pregunta en tu familia o curso qué otras palabras creen que vienen de lenguas indígenas, y revisa en un diccionario.",
)

# ---------------------------------------------------------------- clase 4
P4 = ("Ficha 4: Antes y hoy. ANTES (siglos XV y XVI): los mayas, aztecas e incas tenían gobernantes propios, como ciudades-estado o imperios. "
      "HOY: los pueblos indígenas viven dentro de países con leyes, presidente y autoridades. En Perú, el quechua es oficial en las zonas donde se habla. En Guatemala se reconocen varios idiomas mayas. "
      "CONTINUIDADES: muchas personas siguen hablando lenguas indígenas, tejiendo, cocinando con maíz y celebrando fiestas tradicionales. "
      "Perspectiva: una guía de turismo cuenta a los pueblos indígenas solo como «cosa del pasado». Una dirigente indígena dice que su pueblo es parte del presente.")
register(
    OA5, 4,
    materials="Lápiz y papel. La ficha está escrita en cada ejercicio.",
    use="Aprenderé a distinguir qué cambió y qué continúa en la vida de los pueblos indígenas desde el pasado hasta hoy. Sirve para no ver a estos pueblos solo como cosa del pasado.",
    prior=["Sé qué es un cambio y qué es una continuidad.", "Sé que una perspectiva es un punto de vista."],
    explain=[
        "Cuando comparamos el pasado con el presente, buscamos cambios y continuidades. Un cambio es algo que ya no es igual que antes. Una continuidad es algo que sigue igual o muy parecido. Con ambas ideas podemos entender cómo han vivido los pueblos indígenas a lo largo del tiempo.",
        "Hubo cambios importantes: ya no existen los imperios azteca e inca, y las ciudades-estado mayas del período clásico. Hoy los pueblos indígenas viven dentro de países con leyes, presidentes y autoridades. En algunos lugares se reconocen sus idiomas, como el quechua en Perú o varios idiomas mayas en Guatemala. Pero hay muchas continuidades: las lenguas, los tejidos, la comida con maíz y las fiestas tradicionales.",
        "También hay perspectivas distintas. Una guía de turismo puede contar a los pueblos indígenas solo como «cosa del pasado». Una dirigente indígena puede decir que su pueblo es parte del presente. La segunda mirada incluye a las personas que viven hoy, y ayuda a no confundir historia con desaparición.",
    ],
    vocab=[("cambio", "algo que ya no es igual que antes"), ("continuidad", "algo que sigue igual o muy parecido a través del tiempo"), ("lengua oficial", "idioma reconocido por las leyes de un lugar"), ("dirigente", "persona que representa y lidera a un grupo"), ("tradición", "costumbre que pasa de generación en generación")],
    worked=[
        {"title": "Identificar un cambio", "problem": f"{P4} ¿Qué cambió entre los imperios del pasado y hoy?", "steps": ["Antes había gobernantes propios, como emperadores.", "Hoy los pueblos viven dentro de países con leyes y presidente."], "answer": "Hoy viven dentro de países con leyes, presidente y autoridades"},
        {"title": "Identificar una continuidad", "problem": f"{P4} ¿Qué continúa desde el pasado hasta hoy?", "steps": ["Busco lo que dice la ficha en continuidades.", "Muchas personas siguen hablando lenguas, tejiendo y cocinando con maíz."], "answer": "Las lenguas, los tejidos, la comida con maíz y las fiestas"},
    ],
    mistakes=[
        {"wrong": "Decir que los pueblos indígenas ya no existen porque terminaron los imperios.", "why": "Se confunde el fin de un imperio con el fin de un pueblo.", "fix": "Piensa en las continuidades: lengua, tejidos y fiestas."},
        {"wrong": "Decir que nada ha cambiado desde los incas.", "why": "Se piensa en una sola época.", "fix": "Hoy no hay imperio: hay países con leyes."},
    ],
    tiers={
        "recovery": [
            ex(f"{P4} ¿Qué lengua es oficial en las zonas de Perú donde se habla?", "el quechua", "La ficha lo indica."),
            ex(f"{P4} ¿Qué idiomas se reconocen en Guatemala?", "varios idiomas mayas", "La ficha lo indica."),
            ex(f"{P4} ¿Cómo se llama algo que sigue igual a través del tiempo?", "continuidad", "Es la definición de continuidad."),
        ],
        "understand": [
            ex(f"{P4} ¿Cuál es una continuidad: hablar lenguas indígenas o gobernar con un emperador?", "hablar lenguas indígenas", "La ficha la nombra como algo que sigue hoy."),
            ex(f"{P4} ¿Cómo cuenta la guía de turismo a los pueblos indígenas?", "como cosa del pasado", "La ficha lo dice."),
            ex(f"{P4} ¿Qué dice la dirigente indígena?", "que su pueblo es parte del presente", "La ficha lo dice."),
        ],
        "apply": [
            ex(f"{P4} Clasifica como «cambio» o «continuidad»: hoy los pueblos indígenas viven dentro de países con presidente.", "cambio", "Antes había emperadores o gobernantes propios."),
            ex(f"{P4} Clasifica como «cambio» o «continuidad»: hoy se sigue cocinando con maíz.", "continuidad", "El maíz sigue siendo alimento importante."),
            ex(f"{P4} Clasifica como «cambio» o «continuidad»: hoy se sigue hablando quechua.", "continuidad", "La lengua se mantiene desde el pasado."),
        ],
        "reason": [
            ex(f"{P4} Sofía dice: «La perspectiva de la guía de turismo es completa». ¿Qué le falta?", "La mirada de las personas indígenas que viven hoy", "Presenta a los pueblos solo como cosa del pasado."),
            ex(f"{P4} Pedro dice: «Como ya no hay imperios, ya no hay pueblos indígenas». ¿Qué dato de la ficha lo corrige?", "Muchas personas siguen hablando lenguas indígenas y manteniendo tradiciones", "Esas continuidades muestran su presencia."),
        ],
        "challenge": [
            ex(f"{P4} Marca la frase que une un cambio y una continuidad. A) «Ya no hay imperios y se siguen hablando lenguas indígenas». B) «Ya no hay imperios y ya no hay lenguas indígenas».", "A", "A reconoce lo que cambió y lo que continúa."),
            ex(f"{P4} ¿Qué es más útil para conocer el presente de un pueblo indígena: escuchar a una persona de ese pueblo o leer solo una guía de turismo?", "escuchar a una persona de ese pueblo", "Entrega la perspectiva de quien vive esa realidad."),
        ],
    },
    context=[ex("Una compañera dice: «Mi abuela teje como se tejía hace siglos». ¿Eso es un cambio o una continuidad?", "una continuidad", "Una práctica sigue de generación en generación.")],
    selfcheck=[
        ex("¿Qué es un cambio?", "algo que ya no es igual que antes", "Es lo contrario de una continuidad."),
        ex("¿Qué es una continuidad?", "algo que sigue igual o muy parecido a través del tiempo", "Mantiene algo del pasado."),
        ex("¿Por qué conviene escuchar a las personas indígenas de hoy?", "porque ellas viven el presente de su pueblo", "Ofrecen su propia perspectiva."),
    ],
    open_task=task(
        f"Haz una tabla de dos columnas: «cambios» y «continuidades». Escribe dos datos en cada columna usando la ficha. Debajo, escribe una frase que explique por qué es importante no ver a los pueblos indígenas solo como cosa del pasado. {P4}",
        "Cambios: ya no hay imperios; viven dentro de países con leyes. Continuidades: se habla quechua; se cocina con maíz. Importa porque siguen viviendo hoy.",
        ["dos cambios", "dos continuidades", "una explicación"], ["tabla", "una frase"], ["confundir cambios con continuidades", "decir que los pueblos desaparecieron"],
        "Pregunta cuál continuidad conoce de su familia o barrio."),
    reinforce="Explica con tus palabras la diferencia entre un cambio y una continuidad.",
    extend="Escribe una pregunta que harías a una dirigente indígena sobre el presente de su pueblo.",
)

# ---------------------------------------------------------------- clase 5
P5 = ("Ficha 5: Pregunta: ¿tienen los pueblos indígenas protagonismo hoy? Datos. (1) Rigoberta Menchú, mujer maya de Guatemala, recibió el Premio Nobel de la Paz en 1992 por defender los derechos de los pueblos indígenas. "
      "(2) Varias lenguas indígenas son oficiales o están reconocidas en distintos países. (3) Alimentos y palabras indígenas se usan en todo el continente. "
      "(4) No todos los pueblos viven en las mismas condiciones; en algunos lugares aún enfrentan dificultades. (5) La ficha no dice cuántas personas indígenas hay en cada país.")
register(
    OA5, 5,
    materials="Lápiz y papel. La ficha está escrita en cada ejercicio.",
    use="Aprenderé a defender una conclusión sobre el protagonismo de los pueblos indígenas de hoy con evidencia y a reconocer un límite.",
    prior=["Sé que un argumento tiene afirmación, evidencia y límite.", "Sé que los pueblos indígenas viven hoy."],
    explain=[
        "Protagonismo significa tener un papel importante. Para saber si los pueblos indígenas tienen protagonismo hoy, buscamos evidencia. Un ejemplo es Rigoberta Menchú, mujer maya de Guatemala, que recibió el Premio Nobel de la Paz en 1992 por defender los derechos de los pueblos indígenas.",
        "Otra evidencia es que varias lenguas indígenas son oficiales o están reconocidas en distintos países. También se usan en todo el continente alimentos y palabras de origen indígena. Con estos datos podemos afirmar que los pueblos indígenas tienen un papel importante en el presente de América.",
        "Pero un buen argumento también reconoce un límite. No todos los pueblos viven en las mismas condiciones y en algunos lugares aún enfrentan dificultades. Además, la ficha no dice cuántas personas indígenas hay en cada país, así que no debemos dar cifras. La conclusión debe ser tan fuerte como la evidencia.",
    ],
    vocab=[("protagonismo", "papel importante que alguien tiene en un hecho"), ("Premio Nobel de la Paz", "premio internacional a quien trabaja por la paz y los derechos"), ("derechos", "cosas que toda persona puede exigir para vivir con dignidad"), ("evidencia", "dato o fuente que apoya una idea"), ("límite", "lo que no podemos afirmar")],
    worked=[
        {"title": "Elegir evidencia", "problem": f"{P5} Afirmación: «Hay personas indígenas reconocidas en el mundo». ¿Qué dato la apoya?", "steps": ["Busco un dato sobre una persona reconocida.", "Rigoberta Menchú recibió el Premio Nobel de la Paz en 1992."], "answer": "Rigoberta Menchú, Premio Nobel de la Paz en 1992"},
        {"title": "Reconocer un límite", "problem": f"{P5} ¿Podemos decir cuántas personas indígenas hay en cada país con esta ficha?", "steps": ["Busco el dato 5.", "Dice que la ficha no entrega esas cifras."], "answer": "No, la ficha no lo dice"},
    ],
    mistakes=[
        {"wrong": "Dar una cifra de personas indígenas sin fuente.", "why": "Se recuerda un número sin revisar de dónde viene.", "fix": "Busca una fuente confiable o di que no lo sabes."},
        {"wrong": "Decir que todos los pueblos indígenas están en la misma situación.", "why": "Se generaliza.", "fix": "Recuerda que no todos viven en las mismas condiciones."},
    ],
    tiers={
        "recovery": [
            ex(f"{P5} ¿Qué premio recibió Rigoberta Menchú?", "el Premio Nobel de la Paz", "La ficha lo indica."),
            ex(f"{P5} ¿En qué año lo recibió?", "1992", "La ficha lo dice."),
            ex(f"{P5} ¿De qué país es Rigoberta Menchú?", "Guatemala", "La ficha lo indica."),
        ],
        "understand": [
            ex(f"{P5} ¿Por qué recibió ese premio?", "por defender los derechos de los pueblos indígenas", "La ficha lo explica."),
            ex(f"{P5} ¿Qué significa protagonismo?", "tener un papel importante", "Así se define."),
            ex(f"{P5} ¿Qué dato de la ficha reconoce una dificultad?", "el dato 4", "Dice que en algunos lugares aún enfrentan dificultades."),
        ],
        "apply": [
            ex(f"{P5} Afirmación: «Las lenguas indígenas tienen reconocimiento». ¿Qué dato la apoya?", "el dato 2", "Dice que varias son oficiales o reconocidas."),
            ex(f"{P5} Afirmación: «La influencia indígena está en nuestra comida». ¿Qué dato la apoya?", "el dato 3", "Habla de alimentos y palabras de origen indígena."),
            ex(f"{P5} Elige la mejor conclusión. A) Todos los pueblos indígenas viven igual de bien. B) Los pueblos indígenas tienen protagonismo hoy, aunque no todos viven en las mismas condiciones.", "B", "B respeta el límite de la evidencia."),
        ],
        "reason": [
            ex(f"{P5} Luis dice: «Hay 50 millones de personas indígenas en América». ¿Qué problema tiene?", "La ficha no entrega esa cifra y no hay fuente", "No se puede afirmar sin evidencia."),
            ex(f"{P5} Ema dice: «Si Rigoberta Menchú ganó un premio, todos los pueblos indígenas ya no tienen problemas». ¿Qué falla?", "Un caso no representa a todos y la ficha dice que aún hay dificultades", "Se generaliza desde un solo ejemplo."),
        ],
        "challenge": [
            ex(f"{P5} Marca cada parte: afirmación, evidencia o límite. a) «Los pueblos indígenas tienen protagonismo hoy». b) «Rigoberta Menchú recibió el Nobel de la Paz». c) «No todos viven en las mismas condiciones».", "a: afirmación; b: evidencia; c: límite", "Cada frase cumple una función distinta."),
            ex(f"{P5} Dos estudiantes: Rosa dice «Ya no hay desigualdades»; Tomás dice «Hay protagonismo, pero también dificultades». ¿Quién argumenta mejor?", "Tomás", "Reconoce los dos lados con evidencia."),
        ],
    },
    context=[ex("Un familiar dice que los pueblos indígenas no participan en la vida actual. ¿Qué dato de la ficha usarías para responderle?", "Rigoberta Menchú recibió el Nobel de la Paz en 1992", "Es un ejemplo concreto de participación y reconocimiento.")],
    selfcheck=[
        ex("¿Qué es el protagonismo?", "tener un papel importante", "Es el tema de la clase."),
        ex("¿Qué evidencia de la ficha muestra a una persona indígena reconocida?", "Rigoberta Menchú, Nobel de la Paz 1992", "Es el dato 1."),
        ex("¿Por qué no debemos dar cifras de personas indígenas con esta ficha?", "porque la ficha no las entrega", "No hay evidencia."),
    ],
    open_task=task(
        f"Responde por escrito: «¿Tienen protagonismo los pueblos indígenas hoy?». Escribe cuatro frases: una afirmación, dos evidencias de la ficha y un límite. {P5}",
        "Pienso que los pueblos indígenas tienen protagonismo hoy. Rigoberta Menchú recibió el Nobel de la Paz en 1992. Varias lenguas indígenas están reconocidas. Aun así, no todos viven en las mismas condiciones.",
        ["afirmación clara", "dos evidencias de la ficha", "un límite"], ["cuatro frases"], ["dar cifras sin fuente", "olvidar el límite"],
        "Pide que subraye la afirmación, encierre las evidencias y marque el límite."),
    reinforce="Cuenta a alguien de tu casa por qué los pueblos indígenas tienen protagonismo hoy.",
    extend="Escribe qué otra fuente confiable necesitarías para saber cuántas personas indígenas viven en un país.",
)

# ---------------------------------------------------------------- clase 6
P6 = ("Ficha 6: Un anacronismo es poner algo en una época a la que no pertenece. Ejemplos de anacronismo: «los incas viajaban en tren», «el presidente de los aztecas», «el país de los mayas llamado Guatemala». "
      "Los países actuales se formaron a comienzos del siglo XIX. Hoy las personas indígenas son ciudadanas y ciudadanos con los mismos derechos que cualquier persona del país donde viven, y muchas viven en ciudades y no solo en el campo. "
      "Los territorios donde vivieron las civilizaciones hoy forman parte de países: los mayas, de México, Guatemala y otros; los aztecas, de México; los incas, de Perú, Bolivia y otros. Para hablar de territorios de pueblos originarios de Chile, consulta a las comunidades.")
register(
    OA5, 6,
    materials="Lápiz y papel. La ficha está escrita en cada ejercicio.",
    use="Aprenderé a conectar pasado, territorio y ciudadanía sin mezclar épocas. Sirve para hablar de los pueblos indígenas con precisión y respeto.",
    prior=["Sé que los países actuales no existían en tiempos de las civilizaciones.", "Sé qué es una continuidad."],
    explain=[
        "Un anacronismo es poner algo en una época a la que no pertenece. Decir «los incas viajaban en tren» es un anacronismo, porque el tren no existía. También lo es decir «el presidente de los aztecas»: no tenían presidentes, sino emperadores. Para evitar anacronismos revisamos fechas y palabras.",
        "Esto vale también para los territorios. Los países actuales se formaron a comienzos del siglo XIX. Por eso decimos que los incas vivieron «en lo que hoy es Perú, Bolivia y otros países». Así conectamos el pasado con el territorio actual sin inventar países antiguos. Los mayas hoy están en México, Guatemala y otros países; los aztecas, en México.",
        "La ciudadanía es la condición de pertenecer a un país con derechos y deberes. Hoy las personas indígenas son ciudadanas y ciudadanos con los mismos derechos que cualquier persona del país donde viven, y muchas viven en ciudades. Para hablar de los territorios de los pueblos originarios de Chile, es necesario consultar a las comunidades y a sus educadores tradicionales.",
    ],
    vocab=[("anacronismo", "poner algo en una época a la que no pertenece"), ("ciudadanía", "condición de pertenecer a un país con derechos y deberes"), ("territorio", "espacio de tierra que ocupa un pueblo o un país"), ("época", "período de tiempo con rasgos propios"), ("derechos", "cosas que toda persona puede exigir para vivir con dignidad")],
    worked=[
        {"title": "Detectar un anacronismo", "problem": f"{P6} ¿Es un anacronismo decir «los aztecas tenían teléfono celular»?", "steps": ["Pienso si existía esa tecnología.", "Los celulares son muy posteriores."], "answer": "Sí, es un anacronismo"},
        {"title": "Corregir una frase", "problem": f"{P6} Corrige: «El país de los mayas se llamaba Guatemala».", "steps": ["Guatemala se formó en el siglo XIX.", "Digo en qué territorio actual vivían."], "answer": "Los mayas vivieron en lo que hoy es Guatemala, México y otros países"},
    ],
    mistakes=[
        {"wrong": "Decir «el presidente inca» para el Sapa Inca.", "why": "Se usa una palabra de hoy.", "fix": "Usa el nombre de la época: Sapa Inca."},
        {"wrong": "Decir que las personas indígenas solo viven en el campo.", "why": "Se generaliza.", "fix": "Muchas viven en ciudades y son ciudadanas con los mismos derechos."},
    ],
    tiers={
        "recovery": [
            ex(f"{P6} ¿Qué es un anacronismo?", "poner algo en una época a la que no pertenece", "La ficha lo define así."),
            ex(f"{P6} ¿Cuándo se formaron los países actuales?", "a comienzos del siglo XIX", "La ficha lo dice."),
            ex(f"{P6} ¿Hoy las personas indígenas tienen los mismos derechos que cualquier ciudadano de su país?", "Sí", "La ficha lo indica."),
        ],
        "understand": [
            ex(f"{P6} ¿Por qué «los incas viajaban en tren» es un anacronismo?", "porque el tren no existía en su época", "Pertenece a una época posterior."),
            ex(f"{P6} ¿Qué significa ciudadanía?", "pertenecer a un país con derechos y deberes", "La ficha la define."),
            ex(f"{P6} ¿Dónde viven muchas personas indígenas hoy además del campo?", "en ciudades", "La ficha lo dice."),
        ],
        "apply": [
            ex(f"{P6} Clasifica como «anacronismo» o «correcto»: «el emperador azteca vivía en Tenochtitlán».", "correcto", "Corresponde a la época azteca."),
            ex(f"{P6} Clasifica como «anacronismo» o «correcto»: «los mayas escribían con computadores».", "anacronismo", "Los computadores no existían."),
            ex(f"{P6} Clasifica como «anacronismo» o «correcto»: «los incas vivieron en lo que hoy es Perú».", "correcto", "Dice el territorio sin inventar un país antiguo."),
        ],
        "reason": [
            ex(f"{P6} Tomás dice: «Los incas eran peruanos». ¿Qué problema tiene la frase?", "Perú no existía en tiempos de los incas; es mejor decir que vivieron en lo que hoy es Perú", "Es un anacronismo de país."),
            ex(f"{P6} Ana dice: «Una persona quechua que vive en una ciudad ya no es indígena». ¿Qué dato de la ficha la corrige?", "Muchas personas indígenas viven en ciudades y mantienen sus derechos y su identidad", "La ficha indica que viven en ciudades también."),
        ],
        "challenge": [
            ex(f"{P6} Corrige la frase con un cambio mínimo: «El presidente de los aztecas vivía en Tenochtitlán».", "El emperador de los aztecas vivía en Tenochtitlán", "Cambia presidente por emperador."),
            ex(f"{P6} Elige la frase correcta. A) Los mayas formaban parte de México actual. B) Los territorios mayas hoy forman parte de México, Guatemala y otros países.", "B", "A mezcla épocas; B habla del territorio de hoy."),
        ],
    },
    context=[ex("Un afiche escolar dice: «Los aztecas, antepasados de los mexicanos de hoy, viajaban en micro». ¿Qué anacronismo tiene?", "viajaban en micro", "Los micros no existían en la época azteca.")],
    selfcheck=[
        ex("¿Qué es un anacronismo?", "poner algo en una época a la que no pertenece", "Es el error que evitamos."),
        ex("¿Qué es la ciudadanía?", "pertenecer a un país con derechos y deberes", "Incluye a las personas indígenas."),
        ex("¿Cómo se dice mejor: «el Perú de los incas» o «lo que hoy es Perú, donde vivieron los incas»?", "lo que hoy es Perú, donde vivieron los incas", "Evita mezclar épocas."),
    ],
    open_task=task(
        f"Escribe tres frases sobre los pueblos indígenas: una sobre el pasado, una sobre el territorio de hoy y una sobre ciudadanía. Revisa que ninguna tenga anacronismos. Subraya la palabra que usaste para ubicar el territorio. {P6}",
        "Pasado: los incas tenían un Sapa Inca. Territorio: vivieron en lo que hoy es Perú. Ciudadanía: hoy las personas quechuas tienen los mismos derechos que cualquier ciudadano.",
        ["tres frases", "ningún anacronismo", "territorio ubicado con cuidado"], ["tres frases"], ["usar «presidente» para un emperador", "decir «el país de los incas»"],
        "Pide que lea sus frases buscando algún anacronismo."),
    reinforce="Inventa un anacronismo gracioso y luego corrígelo.",
    extend="Escribe cómo contarías a un niño pequeño dónde vivían los mayas sin mencionar países actuales como si existieran en la época.",
)

# ================================================================ OA 06 · PARALELOS Y MERIDIANOS
# ---------------------------------------------------------------- clase 1
L1 = ("Ficha 1: Para ubicar lugares en la Tierra se usan líneas imaginarias. Los paralelos son círculos que rodean la Tierra de oeste a este, paralelos al ecuador. El ecuador es el paralelo 0° y divide la Tierra en hemisferio norte y hemisferio sur. "
      "Los meridianos son líneas que van de un polo a otro. El meridiano de Greenwich es el meridiano 0° y separa el hemisferio oriental (este) del occidental (oeste). El símbolo ° significa grados. "
      "Chile está en el hemisferio sur y en el hemisferio occidental.")
register(
    OA6, 1,
    materials="Lápiz y papel. La ficha está escrita en cada ejercicio. Un globo terráqueo o un mapa del mundo ayudan, pero no son necesarios.",
    use="Aprenderé qué son los paralelos y los meridianos y cómo dividen la Tierra en hemisferios. Sirve para ubicar cualquier lugar del mundo.",
    prior=["Sé qué es un mapa.", "Sé distinguir norte, sur, este y oeste."],
    explain=[
        "La Tierra es casi una esfera, y para ubicar lugares en ella se dibujan líneas imaginarias en los mapas y globos. Las líneas que rodean la Tierra de oeste a este se llaman paralelos. Se llaman así porque son paralelos entre sí y al ecuador. El ecuador es el paralelo 0° y divide la Tierra en hemisferio norte y hemisferio sur.",
        "Las líneas que van de un polo a otro se llaman meridianos. El meridiano de Greenwich es el meridiano 0° y separa el hemisferio oriental del occidental. El símbolo ° significa grados, que es la unidad con la que se miden las posiciones. Entre los dos, paralelos y meridianos forman una cuadrícula.",
        "Con esta cuadrícula, cualquier lugar queda entre un paralelo y un meridiano. Chile está en el hemisferio sur y en el hemisferio occidental. En un mapa, los paralelos se dibujan como líneas horizontales y los meridianos como líneas verticales, aunque en un globo los meridianos se juntan en los polos.",
    ],
    vocab=[("paralelo", "círculo imaginario que rodea la Tierra de oeste a este"), ("meridiano", "línea imaginaria que va de un polo a otro"), ("ecuador", "paralelo 0° que divide la Tierra en norte y sur"), ("hemisferio", "mitad de la Tierra"), ("grado", "unidad con la que se miden las posiciones; se escribe °")],
    worked=[
        {"title": "Distinguir paralelo y meridiano", "problem": f"{L1} ¿Cuál línea va de un polo a otro?", "steps": ["Los paralelos rodean la Tierra de oeste a este.", "Los meridianos van de un polo a otro."], "answer": "El meridiano"},
        {"title": "Ubicar un hemisferio", "problem": f"{L1} ¿En qué hemisferios está Chile?", "steps": ["Busco lo que dice la ficha sobre Chile.", "Dice que está en el hemisferio sur y en el occidental."], "answer": "En el hemisferio sur y en el occidental"},
    ],
    mistakes=[
        {"wrong": "Confundir paralelos con meridianos.", "why": "Se parecen en el mapa.", "fix": "Los paralelos son horizontales y paralelos al ecuador; los meridianos son verticales y van de polo a polo."},
        {"wrong": "Decir que el ecuador es un meridiano.", "why": "Se confunde la línea 0°.", "fix": "El ecuador es el paralelo 0°; el meridiano 0° es el de Greenwich."},
    ],
    tiers={
        "recovery": [
            ex(f"{L1} ¿Cómo se llama el paralelo 0°?", "ecuador", "La ficha lo indica."),
            ex(f"{L1} ¿Cómo se llama el meridiano 0°?", "meridiano de Greenwich", "La ficha lo indica."),
            ex(f"{L1} ¿Qué significa el símbolo °?", "grados", "La ficha lo dice."),
        ],
        "understand": [
            ex(f"{L1} ¿Qué dos hemisferios separa el ecuador?", "el norte y el sur", "Divide la Tierra en esas dos mitades."),
            ex(f"{L1} ¿Qué dos hemisferios separa el meridiano de Greenwich?", "el oriental y el occidental", "Separa el este del oeste."),
            ex(f"{L1} ¿Cómo se dibujan los meridianos en un mapa?", "como líneas verticales", "Van de arriba hacia abajo."),
        ],
        "apply": [
            ex(f"{L1} Un lugar está en el hemisferio sur y en el occidental. ¿Podría ser Chile?", "Sí", "La ficha dice que Chile está en ambos hemisferios."),
            ex(f"{L1} Un compañero dibuja líneas horizontales en un mapa. ¿Dibuja paralelos o meridianos?", "paralelos", "Los paralelos son horizontales."),
            ex(f"{L1} Si un lugar está justo sobre el ecuador, ¿está en el hemisferio norte, en el sur o en ninguno de los dos?", "en ninguno, está sobre la línea", "El ecuador es el límite entre ambos hemisferios."),
        ],
        "reason": [
            ex(f"{L1} Tomás dice: «El ecuador va de polo a polo». ¿Qué error tiene?", "El ecuador rodea la Tierra de oeste a este; los meridianos van de polo a polo", "Confunde paralelo con meridiano."),
            ex(f"{L1} Ana dice: «Greenwich es el paralelo 0°». ¿Qué error tiene?", "Greenwich es el meridiano 0°; el paralelo 0° es el ecuador", "Son líneas distintas."),
        ],
        "challenge": [
            ex(f"{L1} Clasifica cada línea como «paralelo» o «meridiano»: a) ecuador; b) Greenwich; c) una línea horizontal en el mapa.", "a: paralelo; b: meridiano; c: paralelo", "El ecuador y las horizontales son paralelos; Greenwich es meridiano."),
            ex(f"{L1} Si recorres un meridiano de punta a punta, ¿terminas en un polo, o das una vuelta completa a la Tierra por el ecuador?", "terminas en un polo", "Los meridianos van de polo a polo."),
        ],
    },
    context=[ex("En un globo terráqueo, una línea gruesa rodea la Tierra por el medio. ¿Qué línea es y qué hemisferios separa?", "el ecuador; separa el norte y el sur", "Es el paralelo 0°.")],
    selfcheck=[
        ex("¿Qué es un paralelo?", "un círculo imaginario que rodea la Tierra de oeste a este", "Es paralelo al ecuador."),
        ex("¿Qué es un meridiano?", "una línea imaginaria que va de un polo a otro", "Es la línea vertical del mapa."),
        ex("¿En qué hemisferios está Chile?", "en el sur y en el occidental", "La ficha lo indica."),
    ],
    open_task=task(
        f"Dibuja un círculo grande como si fuera la Tierra. Traza el ecuador con una línea horizontal y tres meridianos que vayan del polo norte al polo sur. Marca con color los hemisferios norte y sur. Escribe una frase que diga en qué hemisferios está Chile. {L1}",
        "Círculo con línea horizontal, tres meridianos curvos, hemisferio norte y sur coloreados y la frase «Chile está en el hemisferio sur y en el occidental».",
        ["ecuador horizontal", "tres meridianos de polo a polo", "hemisferios pintados", "frase sobre Chile"], ["dibujo", "una frase"], ["dibujar meridianos horizontales", "confundir ecuador con Greenwich"],
        "Pregunta qué línea usarías para separar el norte del sur. La respuesta esperada es el ecuador."),
    reinforce="Explica a alguien la diferencia entre paralelo y meridiano usando una naranja o un balón.",
    extend="Escribe cómo describirías con paralelos y meridianos dónde está tu escuela.",
)

# ---------------------------------------------------------------- clase 2
L2 = ("Ficha 2: Dos mapas de práctica para evaluar. MAPA A: tiene título («Isla Sol y sus vecinas»), autor, año 2020 y leyenda con los símbolos. En sus márgenes aparecen paralelos de 10° en 10° (20° N, 10° N, 0°, 10° S, 20° S) y meridianos de 10° en 10° (60° O, 50° O, 40° O, 30° O). "
      "MAPA B: no tiene título, autor ni año; sus líneas no tienen números. Ubicación de las islas en el mapa A: Isla Sol está en el cruce de 10° N y 40° O; Isla Luna está en el cruce de 0° y 50° O; Isla Nube está en el cruce de 20° S y 30° O.")
register(
    OA6, 2,
    materials="Lápiz y papel. Los mapas de práctica están descritos en cada ejercicio.",
    use="Aprenderé a leer los datos de un mapa con coordenadas y a evaluar si el mapa es confiable. Sirve para usar mapas con cuidado.",
    prior=["Sé qué son paralelos y meridianos.", "Sé distinguir hemisferios."],
    explain=[
        "Un mapa es una fuente. Antes de usarlo, preguntamos: ¿quién lo hizo?, ¿cuándo?, ¿tiene título?, ¿tiene leyenda, que explica los símbolos?, ¿tiene números en las líneas? Un mapa con título, autor, año, leyenda y números es más confiable que uno sin ellos.",
        "Los números en los márgenes indican los grados de los paralelos y los meridianos. Los paralelos se rotulan con N si están al norte del ecuador y S si están al sur. Los meridianos se rotulan con O si están al oeste del meridiano de Greenwich y E si están al este. Así se leen las posiciones: primero el paralelo y luego el meridiano.",
        "En el mapa A, la Isla Sol está en 10° N y 40° O; la Isla Luna, en 0° y 50° O; y la Isla Nube, en 20° S y 30° O. Con esos datos podemos decir en qué hemisferio está cada una. Si no sabemos leer los números, no podemos ubicar bien nada. Por eso mapas sin números no sirven para este fin.",
    ],
    vocab=[("leyenda", "explicación de los símbolos de un mapa"), ("margen", "borde de un mapa donde aparecen los números de las líneas"), ("N, S", "norte y sur: indican si un paralelo está al norte o al sur del ecuador"), ("E, O", "este y oeste: indican si un meridiano está al este o al oeste de Greenwich"), ("confiable", "que merece que le creamos porque dice quién, cuándo y cómo se hizo")],
    worked=[
        {"title": "Elegir el mapa más confiable", "problem": f"{L2} ¿Cuál mapa es más confiable, A o B?", "steps": ["A tiene título, autor, año, leyenda y números.", "B no tiene ninguno."], "answer": "El mapa A"},
        {"title": "Leer coordenadas", "problem": f"{L2} ¿En qué cruce de líneas está la Isla Luna?", "steps": ["Busco la Isla Luna en la ficha.", "Está en 0° y 50° O."], "answer": "En 0° y 50° O"},
    ],
    mistakes=[
        {"wrong": "Leer primero el meridiano y luego el paralelo.", "why": "No se sigue el orden convenido.", "fix": "Lee primero el paralelo (N o S) y luego el meridiano (E u O)."},
        {"wrong": "Usar un mapa sin números ni autor para ubicar lugares.", "why": "No se revisa su procedencia.", "fix": "Busca un mapa con título, autor, año y números."},
    ],
    tiers={
        "recovery": [
            ex(f"{L2} ¿Cuál mapa no tiene título, autor ni año?", "el mapa B", "La ficha lo indica."),
            ex(f"{L2} ¿Dónde está la Isla Sol?", "en 10° N y 40° O", "La ficha lo indica."),
            ex(f"{L2} ¿Dónde está la Isla Nube?", "en 20° S y 30° O", "La ficha lo indica."),
        ],
        "understand": [
            ex(f"{L2} ¿Qué letra indica que un paralelo está al sur del ecuador?", "S", "S significa sur."),
            ex(f"{L2} ¿Qué letra indica que un meridiano está al oeste de Greenwich?", "O", "O significa oeste."),
            ex(f"{L2} ¿Para qué sirve la leyenda?", "para explicar los símbolos del mapa", "Indica qué significa cada símbolo."),
        ],
        "apply": [
            ex(f"{L2} La Isla Sol está en 10° N. ¿En qué hemisferio está, norte o sur?", "norte", "La N indica que está al norte del ecuador."),
            ex(f"{L2} La Isla Nube está en 20° S. ¿En qué hemisferio está?", "sur", "La S indica que está al sur del ecuador."),
            arith(f"{L2} La Isla Sol está en 10° N y la Isla Nube en 20° S. ¿Cuántos grados de latitud hay entre ellas? Súmalos, porque están a lados opuestos del ecuador.", "10+20", "Cuando están en lados opuestos del ecuador, se suman.", " grados"),
        ],
        "reason": [
            ex(f"{L2} Luis dice: «El mapa B es igual de confiable que el A». ¿Qué datos del A muestran que no es así?", "El A tiene título, autor, año, leyenda y números; el B no", "Esos datos permiten comprobar el mapa."),
            ex(f"{L2} Ana dice: «Como la Isla Luna está en 0°, está en el hemisferio norte». ¿Qué error tiene?", "0° es el ecuador, que separa norte y sur; la isla está sobre la línea", "No pertenece a ningún hemisferio."),
        ],
        "challenge": [
            ex(f"{L2} ¿Qué isla está más cerca del ecuador: la Isla Sol (10° N), la Isla Luna (0°) o la Isla Nube (20° S)?", "la Isla Luna", "Está justo en el ecuador."),
            ex(f"{L2} ¿Qué isla está en el hemisferio sur: la Isla Sol o la Isla Nube?", "la Isla Nube", "Está en 20° S."),
        ],
    },
    context=[ex("Una persona te muestra un mapa sin título ni números en las líneas y te pide ubicar una ciudad por coordenadas. ¿Qué le dirías?", "Que ese mapa no sirve para ubicar con coordenadas porque no tiene números", "Sin números no se pueden leer las coordenadas.")],
    selfcheck=[
        ex("¿Qué indica la letra O después de un número de meridiano?", "que está al oeste de Greenwich", "O significa oeste."),
        ex("¿Qué se lee primero en una coordenada: el paralelo o el meridiano?", "el paralelo", "Primero se lee la latitud."),
        ex("¿Qué hace más confiable a un mapa?", "que tenga título, autor, año, leyenda y números", "Así se puede comprobar."),
    ],
    open_task=task(
        f"Dibuja en una hoja una cuadrícula con tres líneas horizontales (10° N, 0° y 10° S) y tres verticales (60° O, 50° O y 40° O). Marca con una cruz la Isla Luna (0° y 50° O) y escribe su nombre. Después escribe una frase que explique por qué el mapa A es más confiable que el B. {L2}",
        "Cuadrícula con tres horizontales y tres verticales, una cruz en 0° y 50° O y una frase sobre el título, autor y números.",
        ["cuadrícula rotulada", "isla en el cruce correcto", "frase de confiabilidad"], ["cuadrícula", "una frase"], ["rotular mal las líneas", "olvidar S o N"],
        "Pregunta cómo supo dónde poner la isla. Debe decir 0° y 50° O."),
    reinforce="Lee en voz alta las coordenadas de dos islas de la ficha.",
    extend="Escribe cinco preguntas que harías antes de usar un mapa nuevo.",
)

# ---------------------------------------------------------------- clase 3
L3 = ("Ficha 3: Las coordenadas geográficas son dos números que ubican un lugar: la latitud (distancia al ecuador, se mide con paralelos, de 0° a 90° N o S) y la longitud (distancia al meridiano de Greenwich, se mide con meridianos, de 0° a 180° E u O). "
      "Líneas importantes: Trópico de Cáncer (cerca de 23° N), Trópico de Capricornio (cerca de 23° S) y círculos polares (cerca de 66° N y 66° S). Los polos están en 90° N y 90° S. "
      "Coordenadas aproximadas: Ciudad de México, 19° N y 99° O; Cusco, 13° S y 72° O; Santiago de Chile, 33° S y 71° O.")
register(
    OA6, 3,
    materials="Lápiz y papel. Las coordenadas están escritas en cada ejercicio.",
    use="Aprenderé a leer y escribir coordenadas geográficas con latitud y longitud. Sirve para ubicar ciudades y lugares con precisión.",
    prior=["Sé qué son paralelos, meridianos y hemisferios.", "Sé leer los números de un mapa."],
    explain=[
        "Las coordenadas geográficas son dos números que ubican un lugar. La latitud indica la distancia al ecuador y se mide con los paralelos, de 0° a 90° al norte o al sur. La longitud indica la distancia al meridiano de Greenwich y se mide con los meridianos, de 0° a 180° al este o al oeste. Se escribe primero la latitud y luego la longitud.",
        "Por ejemplo, Santiago de Chile está cerca de 33° S y 71° O. Eso significa que está 33 grados al sur del ecuador y 71 grados al oeste de Greenwich. Cusco está cerca de 13° S y 72° O, y Ciudad de México, cerca de 19° N y 99° O. Los valores son aproximados.",
        "Hay paralelos especiales: el Trópico de Cáncer, cerca de 23° N, el Trópico de Capricornio, cerca de 23° S, y los círculos polares, cerca de 66° N y 66° S. Los polos están en 90° N y 90° S. Con estos datos podemos decir si un lugar está en el norte o sur, y cuán lejos está del ecuador.",
    ],
    vocab=[("latitud", "distancia de un lugar al ecuador, medida en grados"), ("longitud", "distancia de un lugar al meridiano de Greenwich, medida en grados"), ("coordenadas", "dos números que ubican un lugar: latitud y longitud"), ("trópico", "paralelo especial a unos 23° del ecuador"), ("aproximado", "casi exacto, pero no preciso")],
    worked=[
        {"title": "Leer coordenadas", "problem": f"{L3} ¿Qué significan 33° S y 71° O para Santiago?", "steps": ["33° S es la latitud: 33 grados al sur del ecuador.", "71° O es la longitud: 71 grados al oeste de Greenwich."], "answer": "Está 33 grados al sur del ecuador y 71 grados al oeste de Greenwich"},
        {"title": "Comparar latitudes", "problem": f"{L3} ¿Cuántos grados de latitud separan a Cusco (13° S) y Santiago (33° S)?", "steps": ["Los dos están al sur, así que se restan.", "33 − 13 = 20."], "answer": "20 grados"},
    ],
    mistakes=[
        {"wrong": "Escribir primero la longitud y después la latitud.", "why": "No se sigue el orden convenido.", "fix": "Escribe primero la latitud y luego la longitud."},
        {"wrong": "Olvidar N, S, E u O.", "why": "Se piensa que el número basta.", "fix": "Sin la letra no sabemos de qué lado del ecuador o de Greenwich está."},
    ],
    tiers={
        "recovery": [
            ex(f"{L3} ¿Qué mide la latitud?", "la distancia de un lugar al ecuador", "La ficha lo indica."),
            ex(f"{L3} ¿Qué mide la longitud?", "la distancia de un lugar al meridiano de Greenwich", "La ficha lo indica."),
            ex(f"{L3} ¿Cuáles son las coordenadas aproximadas de Santiago de Chile?", "33° S y 71° O", "La ficha las entrega."),
        ],
        "understand": [
            ex(f"{L3} ¿Qué se escribe primero en las coordenadas?", "la latitud", "Primero la latitud y luego la longitud."),
            ex(f"{L3} ¿Cuál es el valor máximo de latitud?", "90°", "Los polos están a 90°."),
            ex(f"{L3} Ciudad de México está en 19° N y 99° O. ¿En qué hemisferio, norte o sur, está?", "norte", "La N indica norte del ecuador."),
        ],
        "apply": [
            arith(f"{L3} Ciudad de México está en 99° O y Santiago en 71° O. Las dos están al oeste de Greenwich. ¿Cuántos grados de longitud las separan?", "99-71", "Ambas están al oeste; se resta la menor de la mayor.", " grados"),
            ex(f"{L3} ¿Cuál de las tres ciudades está más al norte: Ciudad de México, Cusco o Santiago?", "Ciudad de México", "Es la única en latitud norte."),
            ex(f"{L3} ¿Cuál de estas ciudades está en el hemisferio sur: Ciudad de México o Cusco?", "Cusco", "Está en 13° S."),
        ],
        "reason": [
            ex(f"{L3} Tomás dice: «Santiago está en 33° N». ¿Qué error tiene?", "Santiago está en 33° S, es decir, al sur del ecuador", "La letra S indica sur."),
            ex(f"{L3} Ana dice: «Santiago de Chile está exactamente en 33° S y 71° O». ¿Qué dice la ficha sobre esos valores?", "Que son aproximados", "La ficha dice que son coordenadas aproximadas."),
        ],
        "challenge": [
            ex(f"{L3} Escribe las coordenadas de un lugar a 20° al norte del ecuador y 50° al oeste de Greenwich.", "20° N y 50° O", "Se escribe primero la latitud y luego la longitud."),
            ex(f"{L3} ¿Cuántos grados de latitud separan a Ciudad de México (19° N) del ecuador?", "19 grados", "Está a 19 grados al norte del ecuador."),
        ],
    },
    context=[ex("Un navegante dice que su barco está en 33° S y 71° O. ¿A qué distancia en grados está del ecuador y de Greenwich?", "33 grados del ecuador y 71 grados de Greenwich", "Las coordenadas indican esas distancias.")],
    selfcheck=[
        ex("¿Cuáles son las dos coordenadas geográficas?", "latitud y longitud", "Ubican un lugar en la Tierra."),
        ex("¿Qué indica la letra S en 33° S?", "que está al sur del ecuador", "S significa sur."),
        ex("¿Cuál es el orden al escribir coordenadas?", "primero latitud y luego longitud", "Es el orden convenido."),
    ],
    open_task=task(
        f"Haz una tabla con las columnas «lugar», «latitud» y «longitud». Completa tres filas con Ciudad de México, Cusco y Santiago de Chile. Después subraya la ciudad que está más al sur y encierra la que está más al norte. {L3}",
        "Ciudad de México: 19° N, 99° O. Cusco: 13° S, 72° O. Santiago: 33° S, 71° O. Más al sur: Santiago. Más al norte: Ciudad de México.",
        ["tres filas completas", "letras N y S correctas", "sur y norte identificados"], ["tabla", "dos marcas"], ["olvidar las letras", "invertir latitud y longitud"],
        "Pregunta qué ciudad está más cerca del ecuador. La respuesta esperada es Cusco, a 13° del ecuador."),
    reinforce="Lee en voz alta las coordenadas de tres ciudades de la ficha.",
    extend="Averigua la latitud aproximada de tu ciudad en un mapa o atlas y escríbela con N o S.",
)

# ---------------------------------------------------------------- clase 4
L4 = ("Ficha 4: Dos formas de decir dónde está algo. LOCALIZACIÓN RELATIVA: se dice respecto de otra cosa; por ejemplo, «Santiago está al norte del río Maule» o «el colegio está cerca de la plaza». "
      "LOCALIZACIÓN ABSOLUTA: se dice con coordenadas; por ejemplo, «Santiago está cerca de 33° S y 71° O». "
      "Antes, quienes navegaban calculaban su latitud midiendo la altura del Sol o de una estrella. Hoy los satélites del sistema GPS entregan coordenadas muy precisas. "
      "Un navegante antiguo anotaba su posición con descripciones; un mapa moderno usa números.")
register(
    OA6, 4,
    materials="Lápiz y papel. La ficha está escrita en cada ejercicio.",
    use="Aprenderé a comparar la localización relativa con la absoluta y a ver cómo cambió la forma de ubicarse. Sirve para elegir la mejor manera de decir dónde está algo.",
    prior=["Sé leer coordenadas con latitud y longitud.", "Sé qué es un cambio y una continuidad."],
    explain=[
        "Hay dos formas de decir dónde está algo. La localización relativa lo describe respecto de otra cosa: «el colegio está cerca de la plaza». Es fácil de entender, pero cambia según de dónde parta quien lo dice. La localización absoluta usa coordenadas, como 33° S y 71° O, y siempre es la misma para cualquier persona.",
        "Cada forma sirve para algo distinto. Para llegar a una casa en tu barrio, basta la localización relativa. Para indicar un lugar exacto en el mundo, la absoluta es mejor, porque no depende de ningún punto de partida. En los mapas se usan ambas: nombres y relaciones, y coordenadas.",
        "Con el tiempo cambió la forma de ubicarse. Antes, quienes navegaban calculaban la latitud midiendo la altura del Sol o de una estrella. Hoy los satélites del sistema GPS entregan coordenadas muy precisas. Lo que se mantiene es la idea de usar paralelos y meridianos para ubicar un punto en la Tierra.",
    ],
    vocab=[("localización relativa", "decir dónde está algo respecto de otra cosa"), ("localización absoluta", "decir dónde está algo con coordenadas"), ("GPS", "sistema de satélites que entrega la posición de un lugar"), ("navegar", "viajar por el mar guiándose por señales o instrumentos"), ("preciso", "exacto, sin dudas")],
    worked=[
        {"title": "Clasificar una localización", "problem": f"{L4} ¿«El colegio está cerca de la plaza» es relativa o absoluta?", "steps": ["Veo si usa coordenadas.", "No: se compara con la plaza."], "answer": "Relativa"},
        {"title": "Elegir la mejor", "problem": f"{L4} Quieres indicar un lugar exacto de la Tierra para alguien que está en otro país. ¿Qué localización conviene?", "steps": ["La relativa depende del punto de partida.", "La absoluta usa coordenadas y es la misma para todos."], "answer": "La absoluta"},
    ],
    mistakes=[
        {"wrong": "Decir «cerca de la plaza» es una localización absoluta.", "why": "No se revisa si usa coordenadas.", "fix": "Si no usa coordenadas, es relativa."},
        {"wrong": "Pensar que la localización relativa es siempre un error.", "why": "Se cree que solo las coordenadas valen.", "fix": "Sirve en el barrio, aunque no sirve para un lugar exacto del mundo."},
    ],
    tiers={
        "recovery": [
            ex(f"{L4} ¿Cómo se llama la localización que usa coordenadas?", "absoluta", "La ficha lo indica."),
            ex(f"{L4} ¿Cómo se llama la localización que describe respecto de otra cosa?", "relativa", "La ficha lo indica."),
            ex(f"{L4} ¿Qué sistema de satélites entrega coordenadas precisas hoy?", "el GPS", "La ficha lo nombra."),
        ],
        "understand": [
            ex(f"{L4} ¿Por qué la localización relativa puede cambiar según quien la diga?", "porque depende de desde dónde se mire", "No tiene un punto de partida fijo."),
            ex(f"{L4} ¿Qué medían antes quienes navegaban para calcular su latitud?", "la altura del Sol o de una estrella", "La ficha lo dice."),
            ex(f"{L4} ¿Qué se mantiene desde antes hasta hoy al ubicar un punto?", "el uso de paralelos y meridianos", "La idea de coordenadas continúa."),
        ],
        "apply": [
            ex(f"{L4} Clasifica como «relativa» o «absoluta»: «Santiago está al norte del río Maule».", "relativa", "Se compara con el río Maule."),
            ex(f"{L4} Clasifica como «relativa» o «absoluta»: «Cusco está cerca de 13° S y 72° O».", "absoluta", "Se expresa con coordenadas."),
            ex(f"{L4} Clasifica como «relativa» o «absoluta»: «Mi casa queda detrás del almacén».", "relativa", "Se compara con el almacén."),
        ],
        "reason": [
            ex(f"{L4} Luis dice: «Para indicar un lugar exacto en otro continente, basta decir que queda cerca de la plaza». ¿Qué problema tiene?", "No dice de qué plaza ni desde dónde; conviene usar coordenadas", "La localización relativa depende de un punto de partida."),
            ex(f"{L4} Ema dice: «Antes se ubicaban con GPS». ¿Qué dice la ficha?", "Antes se medía la altura del Sol o una estrella; hoy se usa el GPS", "Hay un cambio entre antes y ahora."),
        ],
        "challenge": [
            ex(f"{L4} Clasifica como «cambio» o «continuidad»: hoy se usan satélites para obtener coordenadas.", "cambio", "Antes se medía el cielo."),
            ex(f"{L4} Clasifica como «cambio» o «continuidad»: hoy se sigue usando paralelos y meridianos para ubicar.", "continuidad", "La cuadrícula de coordenadas se mantiene."),
        ],
    },
    context=[ex("Un amigo extranjero te pregunta dónde queda tu escuela. Quieres que la encuentre en un mapa digital. ¿Qué localización le darías, relativa o absoluta, y por qué?", "absoluta, porque las coordenadas no dependen de un punto de partida", "Le permitirían encontrar el lugar exacto.")],
    selfcheck=[
        ex("¿Qué es la localización relativa?", "decir dónde está algo respecto de otra cosa", "Compara con otro lugar."),
        ex("¿Qué es la localización absoluta?", "decir dónde está algo con coordenadas", "Usa latitud y longitud."),
        ex("¿Qué cambió en la forma de ubicarse desde antes hasta hoy?", "antes se medía el cielo y hoy se usa el GPS", "Cambió el instrumento."),
    ],
    open_task=task(
        f"Escribe dos frases para indicar dónde está tu sala de clases: una con localización relativa (por ejemplo, respecto del patio o la biblioteca) y otra con localización absoluta usando solo estas coordenadas de práctica: 33° S y 71° O. Explica cuándo usarías cada una. {L4}",
        "Relativa: mi sala está al lado de la biblioteca. Absoluta: mi escuela está cerca de 33° S y 71° O. La relativa sirve en la escuela; la absoluta sirve para ubicarla en el mundo.",
        ["una frase relativa", "una frase absoluta con coordenadas", "una explicación de uso"], ["dos frases", "una explicación"], ["dar coordenadas sin N, S, E u O", "llamar absoluta a una frase relativa"],
        "Pregunta cuál sirve mejor si el visitante viene desde otro país."),
    reinforce="Escribe tres localizaciones relativas de lugares de tu barrio.",
    extend="Averigua qué es un satélite y cómo ayuda a ubicar lugares en la Tierra.",
)
