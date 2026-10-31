"""Cuaderno del estudiante, 7.º básico Historia, Geografía y Ciencias Sociales: OA 23 (investigación de problemáticas medioambientales)."""
from __future__ import annotations

from hi5_lib import build

OA = "HI07 OA 23"
MAT = "Lápiz y papel. Las fuentes, las tablas y los datos (de ejemplo) están escritos en cada ejercicio; no necesitas internet para resolverlos."

# ---------------------------------------------------------------- Clase 1
build(
    OA, 1, "",
    use="Aprenderé a pasar de un tema amplio (calentamiento global, energía, población) a una pregunta de investigación acotada al lugar donde vivo. Sirve para empezar cualquier investigación escolar.",
    prior=["Sé que las sociedades y el ambiente se influyen en ciclos.", "Sé distinguir escalas local, regional y global.", "Sé que una buena afirmación necesita datos."],
    explain=[
        "Una problemática medioambiental es una situación en que la acción humana y el medio entran en conflicto y causan daño o riesgo. Tres ejemplos son el calentamiento global, que es el aumento del promedio de la temperatura del planeta; los recursos energéticos, que son las fuentes de energía como el petróleo, el carbón, el sol o el viento; y la presión de la población sobre los recursos, es decir, cuánto agua, alimento y energía necesita un grupo humano que crece.",
        "Un tema como «calentamiento global» es demasiado amplio para investigarlo en una clase. Una pregunta investigable es una pregunta acotada que se puede responder con datos. Debe decir qué se estudia, dónde (escala local, como una comuna o un barrio), en qué período y con qué medida. Ejemplo: «¿Cuántos días con más de 30 °C hubo en el verano pasado en mi comuna?».",
        "Para revisar mi pregunta uso una lista: ¿está acotada en lugar y tiempo?, ¿se puede responder con datos y no solo con opiniones?, ¿no se resuelve con un simple sí o no?, ¿existen fuentes donde buscar? Si falla alguna, la reformulo. Una buena pregunta me ayuda a analizar el impacto en mi escala local y no solo repetir lo que se sabe del planeta.",
    ],
    vocab=[("problemática medioambiental", "situación en que la acción humana y el medio entran en conflicto y causan daño o riesgo"), ("calentamiento global", "aumento del promedio de la temperatura del planeta"), ("recurso energético", "fuente de energía, como petróleo, carbón, sol o viento"), ("pregunta investigable", "pregunta acotada que se puede responder con datos"), ("escala local", "el barrio, la ciudad o la comuna")],
    worked=[
        ("Del tema a la pregunta", "Tema: recursos energéticos. Convierte el tema en una pregunta investigable para la comuna de Valle Alegre.",
         ["Delimito el lugar: la comuna de Valle Alegre.", "Delimito el período y la medida: el último año.", "Pregunta: ¿cuántas casas de Valle Alegre usaron leña como fuente principal de calefacción el último invierno?"], "¿Cuántas casas de Valle Alegre usaron leña como fuente principal de calefacción el último invierno?"),
        ("Revisar una pregunta", "Pregunta: «¿El calentamiento global es malo?». ¿Es investigable?",
         ["No dice lugar ni período.", "«Malo» es una opinión, no una medida.", "Se responde con un sí o un no."], "No es investigable; hay que acotarla y medir algo"),
    ],
    mistakes=[
        ("Preguntar «¿Por qué hay contaminación en el mundo?».", "Es demasiado amplia para investigarla con datos propios.", "Acótala a un lugar, un período y una medida."),
        ("Formular una pregunta que se responde con sí o no.", "No obliga a buscar datos ni a explicar.", "Pregunta cuánto, cuántos, cómo cambió o qué factores influyen."),
    ],
    T=[
        ("En Historia: ¿qué es el calentamiento global?", "El aumento del promedio de la temperatura del planeta", "Es una problemática de escala global."),
        ("¿Qué es un recurso energético? Da un ejemplo.", "Una fuente de energía, como el petróleo o el sol", "Se usa para producir energía."),
        ("¿Qué es una pregunta investigable?", "Una pregunta acotada que se puede responder con datos", "Debe decir qué, dónde y cuándo."),
        ("¿Cuál es una pregunta investigable? A) «¿Es malo el calor?», B) «¿Cuántos días superaron los 30 °C en el verano pasado en la comuna de Puerto Claro?».", "B", "Tiene lugar, período y medida."),
        ("¿Cuál es el tema y cuál la pregunta? A) «energía solar», B) «¿Cuántas casas de mi barrio tienen paneles solares?».", "A es tema; B es pregunta", "La pregunta está acotada y mide algo."),
        ("Una pregunta empieza con «¿Qué pasa con el planeta...?». ¿Qué le falta para ser investigable a escala local?", "Un lugar, un período y una medida", "Es demasiado amplia."),
        ("=", "Una pregunta de ejemplo cuenta casas que usan paneles solares: 6 en una calle, 9 en otra y 12 en una tercera. ¿Cuántas casas son en total?", "6+9+12", "Se suman los datos de las tres calles."),
        ("=", "En una comuna de ejemplo hay 400 casas encuestadas y 65 usan leña. ¿Cuántas no usan leña?", "400-65", "Se resta el grupo que usa leña."),
        ("Reformula para que sea investigable: «¿La población crece mucho?». Escribe una versión con lugar y período, para la comuna de Cerro Azul en los últimos 10 años.", "¿Cuántas personas más viven hoy en Cerro Azul que hace 10 años?", "Incluye lugar, período y medida."),
        ("Tema: agua. ¿Cuál es la mejor pregunta local? A) «¿Qué es el agua?», B) «¿Cuántos litros de agua por persona al día gasta un hogar típico de mi barrio?», C) «¿Hay agua en todo el mundo?».", "B", "Es medible y local."),
        ("Una compañera propone la pregunta «¿Debemos cuidar el planeta?». ¿Por qué no sirve para una investigación escolar?", "Porque se responde con una opinión o un sí, y no con datos", "No obliga a medir nada."),
        ("Para la pregunta «¿Cuántos días con más de 30 °C hubo en el verano en la comuna?», ¿qué tipo de fuente sirve? A) un registro de temperaturas de la comuna, B) una opinión en un chat de vecinos, C) un afiche publicitario sin datos.", "A", "Contiene datos de temperatura."),
        ("Ordena para construir una pregunta: A) elegir un tema amplio, B) acotar lugar y período, C) agregar la medida, D) revisar con la lista de comprobación.", "A, B, C, D", "Se parte del tema y se va acotando."),
    ],
    ctx=("Tu curso quiere investigar «la sobrepoblación» y alguien propone la pregunta «¿Hay demasiada gente?». ¿Qué cambio la haría investigable? A) «¿Cuántas personas más viven hoy en mi comuna que hace 10 años y cuánta agua usa cada una?», B) «¿Es injusto?», C) «¿Por qué?».", "A", "Tiene lugar, período y medida."),
    sc=[("En Historia: ¿qué hace investigable a una pregunta?", "Que esté acotada y se pueda responder con datos", "Se basa en medidas."),
        ("¿Qué es la escala local?", "El barrio, la ciudad o la comuna", "Es la más cercana a ti."),
        ("¿Qué pregunta conviene evitar?", "La que se responde con sí o no", "No necesita datos.")],
    op=("Elige uno de estos tres temas: calentamiento global, recursos energéticos o presión de la población sobre los recursos. Escribe una pregunta investigable para tu barrio o comuna con lugar, período y medida, y revísala con las cuatro preguntas de la lista. Si falla alguna, reformúlala.",
        "Tema: recursos energéticos. Pregunta: ¿Cuántas casas de mi calle usan leña para calefacción este invierno? Revisión: tiene lugar y período, se responde con datos, no es sí o no y puedo preguntar a los vecinos.",
        ["escribe una pregunta con lugar, período y medida", "la revisa con la lista", "la reformula si falla"], ["una pregunta final y su revisión"], ["pregunta demasiado amplia", "pregunta de sí o no"], "Léele tu pregunta a una persona de tu casa y pídele que diga qué dato buscaría."),
    reinforce="Escribe tres temas ambientales que conozcas y convierte uno en pregunta acotada.",
    extend="Explica por qué una pregunta local puede aportar a entender un problema global.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 2
FUENTES2 = "Fuente A: informe de la municipalidad de Cerro Azul, año reciente, con autor y método, dice que se registraron 22 días sobre 30 °C en el verano. Fuente B: mensaje reenviado sin autor ni fecha, dice «hubo 50 días de calor extremo». Fuente C: nota de un diario regional con fecha reciente, cita el informe municipal y dice «22 días»."
build(
    OA, 2, FUENTES2,
    use="Aprenderé a elegir fuentes y datos confiables para investigar un problema ambiental. Sirve para evitar errores y noticias falsas.",
    prior=["Sé formular una pregunta investigable.", "Sé que una fuente tiene procedencia: quién, cuándo y para qué.", "Sé leer datos con unidades."],
    explain=[
        "Una fuente primaria es un documento o dato original, como un registro de temperatura, una encuesta propia o un informe de una institución que midió. Una fuente secundaria explica o resume otras fuentes, como un artículo de diario o un libro. Las dos sirven, pero la primaria es la base y la secundaria debe indicar de dónde sacó sus datos.",
        "Para decidir si una fuente es confiable reviso: ¿quién la hizo y tiene experiencia?, ¿cuándo?, ¿cómo obtuvo los datos?, ¿para qué la hizo y a quién le conviene? y ¿otra fuente independiente dice lo mismo? Los datos deben tener unidad (°C, litros, kilos), período y lugar. Un dato sin unidad o sin fecha es difícil de usar.",
        "Contrasto las fuentes: si dos fuentes independientes coinciden, la información es más sólida. Si se contradicen, busco la que explica su método. También distingo hechos, que se pueden comprobar, de opiniones, que expresan lo que alguien piensa. Una investigación fundamentada usa hechos y reconoce los límites de sus datos.",
    ],
    vocab=[("fuente primaria", "documento o dato original, como un registro o un informe que midió"), ("fuente secundaria", "texto que resume o explica otras fuentes"), ("confiable", "que se puede comprobar y tiene procedencia clara"), ("contrastar", "comparar varias fuentes para ver si coinciden"), ("unidad", "medida que acompaña un dato, como °C o litros")],
    worked=[
        ("Elegir entre dos fuentes", "Fuente 1: registro del observatorio de la universidad regional, con fecha y método. Fuente 2: cadena de mensajes sin autor. ¿Cuál usas para dar un dato de temperatura?",
         ["Reviso quién y cómo: el observatorio publica su método.", "La cadena de mensajes no se puede comprobar."], "La del observatorio"),
        ("Hecho u opinión", "«Ayer llovieron 12 milímetros» y «la lluvia de ayer fue horrible». ¿Cuál es un hecho?",
         ["El primero se puede medir.", "El segundo expresa una opinión."], "El primero"),
    ],
    mistakes=[
        ("Creer una cifra porque se repite mucho.", "Mil mensajes iguales pueden venir de una sola fuente dudosa.", "Busca de dónde nació el dato."),
        ("Usar un número sin unidad ni fecha.", "No se sabe qué mide ni a qué período corresponde.", "Anota siempre unidad, lugar y fecha."),
    ],
    T=[
        ("En Historia: ¿qué es una fuente primaria?", "Un documento o dato original, como un registro o un informe que midió", "Es la base de la información."),
        ("¿Qué es una fuente secundaria?", "Un texto que resume o explica otras fuentes", "Debe indicar de dónde sacó los datos."),
        ("¿Qué quiere decir «contrastar fuentes»?", "Compararlas para ver si coinciden", "Aumenta la solidez."),
        ("{F} ¿Cuál fuente es primaria?", "La fuente A, el informe municipal", "Es el documento original con método."),
        ("{F} ¿Cuál fuente no se puede comprobar y por qué?", "La fuente B, porque no tiene autor ni fecha", "Le falta procedencia clara."),
        ("{F} ¿Coinciden la fuente A y la C?", "Sí, ambas dicen 22 días", "Coinciden porque la nota de diario cita el informe, así que no es independiente."),
        ("=", "{F} ¿Cuántos días de diferencia hay entre el dato de la fuente B (50) y el de la fuente A (22)?", "50-22", "Se resta el dato menor al mayor."),
        ("{F} ¿Cuál dato conviene usar en una investigación? A) 50 días de la fuente B, B) 22 días de la fuente A (la nota C solo repite su dato).", "B", "Tiene autor, fecha y método; la nota C solo repite el informe, no es una fuente independiente."),
        ("¿Cuál es un hecho? A) «La laguna está horrible», B) «La laguna mide 3 kilómetros de largo».", "B", "Se puede medir."),
        ("Un dato dice «30» sin más. ¿Qué le falta? A) unidad, lugar y fecha, B) nada.", "A", "Sin ellos no se sabe qué mide."),
        ("Dos informes de universidades distintas, con método publicado, miden el mismo río en el mismo mes y obtienen 14 °C y 15 °C. ¿Qué se puede concluir? A) que son parecidos y refuerzan la confianza, B) que uno miente.", "A", "Dos fuentes independientes coinciden casi del todo."),
        ("Una publicidad dice «Nuestro producto reduce el calentamiento global» y no muestra datos. ¿Qué pregunta de procedencia se debe hacer primero?", "¿Para qué la hizo y a quién le conviene?", "Es de una empresa que busca vender."),
        ("Una compañera dice: «Si salió en tres sitios web, es cierto». ¿Qué error comete?", "Los tres sitios podrían copiar la misma fuente dudosa", "Se necesitan fuentes independientes."),
    ],
    ctx=("Para su investigación, tu curso encuentra dos datos sobre el consumo de leña en la comuna de ejemplo: el censo municipal con método y fecha (2.000 casas, 700 usan leña) y un comentario de un grupo de chat que dice «casi nadie usa leña». ¿Qué dato usas y cuántas casas no usan leña según la fuente confiable?", "El censo municipal; 1.300 casas", "700 de 2.000 usan leña, así que 1.300 no."),
    sc=[("En Historia: ¿cómo sé si una fuente es confiable?", "Reviso quién la hizo, cuándo, cómo y si otras fuentes coinciden", "Son los criterios de la clase."),
        ("¿Cuál es la diferencia entre hecho y opinión?", "El hecho se puede comprobar; la opinión expresa lo que alguien piensa", "Distinguirlas evita errores."),
        ("¿Qué debe tener todo dato?", "Unidad, lugar y fecha", "Permiten interpretar el dato.")],
    op=("Lee estas tres fuentes de ejemplo sobre el agua en la comuna de Valle Alegre. Fuente 1: informe de la empresa sanitaria regional, año reciente, con método: 18.000 litros por casa al mes. Fuente 2: afiche sin autor: «Gastamos el triple». Fuente 3: nota de radio que cita el informe de la empresa: «18.000 litros por casa al mes». Escribe cuál es primaria, cuál no es confiable y qué dato usarías, con las razones.",
        "La fuente 1 es primaria y confiable porque tiene autor, fecha y método. La fuente 2 no es confiable porque no tiene autor ni fecha. La fuente 3 es secundaria y solo repite el dato de la fuente 1. Usaría 18.000 litros por casa al mes.",
        ["clasifica las fuentes", "justifica con procedencia", "elige un dato con su unidad"], ["una clasificación y una decisión"], ["elegir por popularidad", "olvidar la unidad"], "Pide a una persona de tu casa que te pregunte por qué descartaste una fuente."),
    reinforce="Mira una noticia que te llame la atención y anota si dice quién midió y cuándo.",
    extend="Explica en tres líneas por qué dos fuentes independientes dan más confianza que una sola.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 3
build(
    OA, 3, "",
    use="Aprenderé a organizar las causas, los actores y las escalas de un problema ambiental. Sirve para entender quién contribuye, quién resulta afectado y a qué nivel.",
    prior=["Sé elegir fuentes y datos confiables.", "Sé distinguir escalas local, regional y global.", "Sé identificar actores y efectos."],
    explain=[
        "Una causa es lo que origina un problema. En el calentamiento global, una causa importante es que al quemar petróleo, carbón o gas (combustibles fósiles) se liberan gases, como el dióxido de carbono, que retienen calor en la atmósfera. A este efecto se le llama efecto invernadero. Cuantos más de estos gases hay, más se calienta el planeta en promedio. Estos combustibles son recursos energéticos no renovables.",
        "Los actores son quienes contribuyen o resultan afectados: hogares, empresas, municipalidades, el Estado y organizaciones. En la presión de la población sobre los recursos, no solo importa cuántas personas hay, sino también cuánto consume cada una. Un grupo pequeño con mucho consumo puede presionar más un recurso que un grupo grande que consume poco.",
        "Para organizar la información uso una tabla con causas, actores y escalas. Anoto qué ocurre a escala global (por ejemplo, más gases en la atmósfera) y cómo se manifiesta a escala local (por ejemplo, más días de calor, menos agua en el río o más gasto de energía en la comuna). Así veo que un problema global se vive en lo local.",
    ],
    vocab=[("causa", "lo que origina un problema"), ("combustible fósil", "petróleo, carbón o gas que se quema para producir energía"), ("efecto invernadero", "retención de calor en la atmósfera por ciertos gases"), ("actor", "persona o institución que contribuye o resulta afectada"), ("consumo", "cantidad de recursos que usa una persona o un grupo")],
    worked=[
        ("Armar una cadena de causas", "Una ciudad de ejemplo quema carbón para dar calefacción. ¿Cuál es la causa y cuál el efecto sobre el calentamiento global?",
         ["Causa: la quema de carbón libera gases como el dióxido de carbono.", "Efecto: esos gases retienen calor y aumentan la temperatura del planeta en promedio."], "Causa: quemar carbón; efecto: más calor retenido"),
        ("Comparar el consumo", "El grupo A tiene 100 personas que consumen 10 unidades cada una. El grupo B tiene 40 personas que consumen 40 cada una. ¿Cuál consume más en total?",
         ["A: 100 × 10 = 1.000.", "B: 40 × 40 = 1.600."], "El grupo B"),
    ],
    mistakes=[
        ("Culpar solo a las personas comunes.", "Empresas, Estado y organizaciones también aportan causas y soluciones.", "Anota todos los actores en la tabla."),
        ("Decir que el número de habitantes explica todo el uso de recursos.", "También importa cuánto consume cada persona.", "Considera población y consumo por persona."),
    ],
    T=[
        ("En Historia: ¿qué es el efecto invernadero?", "La retención de calor en la atmósfera por ciertos gases", "Es parte de la causa del calentamiento global."),
        ("¿Qué son los combustibles fósiles? Da un ejemplo.", "Petróleo, carbón o gas que se queman para producir energía", "Liberan gases al quemarse."),
        ("¿Qué es un actor en una problemática ambiental?", "Una persona o institución que contribuye o resulta afectada", "Incluye hogares y empresas."),
        ("Al quemar carbón se liberan gases. ¿Cuál es el efecto sobre el calor de la atmósfera? A) retienen calor, B) lo reducen.", "A", "Es el efecto invernadero."),
        ("¿Cuál es un recurso energético no renovable? A) el viento, B) el sol, C) el petróleo.", "C", "No se repone en una vida humana."),
        ("Un hogar y una fábrica queman leña en la misma comuna. Ambos son actores que contribuyen. ¿Cuál es el actor empresarial?", "La fábrica", "Es una empresa."),
        ("=", "El grupo A tiene 50 personas con consumo de 20 unidades cada una. ¿Cuál es su consumo total?", "50*20", "Se multiplica por persona."),
        ("=", "El grupo B tiene 25 personas con consumo de 60 unidades cada una. ¿Cuántas unidades más consume B que A en total (A consume 1.000)?", "25*60-1000", "B consume 1.500 y A 1.000."),
        ("Con esos datos, ¿qué grupo presiona más el recurso, A o B, aunque B tenga menos gente?", "B", "Su consumo total es mayor."),
        ("Una tabla de ejemplo dice: causa, quema de leña húmeda; actor, hogares; escala local, aumento de humo en invierno en la comuna. ¿Qué escala se muestra?", "Local", "El efecto es en la comuna."),
        ("En esa tabla, ¿quién resulta afectado por el humo? A) los hogares de la comuna, B) el planeta entero únicamente.", "A", "Es un problema que se vive localmente."),
        ("Una compañera dice: «Como hay mucha gente, todo es culpa de la gente». ¿Qué le falta considerar?", "El consumo por persona, el rol de las empresas y del Estado", "Hay varios actores y causas."),
        ("Ordena de lo global a lo local: A) más calor en una comuna, B) más gases en la atmósfera del planeta, C) más días de más de 30 °C en un barrio.", "B, A, C", "De lo más amplio a lo más específico."),
    ],
    ctx=("Para tu investigación, ordenas la información de una comuna de ejemplo: causa, uso de gas para calefacción en 300 casas; actor, hogares y empresa de gas; escala local, aumento del gasto en invierno. Un compañero agrega «escala global: más gases en la atmósfera». ¿Está correcto?", "Sí, porque quemar gas libera gases que se suman a los del planeta", "El gas es un combustible fósil."),
    sc=[("En Historia: ¿qué es una causa?", "Lo que origina un problema", "Está antes del efecto."),
        ("¿Qué incluye una tabla de organización?", "Causas, actores y escalas", "Ordena la información."),
        ("¿Por qué importa el consumo por persona?", "Porque cada persona presiona los recursos de forma distinta", "No basta contar habitantes.")],
    op=("Organiza esta información de ejemplo en una tabla de causas, actores y escalas: en la comuna de Cerro Azul, 250 casas usan leña, 3 fábricas queman petróleo y hay 12 días al año con más de 30 °C. Debe haber al menos dos causas, tres actores y una escala local y una global.",
        "Causas: quema de leña y quema de petróleo. Actores: hogares, fábricas y municipalidad. Escala local: 12 días con más de 30 °C en Cerro Azul. Escala global: los gases liberados se suman a los del planeta.",
        ["escribe al menos dos causas", "nombra al menos tres actores", "separa escala local y global"], ["una tabla breve"], ["culpar a un solo actor", "mezclar escalas"], "Pide a una persona de tu casa que lea tu tabla y diga si falta un actor."),
    reinforce="Anota tres formas de energía que se usan en tu casa y di si vienen de un combustible fósil.",
    extend="Explica por qué una comuna pequeña también contribuye al calentamiento global.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 4
TABLA4 = "Tabla de ejemplo para una comuna: Alternativa A, calefacción a leña: 200 pesos por hogar al día, 8 unidades de humo. Alternativa B, calefacción eléctrica con energía solar: 350 pesos por hogar al día, 1 unidad de humo. Alternativa C, aislar las casas y usar menos calefacción: 120 pesos por hogar al día, 3 unidades de humo, requiere obras de 14 días."
build(
    OA, 4, TABLA4,
    use="Aprenderé a comparar alternativas de solución y sus efectos con los mismos criterios. Sirve para decidir qué alternativa conviene en mi comuna.",
    prior=["Sé organizar causas, actores y escalas.", "Sé elegir fuentes confiables.", "Sé calcular totales con sumas y multiplicaciones."],
    explain=[
        "Una alternativa es una opción de solución. Para compararlas uso criterios claros: costo, efecto en el ambiente, plazo y a quién beneficia o perjudica. También reviso si la alternativa es viable en el lugar, es decir, si se puede hacer con los recursos y el tiempo que hay.",
        "En energía, por ejemplo, una alternativa renovable usa fuentes que se reponen, como el sol, el viento o el agua en movimiento. Una alternativa fósil usa petróleo, carbón o gas. Cada una tiene ventajas y límites. La solar produce de día, la eólica depende del viento, la hidráulica necesita agua y puede cambiar un río. Ninguna es perfecta, por eso se compara.",
        "Para decidir uso una tabla con los datos de cada alternativa y calculo totales para toda la comuna. Luego escribo cuál elijo, por qué y qué efecto secundario podría tener. Reviso si el costo recae más en algunos grupos y qué se podría hacer para compensarlo. Una buena decisión se apoya en datos y reconoce lo que no sabe.",
    ],
    vocab=[("alternativa", "opción de solución a un problema"), ("viable", "que se puede hacer con los recursos y el tiempo disponibles"), ("energía renovable", "energía de fuentes que se reponen, como el sol o el viento"), ("efecto secundario", "consecuencia no buscada de una acción"), ("compensar", "reducir una desventaja de una decisión para quienes la sufren")],
    worked=[
        ("Calcular totales", "Una alternativa de ejemplo cuesta 150 pesos por hogar al día y la comuna tiene 400 hogares. ¿Cuánto cuesta al día en toda la comuna?",
         ["Multiplico el costo por hogar por el número de hogares.", "150 × 400 = 60.000."], "60.000 pesos"),
        ("Comparar con dos criterios", "Alternativa M cuesta 100 pesos y contamina 6 unidades. Alternativa N cuesta 160 pesos y contamina 2 unidades. Si solo importa el ambiente, ¿cuál eliges?",
         ["Miro la contaminación: N tiene menos.", "El costo es mayor, pero el criterio es el ambiente."], "N"),
    ],
    mistakes=[
        ("Elegir la alternativa solo por su costo.", "Puede tener efectos negativos en el ambiente o en las personas.", "Compara al menos costo, ambiente y plazo."),
        ("Considerar que una alternativa renovable no tiene ningún efecto negativo.", "Todas tienen límites y efectos, como ocupar terreno o depender del clima.", "Anota ventajas y límites de cada alternativa."),
    ],
    T=[
        ("En Historia: ¿qué es una alternativa de solución?", "Una opción para resolver un problema", "Se compara con otras."),
        ("¿Qué es una energía renovable? Da un ejemplo.", "Una energía de fuentes que se reponen, como el sol", "No se agota en una vida humana."),
        ("¿Qué significa que una alternativa sea viable?", "Que se puede hacer con los recursos y el tiempo disponibles", "Es una opción realista."),
        ("{F} ¿Cuál alternativa produce menos humo?", "La alternativa B", "Tiene 1 unidad de humo."),
        ("{F} ¿Cuál alternativa cuesta menos por hogar al día?", "La alternativa C", "Cuesta 120 pesos."),
        ("{F} ¿Qué requisito tiene la alternativa C que las otras no?", "Obras de 14 días", "Es parte del plazo."),
        ("=", "{F} La comuna tiene 500 hogares. Con la alternativa A, ¿cuánto cuesta la calefacción al día en toda la comuna, en pesos?", "200*500", "Se multiplica por los hogares."),
        ("=", "{F} Con la alternativa B para 500 hogares, ¿cuántos pesos más al día cuesta que con la A?", "350*500-200*500", "Se calcula la diferencia total."),
        ("=", "{F} Con 500 hogares y la alternativa A, ¿cuántas unidades de humo se producen en total?", "8*500", "Se multiplica el humo por hogar."),
        ("{F} Si el criterio principal es el menor costo, ¿cuál eliges? Si es el menor humo, ¿cuál?", "Menor costo: C; menor humo: B", "Cada criterio lleva a una alternativa."),
        ("{F} Una vecina dice: «La B es la mejor porque contamina menos». ¿Qué otro criterio debe considerar? A) el costo por hogar, que es mayor, B) nada más.", "A", "B cuesta 350, más que A y C."),
        ("{F} Para que las familias de menores ingresos no pierdan con la alternativa B, ¿qué podría hacer la municipalidad? A) compensar parte del costo, B) prohibir la calefacción.", "A", "Compensar reduce la desventaja."),
        ("{F} Si se necesitan resultados en menos de una semana, ¿cuál alternativa no cumple?", "La alternativa C, que requiere 14 días de obras", "El plazo supera los 7 días."),
    ],
    ctx=("Tu curso debe elegir entre dos alternativas para el alumbrado de una plaza de ejemplo: lámparas solares que cuestan $900.000 en total y funcionan sin cuenta de luz, o lámparas de red que cuestan $400.000 y $50.000 de luz al mes. ¿En cuántos meses de pago de luz se iguala la diferencia de precio inicial entre ambas?", "10 meses", "La diferencia inicial es de $500.000 y 500.000 ÷ 50.000 = 10."),
    sc=[("En Historia: ¿qué criterios sirven para comparar alternativas?", "Costo, ambiente, plazo y a quién beneficia o perjudica", "Son los criterios de la clase."),
        ("¿Una energía renovable no tiene límites?", "Sí tiene límites, como depender del viento o del sol", "Ninguna alternativa es perfecta."),
        ("¿Qué significa compensar?", "Reducir una desventaja de una decisión para quienes la sufren", "Busca justicia en la decisión.")],
    op=("Usa la tabla de ejemplo de esta clase: {F} Escribe una decisión para una comuna de 500 hogares. Indica los totales de costo diario y de humo de la alternativa que eliges (haz las multiplicaciones), un efecto secundario o límite y una medida para compensar a quienes salgan perdiendo.",
        "Elijo C: costo 120 × 500 = 60.000 pesos al día; humo 3 × 500 = 1.500 unidades. Límite: requiere 14 días de obras. Compensación: apoyo a hogares de menores ingresos para pagar el aislamiento.",
        ["elige una alternativa con datos", "calcula los totales", "nombra un límite y una compensación"], ["una decisión con cálculos"], ["elegir sin calcular", "no mencionar límites"], "Pide a una persona de tu casa que revise tus multiplicaciones."),
    reinforce="Anota dos formas de gastar menos energía en tu casa.",
    extend="Explica por qué una alternativa barata hoy puede costar más en el largo plazo.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 5
build(
    OA, 5, "",
    use="Aprenderé a elaborar una propuesta fundamentada sobre un problema ambiental de mi comuna. Sirve para presentar una solución con datos, responsables y límites.",
    prior=["Sé formular una pregunta investigable.", "Sé elegir fuentes y comparar alternativas.", "Sé organizar causas, actores y escalas."],
    explain=[
        "Una propuesta fundamentada es una solución que se apoya en evidencia. Tiene cinco partes. Primero, el problema, descrito con un dato local. Segundo, la evidencia: datos de fuentes confiables. Tercero, la medida propuesta, con lo que se hará, dónde y cuándo. Cuarto, los responsables, es decir, quién hace cada parte. Quinto, los límites, o sea, qué no sabemos o qué podría fallar.",
        "La propuesta debe ser coherente: la medida debe atacar una causa o un efecto que aparece en la evidencia. Si el problema es el humo de la leña, una medida sobre la basura no sirve. También debe ser realista en costo, tiempo y personas. Y debe considerar a quienes se verían afectados, porque una medida puede ayudar a unos y perjudicar a otros.",
        "Al presentarla uso un lenguaje claro y preciso: indico cifras con unidad, nombro la fuente y evito exagerar. Uso expresiones como «los datos indican» o «es probable que», no «sin duda». Termino diciendo cómo sabré si funcionó, o sea, qué dato mediré después. Así la propuesta se puede revisar y mejorar.",
    ],
    vocab=[("propuesta fundamentada", "solución apoyada en evidencia, con responsables y límites"), ("evidencia", "dato o información de una fuente confiable que respalda una afirmación"), ("coherente", "que sus partes se corresponden entre sí"), ("indicador", "dato que se mide para saber si una medida funcionó"), ("límite", "lo que no se sabe o lo que podría fallar")],
    worked=[
        ("Revisar la coherencia", "Problema: en el invierno hay mucho humo por leña húmeda en Cerro Azul. Medida: instalar más basureros. ¿Es coherente?",
         ["El problema es el humo de la leña.", "La medida actúa sobre la basura.", "No ataca la causa."], "No es coherente"),
        ("Elegir un indicador", "Medida: dar un curso de uso de leña seca a 60 hogares. ¿Qué dato mediría para saber si funcionó?",
         ["Busco algo medible ligado al problema.", "Por ejemplo, cuántos de los 60 hogares usan leña seca después del curso."], "Cuántos hogares usan leña seca después del curso"),
    ],
    mistakes=[
        ("Proponer una medida que no se relaciona con la evidencia.", "No resuelve la causa del problema.", "Revisa que la medida responda al dato principal."),
        ("Terminar la propuesta sin decir cómo se sabrá si funcionó.", "No se puede evaluar ni mejorar.", "Agrega un indicador que se pueda medir."),
    ],
    T=[
        ("En Historia: ¿qué es una propuesta fundamentada?", "Una solución apoyada en evidencia, con responsables y límites", "No es una opinión sin datos."),
        ("¿Qué es un indicador?", "Un dato que se mide para saber si una medida funcionó", "Permite evaluar la propuesta."),
        ("Nombra las cinco partes de una propuesta fundamentada.", "Problema, evidencia, medida, responsables y límites", "Son las partes de la explicación."),
        ("¿Cuál frase es más precisa? A) «Hay muchísimo humo», B) «En el invierno pasado hubo 35 días con humo denso en la comuna, según el informe municipal».", "B", "Da cifra, período y fuente."),
        ("Un problema es el humo de leña húmeda. ¿Qué medida es coherente? A) enseñar a secar la leña y apoyar la compra de leña seca, B) limpiar más seguido las veredas.", "A", "Ataca la causa."),
        ("¿Qué expresión es más prudente? A) «los datos indican que», B) «sin duda alguna».", "A", "Reconoce que puede haber límites."),
        ("=", "Una medida llega a 60 hogares y la comuna tiene 400. ¿Cuántos hogares quedan sin cubrir?", "400-60", "Se resta lo cubierto del total."),
        ("=", "Una campaña cuesta $30.000 por hogar y se hará en 25 hogares. ¿Cuánto cuesta en total?", "30000*25", "Se multiplica el costo por hogar."),
        ("Una propuesta dice: «La municipalidad dará capacitación y los vecinos revisarán su leña». ¿Cuáles son los responsables?", "La municipalidad y los vecinos", "Son los actores nombrados."),
        ("¿Cuál es un límite razonable para esa propuesta? A) no sabemos cuántos hogares participarán, B) la propuesta es perfecta.", "A", "Reconoce una incertidumbre real."),
        ("Una compañera propone una medida que beneficia a un barrio, pero perjudica a otro que perdería su plaza. ¿Qué debe agregar la propuesta?", "Una forma de compensar o considerar al barrio perjudicado", "Una medida justa mira a todos los afectados."),
        ("El indicador de una campaña de ahorro de agua es: «litros por casa al mes». Antes eran 18.000 y después 15.000. ¿Cuántos litros se ahorraron por casa al mes?", "3.000 litros", "18.000 − 15.000 = 3.000."),
        ("Ordena una propuesta: A) medida y responsables, B) problema con un dato local, C) límites e indicador, D) evidencia de fuentes confiables.", "B, D, A, C", "Se parte del problema, se respalda con evidencia, se propone y se cierra con límites e indicador."),
    ],
    ctx=("Tu curso prepara una propuesta de ejemplo sobre el consumo de agua en el colegio: el medidor mostró 90 mil litros al mes y se quiere bajar a 72 mil. ¿Cuántos mil litros se deben ahorrar para llegar a la meta?", "18 mil litros", "90 − 72 = 18."),
    sc=[("En Historia: ¿qué partes tiene una propuesta fundamentada?", "Problema, evidencia, medida, responsables y límites", "Es la estructura de la clase."),
        ("¿Por qué agregar un indicador?", "Para saber si la medida funcionó", "Permite mejorar la propuesta."),
        ("¿Qué quiere decir que la medida sea coherente?", "Que responde a la causa o al efecto que muestra la evidencia", "Sus partes se corresponden.")],
    op=("Escribe una propuesta breve de ejemplo con estos datos: en la comuna de Valle Alegre, el informe municipal (año reciente) indica que 40 de cada 100 hogares usan leña húmeda y que esa es la causa principal del humo en invierno. Incluye: problema, evidencia, una medida, dos responsables, un límite y un indicador con una meta numérica.",
        "Problema: humo en invierno. Evidencia: 40 de cada 100 hogares usan leña húmeda (informe municipal). Medida: capacitar en secado de leña y bajar de 40 a 25 hogares. Responsables: municipalidad y juntas de vecinos. Límite: no se sabe cuántos hogares podrán comprar leña seca. Indicador: hogares que usan leña húmeda.",
        ["incluye las cinco partes", "usa los datos del informe", "propone un indicador con meta"], ["una propuesta con las cinco partes"], ["medida que no ataca la causa", "olvidar el indicador"], "Léele tu propuesta a una persona de tu casa y pregunta qué parte le falta clara."),
    reinforce="Elige un problema de tu barrio y escribe solo el problema con un dato y la medida.",
    extend="Agrega a tu propuesta una segunda escala (regional o global) y explica cómo se conecta.",
    materials=MAT,
)
