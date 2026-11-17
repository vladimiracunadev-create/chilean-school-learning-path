"""Economía y sociedad (electivo HC, 3.º y 4.º medio): OAC-04 (sistemas económicos), clases 1 a 6, y OAC-07 (políticas económicas, crecimiento y desarrollo en Chile), clases 1 a 4. Países, islas, cifras y fuentes de ejemplo, ficticios."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz, goma, papel o cuaderno y, si quieres, una calculadora simple. No se necesita computador ni internet: cada caso, tabla y texto está escrito en el enunciado. "
             "Las islas, países, regiones, programas y cifras son ficticios o «de ejemplo» y sirven para practicar el razonamiento económico; no representan a ningún país real ni son datos oficiales. "
             "Las posturas sobre sistemas económicos y políticas se presentan con sus argumentos, sin tomar partido: tu tarea es analizarlas y evaluarlas con criterios, no adivinar cuál es «la correcta». "
             "Este cuaderno no entrega asesoría financiera ni recomienda inversiones. El dinero está en pesos chilenos cuando no se indica otra cosa.")
build = make_build(MATERIALS)

O4 = "HI-ECSO-3y4-OAC-04"
O7 = "HI-ECSO-3y4-OAC-07"

# ============================================================ OAC-04, clase 1
F = ("Ficha 21 (isla de ejemplo, ficticia). En Isla Brisa viven 100 familias que, con su trabajo de la semana, pueden producir distintas combinaciones de pescado y tela: "
     "combinación A, 400 kg de pescado y 0 m de tela; B, 300 kg y 80 m; C, 200 kg y 140 m; D, 100 kg y 180 m; E, 0 kg y 200 m. La isla debe decidir cuál elegir, con qué técnica producir (redes a mano o una lancha con motor) y cómo repartir lo producido.")
build(
    O4, 1, F,
    use="Aprenderé el problema económico (qué, cómo y para quién producir) y cómo lo resuelven en teoría los tres sistemas: de mercado, centralizado y mixto.",
    prior=["Sé qué es la escasez y el costo de oportunidad.", "Conozco los agentes económicos.", "Sé leer una tabla con varias combinaciones."],
    explain=[
        "Toda sociedad enfrenta el problema económico: como los recursos son escasos, debe decidir qué bienes y servicios producir y en qué cantidad, cómo producirlos (con qué técnica, recursos y trabajo) y para quién producirlos, es decir, cómo se reparte lo producido. Estas tres preguntas se hacen en una isla, en una región o en un país entero.",
        "Un sistema económico es el conjunto de reglas, instituciones y formas de decidir con que una sociedad responde esas preguntas. En una economía de mercado, las decisiones están descentralizadas: las familias y las empresas deciden, la propiedad de los medios de producción es principalmente privada y los precios, formados por la oferta y la demanda, orientan los recursos. En una economía centralizada o planificada, el Estado decide mediante un plan y la propiedad es principalmente estatal o colectiva.",
        "Una economía mixta combina ambos: gran parte de la producción ocurre en mercados, pero el Estado cumple un papel importante, por ejemplo al proveer bienes públicos, regular, cobrar impuestos y redistribuir ingresos. En la práctica, casi todos los países son mixtos, en distintos grados. Por eso la discusión real no es «mercado o Estado», sino cuánto de cada uno y en qué áreas. Los tres sistemas son modelos teóricos, y conviene no confundirlos con casos reales.",
    ],
    vocab=[("problema económico", "decidir qué, cómo y para quién producir con recursos escasos"), ("sistema económico", "reglas y formas de decidir con que una sociedad responde al problema económico"), ("economía de mercado", "sistema con decisiones descentralizadas, propiedad privada y precios"), ("economía centralizada", "sistema donde el Estado decide mediante un plan"), ("economía mixta", "sistema que combina mercado y participación del Estado"), ("medios de producción", "recursos como tierra, fábricas y herramientas con que se produce")],
    worked=[
        ("Clasificar una pregunta", "Una región de ejemplo se pregunta: «¿Cómo se reparte la cosecha entre las familias?». ¿Cuál de las tres preguntas del problema económico es?",
         ["La pregunta trata del reparto de lo producido.", "Eso corresponde a «para quién producir»."],
         "Para quién producir"),
        ("Identificar el sistema", "En un país de ejemplo, un comité estatal fija cuántos pares de zapatos se hacen y en qué fábrica estatal. ¿Qué sistema es?",
         ["Quien decide qué, cómo y cuánto es el Estado.", "Eso es una economía centralizada."],
         "Economía centralizada"),
    ],
    mistakes=[("Creer que un sistema económico evita la escasez.", "Se confunde resolver el problema con eliminarlo.", "Todo sistema enfrenta recursos limitados y debe responder qué, cómo y para quién."),
              ("Pensar que los países reales son de mercado puro o planificados puros.", "Se toman los modelos como si fueran casos.", "En la práctica los países combinan mercado y Estado en distintos grados.")],
    T=[
        ("abc", "{F} ¿Cuál de estas preguntas de la isla corresponde a «cómo producir»?", "¿Con redes a mano o con una lancha con motor?", "¿Cuánta tela se hace?", "¿Cómo se reparte el pescado entre las familias?", "La técnica de producción responde a «cómo»."),
        ("abc", "{F} Si la isla elige la combinación C, ¿cuántos metros de tela produce?", "140", "200", "180", "La combinación C es 200 kg de pescado y 140 m de tela."),
        ("=", "{F} Al pasar de la combinación B a la D, ¿cuántos kilos de pescado se dejan de producir?", "300-100", "Se resta el pescado de D al de B."),
        ("abc", "En Economía y sociedad: ¿qué es un sistema económico?", "Las reglas y formas de decidir con que una sociedad responde qué, cómo y para quién producir", "Una lista de precios de un mercado", "El presupuesto de una familia", "Define cómo se resuelve el problema económico."),
        ("abc", "En una economía de mercado, ¿quién decide principalmente qué producir?", "Las empresas y los consumidores, orientados por los precios", "Un plan del Estado", "El tribunal de justicia", "Las decisiones están descentralizadas y los precios dan las señales."),
        ("abc", "En una economía centralizada, ¿quién decide principalmente qué producir?", "El Estado mediante un plan", "Cada familia por su cuenta", "Los precios del mercado", "Es el rasgo central de la planificación."),
        ("abc", "{F} En Isla Brisa, una asamblea estatal fija cuántos kilos y metros se producen y a quién se entregan. ¿Qué sistema aplican?", "Economía centralizada", "Economía de mercado", "Economía mixta", "El Estado decide qué, cómo y para quién."),
        ("abc", "{F} En Isla Brisa, cada familia decide qué producir y los precios se forman por oferta y demanda, sin intervención del Estado. ¿Qué sistema es?", "Economía de mercado", "Economía centralizada", "Economía mixta", "Las decisiones son descentralizadas y los precios orientan la producción."),
        ("abc", "{F} En la isla, la escuela y la seguridad las financia el Estado con impuestos, y el pescado y la tela se venden en mercados. ¿Qué sistema es?", "Economía mixta", "Economía centralizada", "Economía de mercado", "Combina mercado con participación del Estado."),
        ("{F} Si la isla pasa de la combinación C a la D, ¿cuánto gana de tela y cuánto pierde de pescado?", "Gana 40 m de tela y pierde 100 kg de pescado", "De 140 a 180 m de tela, y de 200 a 100 kg de pescado."),
        ("{F} ¿Por qué ningún sistema económico puede evitar elegir entre pescado y tela?", "Porque los recursos y el trabajo son limitados y producir más de uno exige producir menos del otro", "Todo sistema enfrenta la escasez, y cada combinación tiene un costo de oportunidad."),
        ("abc", "Un economista dice: «Casi ningún país real es de mercado puro ni centralizado puro». ¿Qué enseña eso?", "Que los sistemas son modelos y en la práctica los países son mixtos en distintos grados", "Que los modelos son inútiles", "Que todos los países son iguales", "Los modelos ayudan a pensar, mientras los casos reales combinan elementos."),
        ("abc", "«El Estado debería decidir qué se produce» es una afirmación…", "Normativa, porque expresa lo que debería hacerse", "Positiva, porque se verifica con datos", "Ni positiva ni normativa", "Expresa una preferencia sobre cómo organizar la economía."),
    ],
    ctx=("abc", "En un barrio de ejemplo, la panadería es privada y fija sus precios, la plaza la mantiene el municipio con impuestos, y los buses los opera una empresa bajo normas del Estado. ¿Qué sistema se observa en ese barrio?", "Un sistema mixto", "Un sistema centralizado", "Un sistema de mercado puro", "Hay actividad privada y también participación y regulación del Estado."),
    sc=[
        ("¿Cuáles son las tres preguntas del problema económico?", "Qué, cómo y para quién producir", "Toda sociedad debe responder esas tres preguntas básicas."),
        ("En Economía y sociedad: ¿qué es una economía mixta?", "Un sistema que combina mercado y participación del Estado", "En la práctica casi todos los países lo son, en distintos grados."),
        ("¿Por qué la discusión real no es «mercado o Estado»?", "Porque la mayoría combina ambos y se discute cuánto de cada uno", "Casi todas las economías son mixtas."),
    ],
    op=("Aplica el problema económico a un caso de ejemplo. Elige: (1) una cooperativa de pescadores que decide cuántos botes comprar, o (2) un municipio que decide cómo usar un terreno vacío: una plaza o un mercado. "
        "Escribe una frase para cada pregunta (qué, cómo y para quién), cuál es el recurso escaso, y cómo podría responderla un sistema de mercado y uno centralizado.",
        "Caso 2. Qué: plaza o mercado. Cómo: con fondos municipales o con un concesionario. Para quién: vecinos o comerciantes. Escaso: el terreno. Mercado: quien pague más lo usa. Centralizado: el Estado decide según un plan.",
        ["responde las tres preguntas con claridad", "identifica el recurso escaso", "distingue cómo respondería cada sistema"],
        ["texto con cinco partes"],
        ["confundir cómo con para quién", "olvidar el recurso escaso", "decir que un sistema es mejor sin argumento"],
        "Pregunta: «¿qué decide el mercado y qué decide el plan?». Con eso verifica la diferencia."),
    reinforce="Elige un producto que uses a diario y responde para él las tres preguntas del problema económico.",
    extend="Explica por qué los tres sistemas son modelos y qué diferencia hay entre un modelo y un país real.",
)

# ============================================================ OAC-04, clase 2
F = ("Ficha 22 (fuentes de ejemplo, ficticias). Tres islas de ejemplo: Isla Norte (economía de mercado), Isla Centro (economía mixta) e Isla Sur (economía centralizada). "
     "Indicadores de un instituto independiente de ejemplo: crecimiento anual de la producción: Norte 5%, Centro 4%, Sur 2%. Porcentaje del ingreso que recibe el 20% más rico: Norte 60%, Centro 45%, Sur 35%. Productos distintos disponibles en las tiendas: Norte 120, Centro 90, Sur 40. "
     "Fuente 1, folleto de la asociación de comerciantes de Isla Norte: «La libertad de comerciar trajo variedad y crecimiento.» Fuente 2, informe del comité de planificación de Isla Sur: «El plan aseguró una canasta básica a todas las familias.»")
build(
    O4, 2, F,
    use="Aprenderé a interrogar fuentes e indicadores para comparar sistemas económicos, sin concluir más de lo que los datos permiten.",
    prior=["Sé distinguir fuentes primarias y secundarias.", "Sé qué mide un indicador y qué no mide.", "Conozco los tres sistemas económicos."],
    explain=[
        "Para comparar sistemas económicos se usan indicadores como el crecimiento de la producción, que mide cuánto aumenta la producción de un año a otro; la desigualdad del ingreso, que muestra cómo se reparte (por ejemplo, qué parte recibe el 20% más rico); la variedad de productos disponibles; y el empleo. Cada indicador mide un aspecto, y ninguno resume por sí solo qué tan «buena» es una economía.",
        "Las fuentes también hay que interrogarlas. Un folleto de una asociación de comerciantes o un informe de un comité de planificación tienen un propósito: mostrar lo que favorece a quien los escribe. Eso no significa que mientan, sino que seleccionan datos. Conviene contrastarlos con una fuente independiente y preguntar qué datos no aparecen, por ejemplo la calidad de los productos o la libertad de las personas.",
        "Al comparar casos hay que cuidar tres errores: confundir correlación con causa (que dos cosas ocurran juntas no prueba que una cause la otra), generalizar desde pocos casos y olvidar que los valores influyen en qué indicador se considera más importante. Quien valora la libertad de elección y quien valora la igualdad pueden mirar los mismos datos y priorizar indicadores distintos.",
    ],
    vocab=[("crecimiento de la producción", "aumento de la producción de un año a otro"), ("desigualdad del ingreso", "forma en que se reparte el ingreso entre las personas"), ("fuente independiente", "fuente sin interés directo en el resultado"), ("correlación", "dos cosas que ocurren juntas"), ("causa", "factor que explica por qué ocurre algo"), ("sesgo de la fuente", "inclinación al mostrar solo lo favorable")],
    worked=[
        ("Interrogar una fuente", "Un informe de una empresa de ejemplo dice: «Nuestro servicio es el más rápido». ¿Qué preguntarías antes de usarlo?",
         ["Quién lo escribe: la propia empresa, que tiene interés en mostrarse bien.", "Qué datos usó y si hay otra fuente independiente que lo confirme."],
         "Preguntaría por su autoría, propósito y datos, y buscaría una fuente independiente"),
        ("Distinguir correlación y causa", "En una ciudad de ejemplo, los días en que se venden más helados también hay más personas en la playa. ¿Los helados causan que haya más gente?",
         ["Ambas cosas ocurren juntas.", "Es probable que el calor cause ambas, no que una cause la otra."],
         "No, solo muestra una correlación"),
    ],
    mistakes=[("Elegir un solo indicador y declarar que un sistema es mejor.", "Se olvida que cada indicador mide un aspecto.", "Compara varios indicadores y declara qué valor priorizas."),
              ("Creer que si una fuente tiene intereses, todo lo que dice es falso.", "Se confunde sesgo con mentira.", "Contrasta los datos con otra fuente y revisa qué omite.")],
    T=[
        ("abc", "{F} ¿Qué isla tiene mayor crecimiento anual de la producción?", "Isla Norte", "Isla Centro", "Isla Sur", "Norte tiene 5%, frente a 4% y 2%."),
        ("=", "{F} ¿Cuántos puntos porcentuales más del ingreso recibe el 20% más rico en Isla Norte que en Isla Sur?", "60-35", "Se restan los porcentajes de las dos islas."),
        ("abc", "{F} ¿Qué isla tiene más productos distintos disponibles?", "Isla Norte, con 120", "Isla Centro, con 90", "Isla Sur, con 40", "El mayor valor de la tabla es 120."),
        ("abc", "En Economía y sociedad: ¿qué mide la desigualdad del ingreso?", "Cómo se reparte el ingreso entre las personas", "Cuánto produce el país en total", "Cuántos productos hay en las tiendas", "Muestra la distribución, por ejemplo la parte del 20% más rico."),
        ("abc", "{F} ¿Qué fuente tiene mayor probabilidad de destacar solo lo favorable al mercado?", "La Fuente 1, escrita por la asociación de comerciantes de Isla Norte", "El instituto independiente", "La Fuente 2, escrita por el comité de planificación", "La asociación de comerciantes tiene interés directo en mostrar bien el mercado."),
        ("abc", "{F} ¿Qué fuente tiene mayor probabilidad de destacar solo lo favorable a la planificación?", "La Fuente 2, escrita por el comité de planificación de Isla Sur", "La Fuente 1", "El instituto independiente", "El comité que diseñó el plan tiene interés en mostrar su éxito."),
        ("{F} La Fuente 2 afirma que el plan aseguró una canasta básica a todas las familias. ¿Algún indicador de la tabla mide directamente si todas las familias tienen una canasta básica?", "No: la tabla mide crecimiento, desigualdad y variedad, no el acceso a una canasta básica", "La afirmación de la fuente no puede comprobarse con los indicadores de la ficha."),
        ("abc", "{F} Una estudiante afirma: «Isla Norte tiene un mejor sistema porque crece más». ¿Qué falla en esa conclusión?", "Usa un solo indicador y no considera la desigualdad ni otros valores", "Los datos no se pueden calcular", "El crecimiento solo importa en el sistema de mercado", "Un indicador no resume qué tan bueno es un sistema."),
        ("abc", "{F} Otro estudiante afirma: «Isla Sur es mejor porque reparte más parejo el ingreso». ¿Qué le faltaría considerar?", "Que también tiene el menor crecimiento y la menor variedad", "Nada, es perfecta", "Que la desigualdad no importa", "Quien prioriza la igualdad puede preferirla, pero debe reconocer los otros indicadores."),
        ("{F} Alguien dice: «Isla Centro es mixta y tiene valores intermedios, así que los sistemas mixtos siempre son intermedios en todo». ¿Qué error comete?", "Generaliza desde un solo caso", "Con tres islas de ejemplo no se puede afirmar nada general sobre todos los sistemas."),
        ("abc", "{F} ¿Qué haría más confiable una comparación entre las tres islas?", "Agregar otros indicadores y más países de ejemplo, de fuentes independientes", "Quedarse solo con la Fuente 1", "Quedarse solo con la Fuente 2", "Más datos y fuentes diversas reducen el sesgo."),
        ("abc", "Una persona valora más la libertad de elección y otra valora más la igualdad. Con los mismos datos, ¿pueden llegar a conclusiones distintas?", "Sí, porque priorizan indicadores distintos", "No, porque los datos deciden todo", "No, porque los valores no influyen en cómo se leen los datos", "Los valores influyen en qué indicador pesa más."),
        ("¿Por qué dos hechos que ocurren juntos no prueban que uno cause el otro?", "Porque un tercer factor podría explicar ambos o la coincidencia podría ser casual", "Una correlación entre dos hechos no equivale a una causa."),
    ],
    ctx=("abc", "Un diario de ejemplo publica: «Desde que se abrió la economía de la isla, el número de heladerías creció 30% y también la felicidad de las personas». ¿Qué advertencia sería más prudente?", "Que dos cosas ocurran juntas no prueba que una cause la otra", "Que las heladerías causan la felicidad", "Que el diario no puede informar", "Una correlación no basta para afirmar causa."),
    sc=[
        ("¿Por qué una fuente de una asociación interesada debe contrastarse?", "Porque selecciona datos que le favorecen", "Contrastar con una fuente independiente reduce el sesgo."),
        ("En Economía y sociedad: ¿qué es la correlación?", "Que dos cosas ocurren juntas", "No prueba que una cause la otra."),
        ("¿Por qué ningún indicador resume qué tan buena es una economía?", "Porque cada uno mide solo un aspecto", "Se necesitan varios indicadores y juicios de valor."),
    ],
    op=("Compara dos de las tres islas de la Ficha 22 (elige tú cuáles). Escribe: (1) dos indicadores en que difieren y la diferencia en números; (2) la fuente que usarías y su posible sesgo; (3) una conclusión que sí se puede sostener con los datos; "
        "(4) una conclusión que no se puede sostener y por qué; (5) qué indicador adicional pedirías.",
        "Norte y Sur. (1) Crecimiento: 5% frente a 2%, 3 puntos de diferencia; ingreso del 20% más rico: 60% frente a 35%, 25 puntos. (3) Norte creció más y tiene más variedad. (4) No se puede decir que el mercado causa el crecimiento: son solo dos casos. (5) Empleo.",
        ["calcula diferencias correctas", "identifica el sesgo de la fuente", "distingue lo sostenible de lo no sostenible", "propone un indicador adicional pertinente"],
        ["texto de cinco partes con cifras"],
        ["afirmar causas con solo dos casos", "elegir una fuente sin mencionar su sesgo", "decidir con un solo indicador"],
        "Pregunta: «¿esta conclusión podría ser falsa aunque los datos sean ciertos?». Si dice que sí, pídele explicar por qué."),
    reinforce="Con la tabla de la ficha, escribe una conclusión que se pueda sostener y otra que no, y explica la diferencia.",
    extend="Explica cómo una persona que valora la libertad y otra que valora la igualdad podrían interpretar distinto la misma tabla, sin que ninguna dé datos falsos.",
)

# ============================================================ OAC-04, clase 3
F = ("Ficha 23 (textos originales de ejemplo, que resumen posturas). Postura del mercado: «Si cada persona busca su interés y hay competencia, los precios señalan qué falta y qué sobra, y los recursos se asignan bien sin que nadie los ordene desde arriba.» "
     "Postura de la planificación: «Los recursos son de toda la sociedad. Un plan puede dirigirlos a las necesidades sociales sin que la ganancia privada decida qué se produce.» "
     "Postura de la economía mixta: «El mercado asigna bien muchos bienes, pero tiene fallas y deja necesidades sin cubrir; el Estado puede corregirlas sin reemplazar al mercado.»")
build(
    O4, 3, F,
    use="Aprenderé las ideas centrales que sustentan cada sistema económico, quiénes las asociaron a sus teorías y qué críticas reciben, comparando posturas sin tomar partido.",
    prior=["Conozco los tres sistemas y el problema económico.", "Sé qué son las fallas de mercado.", "Distingo afirmaciones positivas y normativas."],
    explain=[
        "La teoría de la economía de mercado se asocia al economista Adam Smith, que sostuvo que cuando las personas buscan su propio interés en mercados competitivos, el resultado puede beneficiar a la sociedad, como si una «mano invisible» ordenara las decisiones. Sus ideas centrales: propiedad privada, libertad para producir y comerciar, y precios que funcionan como señales. Quienes la critican señalan las fallas de mercado, como monopolios, externalidades y desigualdad.",
        "La economía centralizada se vincula con ideas del pensador Karl Marx, que criticó la propiedad privada de los medios de producción y propuso la propiedad colectiva; él no diseñó un plan económico detallado, pero sus ideas inspiraron a quienes organizaron economías planificadas. En la práctica, una economía planificada asigna recursos por un plan del Estado. Sus defensores destacan la posibilidad de dirigir los recursos a necesidades sociales. Sus críticos señalan la dificultad del planificador para reunir toda la información sobre gustos y costos, y los incentivos débiles.",
        "La economía mixta se apoya en ideas como las de John Maynard Keynes, que sostuvo que el Estado puede actuar frente a crisis y desempleo. Sus defensores dicen que combina la eficiencia del mercado con la corrección de sus fallas. Sus críticos discuten cuánta intervención es conveniente: unos temen el exceso de Estado y otros su insuficiencia. En estas descripciones hay simplificaciones: cada autor tiene matices que se estudian en detalle en otros cursos.",
    ],
    vocab=[("propiedad privada", "los medios de producción pertenecen a personas o empresas"), ("propiedad colectiva", "los medios de producción pertenecen a la sociedad o al Estado"), ("mano invisible", "idea de que el interés propio en mercados competitivos puede beneficiar a todos"), ("planificador", "persona u organismo que diseña el plan económico"), ("señal de precios", "información que entregan los precios sobre lo escaso"), ("intervención del Estado", "acción estatal en la economía")],
    worked=[
        ("Reconocer una postura", "Un texto de ejemplo afirma: «Un plan estatal evita que las ganancias privadas decidan qué se produce». ¿A qué sistema corresponde esta idea?",
         ["La idea central es que el Estado dirige con un plan.", "Corresponde a la economía centralizada."],
         "Economía centralizada"),
        ("Ubicar una crítica", "Se dice: «Un planificador no puede conocer los gustos de millones de personas». ¿A qué sistema critica y qué problema señala?",
         ["Habla de quien diseña el plan.", "Critica la economía centralizada y señala el problema de la información."],
         "Critica la economía centralizada; problema de información"),
    ],
    mistakes=[("Creer que quien explica una teoría la defiende.", "Se confunde describir con tomar partido.", "Describir una postura con sus argumentos no es adherir a ella."),
              ("Pensar que cada sistema tiene solo defensores o solo críticos.", "Se simplifica el debate.", "Cada sistema tiene argumentos a favor y en contra.")],
    T=[
        ("abc", "{F} ¿Qué postura de la ficha destaca que los precios señalan qué falta y qué sobra?", "La del mercado", "La de la planificación", "La de la economía mixta", "Los precios como señal son una idea central del mercado."),
        ("abc", "{F} ¿Qué postura propone que el Estado corrija fallas sin reemplazar al mercado?", "La de la economía mixta", "La del mercado", "La de la planificación", "Combina el mercado con la corrección estatal de sus fallas."),
        ("abc", "{F} ¿Qué postura de la ficha sostiene que los recursos son de toda la sociedad?", "La de la planificación", "La del mercado", "La de la economía mixta", "Defiende la propiedad colectiva de los recursos."),
        ("abc", "En Economía y sociedad: ¿qué economista se asocia a la teoría de la economía de mercado?", "Adam Smith", "Karl Marx", "John Maynard Keynes", "Smith planteó el interés propio y la «mano invisible»."),
        ("abc", "En Economía y sociedad: ¿qué pensador se asocia a la propuesta de propiedad colectiva de los medios de producción?", "Karl Marx", "Adam Smith", "John Maynard Keynes", "Marx criticó la propiedad privada de los medios de producción."),
        ("abc", "En Economía y sociedad: ¿qué economista defendió que el Estado puede actuar frente a crisis y desempleo?", "John Maynard Keynes", "Adam Smith", "Karl Marx", "Keynes se asocia a la acción del Estado en las crisis."),
        ("{F} ¿Qué crítica se hace a la economía centralizada respecto de la información?", "Que un planificador no logra reunir toda la información sobre gustos y costos", "La información dispersa entre millones de personas es difícil de reunir en un plan."),
        ("{F} ¿Qué crítica se hace a la economía de mercado respecto de las fallas?", "Que pueden aparecer monopolios, externalidades y desigualdad", "Las fallas de mercado son la principal crítica a ese modelo."),
        ("abc", "{F} ¿Cuál es una crítica a la economía mixta?", "Se discute cuánta intervención es conveniente: algunos temen su exceso y otros su insuficiencia", "No tiene ninguna crítica", "Que elimina el mercado por completo", "Las posturas discrepan en el grado de intervención."),
        ("{F} Explica por qué la postura del mercado y la de la planificación parten de valores distintos.", "Una valora la libertad y la decisión descentralizada; la otra, dirigir los recursos a necesidades sociales", "Cada postura prioriza un valor, como libertad o igualdad."),
        ("abc", "{F} Una persona dice: «Quien explica la postura del mercado es partidario del mercado». ¿Qué corrección harías?", "Describir una postura con sus argumentos no es adherir a ella", "Es cierto, quien explica una teoría la apoya", "No se puede explicar una postura sin cambiarla", "Explicar una postura es distinto de defenderla."),
        ("abc", "{F} ¿Qué sistema podría responder a la crítica «el mercado deja necesidades sin cubrir» manteniendo la propiedad privada?", "La economía mixta, con intervención del Estado en ciertas áreas", "Una economía de mercado sin ninguna regla", "Ninguno", "La mixta busca corregir fallas sin reemplazar al mercado."),
        ("abc", "«La planificación centralizada es injusta» es una afirmación…", "Normativa, porque expresa un juicio de valor", "Positiva, porque se verifica con datos", "Un dato histórico", "Usa «injusta», que depende de valores."),
    ],
    ctx=("abc", "En un debate escolar de ejemplo, un estudiante dice que los precios altos de una fruta avisan a los agricultores que conviene sembrar más. ¿Qué idea del mercado ilustra?", "Los precios como señales", "La propiedad colectiva", "El plan central", "El precio alto informa que el bien escasea y atrae a más productores."),
    sc=[
        ("¿Qué idea central tiene la economía de mercado?", "Propiedad privada, libertad económica y precios como señales", "Es la base de la teoría asociada a Smith."),
        ("¿Qué propone la economía centralizada sobre la propiedad?", "Que los medios de producción sean colectivos o estatales", "Es una idea vinculada al pensamiento de Marx."),
        ("¿Para qué sirve la intervención del Estado en la economía mixta?", "Para corregir fallas de mercado y atender necesidades", "Mantiene el mercado y corrige sus límites."),
    ],
    op=("Escribe un cuadro con tres columnas (mercado, centralizada, mixta) y cuatro filas: idea central, valor que prioriza, ventaja que destacan sus defensores y crítica principal. "
        "Completa con tus palabras a partir de la Ficha 23 y la explicación. Después escribe un párrafo de cuatro líneas que explique en qué se parecen y en qué se diferencian dos de los sistemas, sin decir cuál es mejor.",
        "Mercado: idea central, precios como señales; valor: libertad; ventaja: asigna sin mando central; crítica: fallas de mercado. Centralizada: plan estatal; igualdad; dirige a necesidades; crítica: información. Mixta: combina; equilibrio; corrige fallas; crítica: grado de intervención.",
        ["completa las doce celdas con precisión", "mantiene un tono neutral", "explica semejanzas y diferencias sin declarar un ganador"],
        ["cuadro de tres por cuatro y un párrafo"],
        ["presentar solo las ventajas de uno", "mezclar críticas de distintos sistemas", "declarar un sistema como el mejor"],
        "Pregunta: «¿esta crítica la haría un defensor del sistema contrario?». Si no, revísala."),
    reinforce="Escribe una frase propia que resuma cada una de las tres posturas de la ficha sin cambiar su sentido.",
    extend="Explica por qué las teorías de Smith, Marx y Keynes no pueden resumirse en una frase y qué precaución conviene tener al estudiarlas.",
)

# ============================================================ OAC-04, clase 4
F = ("Ficha 24 (flujos de ejemplo, ficticios). En un país de ejemplo, durante un año, los hogares reciben ingresos por trabajo por 100 (en millones de unidades monetarias). De ese ingreso pagan impuestos por 20, ahorran 10 y gastan el resto comprando bienes. "
     "Las empresas venden bienes y pagan sueldos. El Estado usa los impuestos para financiar educación y seguridad.")
build(
    O4, 4, F,
    use="Aprenderé cómo se relacionan hogares, empresas y Estado en cada sistema económico y qué consecuencias tiene para la eficiencia, la equidad y los incentivos.",
    prior=["Conozco los tres sistemas y sus ideas centrales.", "Sé qué es un impuesto y un ahorro.", "Sé sumar y restar cantidades."],
    explain=[
        "Los agentes económicos se conectan en un flujo circular. Los hogares ofrecen su trabajo y reciben ingresos; las empresas contratan trabajo, producen y venden bienes a los hogares; el Estado cobra impuestos y entrega servicios. El ingreso que reciben los hogares se divide en consumo, ahorro e impuestos. Lo que los hogares gastan en consumo es ingreso de las empresas.",
        "Cada sistema organiza esas relaciones de modo distinto. En un sistema de mercado, hogares y empresas se relacionan mediante precios y contratos, y el Estado tiene un papel limitado, centrado en reglas básicas. En un sistema centralizado, el Estado es dueño de gran parte de las empresas, asigna los trabajos y puede fijar cuánto se produce y a qué precio. En un sistema mixto, empresas privadas y públicas coexisten, y el Estado regula, cobra impuestos y redistribuye mediante servicios y transferencias.",
        "Las consecuencias dependen del diseño. Un sistema con muchos incentivos de mercado suele promover eficiencia e innovación, pero puede tener más desigualdad. Uno con fuerte control estatal puede garantizar ciertos mínimos, pero corre el riesgo de rigidez y menos incentivos. Un sistema mixto busca equilibrio, y también enfrenta el desafío de decidir dónde termina el Estado y dónde empieza el mercado. Esas decisiones mezclan datos y valores.",
    ],
    vocab=[("flujo circular", "circulación de ingresos y bienes entre hogares, empresas y Estado"), ("consumo", "gasto de los hogares en bienes y servicios"), ("ahorro", "parte del ingreso que no se gasta ni se paga como impuesto"), ("transferencia", "pago del Estado a personas sin que entreguen un bien a cambio"), ("eficiencia", "lograr más con los mismos recursos"), ("redistribución", "traslado de ingresos entre personas mediante impuestos y servicios")],
    worked=[
        ("Calcular el consumo", "Un hogar de ejemplo recibe $600.000, paga $60.000 de impuestos y ahorra $90.000. ¿Cuánto consume?",
         ["Resta impuestos y ahorro del ingreso: 600.000 menos 60.000 menos 90.000.", "El resultado es el gasto en consumo."],
         "$450.000"),
        ("Leer una relación", "En un país de ejemplo, el Estado es dueño de casi todas las fábricas y asigna dónde trabaja cada persona. ¿Qué sistema es y qué relación hay entre hogares y empresas?",
         ["El Estado es dueño y asigna trabajos: es una economía centralizada.", "Los hogares no eligen empleador libremente; la relación la define el plan."],
         "Centralizada; el plan define la relación"),
    ],
    mistakes=[("Pensar que el ahorro desaparece del flujo.", "Se olvida que el ahorro puede financiar inversión.", "El ahorro es parte del ingreso que no se consume y puede usarse para invertir."),
              ("Creer que el Estado solo es agente en economías centralizadas.", "Se ignora su papel en los otros sistemas.", "En todos los sistemas el Estado cumple algún papel, que varía en grado.")],
    T=[
        ("=", "{F} ¿Cuántas unidades monetarias (en millones) consumen los hogares?", "100-20-10", "Al ingreso se le restan los impuestos y el ahorro."),
        ("abc", "{F} ¿Qué parte del ingreso de los hogares es ingreso para las empresas?", "El consumo", "Los impuestos", "El ahorro", "Lo que los hogares gastan en bienes lo reciben las empresas."),
        ("abc", "{F} ¿Qué hace el Estado con los impuestos en la ficha?", "Financia educación y seguridad", "Los entrega a las empresas como sueldo", "Los destruye", "La ficha dice que se usan para educación y seguridad."),
        ("abc", "En Economía y sociedad: ¿qué es el flujo circular?", "La circulación de ingresos y bienes entre hogares, empresas y Estado", "Una ruta de transporte entre ciudades", "Un impuesto anual", "Muestra cómo se conectan los agentes."),
        ("abc", "En un sistema de mercado, ¿cómo se relacionan principalmente hogares y empresas?", "Mediante precios y contratos", "Mediante un plan del Estado", "Mediante sorteos", "El mercado coordina las decisiones con precios."),
        ("abc", "En un sistema centralizado, ¿qué suele hacer el Estado?", "Ser dueño de gran parte de las empresas y fijar el plan", "Limitarse a cobrar impuestos", "No tener ninguna función", "El Estado asume un papel central en la producción."),
        ("=", "Un hogar de ejemplo recibe $800.000, paga $80.000 de impuestos y consume $560.000. ¿Cuánto ahorra?", "800000-80000-560000", "Se restan impuestos y consumo del ingreso."),
        ("abc", "En un sistema mixto, ¿cuál es un papel típico del Estado?", "Regular, cobrar impuestos y redistribuir mediante servicios", "Decidir todo lo que se produce", "No hacer nada", "El Estado interviene en ciertas áreas sin reemplazar al mercado."),
        ("abc", "Una empresa privada de ejemplo contrata a un trabajador y le paga un sueldo. ¿Qué relación del flujo circular es?", "Los hogares ofrecen trabajo y reciben ingresos de las empresas", "Las empresas reciben impuestos", "El Estado paga el sueldo", "El hogar entrega trabajo y recibe un ingreso."),
        ("{F} Si los impuestos suben de 20 a 30 y el ahorro se mantiene en 10, ¿cuánto queda para el consumo?", "60", "Son 100 menos 30 menos 10."),
        ("abc", "{F} Con impuestos de 30 y el mismo ahorro, ¿qué ocurre con el ingreso de las empresas por ventas a los hogares?", "Disminuye, porque los hogares consumen menos", "Aumenta", "Se mantiene igual", "El consumo baja de 70 a 60 y las empresas reciben menos por ventas."),
        ("abc", "{F} Un defensor dice que los impuestos más altos financian servicios; un crítico dice que reducen el consumo. ¿Qué ocurre en esta discusión?", "Cada postura destaca una consecuencia distinta del mismo cambio", "Solo hay un argumento", "Los dos hablan de ahorro", "Los servicios y el menor consumo son efectos del mismo cambio."),
        ("¿Por qué un sistema con fuerte control estatal puede garantizar ciertos mínimos y a la vez tener menos incentivos?", "Porque el plan asegura el acceso pero el premio al esfuerzo individual es menor", "Hay un intercambio entre seguridad y estímulo."),
    ],
    ctx=("abc", "Una familia de ejemplo recibe una transferencia del Estado de $50.000 por mes para ayudar con útiles escolares. ¿Qué es una transferencia?", "Un pago del Estado a personas sin que entreguen un bien a cambio", "Un impuesto sobre las compras", "Un préstamo a una empresa", "Es una forma de redistribución por parte del Estado."),
    sc=[
        ("¿Cómo se divide el ingreso de un hogar en el flujo circular?", "En consumo, ahorro e impuestos", "Esos tres son los destinos posibles del ingreso del hogar."),
        ("En Economía y sociedad: ¿qué es la redistribución?", "El traslado de ingresos entre personas mediante impuestos y servicios", "Ayuda a corregir parte de la desigualdad del ingreso."),
        ("¿Qué riesgo tiene un sistema con muy poco incentivo individual?", "Que haya rigidez y menos innovación", "Los incentivos orientan el esfuerzo individual hacia ciertos resultados."),
    ],
    op=("Dibuja o escribe el flujo circular de este país de ejemplo: los hogares reciben 200 en ingresos por trabajo, pagan 40 de impuestos, ahorran 20 y consumen el resto. El Estado gasta 40 en servicios. "
        "Calcula el consumo, señala quién recibe cada flujo y explica cómo cambiaría el flujo en un sistema centralizado y en uno mixto.",
        "Consumo: 200 menos 40 menos 20 igual 140, que reciben las empresas. Impuestos 40, que recibe el Estado, y usa en servicios. En un sistema centralizado, el Estado sería dueño de las empresas y asignaría trabajos; en uno mixto habría empresas privadas y públicas.",
        ["calcula el consumo correctamente", "señala quién recibe cada flujo", "explica un cambio por sistema"],
        ["dibujo o esquema con tres explicaciones"],
        ["olvidar el ahorro", "confundir quién recibe los impuestos", "no distinguir centralizado de mixto"],
        "Pregunta: «¿hacia dónde va cada parte del ingreso?». Pide que dibuje una flecha por cada una."),
    reinforce="Con tu mesada o ingreso de ejemplo, calcula cuánto consumirías, ahorrarías y pagarías en impuestos si fueras un hogar de la ficha.",
    extend="Explica una ventaja y un riesgo de que el Estado sea dueño de empresas, sin decir si debe serlo.",
)

# ============================================================ OAC-04, clase 5
F = ("Ficha 25 (evaluación de ejemplo, ficticia). Un grupo de ejemplo evalúa los tres sistemas para organizar la producción y el reparto de alimentos de una región. Puntajes de 1 a 5 (más es mejor), asignados por el grupo: "
     "Mercado: eficiencia 5, equidad 2, libertad 5, estabilidad 2. Centralizado: eficiencia 2, equidad 4, libertad 1, estabilidad 4. Mixto: eficiencia 4, equidad 4, libertad 3, estabilidad 4. "
     "Estabilidad significa menor riesgo de crisis bruscas en precios y abastecimiento.")
build(
    O4, 5, F,
    use="Aprenderé a evaluar alternativas de sistema económico con criterios y ponderaciones, y a ver cómo cambia la conclusión cuando cambian los valores que se priorizan.",
    prior=["Conozco las ideas y críticas de cada sistema.", "Sé que los valores influyen en las decisiones.", "Sé sumar y multiplicar."],
    explain=[
        "Evaluar alternativas es compararlas con criterios explícitos. Para hacerlo de forma ordenada se puede usar una matriz de decisión: una tabla con las alternativas en filas, los criterios en columnas y un puntaje en cada celda. Los puntajes los asigna quien evalúa, a partir de evidencia o de juicios que se explican, de modo que son revisables.",
        "No todos los criterios pesan igual para todas las personas. La ponderación consiste en dar más peso a un criterio, por ejemplo contando doble los puntos de equidad. Al sumar puntajes ponderados se obtiene un total por alternativa. Si se cambia la ponderación, puede cambiar la alternativa ganadora, lo que muestra que la conclusión depende de los valores que se priorizan.",
        "Una buena evaluación declara los criterios y sus pesos, explica de dónde salen los puntajes, indica qué datos faltan y presenta la mejor objeción a la alternativa elegida. También reconoce que un puntaje de ejemplo no es una medición. El método ayuda a pensar con orden, pero no reemplaza la discusión sobre qué valores deberían guiar la decisión.",
    ],
    vocab=[("matriz de decisión", "tabla que compara alternativas según criterios"), ("ponderación", "peso que se da a cada criterio"), ("puntaje ponderado", "puntaje multiplicado por el peso del criterio"), ("criterio", "característica con que se juzga una alternativa"), ("estabilidad", "menor riesgo de crisis bruscas"), ("objeción", "argumento en contra de una elección")],
    worked=[
        ("Sumar puntajes", "Una alternativa de ejemplo obtiene eficiencia 3, equidad 5 y libertad 2. Sumados sin ponderar, ¿qué total tiene?",
         ["Suma los tres puntajes: 3 más 5 más 2.", "El total es 10."],
         "10"),
        ("Ponderar un criterio", "La misma alternativa, pero la equidad cuenta doble. ¿Qué total tiene?",
         ["Equidad doble: 5 por 2 es 10.", "Suma: 3 más 10 más 2."],
         "15"),
    ],
    mistakes=[("Creer que un puntaje es una medición objetiva.", "Se olvida que lo asignan personas.", "Declara de dónde sale cada puntaje y revísalo."),
              ("Pensar que ponderar es manipular el resultado.", "Se ignora que los pesos expresan valores.", "Los pesos deben declararse y justificarse, no esconderse.")],
    T=[
        ("=", "{F} Sin ponderar, ¿cuál es el total del sistema de mercado?", "5+2+5+2", "Se suman los cuatro puntajes."),
        ("=", "{F} Sin ponderar, ¿cuál es el total del sistema centralizado?", "2+4+1+4", "Se suman los cuatro puntajes."),
        ("=", "{F} Sin ponderar, ¿cuál es el total del sistema mixto?", "4+4+3+4", "Se suman los cuatro puntajes."),
        ("abc", "{F} Sin ponderar, ¿qué sistema obtiene el mayor total?", "El mixto", "El de mercado", "El centralizado", "Mixto suma 15, mercado 14 y centralizado 11."),
        ("abc", "En Economía y sociedad: ¿qué es una matriz de decisión?", "Una tabla que compara alternativas según criterios", "Una ley que obliga a elegir", "Un impuesto", "Ordena la comparación con criterios explícitos."),
        ("=", "{F} Si la equidad cuenta doble, ¿cuál es el total del mercado? (eficiencia más equidad por 2 más libertad más estabilidad)", "5+2*2+5+2", "Se duplica el puntaje de equidad antes de sumar."),
        ("=", "{F} Si la equidad cuenta doble, ¿cuál es el total del centralizado?", "2+4*2+1+4", "Se duplica la equidad y se suma el resto."),
        ("=", "{F} Si la equidad cuenta doble, ¿cuál es el total del mixto?", "4+4*2+3+4", "Se duplica la equidad y se suma el resto."),
        ("abc", "{F} Si la libertad cuenta doble, ¿qué sistema obtiene el mayor total?", "El de mercado, con 19", "El mixto, con 18", "El centralizado, con 12", "Mercado: 5+2+10+2=19; mixto: 4+4+6+4=18; centralizado: 2+4+2+4=12."),
        ("{F} Con la equidad doble, ¿qué sistema queda segundo?", "El de mercado", "Mixto 19, mercado 16 y centralizado 15."),
        ("abc", "{F} Una persona dice: «El sistema ganador no cambia nunca, porque los números son exactos». ¿Qué corrección harías?", "Los puntajes son juicios y al cambiar los pesos puede cambiar el ganador", "Los números de ejemplo no se pueden cambiar", "El ganador siempre es el sistema con más eficiencia", "Con libertad doble gana el mercado."),
        ("abc", "{F} ¿Qué valor priorizan quienes cuentan doble la equidad?", "La igualdad en el reparto", "La libertad de comerciar", "La velocidad de producción", "La equidad se refiere a un reparto más justo."),
        ("¿Por qué conviene declarar los pesos y no esconderlos?", "Porque los pesos expresan valores y otros deben poder revisarlos y discutirlos", "La transparencia permite discutir los valores de la evaluación."),
    ],
    ctx=("abc", "Un municipio de ejemplo compara tres formas de administrar el aseo del barrio con criterios de costo, calidad y participación vecinal, y da peso doble a la participación. Una alternativa saca costo 3, calidad 4 y participación 5. ¿Qué total ponderado tiene?", "17", "12", "15", "Son 3 más 4 más 5 por 2, o sea 17."),
    sc=[
        ("¿Qué es la ponderación?", "El peso que se da a cada criterio", "Refleja los valores de quien evalúa."),
        ("¿Por qué puede cambiar el sistema ganador al cambiar los pesos?", "Porque se prioriza otro valor", "El resultado depende de lo que se considera más importante."),
        ("¿Qué debe declarar una buena evaluación?", "Criterios, pesos, fuente de los puntajes, datos faltantes y objeciones", "Así otras personas pueden revisar y discutir la evaluación."),
    ],
    op=("Haz tu propia matriz de decisión. Elige una decisión de ejemplo: (1) cómo organizar el uso de una cancha del barrio entre tres alternativas (por orden de llegada, por reserva con pago, por turnos asignados por el municipio) o (2) cómo organizar la entrega de útiles escolares. "
        "Define cuatro criterios, da puntajes de 1 a 5 y explica cada uno en una frase, aplica un peso doble al criterio que tú priorizas, calcula los totales, declara el valor que priorizaste y escribe la mejor objeción a tu elección.",
        "Decisión 1. Criterios: costo, equidad, facilidad, uso. Peso doble a equidad. Los turnos del municipio obtienen más equidad; por pago, más facilidad. Calculo los totales. Valor: igualdad de acceso. Objeción: requiere más trabajo municipal.",
        ["define cuatro criterios y los explica", "calcula correctamente los totales ponderados", "declara el valor priorizado", "presenta una objeción sólida"],
        ["matriz con puntajes y totales, más tres frases"],
        ["no explicar los puntajes", "no ponderar o no decir por qué", "no dar objeción"],
        "Pregunta: «¿qué cambiaría si dieras peso doble a otro criterio?». Pide que lo pruebe."),
    reinforce="Rehace la matriz de la Ficha 25 dando peso doble a la estabilidad y calcula los tres totales.",
    extend="Compara por escrito cómo evaluaría un economista que valora la eficiencia y otro que valora la equidad la misma matriz, sin decidir quién tiene razón.",
)

# ============================================================ OAC-04, clase 6
F = ("Ficha 26 (países de ejemplo, ficticios). País Norte (mercado con poca intervención): crecimiento anual 4%, desempleo 6%, el 20% más rico recibe 55% del ingreso, 70% de los jóvenes termina la educación secundaria. "
     "País Centro (economía mixta): crecimiento 3%, desempleo 5%, 20% más rico 42%, secundaria completa 85%. País Sur (planificación centralizada): crecimiento 1%, desempleo oficial 3%, 20% más rico 30%, secundaria completa 80%. "
     "Nota histórica: en el siglo XX hubo países que aplicaron planificación centralizada durante décadas, y hoy casi todos los países combinan mercado y Estado en distintos grados.")
build(
    O4, 6, F,
    use="Aprenderé a comunicar una conclusión situada sobre sistemas económicos: una afirmación sostenida con evidencia, con sus límites y con otra mirada posible.",
    prior=["Conozco los tres sistemas, sus teorías y críticas.", "Sé comparar indicadores y evaluar fuentes.", "Sé distinguir lo positivo de lo normativo."],
    explain=[
        "Una conclusión situada es una afirmación que dice dónde, cuándo y en qué condiciones es válida. En economía se arma con cuatro partes: una afirmación clara, la evidencia que la sostiene, el límite de esa evidencia (qué no muestra, cuántos casos hay, qué se supone) y una mirada alternativa que alguien con otros valores o datos podría defender. Así se evita generalizar, y se invita a discutir con razones.",
        "Al comunicarla conviene usar expresiones que reflejen el grado de certeza: «los datos de ejemplo muestran que…», «en estos tres casos…», «no se puede concluir que…». También hay que separar lo que los datos permiten afirmar (positivo) de lo que se recomienda o valora (normativo). Una buena conclusión no oculta lo que no calza, como un indicador que contradice la tesis.",
        "En esta clase se trabaja con tres países de ejemplo. Los datos son ficticios, de modo que no se pueden usar para saber cómo funciona un sistema real. Lo que se practica es el método: leer una tabla, decir qué se sostiene y qué no, y presentar la conclusión sin ocultar sus límites ni descalificar otras posturas. La nota histórica es un recordatorio de que los modelos tuvieron aplicaciones reales, con resultados que se estudian en historia.",
    ],
    vocab=[("conclusión situada", "afirmación con su lugar, tiempo y condiciones de validez"), ("evidencia", "datos o hechos que respaldan una afirmación"), ("límite", "aquello que la evidencia no permite afirmar"), ("mirada alternativa", "interpretación distinta, con otros valores o datos"), ("grado de certeza", "qué tan segura es una afirmación"), ("tesis", "afirmación central que se defiende")],
    worked=[
        ("Escribir una afirmación con evidencia", "Con la tabla de un instituto de ejemplo: ciudad X, desempleo 4%; ciudad Y, desempleo 8%. Escribe una afirmación prudente.",
         ["Usa expresiones de certeza limitada: «en estas dos ciudades de ejemplo».", "Afirma lo que muestran los datos: X tiene menor desempleo."],
         "En estas dos ciudades de ejemplo, X tiene menor desempleo que Y"),
        ("Detectar una generalización", "«El sistema mixto siempre es mejor que los otros dos.» ¿Qué le falta a esta frase?",
         ["Dice «siempre» sin evidencia suficiente.", "No indica criterios, casos ni límites."],
         "Le faltan evidencia, criterios y límites"),
    ],
    mistakes=[("Escribir una conclusión sin ningún límite.", "Se confunde fuerza con certeza.", "Declara qué no muestra la evidencia."),
              ("Ocultar el indicador que contradice la tesis.", "Se busca que la conclusión parezca perfecta.", "Incluye lo que no calza y explícalo.")],
    T=[
        ("abc", "{F} ¿Qué país tiene el menor porcentaje de jóvenes con secundaria completa?", "País Norte, con 70%", "País Centro, con 85%", "País Sur, con 80%", "El valor más bajo de la tabla es 70%."),
        ("=", "{F} ¿Cuántos puntos porcentuales más de jóvenes termina la secundaria en País Centro que en País Norte?", "85-70", "Se restan los porcentajes de los dos países."),
        ("abc", "{F} ¿Qué país tiene el menor crecimiento anual?", "País Sur, con 1%", "País Centro, con 3%", "País Norte, con 4%", "El menor valor de crecimiento es 1%."),
        ("abc", "En Economía y sociedad: ¿qué es una conclusión situada?", "Una afirmación que indica dónde, cuándo y en qué condiciones es válida", "Una frase sin datos", "Una opinión universal", "Se acompaña de su evidencia y sus límites."),
        ("abc", "{F} ¿Cuál de estas afirmaciones está sostenida por la tabla?", "En estos tres países de ejemplo, País Norte crece más y tiene mayor parte del ingreso en manos del 20% más rico", "El mercado siempre produce menos desigualdad", "La planificación siempre mejora la educación", "La primera usa solo datos de la tabla y declara el alcance."),
        ("abc", "{F} ¿Cuál de estas afirmaciones generaliza más de lo que permiten los datos?", "Los sistemas mixtos siempre tienen mejor educación que los otros", "País Centro tiene mayor porcentaje de secundaria completa que País Norte", "País Sur tiene menor crecimiento que País Norte", "«Siempre» se extiende más allá de tres países de ejemplo."),
        ("abc", "{F} ¿Cuál es una afirmación prudente sobre el desempleo?", "En estos tres países de ejemplo, País Sur tiene el menor desempleo oficial (3%) y País Norte el mayor (6%)", "La planificación siempre produce menos desempleo que el mercado", "País Centro tiene el desempleo más bajo de todos los países", "Usa los datos con el alcance de «estos tres países» y nombra el desempleo como oficial."),
        ("{F} ¿Qué indicador de la tabla podría contradecir una tesis que dijera «el mercado es mejor en todo»?", "El porcentaje de jóvenes con secundaria completa, donde País Norte tiene el menor valor", "País Norte tiene el menor porcentaje de secundaria completa."),
        ("abc", "{F} ¿Qué límite señalarías del desempleo de País Sur?", "Es una cifra oficial y no se sabe si mide igual que en los otros países", "Es el valor más alto", "No existe", "Una cifra oficial puede construirse con criterios distintos."),
        ("{F} Un compañero afirma que País Sur es el mejor porque tiene menos desigualdad. ¿Qué indicador incluiría una mirada alternativa?", "El crecimiento, donde País Sur tiene el menor valor", "Quien prioriza el crecimiento destacaría que País Sur crece menos."),
        ("abc", "«En el siglo XX hubo países que aplicaron planificación centralizada durante décadas» es una afirmación…", "Positiva, porque es un hecho histórico verificable", "Normativa, porque expresa un valor", "Falsa", "Describe un hecho que se puede contrastar con fuentes."),
        ("abc", "{F} ¿Qué dato de ejemplo ayudaría a hacer más fuerte una conclusión sobre el efecto del sistema en la educación?", "Los gastos en educación por estudiante y los años de cada sistema", "La opinión de los habitantes sobre su país", "El año de fundación de cada país", "Datos del gasto y el tiempo permiten acercarse a una explicación."),
        ("¿Por qué conviene usar expresiones como «en estos tres casos»?", "Porque indican el alcance y evitan generalizar", "Muestran el grado de certeza de la afirmación."),
    ],
    ctx=("abc", "Una estudiante prepara un afiche sobre sistemas económicos con la frase: «Con datos de ejemplo de tres países, no se puede concluir que un sistema siempre sea mejor». ¿Qué hace bien esa frase?", "Declara el alcance de la evidencia y evita generalizar", "Oculta los datos", "Defiende un sistema", "Indica el límite de la evidencia."),
    sc=[
        ("¿Cuáles son las cuatro partes de una conclusión situada?", "Afirmación, evidencia, límite y mirada alternativa", "Permite comunicar con rigor y apertura."),
        ("¿Por qué no se debe ocultar un indicador que contradice la tesis?", "Porque la conclusión sería parcial y engañosa", "Incluirlo muestra honestidad intelectual y evita engañar al lector."),
        ("En Economía y sociedad: ¿qué es una tesis?", "La afirmación central que se defiende", "Se apoya con evidencia y se presenta con sus límites."),
    ],
    op=("Escribe una conclusión situada de cuatro a seis líneas con los datos de la Ficha 26. Elige uno de estos propósitos: (a) comparar los tres países en igualdad del ingreso y educación, o (b) comparar el crecimiento con la desigualdad. "
        "Debe tener: afirmación, evidencia con cifras, un límite, una mirada alternativa y una frase que no recomiende un sistema para todos los casos.",
        "(b) En estos tres países de ejemplo, el que más crece (Norte, 4%) es también donde el 20% más rico recibe más ingreso (55%); el que menos crece (Sur, 1%) tiene la menor parte (30%). Límite: solo tres países y datos de ejemplo. Alternativa: quien prioriza la igualdad destacaría a Sur. No concluyo que un sistema sea mejor en todos los casos.",
        ["afirma con cifras de la tabla", "declara un límite", "presenta una mirada alternativa", "evita recomendar un sistema universal"],
        ["párrafo de cuatro a seis líneas"],
        ["usar cifras que no están", "no incluir ningún límite", "terminar con un «siempre»"],
        "Pregunta: «¿qué parte de tu conclusión podría discutir alguien con otros valores?». Pídele que la marque."),
    reinforce="Convierte la afirmación «el sistema mixto es el mejor» en una conclusión situada con evidencia, límite y mirada alternativa.",
    extend="Elige otro indicador que no esté en la tabla y explica cómo cambiaría la conclusión si se agregara.",
)

# ============================================================ OAC-07, clase 1
F = ("Ficha 27 (países de ejemplo, ficticios). País Verde: producción total (PIB) de 400 (miles de millones de unidades monetarias, u.m.) el año 1 y 416 el año 2; población el año 2: 8 millones de habitantes. "
     "País Azul: PIB de 300 el año 2 y población de 3 millones. En Verde los precios subieron 3% entre el año 1 y el año 2.")
build(
    O7, 1, F,
    use="Aprenderé qué son el PIB, el crecimiento y el desarrollo, cómo se calculan el crecimiento y el PIB per cápita, y por qué crecer no es lo mismo que desarrollarse.",
    prior=["Sé calcular un cambio porcentual.", "Sé qué es la inflación.", "Conozco los agentes económicos y los sistemas económicos."],
    explain=[
        "El Producto Interno Bruto (PIB) es el valor de los bienes y servicios finales producidos en un país durante un período, por ejemplo un año. El crecimiento económico es el aumento del PIB de un período a otro, y se expresa como cambio porcentual. Para saber si el país realmente produce más y no solo con precios más altos, se descuenta la inflación: así se habla de crecimiento real, que de forma aproximada es el crecimiento nominal menos la inflación.",
        "El PIB per cápita es el PIB dividido por la cantidad de habitantes. Es un promedio que permite comparar países de tamaños distintos, pero no muestra cómo se reparte entre las personas. Un país puede tener un PIB grande y un PIB per cápita menor que otro más pequeño. Tampoco mide el trabajo doméstico ni el daño ambiental.",
        "El desarrollo es un concepto más amplio que el crecimiento: incluye la calidad de vida, la salud, la educación, la equidad y la sostenibilidad. Por eso existen indicadores como el Índice de Desarrollo Humano, elaborado por el Programa de las Naciones Unidas para el Desarrollo, que combina ingreso, salud y educación. Las políticas económicas de Chile se discuten usando estos conceptos, y la clase usa países de ejemplo, no cifras reales.",
    ],
    vocab=[("PIB", "valor de los bienes y servicios finales producidos en un país en un período"), ("crecimiento económico", "aumento del PIB de un período a otro"), ("PIB per cápita", "PIB dividido por el número de habitantes"), ("crecimiento real", "crecimiento descontada la inflación"), ("desarrollo", "mejora de la calidad de vida: salud, educación, equidad y sostenibilidad"), ("IDH", "Índice de Desarrollo Humano, que combina ingreso, salud y educación")],
    worked=[
        ("Calcular el crecimiento", "El PIB de un país de ejemplo pasó de 500 a 520. ¿Cuánto creció en porcentaje?",
         ["Crecimiento = (520 menos 500) dividido por 500, por 100.", "20 dividido por 500 da 0,04, o sea 4%."],
         "4%"),
        ("Calcular el PIB per cápita", "Un país de ejemplo tiene PIB de 900 (miles de millones de u.m.) y 6 millones de habitantes. ¿Cuál es el PIB per cápita?",
         ["Divide 900 por 6.", "Resulta 150 (miles de u.m. por habitante)."],
         "150"),
    ],
    mistakes=[("Creer que el PIB mide el bienestar de las personas.", "Se confunde producir con vivir bien.", "El PIB mide producción; el desarrollo incluye salud, educación, equidad y sostenibilidad."),
              ("Comparar el PIB de países de tamaños muy distintos sin dividir por la población.", "Se olvida el tamaño de la población.", "Usa el PIB per cápita para comparar.")],
    T=[
        ("=", "{F} ¿En qué porcentaje creció el PIB de País Verde del año 1 al año 2?", "(416-400)/400*100", "Se divide el aumento por el PIB antiguo y se multiplica por 100."),
        ("=", "{F} ¿Cuál es el PIB per cápita de País Verde en el año 2 (en miles de u.m. por habitante)?", "416/8", "Se divide el PIB por los habitantes, en millones."),
        ("=", "{F} ¿Cuál es el PIB per cápita de País Azul en el año 2 (en miles de u.m. por habitante)?", "300/3", "Se divide el PIB por los habitantes, en millones."),
        ("abc", "{F} ¿Qué país tiene el mayor PIB total en el año 2?", "País Verde", "País Azul", "Los dos igual", "Verde tiene 416 y Azul 300."),
        ("abc", "{F} ¿Qué país tiene el mayor PIB per cápita?", "País Azul", "País Verde", "Los dos igual", "Azul tiene 100 y Verde 52."),
        ("abc", "En Economía y sociedad: ¿qué es el PIB?", "El valor de los bienes y servicios finales producidos en un país en un período", "El total de dinero que tienen las familias", "El presupuesto del Estado", "Mide la producción, no el dinero ahorrado ni el presupuesto."),
        ("{F} Con la inflación de 3% en País Verde, ¿cuál es de forma aproximada su crecimiento real?", "Cerca de 1%", "El crecimiento nominal de 4% menos la inflación de 3% da una aproximación de 1%."),
        ("abc", "{F} Un periodista dice: «Verde produce más que Azul, así que sus habitantes producen más cada uno». ¿Qué corrección harías?", "Hay que mirar el PIB per cápita, que es mayor en Azul", "Es cierto si el país tiene más población", "El PIB no mide producción", "El total no dice cuánto toca por habitante."),
        ("abc", "En Economía y sociedad: ¿qué diferencia hay entre crecimiento y desarrollo?", "El crecimiento es el aumento del PIB y el desarrollo incluye calidad de vida, equidad y sostenibilidad", "Son exactamente lo mismo", "El desarrollo solo mide el ingreso", "El desarrollo es un concepto más amplio."),
        ("{F} País Verde crece 4% pero el ingreso se concentra en pocas personas. ¿Qué indicador pediría un economista además del PIB per cápita?", "Uno de desigualdad del ingreso", "El promedio no muestra cómo se reparte el ingreso."),
        ("abc", "¿Qué combina el Índice de Desarrollo Humano según la clase?", "Ingreso, salud y educación", "Solo el PIB", "Solo la inflación", "Es un indicador de desarrollo más amplio que el PIB."),
        ("abc", "Un país aumenta su producción cortando bosques sin límite. ¿Qué limitación del PIB muestra?", "No mide el daño ambiental", "Mide la salud de las personas", "Mide la desigualdad", "El PIB cuenta la producción, pero no descuenta el daño ambiental."),
        ("{F} En País Azul el PIB se mantiene en 300 y la población sube de 3 a 4 millones. ¿Qué pasa con el PIB per cápita?", "Baja de 100 a 75 (miles de u.m. por habitante)", "300 dividido por 4 es 75, menor que 300 dividido por 3."),
    ],
    ctx=("abc", "Una región de ejemplo tiene un PIB que crece 5% al año, pero la proporción de jóvenes que termina la secundaria no cambia desde hace años. ¿Qué conclusión es adecuada?", "Hay crecimiento, pero eso no basta para afirmar que mejora el desarrollo", "El desarrollo está garantizado", "El PIB no crece realmente", "El desarrollo incluye educación, que aquí no mejora."),
    sc=[
        ("¿Cómo se calcula el PIB per cápita?", "Dividiendo el PIB por la cantidad de habitantes", "Permite comparar países de distinto tamaño."),
        ("En Economía y sociedad: ¿qué es el crecimiento real?", "El crecimiento descontada la inflación", "Muestra si se produce más y no solo con precios más altos."),
        ("¿Por qué el PIB per cápita no basta para medir el bienestar?", "Porque es un promedio y no muestra cómo se reparte ni otros aspectos como la salud", "El desarrollo incluye más que el ingreso."),
    ],
    op=("Compara dos países de ejemplo. País Rojo: PIB de 600 el año 1 y 624 el año 2, con 12 millones de habitantes y precios que suben 2%. País Gris: PIB de 150 el año 1 y 156 el año 2, con 2 millones de habitantes y precios que suben 5%. "
        "Calcula el crecimiento nominal de cada uno, el crecimiento real aproximado, el PIB per cápita del año 2, y escribe dos frases: una que compare ambos países con tus cálculos y una que explique qué más habría que saber para hablar de desarrollo.",
        "Rojo: (624 menos 600) sobre 600, 4%; real cerca de 2%; per cápita 52. Gris: (156 menos 150) sobre 150, 4%; real cerca de -1%; per cápita 78. Para desarrollo faltan salud, educación, desigualdad y sostenibilidad.",
        ["calcula crecimiento nominal y real", "calcula el PIB per cápita", "compara con cifras", "nombra indicadores de desarrollo que faltan"],
        ["cálculos de dos países y dos frases"],
        ["no descontar la inflación", "dividir mal el PIB per cápita", "concluir desarrollo solo con el PIB"],
        "Pregunta: «¿es lo mismo que un país produzca más a que sus personas vivan mejor?». Pide una razón."),
    reinforce="Calcula el PIB per cápita de un país imaginario con PIB de 800 y 10 millones de habitantes, y explica qué te dice y qué no.",
    extend="Explica por qué un país puede tener un PIB per cápita alto y aun así tener problemas de equidad o de sostenibilidad.",
)

# ============================================================ OAC-07, clase 2
F = ("Ficha 28 (región de ejemplo, ficticia). Mercado laboral en el período 1: 9.500 personas ocupadas, 500 desocupadas (buscan trabajo y no lo encuentran) y 4.000 inactivas (no trabajan ni buscan, por ejemplo estudiantes). "
     "En el período 2: 9.600 ocupadas, 400 desocupadas y 4.000 inactivas. Canasta de precios: costo 80.000 en el período 1 y 84.800 en el período 2. Crecimiento de la producción regional de ejemplo: 3%.")
build(
    O7, 2, F,
    use="Aprenderé a leer y calcular indicadores macroeconómicos (desempleo, inflación y crecimiento) y a reconocer sus límites al explicar la situación de una economía.",
    prior=["Sé calcular un cambio porcentual.", "Sé qué es el PIB y la inflación.", "Sé interpretar una tabla con dos períodos."],
    explain=[
        "La macroeconomía estudia la economía en su conjunto: producción, empleo y precios. Tres indicadores básicos son el crecimiento del PIB, la tasa de desocupación y la inflación. Con ellos se describe cómo está la economía y qué problemas enfrenta, pero ninguno basta por sí solo. Estos indicadores los calculan organismos estadísticos, como el Instituto Nacional de Estadísticas en Chile.",
        "La fuerza de trabajo es la suma de las personas ocupadas y las desocupadas. Las personas inactivas no la integran. La tasa de desocupación es el porcentaje de la fuerza de trabajo que está desocupada: desocupadas dividido por la fuerza de trabajo, por 100. Una baja del desempleo puede ocurrir porque más personas encuentran trabajo, pero también porque algunas dejan de buscarlo y pasan a ser inactivas.",
        "Los indicadores tienen límites. El desempleo no distingue empleos formales de informales ni la calidad de los salarios. La inflación es un promedio de una canasta, y cada hogar siente una distinta. El crecimiento no dice cómo se reparte la producción. Por eso se interpretan juntos: por ejemplo, un crecimiento alto con inflación alta y desempleo bajo describe una economía «recalentada», mientras que bajo crecimiento y alto desempleo sugiere una economía débil.",
    ],
    vocab=[("macroeconomía", "estudio de la economía en su conjunto"), ("fuerza de trabajo", "personas ocupadas más desocupadas"), ("tasa de desocupación", "porcentaje de la fuerza de trabajo que está desocupada"), ("persona desocupada", "quien busca trabajo y no lo encuentra"), ("persona inactiva", "quien no trabaja ni busca trabajo"), ("informalidad", "trabajo sin contrato o fuera de las reglas legales")],
    worked=[
        ("Calcular la tasa de desocupación", "En una comuna de ejemplo hay 4.700 ocupadas y 300 desocupadas. ¿Cuál es la tasa de desocupación?",
         ["Fuerza de trabajo: 4.700 más 300, es decir 5.000.", "Tasa: 300 dividido por 5.000, por 100, da 6%."],
         "6%"),
        ("Interpretar un cambio", "En otra comuna de ejemplo la tasa de desocupación bajó, pero el número de personas inactivas subió mucho. ¿Qué precaución debes tener?",
         ["La baja puede deberse a que algunas personas dejaron de buscar trabajo.", "Hay que mirar también cuántas personas están ocupadas."],
         "Revisar si la baja se debe a personas que dejaron de buscar trabajo"),
    ],
    mistakes=[("Contar a las personas inactivas dentro de la fuerza de trabajo.", "Se confunde no tener trabajo con estar desocupado.", "Desocupado es quien busca trabajo y no lo encuentra."),
              ("Interpretar un indicador sin mirar los otros.", "Se supone que uno basta para describir la economía.", "Lee juntos crecimiento, desempleo e inflación.")],
    T=[
        ("=", "{F} ¿Cuál es la fuerza de trabajo en el período 1?", "9500+500", "Se suman ocupadas y desocupadas."),
        ("=", "{F} ¿Cuál es la tasa de desocupación en el período 1?", "500/10000*100", "Se divide las desocupadas por la fuerza de trabajo y se multiplica por 100."),
        ("=", "{F} ¿Cuál es la tasa de desocupación en el período 2?", "400/10000*100", "La fuerza de trabajo es 9.600 más 400, es decir 10.000."),
        ("abc", "En Economía y sociedad: ¿quién es una persona desocupada?", "Quien busca trabajo y no lo encuentra", "Quien no quiere trabajar", "Cualquier estudiante", "Estar desocupado exige buscar trabajo activamente."),
        ("abc", "{F} ¿Las 4.000 personas inactivas forman parte de la fuerza de trabajo?", "No", "Sí", "Solo en el período 2", "La fuerza de trabajo incluye solo ocupadas y desocupadas."),
        ("=", "{F} ¿En qué porcentaje subió el costo de la canasta entre ambos períodos?", "(84800-80000)/80000*100", "Se divide el aumento por el costo antiguo y se multiplica por 100."),
        ("abc", "{F} Con la inflación y el desempleo calculados, ¿qué ocurrió entre los dos períodos?", "El desempleo bajó y la inflación fue de 6%", "El desempleo subió y no hubo inflación", "No cambió nada", "El desempleo bajó de 5% a 4% y los precios subieron 6%."),
        ("abc", "{F} La inflación fue de 6% y la producción creció 3% (dato de la ficha). ¿Qué relación hay entre ambos?", "Los precios crecen más que la producción", "La producción crece más que los precios", "Son iguales", "El 6% de inflación es mayor que el 3% de crecimiento."),
        ("abc", "Un informe de ejemplo dice: «El desempleo bajó de 8% a 6%». ¿Qué dato adicional sería útil para interpretar mejor?", "Cuántas personas dejaron de buscar trabajo", "El número de oficinas de empleo", "El número de empresas de la ciudad", "La baja puede venir de quienes dejaron de buscar empleo."),
        ("{F} ¿Por qué la tasa de desocupación no muestra si los empleos son de buena calidad?", "Porque cuenta personas ocupadas sin distinguir informalidad ni salarios", "El indicador solo clasifica a las personas según si trabajan o buscan trabajo."),
        ("abc", "Una economía de ejemplo tiene alto crecimiento, inflación alta y bajo desempleo. ¿Cómo se suele describir?", "Como una economía recalentada", "Como una economía débil", "Como una economía sin datos", "Mucha demanda presiona los precios hacia arriba."),
        ("abc", "Una economía de ejemplo tiene bajo crecimiento y alto desempleo. ¿Qué sugiere?", "Una economía débil", "Una economía recalentada", "Una economía sin problemas", "La producción y el empleo están por debajo de lo posible."),
        ("¿Por qué conviene leer juntos el crecimiento, el desempleo y la inflación?", "Porque cada indicador muestra un aspecto y juntos describen mejor la economía", "Uno solo puede esconder problemas que otro revela."),
    ],
    ctx=("abc", "En una comuna de ejemplo hay 6.800 personas ocupadas y 200 desocupadas. ¿Cuál es su tasa de desocupación, aproximada?", "Cerca de 2,9%", "2%", "10%", "200 dividido por 7.000 es cerca de 2,86%, o 2,9%."),
    sc=[
        ("¿Cómo se calcula la fuerza de trabajo?", "Sumando las personas ocupadas y las desocupadas", "Las personas inactivas no se incluyen en la fuerza de trabajo."),
        ("En Economía y sociedad: ¿qué es la informalidad laboral?", "El trabajo sin contrato o fuera de las reglas legales", "El indicador de desocupación no la distingue."),
        ("¿Por qué una baja del desempleo puede engañar?", "Porque quienes dejan de buscar trabajo salen de la fuerza de trabajo", "Esas personas dejan de contarse como desocupadas."),
    ],
    op=("Resuelve este caso de ejemplo. Región Costa: período 1, 18.000 ocupadas, 2.000 desocupadas; período 2, 18.900 ocupadas, 1.600 desocupadas. La canasta cuesta 50.000 en el período 1 y 52.000 en el período 2; la producción crece 2%. "
        "Calcula la tasa de desocupación de cada período, la inflación, y compara con el crecimiento. Luego escribe tres frases: qué describe la economía, un límite de los indicadores y qué otro dato pedirías.",
        "Período 1: 2.000 sobre 20.000, 10%. Período 2: 1.600 sobre 20.500, cerca de 7,8%. Inflación: 2.000 sobre 50.000, 4%. Los precios suben más que la producción. Límite: no distingue informalidad. Pediría la proporción de empleo formal.",
        ["calcula bien la fuerza de trabajo y la tasa", "calcula la inflación", "compara con el crecimiento", "nombra un límite y un dato adicional"],
        ["cálculos y tres frases"],
        ["incluir inactivas en la fuerza de trabajo", "dividir por el valor nuevo en la inflación", "interpretar un solo indicador"],
        "Pregunta: «¿quiénes están dentro de la fuerza de trabajo?». Con eso rehace el denominador."),
    reinforce="Con la Ficha 28, calcula la fuerza de trabajo de cada período y explica por qué es igual aunque cambió el número de personas ocupadas.",
    extend="Explica por qué la informalidad laboral puede esconderse en la tasa de desocupación.",
)

# ============================================================ OAC-07, clase 3
F = ("Ficha 29 (situaciones de ejemplo, ficticias). Situación 1: en un país de ejemplo la producción cae y el desempleo sube (recesión). Situación 2: los precios suben con rapidez, más allá de lo que el banco central considera deseable. "
     "Situación 3: la red de salas cuna de una ciudad de ejemplo no alcanza para las familias que trabajan, y muchas madres y padres no pueden emplearse (necesidad pública). "
     "Datos de ejemplo del Estado: ingresos del año 90 y gastos del año 100 (en miles de millones de u.m.).")
build(
    O7, 3, F,
    use="Aprenderé a explicar la política fiscal y la monetaria, qué necesidad pública atienden y cómo se discuten sus efectos y costos, con ejemplos de Chile y casos ficticios.",
    prior=["Conozco el PIB, la inflación y el desempleo.", "Sé qué es un impuesto y un subsidio.", "Distingo afirmaciones positivas y normativas."],
    explain=[
        "Una política económica es un conjunto de decisiones del Estado para influir en la economía y atender necesidades públicas, es decir, necesidades que afectan a muchas personas y que se espera que el Estado ayude a resolver, como educación, salud, seguridad o infraestructura. Las dos políticas macroeconómicas centrales son la fiscal y la monetaria.",
        "La política fiscal usa el gasto público y los impuestos. Si el Estado gasta más o cobra menos impuestos, impulsa la demanda; si gasta menos o cobra más, la modera. Cuando los gastos superan a los ingresos hay déficit fiscal, que se financia con deuda; cuando los ingresos superan a los gastos hay superávit. En Chile, el presupuesto anual se aprueba por ley en el Congreso. La política monetaria la conduce el banco central: en Chile, el Banco Central es autónomo y usa una tasa de interés de política monetaria para cuidar la estabilidad de los precios. Su autonomía busca que las decisiones sobre la tasa no dependan de las urgencias del gobierno de turno.",
        "Si la tasa baja, el crédito es más barato y tiende a aumentar el consumo y la inversión; si sube, se encarece el crédito y se modera la demanda, lo que ayuda a bajar la inflación. Estas herramientas tienen costos y plazos: un mayor gasto puede aumentar la deuda y subir tasas puede frenar el empleo. Las posturas difieren en cuánto gasto público conviene y cómo cuidar la deuda; aquí se explican los mecanismos sin tomar partido.",
    ],
    vocab=[("necesidad pública", "necesidad de muchas personas que se espera que el Estado ayude a resolver"), ("política fiscal", "uso del gasto público y los impuestos para influir en la economía"), ("política monetaria", "uso de la tasa de interés y el dinero para cuidar la estabilidad de precios"), ("déficit fiscal", "gastos del Estado mayores que sus ingresos"), ("tasa de interés", "precio del dinero prestado"), ("banco central", "institución que conduce la política monetaria")],
    worked=[
        ("Calcular un déficit", "Un Estado de ejemplo tiene ingresos de 70 y gastos de 80 (miles de millones de u.m.). ¿Hay déficit o superávit y de cuánto?",
         ["Compara ingresos y gastos: 70 y 80.", "Los gastos superan a los ingresos en 10: déficit."],
         "Déficit de 10"),
        ("Efecto de la tasa", "El banco central de un país de ejemplo sube la tasa de interés. ¿Qué efecto se espera sobre el crédito y la demanda?",
         ["Una tasa más alta encarece el crédito.", "Hay menos consumo e inversión, lo que modera la demanda y la inflación."],
         "Crédito más caro y menor demanda"),
    ],
    mistakes=[("Creer que el banco central y el gobierno hacen lo mismo.", "Se confunde política monetaria con fiscal.", "El banco central maneja la tasa de interés; el gobierno maneja gasto e impuestos."),
              ("Pensar que más gasto público siempre es bueno o siempre es malo.", "Se ignoran los efectos y costos.", "Evalúa a qué necesidad responde, cuánto cuesta y cómo se financia.")],
    T=[
        ("abc", "{F} ¿Qué tipo de política es subir el gasto público y bajar los impuestos para impulsar la demanda?", "Fiscal", "Monetaria", "De comercio exterior", "Esta política usa el gasto público y los impuestos."),
        ("abc", "{F} ¿Qué política usa la tasa de interés?", "La monetaria", "La fiscal", "La de gasto público", "El banco central conduce la tasa."),
        ("=", "{F} ¿Cuántos miles de millones de u.m. es el déficit del Estado de la ficha?", "100-90", "Se resta el ingreso al gasto."),
        ("abc", "En Economía y sociedad: ¿qué es una necesidad pública?", "Una necesidad de muchas personas que se espera que el Estado ayude a resolver", "Un gasto privado de una familia", "Un impuesto", "Incluye educación, salud, seguridad e infraestructura."),
        ("abc", "{F} Situación 1 (recesión): ¿qué política fiscal se suele discutir?", "Aumentar el gasto o bajar impuestos para impulsar la demanda", "Subir la tasa de interés", "Prohibir el comercio", "Se busca estimular la producción y el empleo."),
        ("abc", "{F} Situación 2 (inflación alta): ¿qué hace el banco central en general?", "Sube la tasa de interés para moderar la demanda", "Baja la tasa de interés", "Aumenta el gasto público", "Una tasa mayor encarece el crédito y modera los precios."),
        ("abc", "{F} Situación 3: ¿qué necesidad pública aparece?", "Cuidado infantil para que las familias puedan trabajar", "Falta de moneda", "Exceso de importaciones", "La falta de salas cuna impide que algunas personas se empleen."),
        ("abc", "¿Qué busca la autonomía del banco central?", "Que las decisiones sobre la tasa de interés no dependan de las urgencias del gobierno de turno", "Que el banco fije los impuestos y el gasto público", "Que el banco no tenga que cuidar los precios", "La autonomía separa la política monetaria de la presión política de corto plazo."),
        ("{F} Si el Estado de la ficha aumenta aún más su gasto sin subir ingresos, ¿qué ocurre con el déficit?", "Aumenta", "Gastar más sin más ingresos amplía la diferencia."),
        ("abc", "{F} Una concejala propone construir más salas cuna y otra propone cuidar la deuda. ¿Qué ocurre con estas posturas?", "Priorizan valores o riesgos distintos, y ambas pueden usar argumentos", "Solo una tiene argumentos", "Las dos hablan de política monetaria", "Una enfatiza la necesidad pública y la otra el costo y la deuda."),
        ("abc", "El banco central baja la tasa de interés. ¿Qué efecto se espera?", "Crédito más barato y más consumo e inversión", "Crédito más caro y menos consumo", "Que se cierre el comercio", "Una tasa menor abarata el crédito."),
        ("{F} ¿Por qué subir la tasa puede ayudar contra la inflación pero tener un costo?", "Modera la demanda y los precios, pero puede frenar la inversión y el empleo", "La política tiene un intercambio entre estabilidad de precios y actividad."),
        ("abc", "«El Estado debería gastar más en salas cuna» es una afirmación…", "Normativa, porque expresa lo que debería hacerse", "Positiva, porque tiene un dato", "Falsa", "Contiene un deber que depende de valores."),
    ],
    ctx=("abc", "Una ciudad de ejemplo analiza ampliar los consultorios con fondos del presupuesto. Los ingresos del municipio son de 40 y los gastos previstos son de 46 (millones de u.m.). ¿Qué situación fiscal tendría?", "Un déficit de 6", "Un superávit de 6", "Equilibrio exacto", "Los gastos superan en 6 a los ingresos."),
    sc=[
        ("¿Qué instrumentos usa la política fiscal?", "El gasto público y los impuestos", "Se aplican por el Estado y el Congreso en el presupuesto."),
        ("En Economía y sociedad: ¿qué instrumento usa el banco central?", "La tasa de interés de política monetaria", "Su objetivo principal es la estabilidad de precios."),
        ("¿Qué es un déficit fiscal?", "Cuando los gastos del Estado superan a sus ingresos", "Ese déficit se financia generalmente con deuda pública."),
    ],
    op=("Elige una situación de ejemplo y explícala. Situación 1: una comuna sin suficientes salas cuna. Situación 2: un país en recesión con desempleo creciente. "
        "Escribe: (1) la necesidad pública o el problema; (2) una política fiscal posible y una monetaria si corresponde; (3) un efecto esperado; (4) un costo o riesgo; (5) un argumento de quienes la apoyan y otro de quienes la cuestionan, sin que tomes partido.",
        "Situación 2. Problema: recesión. Fiscal: más gasto en obras. Monetaria: bajar la tasa. Efecto: más empleo. Riesgo: más deuda o inflación. Apoyo: estimula el empleo. Cuestionamiento: eleva la deuda.",
        ["identifica el problema o la necesidad", "distingue política fiscal y monetaria", "nombra efecto y riesgo", "presenta argumentos de dos posturas sin tomar partido"],
        ["texto de cinco partes"],
        ["confundir quién aplica cada política", "no mencionar riesgos", "tomar partido sin argumentos"],
        "Pregunta: «¿quién decide esta herramienta, el gobierno o el banco central?». Con eso verifica la política."),
    reinforce="Escribe una necesidad pública de tu comuna y una política fiscal que podría atenderla.",
    extend="Explica qué ventaja tiene que el banco central decida la tasa de interés de forma autónoma y qué discusión puede provocar.",
)

# ============================================================ OAC-07, clase 4
F = ("Ficha 30 (programa de ejemplo, ficticio). El programa «Oficio Joven» capacita a 2.000 jóvenes con un costo total de $1.800 millones. Resultados de ejemplo seis meses después: el 60% de los capacitados consigue empleo formal. "
     "En un grupo comparable de jóvenes que no recibió el programa, el 40% consiguió empleo formal en el mismo plazo. La necesidad pública que busca atender es el desempleo juvenil. El programa se financia con impuestos generales.")
build(
    O7, 4, F,
    use="Aprenderé a explicar las relaciones y consecuencias de una política económica en Chile: qué efectos produce, a quién llegan, cuánto cuesta y qué compromisos implica con el crecimiento y el desarrollo.",
    prior=["Conozco política fiscal y necesidades públicas.", "Sé calcular porcentajes y costos por persona.", "Sé comparar un grupo con otro."],
    explain=[
        "Evaluar una política económica es preguntar si logra lo que busca y a qué costo. Para medir su efecto no basta mirar cuántas personas mejoraron: hay que comparar con un grupo similar que no recibió la política, porque parte de la mejora ocurriría de todas formas. La diferencia entre ambos grupos es el efecto atribuible a la política.",
        "También se calcula el costo por persona atendida y el costo por resultado adicional. Esos números permiten comparar con otras formas de usar los mismos recursos, recordando el costo de oportunidad: el dinero gastado en un programa no se usa en otro. Además se miran consecuencias indirectas, como el efecto en la equidad, en el crecimiento y en el financiamiento futuro.",
        "Una política puede tener efectos buenos y riesgos. Un programa de capacitación puede aumentar el empleo, pero también puede no llegar a quienes más lo necesitan o competir por recursos con otras necesidades. Quienes lo apoyan destacan la inversión en las personas; quienes lo cuestionan, los costos y la efectividad. Un análisis honesto presenta ambos argumentos, indica los límites de la evidencia y deja la decisión final abierta a los valores.",
    ],
    vocab=[("efecto atribuible", "diferencia entre quienes recibieron la política y un grupo comparable"), ("grupo comparable", "grupo parecido que no recibió la política"), ("costo por persona", "costo total dividido por las personas atendidas"), ("costo por resultado adicional", "costo total dividido por los resultados que genera la política"), ("consecuencia indirecta", "efecto no buscado o de segundo orden"), ("empleo formal", "empleo con contrato y protección legal")],
    worked=[
        ("Calcular el efecto", "Un programa de ejemplo con 500 personas logra empleo para el 70%. Un grupo comparable logra el 50%. ¿Cuál es el efecto en puntos porcentuales?",
         ["Resta el resultado del grupo comparable al de quienes recibieron el programa.", "70 menos 50."],
         "20 puntos porcentuales"),
        ("Calcular el costo por persona", "El programa anterior cuesta $100 millones. ¿Cuánto cuesta por persona?",
         ["Divide el costo total por las personas: 100.000.000 dividido por 500.", "Resulta 200.000."],
         "$200.000 por persona"),
    ],
    mistakes=[("Atribuir al programa todo el empleo conseguido.", "Se olvida que parte habría ocurrido sin el programa.", "Compara con un grupo comparable."),
              ("Mirar solo el costo o solo el resultado.", "Se usa un único criterio.", "Evalúa efecto, costo, equidad y alternativas.")],
    T=[
        ("=", "{F} ¿Cuántos puntos porcentuales más de empleo formal logró el grupo del programa respecto del grupo comparable?", "60-40", "Se resta el 40% al 60%."),
        ("=", "{F} ¿Cuántos jóvenes de los 2.000 capacitados consiguieron empleo formal?", "2000*60/100", "Se calcula el 60% de 2.000."),
        ("=", "{F} ¿Cuántos de ellos, en una cantidad parecida, habrían conseguido empleo igual sin programa (40% de 2.000)?", "2000*40/100", "Se calcula el 40% de 2.000."),
        ("=", "{F} ¿Cuántos empleos adicionales atribuibles genera el programa?", "1200-800", "Se restan los 800 que habrían conseguido sin programa a los 1.200 con programa."),
        ("abc", "En Economía y sociedad: ¿qué es un grupo comparable?", "Un grupo parecido que no recibió la política", "El mismo grupo de siempre", "Un grupo elegido por su resultado", "Permite estimar qué habría pasado sin la política."),
        ("=", "{F} ¿Cuánto cuesta el programa por joven capacitado (en pesos)? El costo es de $1.800 millones, es decir 1.800.000.000.", "1800000000/2000", "Se divide el costo total por las personas."),
        ("=", "{F} ¿Cuánto cuesta por cada empleo adicional atribuible (en pesos)?", "1800000000/400", "Con 400 empleos adicionales, se divide el costo total por 400."),
        ("abc", "{F} Un periodista dice: «Mil doscientos jóvenes encontraron trabajo gracias al programa». ¿Qué corrección harías?", "Parte de ellos habría encontrado empleo igual: el efecto atribuible es de 400", "Es correcto, no hay nada que corregir", "El programa no tuvo ningún efecto", "La diferencia con el grupo comparable muestra el efecto real."),
        ("abc", "{F} ¿Qué consecuencia indirecta convendría revisar?", "Si el programa llega a los jóvenes que más lo necesitan", "El prestigio del instituto que da los cursos", "El horario de los cursos solamente", "El efecto en la equidad es una consecuencia relevante."),
        ("abc", "{F} El programa se financia con impuestos generales. ¿Qué concepto económico se relaciona con eso?", "Costo de oportunidad: ese dinero no se usa en otra necesidad", "Competencia perfecta", "Monopolio", "Usar recursos limitados en un programa impide usarlos en otro."),
        ("abc", "{F} Quienes cuestionan el programa dicen: «Con $1.800 millones se podrían atender otras necesidades». ¿Qué tipo de argumento es?", "Un argumento de costo de oportunidad", "Un argumento de oferta y demanda", "Un argumento sobre inflación", "Compara este uso del dinero con otros usos posibles."),
        ("abc", "{F} Quienes apoyan el programa dicen: «Invertir en capacitación mejora las oportunidades de los jóvenes». ¿Qué valor priorizan?", "La inversión en las personas y la igualdad de oportunidades", "La reducción de impuestos", "El ahorro de recursos públicos por sobre todo", "Destacan el efecto en las oportunidades de los jóvenes."),
        ("¿Por qué una evaluación honesta debe indicar los límites de la evidencia del programa?", "Porque los resultados son de ejemplo y de un solo plazo, y podrían no repetirse", "Reconocer límites evita presentar como cierto lo que es incierto."),
    ],
    ctx=("abc", "Una comuna de ejemplo gasta $90 millones en un programa de apoyo a emprendimientos de 300 familias. Un año después, 180 emprendimientos siguen funcionando, frente a 120 en un grupo comparable de 300 familias. ¿Cuántos emprendimientos adicionales se atribuyen al programa?", "60", "180", "120", "La diferencia entre 180 y 120 es 60."),
    sc=[
        ("¿Por qué hace falta un grupo comparable?", "Para estimar qué habría pasado sin la política", "Así se mide el efecto atribuible."),
        ("¿Qué es el costo por resultado adicional?", "El costo total dividido por los resultados que genera la política", "Permite comparar con otras alternativas de uso de los recursos."),
        ("En Economía y sociedad: ¿qué es una consecuencia indirecta?", "Un efecto no buscado o de segundo orden", "Por ejemplo, el efecto en la equidad."),
    ],
    op=("Evalúa este programa de ejemplo: «Subsidio al transporte escolar» atiende a 3.000 estudiantes con un costo de $600 millones; con el subsidio asisten regularmente el 90%, frente al 80% en un grupo comparable. "
        "Calcula el costo por estudiante, el efecto en puntos porcentuales, los estudiantes adicionales que asisten regularmente por el programa, y el costo por estudiante adicional. "
        "Escribe un argumento a favor y uno en contra, una consecuencia indirecta y un límite de la evidencia.",
        "Costo por estudiante: 600.000.000 dividido por 3.000, 200.000. Efecto: 10 puntos. Adicionales: 300. Costo por adicional: 2.000.000. A favor: reduce la deserción. En contra: es caro por resultado. Límite: un solo grupo de ejemplo.",
        ["calcula el costo por persona", "calcula el efecto atribuible", "calcula el costo por resultado adicional", "presenta argumentos de ambas posturas"],
        ["cálculos y cuatro frases"],
        ["atribuir al programa todo el resultado", "calcular el costo por resultado con el total", "no mencionar límites"],
        "Pregunta: «¿cuántos habrían asistido igual sin el programa?». Con eso corrige el efecto."),
    reinforce="Con la Ficha 30, explica con tus palabras por qué los 400 empleos adicionales, y no los 1.200, son el efecto del programa.",
    extend="Compara dos programas de ejemplo con el mismo costo, uno con mayor efecto y otro que llega a más personas, y explica qué valores llevarían a elegir uno u otro.",
)
