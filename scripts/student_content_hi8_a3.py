"""Material del estudiante de 8.º básico, Historia, Geografía y Ciencias Sociales: OA 03 (formación y rasgos del Estado moderno)."""
from __future__ import annotations

from hi5_lib import build

OA = "HI08 OA 03"

# ---------------------------------------------------------------- clase 1
F = ("Ficha 1 (resumen). Estado medieval (siglos IX a XIV): el rey es uno entre muchos poderosos; los señores feudales tienen tierras, tribunales, ejércitos y tributos propios, y el territorio está dividido en señoríos. "
     "Estado moderno (siglos XV a XVIII), seis rasgos: (1) poder concentrado en la figura del rey; (2) burocracia, es decir, funcionarios que administran en nombre del rey; (3) sistema fiscal centralizado, con impuestos cobrados para todo el reino; "
     "(4) ejércitos profesionales, con soldados pagados por el Estado; (5) expansión del territorio; (6) monopolio del comercio internacional, es decir, solo el Estado o quienes él autoriza comercian con ciertas regiones. "
     "Hitos de España: matrimonio de Isabel de Castilla y Fernando de Aragón, 1469; conquista de Granada, 1492; Casa de Contratación en Sevilla para controlar el comercio con América, 1503; Felipe II, rey de 1556 a 1598.")
build(
    OA, 1, F,
    use="Aprenderé a situar el Estado moderno en el tiempo y a nombrar sus seis rasgos, comparándolo con el poder fragmentado de la Edad Media.",
    prior=["Sé distinguir Edad Media y Edad Moderna.", "Sé calcular diferencias entre años.", "Conozco la unidad religiosa medieval y su ruptura."],
    explain=[
        "Un Estado es una organización política que gobierna un territorio y a sus habitantes. En la Edad Media europea el poder estaba fragmentado, es decir, repartido: el rey existía, pero los señores feudales tenían tierras, tribunales, soldados y tributos propios. Ningún rey podía decidir solo en todo su reino.",
        "Entre los siglos XV y XVIII se formó en varios países el Estado moderno. El OA señala seis rasgos: poder concentrado en el rey, una burocracia de funcionarios, un sistema fiscal centralizado, ejércitos profesionales, expansión del territorio y monopolio del comercio internacional. Estos rasgos se reforzaban entre sí: sin impuestos no se pagaba un ejército, y sin funcionarios no se cobraban impuestos.",
        "El Estado moderno no es una democracia como la actual. El rey no era elegido y las personas eran súbditos, no ciudadanos con derecho a votar. Tampoco apareció en todos los países al mismo tiempo: España, Francia e Inglaterra lo hicieron antes que otros territorios divididos en muchos señoríos.",
    ],
    vocab=[("Estado", "organización política que gobierna un territorio y a sus habitantes"), ("fragmentación del poder", "situación en que el poder está repartido entre muchos señores"), ("burocracia", "conjunto de funcionarios que administran en nombre del gobierno"), ("sistema fiscal", "forma en que un Estado cobra impuestos y los administra"), ("monopolio", "control exclusivo de una actividad por una sola persona o institución")],
    worked=[
        ("Reconocer un rasgo", "Un reino contrata a 300 soldados de manera permanente y les paga un sueldo. ¿Qué rasgo del Estado moderno es?", ["Los soldados no dependen de un señor sino del Estado.", "Cobran sueldo del reino."], "Ejército profesional"),
        ("Calcular una duración", "Según la ficha, Felipe II fue rey de 1556 a 1598. ¿Cuántos años reinó?", ["Resto: 1598 − 1556.", "El resultado es 42."], "42 años"),
    ],
    mistakes=[("Pensar que en la Edad Media no había reyes.", "Se confunde un rey con poder limitado con la ausencia de rey.", "Recuerda que había reyes, pero eran uno entre muchos poderosos."),
              ("Creer que el Estado moderno es una democracia.", "Se aplica el presente al pasado.", "Distingue entre súbditos y ciudadanos, y entre un rey no elegido y un gobierno electo.")],
    T=[
        ("{F} ¿Cuántos rasgos del Estado moderno lista la ficha?", "Seis", "Están numerados del 1 al 6."),
        ("{F} ¿Qué es la burocracia según la ficha?", "Funcionarios que administran en nombre del rey", "Así lo define el rasgo 2."),
        ("{F} ¿Quiénes tenían tribunales y ejércitos propios en el Estado medieval?", "Los señores feudales", "La ficha lo indica."),
        ("=", "{F} ¿Cuántos años pasaron entre la conquista de Granada y la creación de la Casa de Contratación?", "1503-1492", "Se resta el primer año al segundo.", " años"),
        ("=", "{F} ¿Cuántos años pasaron entre el matrimonio de Isabel y Fernando y el comienzo del reinado de Felipe II?", "1556-1469", "Se resta el año del matrimonio al del comienzo del reinado.", " años"),
        ("{F} ¿A qué siglo pertenece la creación de la Casa de Contratación (1503)?", "Siglo XVI", "El siglo XVI va de 1501 a 1600."),
        ("{F} Clasifica cada situación con el rasgo del Estado moderno: a) funcionarios que administran el reino, b) impuestos cobrados para todo el reino, c) soldados pagados por el Estado.", "a) burocracia; b) sistema fiscal centralizado; c) ejército profesional", "Cada situación corresponde a un rasgo distinto de la ficha."),
        ("{F} Un conde cobra tributos y juzga en sus tierras sin consultar al rey. ¿A qué tipo de poder corresponde? A) Fragmentado, medieval B) Concentrado en el rey, moderno", "A) Fragmentado, medieval", "El conde actúa con poder propio, como los señores feudales de la ficha."),
        ("=", "{F} Una línea de tiempo usa 1 cm = 10 años. ¿Cuántos centímetros separan el matrimonio de Isabel y Fernando (1469) del comienzo del reinado de Felipe II (1556), redondeando hacia abajo?", "(1556-1469)//10", "Se calcula la diferencia y se divide por la escala.", " cm"),
        ("{F} ¿Por qué la Casa de Contratación ilustra el monopolio del comercio internacional?", "Porque controlaba el comercio con América desde un solo lugar", "La ficha dice que se creó para controlar ese comercio."),
        ("{F} Un compañero dice: «El Estado moderno es lo mismo que una democracia actual». ¿Qué dato de la ficha lo contradice?", "El poder está concentrado en el rey, que no es elegido", "El primer rasgo habla de poder en una persona."),
        ("{F} En un reino, el rey nombra funcionarios y cobra impuestos para todo el territorio. ¿Qué dos rasgos cumple?", "Burocracia y sistema fiscal centralizado", "Funcionarios más impuestos centralizados corresponden a los rasgos 2 y 3."),
        ("{F} Un compañero afirma: «En la Edad Media no existían reyes». Corrígelo con la ficha.", "Había reyes, pero eran uno entre muchos poderosos", "La ficha dice que el rey era uno entre muchos poderosos."),
    ],
    ctx=("Un museo quiere explicar a su público por qué los reyes de los siglos XVI y XVII podían mantener grandes ejércitos. Con la ficha, ¿qué rasgos relaciona en la explicación? {F}", "El sistema fiscal centralizado, que da dinero, y el ejército profesional, que el Estado paga", "Los impuestos permiten pagar soldados."),
    sc=[("¿Qué es la fragmentación del poder?", "El poder repartido entre muchos señores", "Así era en la Edad Media."),
        ("¿Qué rasgo describe «solo el Estado o quienes él autoriza comercian con ciertas regiones»?", "El monopolio del comercio internacional", "Es el rasgo 6."),
        ("=", "¿Cuántos años reinó un monarca de 1643 a 1715?", "1715-1643", "Se resta el año de inicio al de término.", " años")],
    op=("Haz una tabla de dos columnas, «Estado medieval» y «Estado moderno», y escribe tres filas: quién tiene tribunales, quién tiene ejército y quién cobra los impuestos. Usa la ficha para llenar cada celda. Después escribe una frase que explique por qué el Estado moderno no es una democracia. {F}",
        "Tribunales: señores feudales / funcionarios del rey. Ejército: de cada señor / profesional pagado por el Estado. Impuestos: tributos de cada señor / sistema fiscal centralizado. Frase: el rey no era elegido y las personas eran súbditos.",
        ["completa las tres filas", "usa datos de la ficha", "explica por qué no es democracia"], ["tabla", "frase"], ["poner igual el poder en ambos Estados", "decir que el rey era elegido"],
        "Pide que explique qué rasgo permite pagar el ejército profesional."),
    reinforce="Nombra de memoria los seis rasgos del Estado moderno con una palabra clave para cada uno.",
    extend="Escribe una pregunta que ayude a saber si en un reino concreto se cumplía cada uno de los seis rasgos.",
)

# ---------------------------------------------------------------- clase 2
F = ("Ficha 2 (fuentes de ejemplo escritas para este cuaderno; no son documentos históricos reales). "
     "Fuente A, cédula real de un reino imaginario, 1560, dirigida a los corregidores (funcionarios del rey en cada ciudad): «Ordeno que en cada ciudad se cobre una parte de las ventas: de cada 10 monedas vendidas, 1 va al tesoro del reino. Los corregidores enviarán el dinero cada seis meses.» "
     "Fuente B, cuenta anual de ese reino, 1560, en miles de ducados: Ingresos: impuestos 400, metales de las colonias 300, venta de cargos 100. Gastos: ejército 450, burocracia 150, corte 100, deudas 200.")
build(
    OA, 2, F,
    use="Aprenderé a analizar una cédula real y una cuenta del reino para reconocer los rasgos del Estado moderno y sus límites como fuentes.",
    prior=["Sé contextualizar una fuente.", "Conozco los seis rasgos del Estado moderno.", "Sé sumar y restar con números hasta mil."],
    explain=[
        "Una cédula real es un documento con que el rey da una orden. Sirve para ver cómo el poder central se hacía presente en las ciudades: la cédula de la ficha ordena a los corregidores cobrar una parte de las ventas y enviarla al tesoro. Eso muestra burocracia (funcionarios del rey) y sistema fiscal centralizado.",
        "La cuenta anual es un registro de ingresos y gastos. Permite ver en qué se gastaba: en este ejemplo, el ejército y las deudas son los gastos mayores. Esto ayuda a entender por qué un Estado con ejército profesional necesitaba impuestos, metales y venta de cargos. Los números son de ejemplo y no deben leerse como cifras reales.",
        "Ambas fuentes tienen límites. Una cédula dice lo que el rey ordenaba, no si en la práctica se cumplía. Una cuenta resume cifras, pero no cuenta cómo se sentían quienes pagaban. Para concluir con cuidado hay que contextualizar y comparar fuentes.",
    ],
    vocab=[("cédula real", "documento con que el rey da una orden"), ("corregidor", "funcionario del rey que gobernaba una ciudad o distrito"), ("tesoro del reino", "dinero que recibe el Estado"), ("ingreso", "dinero que entra al Estado"), ("gasto", "dinero que sale del Estado")],
    worked=[
        ("Sumar ingresos", "En la Fuente B de la ficha, ¿cuánto suman los ingresos en miles de ducados?", ["Sumo: 400 + 300 + 100.", "El total es 800."], "800 mil ducados"),
        ("Leer una orden", "En la Fuente A, ¿qué parte de lo que se vende va al tesoro?", ["Leo: de cada 10 monedas, 1 va al tesoro.", "Es una de cada diez."], "Una de cada diez monedas"),
    ],
    mistakes=[("Creer que si el rey ordena algo, todo se cumple.", "Se confunde una orden con lo que realmente ocurría.", "Pregunta qué otra fuente muestra si se cumplió."),
              ("Leer los números de ejemplo como cifras reales de España.", "Se olvida que los datos fueron escritos para este cuaderno.", "Rotula siempre los datos inventados como de ejemplo.")],
    T=[
        ("{F} ¿A quién se dirige la cédula de la Fuente A?", "A los corregidores", "La ficha lo indica al comienzo."),
        ("{F} ¿Cada cuánto deben enviar el dinero los corregidores?", "Cada seis meses", "La orden lo señala."),
        ("{F} ¿En qué rubro, el gasto del ejército o el de la corte, gastó más el reino de la Fuente B?", "El ejército", "450 es mayor que 100."),
        ("=", "{F} ¿Cuántos miles de ducados suman los gastos del reino?", "450+150+100+200", "Se suman los cuatro gastos.", " mil ducados"),
        ("=", "{F} ¿Cuántos miles de ducados faltan para cubrir los gastos con los ingresos?", "900-800", "Se resta el total de ingresos del total de gastos.", " mil ducados"),
        ("{F} ¿Qué rasgo del Estado moderno muestra la Fuente A? A) Sistema fiscal centralizado B) Monopolio del comercio internacional", "A) Sistema fiscal centralizado", "La cédula ordena cobrar un impuesto para el tesoro del reino."),
        ("=", "{F} Una ciudad vende 500 monedas. Según la Fuente A, ¿cuántas monedas deben ir al tesoro del reino?", "500//10", "Una de cada diez monedas va al tesoro.", " monedas"),
        ("{F} ¿Qué parte de los gastos de la Fuente B corresponde a la burocracia, en miles de ducados?", "150", "Es el valor de burocracia en la lista de gastos."),
        ("{F} ¿Qué rasgo del Estado moderno aparece en el ítem «ejército 450» de la Fuente B?", "Ejército profesional pagado por el Estado", "El gasto del ejército lo paga el Estado."),
        ("{F} Un compañero concluye con la Fuente A: «Todas las ciudades enviaban el dinero cada seis meses». ¿Qué falla?", "La cédula es una orden y no prueba que se cumpliera", "Falta una fuente que muestre los envíos reales."),
        ("{F} ¿Por qué hay que tratar con cuidado los números de la Fuente B?", "Porque son datos de ejemplo escritos para este cuaderno", "No representan cifras reales de un reino."),
        ("{F} Con la Fuente B, ¿qué puedes decir sobre la dependencia del reino de las colonias? A) Los metales de las colonias aportan 300 de 800 de los ingresos B) Las colonias no aportan ingresos", "A) Los metales de las colonias aportan 300 de 800 de los ingresos", "La cuenta muestra los metales como ingreso importante."),
        ("{F} ¿Qué otra fuente ayudaría a saber si los corregidores cumplían la orden? A) Un registro de pagos recibidos por el tesoro B) Un retrato del rey", "A) Un registro de pagos recibidos por el tesoro", "Un registro muestra si el dinero llegó."),
    ],
    ctx=("Un historiador escolar quiere explicar por qué el reino de la ficha necesitaba tantos impuestos. ¿Qué dato de la Fuente B usaría? {F}", "Que los gastos del ejército y las deudas suman 650 mil ducados, más que los 400 mil de impuestos", "Los gastos grandes obligaban a buscar más ingresos."),
    sc=[("¿Qué es una cédula real?", "Un documento con que el rey da una orden", "Así se definió."),
        ("¿Qué ingreso de la Fuente B es mayor: impuestos o venta de cargos?", "Los impuestos", "400 es mayor que 100."),
        ("=", "En la Fuente B, ¿cuánto suman los gastos del ejército y de la burocracia?", "450+150", "Se suman los dos gastos.", " mil ducados")],
    op=("Escribe un informe de cinco líneas con este orden: (1) quién escribió la cédula, para quién y con qué propósito; (2) dos rasgos del Estado moderno que muestran las fuentes; (3) un límite que explique qué no prueban las fuentes. Usa datos de la ficha. {F}",
        "(1) El rey, a los corregidores, para cobrar un impuesto. (2) Sistema fiscal centralizado y ejército profesional. (3) No prueban que todos pagaran ni cómo se sentían los que pagaban.",
        ["contextualiza la cédula", "nombra dos rasgos", "incluye un límite"], ["informe escrito"], ["no mencionar el propósito", "decir que lo ordenado se cumplía siempre"],
        "Pide que diga qué segunda fuente buscaría para comprobar el cumplimiento."),
    reinforce="Explica con tus palabras qué es un corregidor y qué rasgo del Estado moderno representa.",
    extend="Escribe una pregunta sobre la cuenta anual que no se pueda responder solo con la ficha.",
)

# ---------------------------------------------------------------- clase 3
F = ("Ficha 3 (mapa simplificado de la formación del Estado español). Hacia 1469 había varios reinos en la península ibérica; este mapa simplificado marca cuatro: Castilla, Aragón, Navarra y el reino musulmán de Granada (Portugal, otro reino, queda fuera del mapa). "
     "1469: matrimonio de Isabel de Castilla y Fernando de Aragón; los reinos siguen separados, pero comparten una política común. 1492: Granada pasa a formar parte de Castilla. 1512: Fernando conquista la Alta Navarra, que queda unida a Castilla (la incorporación formal se completa en 1515). Desde 1492: España llega a América y suma territorios en otro continente. "
     "Continuidades: cada reino conservaba sus leyes y costumbres propias (fueros); la nobleza mantenía privilegios; la mayoría de la población vivía del campo.")
build(
    OA, 3, F,
    use="Aprenderé a describir cómo se expandió y unificó el territorio español y qué rasgos medievales continuaron mientras se formaba el Estado moderno.",
    prior=["Conozco los seis rasgos del Estado moderno.", "Sé leer un mapa simple de la península ibérica.", "Sé distinguir cambio y continuidad."],
    explain=[
        "La expansión del territorio es uno de los rasgos del Estado moderno. En España, el matrimonio de Isabel de Castilla y Fernando de Aragón, en 1469, no unió de inmediato los reinos, pero inició una política común. Después Granada (1492) y la Alta Navarra (conquistada en 1512) quedaron unidas a Castilla, y desde 1492 España llegó a América.",
        "El territorio explica el cambio. Un rey con más tierras bajo su control podía cobrar más impuestos, mantener un ejército mayor y nombrar más funcionarios. Pero el cambio fue gradual: cada reino siguió con sus fueros, es decir, leyes y privilegios locales. Por eso la formación del Estado moderno fue un proceso largo y no un solo acto.",
        "Entre las continuidades están los privilegios de la nobleza y la vida campesina. Si solo miras la expansión, creerás que todo cambió. Si miras también las continuidades, verás que el Estado moderno convivió con muchos rasgos medievales.",
    ],
    vocab=[("expansión del territorio", "ampliación de las tierras bajo el control de un Estado"), ("fuero", "ley o privilegio propio de un reino o ciudad"), ("península ibérica", "territorio de Europa donde hoy están España y Portugal"), ("incorporar", "agregar un territorio a otro Estado"), ("privilegio", "ventaja que tiene un grupo por ley o costumbre")],
    worked=[
        ("Calcular un plazo", "Según la ficha, ¿cuántos años pasaron entre la incorporación de Granada y la conquista de la Alta Navarra?", ["Restamos 1512 − 1492.", "El resultado es 20."], "20 años"),
        ("Distinguir cambio y continuidad", "Una ciudad conserva sus leyes locales (fueros), pero ahora depende de un rey con más territorio. ¿Qué es cambio y qué continuidad?", ["Los fueros siguen igual: continuidad.", "Depender de un rey con más territorio es cambio."], "Continuidad: fueros; cambio: depende de un rey con más territorio"),
    ],
    mistakes=[("Creer que Isabel y Fernando unieron todos los reinos en 1469.", "Se confunde matrimonio con unificación inmediata.", "La ficha dice que los reinos siguieron separados y compartían política común."),
              ("Olvidar las continuidades cuando se estudia la expansión.", "Solo se mira lo nuevo.", "Nombra fueros, privilegios de la nobleza y vida campesina.")],
    T=[
        ("{F} ¿Qué reino musulmán se incorporó a Castilla en 1492?", "Granada", "La ficha lo indica."),
        ("{F} ¿Qué dos reinos se casaron en 1469 mediante Isabel y Fernando?", "Castilla y Aragón", "Isabel era de Castilla y Fernando de Aragón."),
        ("{F} ¿En qué continente suma territorios para España desde 1492?", "América", "La ficha dice que España llega a América."),
        ("=", "{F} ¿Cuántos años pasaron entre el matrimonio de Isabel y Fernando y la incorporación de Granada?", "1492-1469", "Se resta el año del matrimonio al de la incorporación.", " años"),
        ("{F} ¿Cuántos reinos marca el mapa de la ficha para 1469?", "Cuatro", "Castilla, Aragón, Navarra y Granada."),
        ("{F} Ordena de más antiguo a más reciente: Fernando conquista la Alta Navarra, Isabel y Fernando se casan, Granada se incorpora a Castilla.", "Isabel y Fernando se casan, Granada se incorpora a Castilla, Fernando conquista la Alta Navarra", "Los años son 1469, 1492 y 1512."),
        ("{F} Clasifica como cambio o continuidad: a) Granada pasa a Castilla, b) cada reino conserva sus fueros, c) la mayoría vive del campo.", "a) cambio; b) continuidad; c) continuidad", "Lo nuevo es la ampliación del territorio."),
        ("{F} ¿Qué efecto tiene que el rey controle más territorio? A) Puede cobrar más impuestos y mantener un ejército mayor B) Se elimina la nobleza", "A) Puede cobrar más impuestos y mantener un ejército mayor", "El texto explica que más territorio aumenta los recursos del Estado."),
        ("{F} ¿Por qué se dice que la formación del Estado fue gradual?", "Porque los reinos mantuvieron sus fueros y se incorporaron en distintas fechas", "Granada en 1492 y la conquista de la Alta Navarra en 1512 no ocurrieron a la vez."),
        ("{F} Un compañero dice: «En 1469 todos los reinos de la península ya eran un solo Estado». ¿Qué responde la ficha?", "Que los reinos seguían separados y solo compartían política común", "La ficha lo dice explícitamente."),
        ("{F} ¿Qué tienen en común los fueros y los privilegios de la nobleza respecto del Estado moderno?", "Son continuidades que limitaban el poder del rey", "Mostraban poderes locales dentro del reino."),
        ("{F} Un mapa de 1520 pinta toda la península con un solo color y sin diferencias. ¿Qué ocultaría? A) Los fueros y las diferencias entre reinos B) La ubicación exacta de las ciudades", "A) Los fueros y las diferencias entre reinos", "Los reinos conservaron leyes y costumbres propias."),
        ("{F} ¿Qué pregunta ayudaría a entender mejor el ritmo del cambio?", "¿Cuánto tardó cada territorio en aceptar las decisiones del rey?", "Mide la velocidad de la centralización."),
    ],
    ctx=("Un guía de museo dice: «Con el matrimonio de 1469, Isabel y Fernando crearon un Estado moderno completo». Con la ficha, ¿cómo lo corriges? {F}", "Falta que se sumen Granada y la Alta Navarra y que los reinos mantengan fueros; el proceso fue gradual", "El Estado moderno se formó con varias etapas."),
    sc=[("¿Qué es un fuero?", "Ley o privilegio propio de un reino o ciudad", "Se definió en la clase."),
        ("¿En qué año conquistó Fernando la Alta Navarra, según la ficha?", "1512", "Está en la ficha."),
        ("¿Qué rasgo del Estado moderno muestra la incorporación de Granada? A) Expansión del territorio B) Ejército profesional", "A) Expansión del territorio", "Granada amplía el territorio controlado.")],
    op=("Dibuja un croquis de la península ibérica con los cuatro reinos del mapa de 1469 usando cuatro colores. Añade una flecha para Granada (1492) y otra para la Alta Navarra (1512), indicando que quedan unidas a Castilla. Escribe debajo una frase sobre una continuidad que se mantuvo. {F}",
        "Castilla, Aragón, Navarra y Granada con colores distintos; flechas desde Granada y Navarra hacia Castilla con sus años; frase: cada reino conservó sus fueros.",
        ["colorea los cuatro reinos", "las flechas tienen años", "nombra una continuidad"], ["croquis", "frase"], ["pintar un solo reino", "no escribir los años"],
        "Pide que explique por qué Navarra se muestra separada en 1469."),
    reinforce="Explica a otra persona por qué no hubo unificación instantánea con el matrimonio de 1469.",
    extend="Escribe cómo cambiaría tu respuesta si el rey de ejemplo hubiera eliminado todos los fueros.",
)

# ---------------------------------------------------------------- clase 4
F = ("Ficha 4 (voces de ejemplo escritas para este cuaderno; no son testimonios reales). "
     "Voz 1, rey de un reino imaginario, 1580: «Necesito funcionarios leales y un ejército que me obedezca a mí, no a los señores; para pagarlos debo cobrar impuestos en todo el reino.» "
     "Voz 2, duque, 1580: «Mis antepasados tenían sus propios soldados y tribunales; no acepto que un funcionario del rey me ordene.» "
     "Voz 3, comerciante de una ciudad portuaria, 1580: «Prefiero un rey fuerte que mantenga los caminos seguros, aunque me cobre impuestos.» "
     "Voz 4, campesino, 1580: «Cada año pagan más impuestos y no veo qué gano.» "
     "Causas que mencionan los historiadores: guerras largas y caras; crecimiento del comercio; necesidad de leyes iguales para todo el reino; y el apoyo de los grupos que querían orden.")
build(
    OA, 4, F,
    use="Aprenderé a contrastar las perspectivas de quienes ganaban y perdían con el Estado moderno y a explicar sus causas sin atribuirlas solo a la voluntad del rey.",
    prior=["Sé que cada actor tiene una perspectiva.", "Conozco los seis rasgos del Estado moderno.", "Sé que un hecho suele tener varias causas."],
    explain=[
        "La formación del Estado moderno no fue solo decisión de un rey. Influyeron causas como las guerras largas, que exigían dinero y soldados, y el comercio, que necesitaba seguridad y reglas iguales. Los reyes, además, tuvieron apoyo de grupos que querían orden, como algunos comerciantes de las ciudades.",
        "Cada actor miraba el proceso desde su posición. El rey buscaba funcionarios leales y un ejército propio. Un duque defendía sus antiguos poderes, porque perdía autonomía. Un comerciante podía ganar con caminos seguros. Un campesino veía subir los impuestos. Contrastar estas voces ayuda a entender que el cambio benefició a unos y perjudicó a otros.",
        "Una explicación multicausal combina esas causas y esas perspectivas. Atribuir todo a «un rey ambicioso» deja fuera las guerras, el comercio y el apoyo de ciertos grupos. Tampoco hay que olvidar que quienes pagaban impuestos tenían poca voz en las decisiones.",
    ],
    vocab=[("autonomía", "capacidad de decidir por uno mismo sin depender de otro"), ("lealtad", "fidelidad a una persona o institución"), ("impuesto", "dinero que se paga al Estado"), ("multicausal", "explicación que combina varias causas"), ("perspectiva", "punto de vista según la posición de cada actor")],
    worked=[
        ("Reconocer perspectivas", "En la ficha, ¿por qué el duque se opone a los funcionarios del rey?", ["Leo la voz 2.", "Dice que sus antepasados tenían soldados y tribunales propios."], "Porque pierde autonomía y poder"),
        ("Evitar una causa única", "Alguien dice: «El Estado moderno se formó solo porque los reyes eran ambiciosos». ¿Qué causas de la ficha faltan?", ["Busco las causas de los historiadores.", "Faltan guerras, comercio, leyes iguales y apoyo social."], "Las guerras, el comercio, las leyes iguales y el apoyo de grupos"),
    ],
    mistakes=[("Explicar el Estado moderno solo por el deseo de poder del rey.", "Se ignoran las guerras, el comercio y los grupos que apoyaron.", "Nombra varias causas y actores."),
              ("Creer que el Estado moderno benefició a todos igual.", "Se olvida la voz de los que pagaban impuestos.", "Contrasta al comerciante con el campesino.")],
    T=[
        ("{F} ¿Quién dice que prefiere un rey fuerte que mantenga los caminos seguros?", "El comerciante de la ciudad portuaria", "Es la voz 3."),
        ("{F} ¿Qué necesita el rey para pagar funcionarios y ejército, según su voz?", "Cobrar impuestos en todo el reino", "La voz 1 lo explica."),
        ("{F} ¿Qué perspectiva tiene el campesino sobre los impuestos?", "Cada año pagan más y no ve qué gana", "Es lo que dice la voz 4."),
        ("{F} ¿Qué voz defiende que los soldados deben obedecer al rey y no a los señores: la del rey o la del comerciante?", "La del rey", "La voz 1 lo dice con esas palabras."),
        ("{F} ¿Quién pierde más autonomía con el avance del Estado: el duque o el comerciante?", "El duque", "Perdía tribunales y soldados propios."),
        ("{F} ¿Qué causa de los historiadores explica la necesidad de mucho dinero? A) Las guerras largas y caras B) La difusión de la imprenta", "A) Las guerras largas y caras", "Las guerras exigían soldados y recursos."),
        ("{F} Clasifica cada voz como favorable o crítica del avance del Estado: a) rey, b) duque, c) comerciante.", "a) favorable; b) crítica; c) favorable", "El rey busca más poder, el duque lo pierde y el comerciante gana seguridad."),
        ("{F} Según las voces, ¿qué grupo tenía antes soldados y tribunales propios: los señores o los campesinos?", "Los señores", "El duque dice que sus antepasados los tenían."),
        ("{F} Un compañero dice: «Todos apoyaban al rey porque traía orden». ¿Qué voz lo contradice?", "La del duque o la del campesino", "El duque pierde poder y el campesino paga más."),
        ("{F} ¿Por qué se dice que el avance del Estado moderno no fue solo decisión del rey?", "Porque influyeron guerras, comercio y el apoyo de grupos que querían orden", "Hubo causas y actores además del rey."),
        ("{F} Una causa de la lista exige leyes iguales para todo el reino. ¿Qué rasgo del Estado moderno se relaciona con ella? A) Poder concentrado en el rey B) Expansión a otro continente", "A) Poder concentrado en el rey", "Leyes iguales requieren una autoridad central."),
        ("{F} ¿Qué voz falta en la ficha y sería importante escuchar?", "La de las mujeres o la de los artesanos de las ciudades", "La ficha no incluye a esos grupos."),
        ("{F} ¿Qué conclusión es proporcional a las cuatro voces? A) El Estado moderno benefició a algunos y perjudicó a otros B) Todos estuvieron de acuerdo", "A) El Estado moderno benefició a algunos y perjudicó a otros", "Las voces muestran intereses distintos."),
    ],
    ctx=("En un debate de curso, un grupo defiende al duque y otro al comerciante de la ficha. ¿Qué argumento principal daría cada uno? {F}", "El duque, que pierde su autonomía; el comerciante, que gana caminos seguros aunque pague impuestos", "Cada uno habla desde su interés."),
    sc=[("¿Qué es la autonomía?", "La capacidad de decidir sin depender de otro", "Se definió en el vocabulario."),
        ("¿Qué voz critica los impuestos crecientes?", "La del campesino", "La voz 4 lo dice."),
        ("¿Qué causa de la ficha se relaciona con el comercio? A) La necesidad de seguridad y leyes iguales B) La derrota de un reino", "A) La necesidad de seguridad y leyes iguales", "El comercio necesita reglas iguales y caminos seguros.")],
    op=("Escribe una carta de cinco a seis líneas del campesino al rey de la ficha. Debe incluir un dato de la voz 4, una pregunta y una frase de respeto que el campesino podría usar. Después anota en una línea qué perspectiva muestra la carta. {F}",
        "Majestad: cada año pagamos más impuestos. ¿Qué mejorará para nuestra aldea? Le saluda con respeto un campesino. Perspectiva: la de quien paga y no ve qué gana.",
        ["usa un dato de la voz 4", "incluye una pregunta", "identifica la perspectiva"], ["carta", "línea de perspectiva"], ["inventar hechos que contradicen la ficha", "olvidar la perspectiva"],
        "Pide que explique qué respondería el rey según su voz."),
    reinforce="Nombra una causa y una perspectiva distinta de la formación del Estado moderno.",
    extend="Escribe una pregunta que le harías al duque para saber si aceptó o resistió.",
)

# ---------------------------------------------------------------- clase 5
F = ("Ficha 5 (pregunta y evidencias de ejemplo). Pregunta: ¿tenía un rey moderno un poder absoluto, es decir, sin límites? "
     "Evidencia 1: un rey nombra funcionarios y cobra impuestos en todo el reino. "
     "Evidencia 2: los nobles conservan privilegios, como no pagar ciertos impuestos. "
     "Evidencia 3: cada reino conserva sus fueros. "
     "Evidencia 4: el rey no es elegido y no rinde cuentas a la población con votaciones. "
     "Evidencia 5: las órdenes tardan semanas en llegar a las ciudades lejanas y algunos corregidores no las cumplen.")
build(
    OA, 5, F,
    use="Aprenderé a construir un argumento sobre el alcance del poder del rey moderno, usando evidencias y reconociendo sus límites, sin confundirlo con una democracia actual.",
    prior=["Sé que un argumento tiene tesis, evidencias y límite.", "Conozco los rasgos del Estado moderno.", "Conozco los fueros y los privilegios de la nobleza."],
    explain=[
        "Un rey moderno concentró mucho poder, pero eso no significa que lo tuviera sin límites. Para argumentar hay que mirar evidencias a favor y en contra. A favor del poder: el rey nombra funcionarios y cobra impuestos en todo el reino. En contra de que fuera total: los nobles mantienen privilegios, los reinos conservan fueros y las órdenes se cumplen con lentitud o no se cumplen.",
        "También hay que evitar un error: pensar que el Estado moderno es lo mismo que una democracia. El rey no era elegido ni rendía cuentas con votaciones. La población era súbdita. La palabra «poder concentrado» describe una forma de gobierno, no un juicio sobre si era justa.",
        "Una buena tesis puede ser equilibrada: «El rey concentró poder, pero su poder fue limitado por privilegios, fueros y dificultades de comunicación». El límite del argumento reconoce que otras fuentes podrían mostrar casos distintos según el reino o la época.",
    ],
    vocab=[("poder absoluto", "poder sin límites ni control"), ("súbdito", "persona que obedece a un rey y no elige a su gobernante"), ("rendir cuentas", "explicar ante otros cómo se usó el poder"), ("privilegio", "ventaja de un grupo por ley o costumbre"), ("tesis", "respuesta que se defiende con evidencias")],
    worked=[
        ("Clasificar evidencias", "¿Qué evidencias de la ficha muestran que el poder del rey era limitado?", ["Busco datos que lo frenen.", "Evidencias 2, 3 y 5."], "Evidencias 2, 3 y 5"),
        ("Redactar un límite", "Tesis: «El rey concentró mucho poder». ¿Qué límite agregas?", ["Las evidencias hablan de reyes en general.", "Puede variar entre reinos y épocas."], "Las evidencias no prueban que fuera igual en todos los reinos"),
    ],
    mistakes=[("Decir que el rey moderno tenía poder total.", "Se ignoran privilegios, fueros y problemas de comunicación.", "Cita evidencias que muestren límites."),
              ("Decir que el Estado moderno era una democracia.", "Se confunde concentración de poder con participación ciudadana.", "Recuerda que el rey no era elegido ni rendía cuentas con votaciones.")],
    T=[
        ("{F} ¿Qué evidencia muestra la concentración del poder fiscal?", "La evidencia 1", "El rey cobra impuestos en todo el reino."),
        ("{F} ¿Qué evidencia indica que el rey no era elegido?", "La evidencia 4", "Dice que no es elegido ni rinde cuentas con votaciones."),
        ("{F} ¿Qué es un poder absoluto?", "Un poder sin límites ni control", "Así se definió en la clase."),
        ("{F} ¿Cuáles evidencias muestran límites al poder del rey?", "La 2, la 3 y la 5", "Privilegios de nobles, fueros y órdenes que tardan o no se cumplen."),
        ("{F} ¿Qué evidencia mezcla poder del rey con un límite práctico?", "La evidencia 5, porque las órdenes tardan semanas y a veces no se cumplen", "Muestra un poder que depende de la comunicación y la obediencia."),
        ("{F} ¿Qué tesis se apoya mejor en las evidencias? A) El rey concentró poder, pero no fue ilimitado B) El rey tenía poder absoluto sobre todo", "A) El rey concentró poder, pero no fue ilimitado", "Hay evidencias de poder y de límites."),
        ("{F} Un compañero dice: «Era una democracia porque había un gobierno único». ¿Qué evidencia lo contradice?", "La evidencia 4: el rey no es elegido ni rinde cuentas con votaciones", "La democracia exige elecciones y participación."),
        ("{F} Clasifica cada evidencia como poder o límite: a) 1, b) 2, c) 5.", "a) poder; b) límite; c) límite", "La evidencia 1 muestra control del rey; las otras muestran frenos."),
        ("{F} ¿Por qué las órdenes que tardan semanas debilitan la idea de poder absoluto?", "Porque el rey no podía controlar lo que pasaba lejos en el momento", "La comunicación lenta limita la obediencia efectiva."),
        ("{F} Escribe un límite honesto para la tesis «el rey concentró mucho poder».", "Las evidencias no muestran que fuera igual en todos los reinos o épocas", "Un argumento reconoce lo que no prueba."),
        ("{F} ¿Qué diferencia hay entre súbdito y ciudadano en el Estado moderno?", "El súbdito obedece al rey y no elige gobierno; el ciudadano actual participa con voto", "El Estado moderno no tenía votaciones."),
        ("{F} Un compañero cita solo las evidencias 1 y 4 y dice que el poder del rey era total. ¿Qué error comete?", "Ignora las evidencias 2, 3 y 5 que muestran límites", "Selecciona solo lo que apoya su idea."),
        ("{F} ¿Qué respuesta es más sólida? A) «Fue un poder fuerte pero limitado por privilegios, fueros y comunicación lenta» B) «Fue total porque era el rey»", "A) «Fue un poder fuerte pero limitado por privilegios, fueros y comunicación lenta»", "Cita evidencias concretas y reconoce límites."),
    ],
    ctx=("Para un panel de curso se pregunta: «¿Se parecía el Estado moderno a nuestra democracia?». Responde en una frase con una evidencia de la ficha. {F}", "No, porque el rey no era elegido ni rendía cuentas con votaciones", "Esa evidencia marca una diferencia clave."),
    sc=[("¿Qué es un súbdito?", "Una persona que obedece a un rey y no elige a su gobernante", "Se definió en el vocabulario."),
        ("¿Qué evidencia muestra privilegios de la nobleza?", "La evidencia 2", "Habla de que los nobles no pagan ciertos impuestos."),
        ("¿Qué partes tiene un argumento? A) Tesis, evidencias y límite B) Tesis y fechas únicamente", "A) Tesis, evidencias y límite", "Son las tres partes de un argumento.")],
    op=("Escribe un párrafo de seis líneas que responda a la pregunta de la ficha. Incluye tu tesis, dos evidencias numeradas (una que muestre poder y otra que muestre un límite) y una frase final de límite del argumento. {F}",
        "Pienso que el rey moderno concentró mucho poder, pero no era ilimitado. Evidencia 1: nombra funcionarios y cobra impuestos. Evidencia 3: cada reino conserva sus fueros. Límite: no sé si ocurría igual en todos los reinos.",
        ["tiene tesis clara", "cita una evidencia de poder y una de límite", "incluye límite del argumento"], ["párrafo"], ["no citar evidencia de límite", "afirmar que era una democracia"],
        "Pide que explique por qué su límite es necesario."),
    reinforce="Explica oralmente por qué el Estado moderno no es una democracia.",
    extend="Escribe una evidencia que buscarías para saber si los nobles pagaban impuestos o no.",
)
