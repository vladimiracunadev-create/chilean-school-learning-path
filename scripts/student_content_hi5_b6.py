"""Cuaderno del estudiante, 5.º básico Historia, Geografía y Ciencias Sociales: OA 19 (organizaciones para resolver problemas comunes)."""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import arith, ex, register

OA19 = "HI05 OA 19"
E = ex


def W(title, problem, steps, answer):
    return {"title": title, "problem": problem, "steps": steps, "answer": answer}


def M(wrong, why, fix):
    return {"wrong": wrong, "why": why, "fix": fix}


def tiers(recovery, understand, apply, reason, challenge):
    return {"recovery": recovery, "understand": understand, "apply": apply, "reason": reason, "challenge": challenge}


register(
    OA19, 1,
    materials="Este cuaderno y un lápiz. Los casos están escritos en los ejercicios.",
    use="Aprenderé a reconocer distintas formas de organizarse (fundaciones, voluntariado, empresas, agrupaciones y recolección de fondos) y qué problema resuelve cada una. Sirve para saber cómo un grupo puede lograr metas que una persona sola no alcanza.",
    prior=["Sé que participar en la comunidad es un derecho y una responsabilidad.", "Sé qué es un proyecto con objetivo y plan."],
    explain=[
        "Muchos problemas se resuelven mejor entre varias personas. Cuando un grupo se organiza, reparte tareas, junta recursos y logra metas comunes. Hay distintas formas de hacerlo. Una fundación es una organización que trabaja por una causa, por ejemplo ayudar a niños enfermos o cuidar el medioambiente, y no reparte ganancias entre sus integrantes.",
        "El voluntariado reúne a personas que ayudan por decisión propia, sin recibir pago. Una agrupación es un grupo de personas con un interés común, como una junta de vecinos, un club deportivo o un centro de padres. Una empresa produce bienes o servicios para venderlos y obtener ganancias, y además da empleo. La recolección de fondos es reunir dinero para una causa, por ejemplo con una colecta o una feria solidaria.",
        "Para ubicar una organización decimos qué problema enfrenta, quiénes la forman, qué hacen, dónde actúan y desde cuándo. Un grupo de vecinos que limpia su plaza actúa en su barrio; una fundación puede trabajar en varias regiones del país.",
    ],
    vocab=[("fundación", "organización que trabaja por una causa y no reparte ganancias"), ("voluntariado", "trabajo para ayudar que se hace por decisión propia, sin pago"), ("agrupación", "grupo de personas unidas por un interés común"), ("empresa", "organización que produce bienes o servicios para venderlos"), ("recolección de fondos", "reunir dinero para una causa")],
    worked=[
        W("Reconocer la organización", "Un grupo de vecinos se junta cada sábado para limpiar su plaza, sin cobrar. ¿Qué forma de organización es?",
          ["Lo hacen por decisión propia.", "No reciben pago.", "Es un voluntariado."], "Un voluntariado"),
        W("Diferenciar", "Una panadería vende pan para obtener ganancias y da trabajo a 6 personas. ¿Es fundación o empresa?",
          ["Vende para obtener ganancias.", "Da empleo.", "Es una empresa."], "Una empresa"),
    ],
    mistakes=[
        M("Pensar que toda organización busca ganancias.", "Las fundaciones y los voluntariados trabajan por una causa.", "Pregunta por qué existe la organización."),
        M("Creer que los problemas comunes solo los resuelven las autoridades.", "Los grupos de personas también pueden organizarse.", "Busca las organizaciones de tu comunidad."),
    ],
    tiers=tiers(
        [E("Un trabajo para ayudar sin pago, por decisión propia, ¿es voluntariado o empleo?", "Voluntariado", "El empleo recibe pago."),
         E("Reunir dinero para una causa, ¿es recolección de fondos o producción?", "Recolección de fondos", "Es el nombre de esa actividad."),
         E("Una junta de vecinos, ¿es una agrupación o una empresa?", "Una agrupación", "Reúne a personas con un interés común.")],
        [E("¿Qué diferencia hay entre una empresa y una fundación?", "La empresa busca ganancias y la fundación trabaja por una causa sin repartirlas", "Su finalidad es distinta."),
         E("¿Por qué un grupo organizado logra más que una persona sola?", "Porque reparte tareas y junta recursos", "Se suman esfuerzos."),
         E("¿Qué datos sirven para ubicar una organización?", "Qué problema enfrenta, quiénes la forman, qué hacen y dónde actúan", "Son los datos de la clase.")],
        [E("Clasifica: a) un club deportivo del barrio; b) una fundación que cuida perros abandonados; c) una tienda de ropa. Tipos: agrupación, fundación, empresa.", "a agrupación; b fundación; c empresa", "Cada una tiene un propósito distinto."),
         E("Un curso vende pasteles para reunir dinero y ayudar a un hogar de niños. ¿Qué hace: recolección de fondos o producción de ganancias propias?", "Recolección de fondos", "El dinero va a una causa."),
         arith("Un grupo voluntario de 12 personas se divide en equipos de 4. ¿Cuántos equipos se forman?", "12//4", "Se reparte entre equipos del mismo tamaño.")],
        [E("Ema dice: «Si nadie me paga, no vale la pena ayudar». ¿Qué error tiene?", "El voluntariado ayuda a otros por decisión propia", "Ayudar también tiene valor sin pago."),
         E("Un vecino dice que solo la municipalidad puede arreglar una plaza. ¿Qué otra posibilidad hay?", "Que los vecinos se organicen y colaboren", "Los grupos también pueden actuar.")],
        [E("Ordena de menor a mayor alcance: A) un grupo de vecinos de una calle, B) una fundación que trabaja en todo el país, C) un club de un barrio.", "A, C, B", "La calle es lo más pequeño y el país lo más amplio."),
         E("Un hogar de ancianos recibe a 5 voluntarios por semana. ¿Cuántos voluntarios recibe en 4 semanas?", "20", "5 por 4 son 20.", "5*4")],
    ),
    context=[E("Tras unas lluvias fuertes, vecinos juntan ropa y alimentos y los reparten entre familias afectadas. ¿Es una empresa o una forma de voluntariado y ayuda solidaria?", "Una forma de voluntariado y ayuda solidaria", "Ayudan sin recibir pago.")],
    selfcheck=[E("¿Qué es una fundación?", "Una organización que trabaja por una causa y no reparte ganancias", "Es la definición de la clase."), E("¿Qué es el voluntariado?", "Ayuda por decisión propia sin pago", "Es la definición de la clase."), E("¿Qué es una empresa?", "Una organización que produce bienes o servicios para venderlos", "Es la definición de la clase.")],
    open_task=task("Elige uno de estos problemas: a) falta de libros en la biblioteca; b) una plaza descuidada; c) un grupo de personas mayores solas (cualquier visita se haría con adultos de la escuela). Escribe qué forma de organización (fundación, voluntariado, agrupación, empresa o recolección de fondos) podría ayudar y cómo, dónde actuaría y quiénes participarían.", "Problema c: voluntariado de estudiantes que visita a personas mayores; actúa en el barrio; participan estudiantes, familias y la junta de vecinos.", ["elige la forma de organización con una razón", "ubica dónde actúa", "nombra quiénes participan"], ["párrafo de tres a cuatro frases"], ["decir que solo una autoridad puede ayudar", "no explicar cómo"], "Pide a una persona que diga si tu idea se puede hacer en tu barrio."),
    reinforce="Nombra una organización que conozcas en tu barrio y qué problema atiende.",
    extend="Escribe cómo se puede convencer a otras personas de sumarse a una causa.",
)

register(
    OA19, 2,
    materials="Este cuaderno y un lápiz. Los textos y datos están escritos en los ejercicios.",
    use="Aprenderé a leer información de una organización (un folleto, un informe de gastos) y a preguntar quién la hizo, qué cuenta y qué falta. Sirve para decidir con información si colaborar con una organización.",
    prior=["Sé reconocer distintas formas de organización.", "Sé preguntar por la procedencia de una fuente."],
    explain=[
        "Las organizaciones entregan información sobre su trabajo: folletos, sitios web, informes y rendiciones de cuentas. Una rendición de cuentas explica cuánto dinero recibió la organización y en qué lo gastó. Es una forma de ser transparente con quienes colaboran.",
        "Para leer esta información preguntamos: ¿quién la hizo y para qué?, ¿qué problema dice resolver?, ¿entrega datos concretos?, ¿explica cómo se usa el dinero? Un folleto invita a participar, así que muestra lo más atractivo. Un informe con cifras permite revisar si lo que dice es verdad.",
        "Conviene buscar otra fuente para comprobar: la opinión de personas que fueron ayudadas, o la información de una institución que regula el tema. Y reconocer lo que la fuente no dice, como los resultados a largo plazo.",
    ],
    vocab=[("folleto", "hoja que invita o informa sobre algo"), ("rendición de cuentas", "informe de cuánto dinero se recibió y en qué se gastó"), ("transparente", "claro, que se puede revisar"), ("ingreso", "dinero que entra"), ("gasto", "dinero que sale")],
    worked=[
        W("Leer ingresos y gastos", "Informe de ejemplo: ingresos $50.000, gastos $42.000. ¿Cuánto dinero queda?",
          ["Resto los gastos a los ingresos.", "50.000 − 42.000.", "Quedan $8.000."], "$8.000"),
        W("Procedencia de un folleto", "Un folleto de una organización dice «¡Ayudamos a miles de niños!». ¿Qué pregunta haces?",
          ["Pregunto quién lo hizo y para qué.", "Quiere invitar a participar.", "Falta saber cuántos niños y con qué datos."], "Cuántos niños y cómo lo comprueban"),
    ],
    mistakes=[
        M("Creer que un folleto muestra todo el trabajo de una organización.", "Se hace para invitar y muestra lo mejor.", "Busca informes con cifras."),
        M("Confundir ingresos con gastos.", "Los ingresos entran y los gastos salen.", "Revisa qué columna es cada una."),
    ],
    tiers=tiers(
        [E("El dinero que entra a una organización, ¿es un ingreso o un gasto?", "Un ingreso", "El gasto es el dinero que sale."),
         E("Un informe de cuánto dinero se recibió y en qué se gastó, ¿es una rendición de cuentas o un folleto?", "Una rendición de cuentas", "El folleto invita a participar."),
         E("Algo claro y que se puede revisar, ¿es transparente o confuso?", "Transparente", "Se puede comprobar.")],
        [E("¿Para qué hace una organización un folleto?", "Para informar e invitar a participar", "Muestra lo más atractivo de su trabajo."),
         E("¿Por qué conviene que una organización publique en qué gasta el dinero?", "Para que quienes colaboran puedan confiar en ella", "Así se muestra transparencia ante todos."),
         E("¿Qué otra fuente ayuda a comprobar lo que dice una organización?", "La opinión de personas que fueron ayudadas", "Aporta otra mirada.")],
        [arith("Informe de ejemplo: ingresos $60.000 y gastos $45.000. ¿Cuánto dinero queda?", "60000-45000", "Se resta los gastos a los ingresos.", " pesos"),
         arith("Informe de ejemplo: gastos de $12.000 en comida, $8.000 en transporte y $5.000 en materiales. ¿Cuál es el gasto total?", "12000+8000+5000", "Se suman todos los gastos.", " pesos"),
         E("Un informe dice que 30 de 50 personas ayudadas viven en el sur del país. ¿Cuántas viven en otras zonas?", "20", "50 menos 30 son 20.", "50-30")],
        [E("Beto lee «¡Somos la mejor fundación!» y dice: «Entonces lo son». ¿Qué le falta?", "Datos que lo comprueben", "Es una afirmación sin evidencia."),
         E("Una organización no publica en qué gasta el dinero. ¿Es transparente? Responde sí o no.", "No", "No permite revisar su uso del dinero.")],
        [E("Ordena los pasos para evaluar a una organización: A) buscar otra fuente, B) leer el folleto, C) pedir las cifras.", "B, C, A", "Primero el folleto, luego las cifras y luego la comparación."),
         E("Una organización recibió $90.000 y gastó $90.000. ¿Le quedó dinero? Responde sí o no.", "No", "Los gastos igualan los ingresos.")],
    ),
    context=[E("Un folleto invita a donar a un hogar de niños. Un informe aparte dice que de $100.000 recibidos, $80.000 se usaron en alimentos y útiles y $20.000 en gastos de funcionamiento. ¿Qué fuente permite saber en qué se usa el dinero?", "El informe", "Entrega cifras sobre el uso del dinero.")],
    selfcheck=[E("¿Qué es una rendición de cuentas?", "Un informe de cuánto dinero se recibió y en qué se gastó", "Es la definición del vocabulario."), E("¿Qué es un ingreso?", "El dinero que entra", "Es la definición del vocabulario."), E("¿Un folleto muestra todo el trabajo?", "No", "Muestra lo más atractivo.")],
    open_task=task("Lee este folleto de ejemplo: «Fundación Pasos Nuevos: ayudamos a niños en cinco regiones. ¡Dona hoy!». Y esta rendición de ejemplo: ingresos $100.000, gastos $85.000. Escribe dos preguntas de procedencia sobre el folleto, cuánto dinero sobró según la rendición y qué otra fuente buscarías.", "Preguntas: ¿quién lo hizo? ¿cuántos niños ayudaron? Sobraron $15.000. Otra fuente: opinión de familias ayudadas.", ["dos preguntas de procedencia", "calcula el saldo", "propone otra fuente"], ["cuatro frases"], ["creer el folleto sin revisar", "calcular mal el saldo"], "Revisa tus cálculos con una persona."),
    reinforce="Mira un afiche de una campaña solidaria y escribe quién lo hizo.",
    extend="Escribe qué información te gustaría que publicara una organización para confiar en ella.",
)

register(
    OA19, 3,
    materials="Este cuaderno y un lápiz. Los casos están escritos en los ejercicios.",
    use="Aprenderé a relacionar el problema de una comunidad con la organización que se forma, sus actores y sus consecuencias. Sirve para entender por qué las personas se organizan y qué logran.",
    prior=["Sé reconocer formas de organización.", "Sé leer información de una organización."],
    explain=[
        "Las organizaciones nacen por una causa. Una causa puede ser un problema que afecta a muchos: falta de alimentos después de una catástrofe, una plaza abandonada, niños que necesitan apoyo para estudiar. Cuando las personas ven que solas no pueden resolverlo, se agrupan y definen una meta común.",
        "Los actores de una organización son sus integrantes, los voluntarios, quienes donan, las instituciones que colaboran y las personas que reciben ayuda. Cada uno cumple un rol. También participan el Estado, con leyes y apoyos, y las empresas, que pueden colaborar con productos o dinero.",
        "Las consecuencias pueden ser mejorar la calidad de vida de las personas ayudadas y de los voluntarios, que aprenden y se comprometen. También hay desafíos: cansancio, falta de recursos o desacuerdos. Una buena organización reparte tareas y revisa sus resultados.",
    ],
    vocab=[("meta común", "objetivo que comparte todo un grupo"), ("donar", "dar dinero, tiempo o cosas sin recibir pago"), ("calidad de vida", "cómo viven las personas en salud, vivienda, estudio y compañía"), ("integrante", "persona que forma parte de un grupo"), ("compromiso", "decisión de cumplir lo que se prometió")],
    worked=[
        W("Cadena de una organización", "Un barrio sin plaza segura. Los vecinos se organizan y juntan fondos para arreglarla. Nombra la causa, los actores y una consecuencia.",
          ["Causa: la plaza insegura.", "Actores: vecinos, quienes donan, la municipalidad.", "Consecuencia: los niños pueden jugar con seguridad."], "Causa: plaza insegura; actores: vecinos y donantes; consecuencia: juego seguro"),
        W("Un desafío", "Un voluntariado empieza con 20 personas y baja a 8. ¿Qué desafío enfrenta?",
          ["Comparo 20 con 8.", "Perdió voluntarios.", "El desafío es mantener el compromiso."], "Mantener el compromiso de los voluntarios"),
    ],
    mistakes=[
        M("Creer que las organizaciones no tienen dificultades.", "A veces falta gente o dinero.", "Considera los desafíos y cómo enfrentarlos."),
        M("Nombrar solo a los voluntarios como actores.", "También participan quienes donan, reciben ayuda y las instituciones.", "Haz una lista completa."),
    ],
    tiers=tiers(
        [E("Dar dinero, tiempo o cosas sin recibir pago, ¿es donar o vender?", "Donar", "Vender recibe pago."),
         E("Un objetivo que comparte todo un grupo, ¿es una meta común o un desafío?", "Una meta común", "El desafío es una dificultad."),
         E("La decisión de cumplir lo que se prometió, ¿es compromiso o rumor?", "Compromiso", "Es la decisión de cumplir.")],
        [E("¿Por qué las personas forman organizaciones?", "Porque solas no pueden resolver un problema común", "Juntas logran más."),
         E("¿Qué consecuencias puede tener una organización en la calidad de vida de las personas?", "Mejorar cómo viven las personas ayudadas", "Ese es su propósito."),
         E("¿Qué desafíos puede enfrentar una organización?", "Falta de gente, de dinero o desacuerdos", "Son dificultades comunes.")],
        [E("Una escuela de ejemplo organiza una campaña de abrigos para el invierno. ¿Cuál es la causa de la campaña: que algunas familias no tienen abrigo suficiente para el frío o que el curso tenía tiempo libre?", "Que algunas familias no tienen abrigo suficiente para el frío", "Es el problema que motiva la campaña."),
         arith("Una campaña reúne 35 abrigos de un curso y 25 de otro. ¿Cuántos abrigos reúne en total?", "35+25", "Se suman los abrigos de ambos cursos.", " abrigos"),
         E("Quienes donan, los vecinos y la municipalidad participan en una colecta. ¿Son actores o consecuencias?", "Actores", "Participan en el hecho.")],
        [E("Clara dice: «Una organización solo la forman los voluntarios». ¿Qué error tiene?", "También participan quienes donan, reciben ayuda y las instituciones", "Hay varios actores."),
         E("Un grupo se desanima porque nadie le ayuda y deja el trabajo. ¿Qué podría hacer para seguir: pedir ayuda a más personas y repartir tareas, o rendirse?", "Pedir ayuda a más personas y repartir tareas", "Compartir el trabajo reduce el cansancio.")],
        [E("Ordena la cadena: A) mejora la calidad de vida de las familias, B) los vecinos se organizan, C) hay un problema que afecta a muchos.", "C, B, A", "Primero el problema, luego la organización y luego el resultado."),
         arith("Un grupo planea ayudar a 40 familias y logra ayudar a 32. ¿A cuántas familias faltó llegar?", "40-32", "Se resta las ayudadas a las planeadas.", " familias")],
    ),
    context=[E("Después de un temporal, un grupo de estudiantes y familias junta frazadas y las reparte a vecinos que perdieron las suyas. ¿Qué actores aparecen: estudiantes, familias y vecinos, o solo la municipalidad?", "Estudiantes, familias y vecinos", "Ellos se organizan para ayudar.")],
    selfcheck=[E("En Historia: ¿Qué es una meta común?", "Un objetivo que comparte todo un grupo", "Es la definición del vocabulario."), E("¿Qué es donar?", "Dar dinero, tiempo o cosas sin recibir pago", "Es la definición del vocabulario."), E("Nombra un desafío de una organización.", "Por ejemplo: falta de dinero o de voluntarios", "Es una dificultad común.")],
    open_task=task("Caso de ejemplo: una población quiere un comedor solidario para familias que lo necesitan. Escribe la causa, cuatro actores (por ejemplo, vecinos, personas que donan, la municipalidad, familias beneficiadas), dos consecuencias buenas y un desafío con una forma de enfrentarlo.", "Causa: familias sin alimentos suficientes. Actores: vecinos, donantes, municipalidad, familias. Consecuencias: mejor alimentación, vecinos más unidos. Desafío: pocos voluntarios; repartir turnos.", ["nombra la causa", "nombra cuatro actores", "incluye consecuencias y un desafío con solución"], ["ficha de cuatro partes"], ["omitir a las personas beneficiadas", "no considerar desafíos"], "Pide a otra persona que agregue un actor que olvidaste."),
    reinforce="Escribe cómo podrías ayudar a una causa de tu barrio con tu tiempo.",
    extend="Escribe cómo una empresa podría colaborar con una fundación.",
)

register(
    OA19, 4,
    materials="Este cuaderno y un lápiz. Los casos están escritos en los ejercicios.",
    use="Aprenderé a comparar organizaciones que enfrentan un mismo problema en distintos lugares y a reconocer perspectivas de quienes participan. Sirve para entender que hay varias formas válidas de organizarse.",
    prior=["Sé relacionar problema, organización y consecuencias.", "Sé comparar con criterios."],
    explain=[
        "Un mismo problema puede ser enfrentado de formas distintas. Para ayudar a niños a estudiar, una fundación puede dar becas, un voluntariado puede ofrecer reforzamiento los sábados, un centro de padres puede organizar una biblioteca y una empresa puede donar computadores. Todas ayudan, pero con medios, costos y alcance distintos.",
        "Comparamos con criterios: el problema que atienden, quiénes participan, de dónde viene el dinero, a cuántas personas llegan y qué tan permanente es su trabajo. Un voluntariado puede responder rápido, pero depender de que haya voluntarios. Una fundación puede ser más estable, pero necesita recursos regulares.",
        "El territorio también importa. En una ciudad hay más organizaciones y más donantes; en una zona rural, la ayuda mutua entre vecinos suele ser clave porque hay menos instituciones cerca. Las perspectivas cambian: quien da, quien recibe y quien organiza ven distintas cosas.",
    ],
    vocab=[("beca", "ayuda económica para estudiar"), ("alcance", "cuántas personas o lugares llega una ayuda"), ("estable", "que dura en el tiempo"), ("ayuda mutua", "personas que se ayudan entre sí"), ("beneficiario", "persona que recibe la ayuda")],
    worked=[
        W("Comparar dos organizaciones", "Fundación A da becas a 100 niños. Voluntariado B da clases a 20 niños los sábados. Con el criterio «alcance», ¿cuál llega a más?",
          ["Comparo 100 con 20.", "100 es mayor.", "La fundación A llega a más."], "La fundación A"),
        W("Comparar territorios", "En una zona rural los vecinos se turnan para llevar a los niños a la escuela. En la ciudad, hay buses. ¿Qué forma de organización destaca en el campo?",
          ["Pregunto cómo se resuelve.", "Los vecinos se turnan.", "Es ayuda mutua."], "La ayuda mutua entre vecinos"),
    ],
    mistakes=[
        M("Pensar que existe una única forma correcta de organizarse.", "Cada situación necesita una solución adaptada.", "Compara con criterios."),
        M("Olvidar la perspectiva de quien recibe la ayuda.", "Es quien mejor sabe lo que necesita.", "Escucha a los beneficiarios."),
    ],
    tiers=tiers(
        [E("Una ayuda económica para estudiar, ¿es una beca o una colecta?", "Una beca", "La colecta junta dinero para una causa."),
         E("Personas que se ayudan entre sí, ¿practican ayuda mutua o competencia?", "Ayuda mutua", "Se apoyan entre todos."),
         E("La persona que recibe la ayuda, ¿es el beneficiario o el donante?", "El beneficiario", "El donante es quien da.")],
        [E("¿Por qué un mismo problema puede resolverse con distintas organizaciones?", "Porque cada una tiene medios y formas distintas de ayudar", "Hay varias vías válidas."),
         E("¿Por qué en una zona rural la ayuda mutua entre vecinos puede ser clave?", "Porque hay menos instituciones cerca", "Los vecinos se apoyan entre sí."),
         E("¿Por qué conviene escuchar a los beneficiarios?", "Porque saben mejor lo que necesitan", "Aportan su perspectiva.")],
        [E("Organización A atiende a 60 niños y Organización B a 45. ¿Cuál tiene mayor alcance?", "La organización A", "60 es mayor que 45."),
         arith("Con las organizaciones A (60 niños) y B (45 niños), ¿cuántos niños atienden entre las dos?", "60+45", "Se suman los niños de ambas.", " niños"),
         E("Un voluntariado funciona mientras haya voluntarios. Una fundación tiene un equipo pagado. ¿Cuál es más estable a largo plazo?", "La fundación", "Su equipo no depende solo de que haya voluntarios.")],
        [E("Julián dice: «Solo las fundaciones pueden ayudar». ¿Qué error tiene?", "Los voluntariados, las agrupaciones y las empresas también pueden ayudar", "Hay varias formas válidas."),
         E("Una organización decide qué necesitan los beneficiarios sin preguntarles. ¿Es buena práctica? Responde sí o no.", "No", "Hay que escuchar a quienes reciben la ayuda.")],
        [E("Ordena de menor a mayor alcance: A) 30 familias, B) 120 familias, C) 80 familias.", "A, C, B", "30 es menor que 80 y 80 menor que 120."),
         arith("Una fundación quiere llegar a 200 familias y por ahora atiende a 150. ¿A cuántas más debe llegar?", "200-150", "Se resta lo que atiende a la meta.", " familias")],
    ),
    context=[E("En una ciudad y en una aldea hay niños que necesitan útiles escolares. En la ciudad una empresa dona cuadernos; en la aldea los vecinos juntan dinero entre todos. ¿Qué tienen en común ambas soluciones?", "Ambas usan la ayuda de personas organizadas", "Las dos reúnen recursos para una meta común.")],
    selfcheck=[E("¿Qué es una beca?", "Una ayuda económica para estudiar", "Es la definición del vocabulario."), E("¿Qué es la ayuda mutua?", "Personas que se ayudan entre sí", "Es la definición del vocabulario."), E("¿Qué es un beneficiario?", "La persona que recibe la ayuda", "Es la definición del vocabulario.")],
    open_task=task("Compara dos organizaciones de ejemplo que ayudan a que niños tengan útiles: la fundación Lápiz Azul (reparte útiles a 150 niños de varias regiones con dinero de donaciones) y el grupo de vecinos Unidos del Cerro (junta útiles usados y ayuda a 30 niños de su cerro). Compara alcance, quiénes participan y de dónde viene el dinero o los recursos. Escribe una semejanza y cómo podrían colaborar.", "Alcance: 150 contra 30. Participan: donantes frente a vecinos. Semejanza: ambas quieren que los niños tengan útiles. Colaboración: la fundación puede entregar útiles al grupo del cerro.", ["compara con tres criterios", "escribe una semejanza", "propone cómo colaborar"], ["tabla y dos frases"], ["decir que una es mejor sin criterios", "ignorar a los beneficiarios"], "Pide a una persona que diga qué organización le parece más cercana a tu barrio."),
    reinforce="Escribe un problema de tu barrio que podría resolverse con ayuda mutua.",
    extend="Escribe una pregunta que le harías a una persona que recibió ayuda de una organización.",
)

register(
    OA19, 5,
    materials="Este cuaderno y un lápiz. Los datos están escritos en los ejercicios.",
    use="Aprenderé a argumentar con evidencia cómo organizar una recolección de fondos o una acción solidaria para que sea efectiva y segura. Sirve para planificar una ayuda real a una causa.",
    prior=["Sé comparar organizaciones.", "Sé armar un argumento con afirmación, evidencia y razón."],
    explain=[
        "La recolección de fondos reúne dinero para una causa. Se puede hacer con una colecta, una feria de libros usados, una venta de productos o una feria de pasteles. Para que sea efectiva se necesita una meta clara, un plan y una cuenta clara de ingresos y gastos.",
        "Para argumentar a favor de una forma de recolectar usamos datos. Por ejemplo, si una feria de libros usados cuesta $2.000 en carteles y recauda $38.000, la ganancia para la causa es $36.000. Una colecta puerta a puerta, en cambio, puede ser insegura para niñas y niños: las actividades con público deben hacerse con adultos responsables y en lugares conocidos, como la escuela.",
        "Un buen argumento incluye la meta, la evidencia de que es posible, la razón y los límites. Y se informa a todos cuánto se juntó y en qué se usará, para mantener la confianza.",
    ],
    vocab=[("colecta", "recolección de dinero o cosas para una causa"), ("feria solidaria", "venta o intercambio de productos para reunir fondos"), ("ganancia", "dinero que queda después de restar los gastos"), ("meta de recaudación", "cantidad de dinero que se quiere reunir"), ("donación", "dinero o cosas que alguien entrega a una causa sin recibir pago")],
    worked=[
        W("Calcular la ganancia", "Una feria recaudó $38.000 y gastó $2.000 en carteles. ¿Cuánto dinero queda para la causa?",
          ["Resto el gasto a lo recaudado.", "38.000 − 2.000.", "Quedan $36.000."], "$36.000"),
        W("Elegir una forma segura", "Opción A: feria en la escuela con adultos. Opción B: pedir dinero a desconocidos en la calle. ¿Cuál es más segura?",
          ["Reviso el riesgo.", "A tiene adultos y lugar conocido.", "B expone a niñas y niños."], "La opción A"),
    ],
    mistakes=[
        M("Recaudar sin una meta ni cuentas claras.", "Nadie sabrá si se logró ni en qué se usó el dinero.", "Define meta y lleva registro."),
        M("Pedir dinero a desconocidos sin un adulto.", "Es inseguro.", "Hazlo solo en actividades organizadas y con adultos."),
    ],
    tiers=tiers(
        [E("La cantidad de dinero que se quiere reunir, ¿es la meta de recaudación o la ganancia?", "La meta de recaudación", "La ganancia es lo que queda después de gastos."),
         E("Dinero que queda después de restar los gastos, ¿es la ganancia o el ingreso?", "La ganancia", "El ingreso es todo el dinero que entra."),
         E("Una venta de productos para reunir fondos para una causa, ¿es una feria solidaria o una empresa?", "Una feria solidaria", "Su fin es ayudar a una causa.")],
        [E("¿Por qué una recolección de fondos necesita una meta clara?", "Para saber si se logró lo propuesto", "Permite evaluar el resultado."),
         E("¿Por qué conviene informar cuánto se juntó y en qué se usará?", "Para mantener la confianza de quienes colaboraron", "Así se muestra transparencia ante todos."),
         E("¿Por qué una actividad de fondos debe hacerse con adultos responsables?", "Para cuidar la seguridad de niñas y niños", "Así se evitan riesgos innecesarios.")],
        [arith("Una feria de libros recaudó $38.000 y gastó $2.000 en carteles. ¿Cuánta ganancia dejó?", "38000-2000", "Se resta el gasto a lo recaudado.", " pesos"),
         arith("La meta es reunir $50.000. Ya se tienen $36.000. ¿Cuánto falta?", "50000-36000", "Se resta lo reunido a la meta.", " pesos"),
         arith("Se venden 40 libros usados a $500 cada uno. ¿Cuánto dinero se recauda?", "40*500", "Se multiplica la cantidad por el precio.", " pesos")],
        [E("Ema dice: «Para juntar dinero, vamos solos a pedir en la calle». ¿Qué riesgo no considera?", "Es inseguro para niñas y niños", "Debe hacerse en lugares conocidos y con adultos."),
         E("Una colecta reunió $20.000 pero nadie sabe en qué se gastó. ¿Se mantiene la confianza? Responde sí o no.", "No", "Falta transparencia sobre el uso del dinero.")],
        [E("Afirmación: «La feria de libros es una buena opción». ¿Qué evidencia la apoya: «dejó $36.000 de ganancia» o «el cartel era de color rojo»?", "«Dejó $36.000 de ganancia»", "El dato muestra su resultado."),
         arith("La ganancia de $36.000 se reparte en partes iguales entre 4 hogares de niños. ¿Cuánto recibe cada hogar?", "36000//4", "Se reparte el total entre los hogares.", " pesos")],
    ),
    context=[arith("Un curso vende 30 jugos a $400 cada uno para ayudar a un hogar de niños. ¿Cuánto dinero recauda?", "30*400", "Se multiplica la cantidad por el precio.", " pesos")],
    selfcheck=[E("¿Qué es una colecta?", "Una recolección de dinero o cosas para una causa", "Es la definición del vocabulario."), E("¿Qué es la ganancia?", "El dinero que queda después de restar los gastos", "Es la definición del vocabulario."), E("¿Quién debe acompañar una actividad de fondos?", "Adultos responsables", "Cuidan la seguridad.")],
    open_task=task("Planifica una feria solidaria de ejemplo para ayudar a un hogar de niños: la meta es que lleguen $60.000 de ganancia a la causa. Datos: 50 libros usados a $600 cada uno, 40 jugos a $500 cada uno, gasto de $4.000 en carteles. Calcula cuánto se recauda, la ganancia y si la ganancia llega a la meta. Escribe también quién supervisaría y cómo informarías los resultados.", "Libros: 30.000. Jugos: 20.000. Recaudación: 50.000. Ganancia: 46.000. No se llega a la meta: faltan 14.000. Supervisan los profesores. Se informa en un cartel de la escuela.", ["calcula recaudación y ganancia", "compara con la meta", "incluye supervisión y cómo informar"], ["cálculos y tres frases"], ["calcular mal la ganancia", "olvidar la supervisión de adultos"], "Revisa las cuentas con una persona de tu casa."),
    reinforce="Escribe una causa que te gustaría apoyar y una forma segura de ayudar.",
    extend="Escribe cómo contarías a la escuela los resultados de una colecta.",
)
