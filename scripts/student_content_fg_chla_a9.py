"""Chile y la región latinoamericana 3.º/4.º medio FG: OA 05 clases 4 y 5 (relaciones y consecuencias ambientales; evaluación de acciones de los Estados) y OA 06 clase 1 (integración: conceptos y actores). Datos y países de ejemplo inventados."""
from __future__ import annotations

from fg_chla_common import build

O5 = "FG-CHLA-3y4-OAC-05"
O6 = "FG-CHLA-3y4-OAC-06"

# ============================================================ OA 05, clase 4
F = ("Ficha 4 (datos de ejemplo, inventados; país ficticio Costa Alta). Un año normal, la zona agrícola produce 100 toneladas de maíz y el kilo se vende a 10 u.m. "
     "En un año seco, con temperaturas más altas y menos lluvia, la producción baja a 70 toneladas y el kilo sube a 12 u.m. "
     "Los días con alerta de mala calidad del aire en la ciudad pasaron de 10 a 25 por año. Un incendio forestal destruyó parte de un bosque cercano. "
     "Los científicos de ejemplo señalan que el calentamiento se asocia a gases de efecto invernadero, que se emiten al quemar combustibles y al talar bosques.")
build(
    O5, 4, F,
    use="Aprenderé a explicar relaciones y consecuencias entre actividades humanas, cambio climático, agua, producción de alimentos y salud en Chile y América Latina.",
    explain=[
        'El cambio climático es el cambio de largo plazo del clima del planeta. Hoy se explica principalmente por actividades humanas que emiten gases de efecto invernadero, como quemar petróleo, carbón y gas, o talar bosques. Esos gases retienen calor y aumentan la temperatura media. Sus consecuencias pueden ser sequías, olas de calor, incendios más intensos, derretimiento de glaciares y cambios en las lluvias. No ocurren igual en todos los lugares: dependen de la geografía y de cómo se prepare cada sociedad.',
        'Los problemas ambientales se relacionan en cadena con la economía y la salud. Menos agua puede bajar la producción agrícola y subir los precios de los alimentos; la contaminación del aire puede aumentar las enfermedades respiratorias; perder bosques reduce la biodiversidad y la protección del suelo. Al explicar una cadena, conviene separar lo que muestran los datos de lo que es probable, y decir qué tan grande es el efecto. Una variación se mide con una resta y un porcentaje con una división.',
    ],
    vocab=[("cambio climático", "cambio de largo plazo del clima del planeta, explicado hoy sobre todo por actividades humanas"), ("gases de efecto invernadero", "gases que retienen calor en la atmósfera"), ("sequía", "período con falta de lluvia que afecta al agua disponible"), ("incendio forestal", "fuego que se propaga en un bosque o pastizal"), ("erosión", "pérdida de suelo por viento o agua")],
    worked=[
        ("Calcular una variación", "Una cosecha de ejemplo baja de 80 a 60 toneladas. ¿En cuántas toneladas y qué porcentaje?", ["Se resta: 80 − 60 = 20.", "20 sobre 80 es 25 %."], "20 toneladas, 25 %"),
        ("Seguir una cadena", "En una zona de ejemplo hay sequía, se produce menos trigo y el precio de la harina sube. ¿Qué consecuencia es probable en los hogares?", ["Si el precio sube, comprar la misma cantidad cuesta más.", "Los hogares con menos ingresos sufren más."], "Gastan más en alimentos; se ven más afectados los hogares con menos ingresos"),
    ],
    mistakes=[("Atribuir un solo hecho, como un incendio, al cambio climático sin datos.", "Cada hecho tiene varias causas, y el clima puede ser una de ellas.", "Distingue tendencias de largo plazo de eventos puntuales."),
              ("Creer que el cambio climático afecta igual a todos los lugares.", "Depende de la geografía y de la capacidad de adaptación.", "Describe el efecto en cada lugar con sus datos.")],
    T=[
        ('¿Qué es el cambio climático?', 'Un cambio de largo plazo del clima del planeta', 'Un cambio del tiempo de un solo día', 'Un cambio de estación del año', 'El cambio climático es de largo plazo; el tiempo diario o las estaciones son variaciones normales.'),
        ('¿Qué son los gases de efecto invernadero?', 'Gases que retienen calor en la atmósfera', 'Gases que enfrían el planeta cuando se acumulan', 'Gases que solo existen en el interior de los invernaderos', 'Esos gases retienen calor y contribuyen al calentamiento.'),
        ('¿Qué es la erosión del suelo?', 'La pérdida de suelo que arrastran el viento o el agua', 'El aumento de plantas en un terreno agrícola', 'La construcción de casas en terrenos con pendiente', 'La erosión desgasta el suelo; sin cobertura vegetal se acelera.'),
        ('=', '{F} ¿En cuántas toneladas bajó la producción de maíz en el año seco?', '100-70', 'Se resta la producción del año seco a la del año normal.', ' toneladas'),
        ('=', '{F} ¿Qué porcentaje bajó la producción de maíz en el año seco?', '(100-70)*100//100', 'Se divide la baja por la producción normal y se multiplica por 100.', ' %'),
        ('=', '{F} Un comprador necesita 50 kilos de maíz. ¿Cuánto más paga en el año seco que en el normal?', '50*12-50*10', 'Se calcula el costo con cada precio y se restan.', ' u.m.'),
        ('=', '{F} ¿Cuántos días más con alerta de mala calidad del aire hubo?', '25-10', 'Se resta el valor inicial al final.', ' días'),
        ('{F} ¿Qué cadena describe mejor lo que muestra la ficha sobre el maíz?', 'Más calor, menos lluvia, menos producción y mayor precio', 'Más lluvia, mayor producción y un precio más bajo', 'Menos calor, menor producción y un precio más alto', 'La ficha describe un año seco y caluroso, con menos producción y precio mayor.'),
        ('{F} ¿Qué actividad humana mencionan los científicos de ejemplo como fuente de gases de efecto invernadero?', 'Quemar combustibles y talar bosques', 'Plantar árboles en zonas desérticas', 'Medir la calidad del aire con estaciones', 'La ficha indica esas dos actividades como emisoras de gases.'),
        ('{F} Alguien dice: «El incendio forestal prueba por sí solo que hay cambio climático». ¿Qué corrección es más precisa?', 'Un evento puntual no prueba una tendencia de largo plazo', 'Es cierto, porque cada incendio forestal tiene como única causa el clima', 'Es falso, porque los incendios nunca se relacionan con el clima de la zona', 'El cambio climático se identifica con tendencias de muchos años; un incendio puede tener varias causas.'),
        ('{F} ¿A quiénes afecta más el alza del precio del maíz?', 'A los hogares con menos ingresos, que gastan más en alimentos', 'A los hogares con más ingresos, que compran lo mismo', 'A nadie, porque el precio no influye en el gasto', 'Un mismo aumento pesa más en quienes destinan mayor parte de sus ingresos a comer.'),
        ('{F} ¿Qué dato de la ficha relaciona la contaminación del aire con la salud?', 'Los días de alerta de aire pasaron de 10 a 25', 'La producción de maíz bajó de 100 a 70 toneladas al año', 'El kilo de maíz subió de 10 a 12 u.m. en el año seco', 'Las alertas por aire de mala calidad indican riesgo para la salud respiratoria.'),
        ('{F} Si el país quisiera reducir los riesgos de la sequía para la agricultura, ¿qué acción sería coherente?', 'Mejorar el riego y proteger las fuentes de agua', 'Aumentar la tala de bosques cercanos a la zona', 'Usar más agua cada año sin medir el caudal', 'Usar mejor el agua y proteger sus fuentes reduce la vulnerabilidad.'),
    ],
    ctx=('Un país de ejemplo pierde cada año parte de sus bosques cerca de un río. Llueve fuerte y el suelo se desliza hacia el río. ¿Qué relación se observa?', 'La pérdida de bosque aumenta la erosión del suelo', 'La pérdida de bosque aumenta la protección del suelo', 'La lluvia fuerte siempre mejora el suelo', 'Sin árboles que sujeten el suelo, la lluvia arrastra tierra: es erosión.'),
    sc=[
        ('En Chile y la región, ¿cómo se relaciona la sequía con los alimentos?', 'Menos agua puede bajar la producción y subir los precios', 'Es una relación de causa y consecuencia que depende de cada lugar.'),
        ('=', 'La producción de un cultivo de ejemplo baja de 200 a 150 toneladas. ¿En cuántas toneladas bajó?', '200-150', 'Se resta la producción final a la inicial.', ' toneladas'),
        ('¿Por qué un evento puntual no basta para hablar de cambio climático?', 'Porque el cambio climático se mide con tendencias de largo plazo', 'Hay que mirar muchos años de datos.'),
    ],
    op=("Usa la {F} Escribe una cadena de cinco eslabones desde las actividades que emiten gases de efecto invernadero hasta una consecuencia en los hogares. Incluye al menos una cifra de la ficha y marca con «probable» lo que no es seguro.",
        "Quemar combustibles y talar bosques emite gases de efecto invernadero → sube la temperatura → hay años más secos → la producción de maíz baja 30 % (de 100 a 70 toneladas) → el kilo sube a 12 u.m. y los hogares con menos ingresos gastan más (probable).",
        ["cinco eslabones", "usa una cifra de la ficha", "marca lo probable"], ["cadena de cinco eslabones"], ["afirmar certezas sin evidencia", "saltar eslabones"],
        "Pregunta qué dato nuevo comprobaría un eslabón."),
    rx=("Dibuja una cadena causal con tres eslabones sobre bosque, suelo y río.", "Pregunta a una persona de tu casa qué cambios en el clima ha notado en tu zona y anota una observación sin datos privados."),
)

# ============================================================ OA 05, clase 5
F = ("Ficha 5 (datos de ejemplo, inventados; país ficticio Costa Alta). Tres acciones posibles del Estado para avanzar en sustentabilidad. "
     "Acción A: ampliar las áreas protegidas; cuesta 300 millones de u.m. y protegería ecosistemas que absorben 100 toneladas de gases al año; efecto de largo plazo. "
     "Acción B: subsidiar el cambio de calefactores a leña por equipos menos contaminantes; cuesta 800 millones y evita 200 toneladas de emisiones al año; mejora la salud en invierno. "
     "Acción C: cobrar un impuesto a las emisiones de las grandes empresas; cuesta 100 millones de administración y reduciría 50 toneladas al año; los costos pueden pasar a los precios. "
     "Existe además un acuerdo internacional sobre cambio climático en el que el país se comprometió a reducir emisiones.")
build(
    O5, 5, F,
    use="Aprenderé a evaluar acciones que los Estados de la región emprenden para avanzar en sustentabilidad, con criterios de efecto ambiental, costo, plazo y equidad.",
    explain=[
        'Los Estados de América Latina emprenden distintas acciones para avanzar en sustentabilidad: crean y amplían áreas protegidas, fijan normas de calidad del aire y del agua, promueven las energías renovables, cobran impuestos a las emisiones, ofrecen subsidios y firman acuerdos internacionales sobre cambio climático y biodiversidad. Para evaluarlas se usan criterios: el efecto ambiental (cuánto reduce el problema), el costo, el plazo, la equidad (quién paga y quién se beneficia) y la capacidad de ser cumplida y fiscalizada.',
        'Un cálculo útil es el costo por unidad de efecto, por ejemplo, el costo por tonelada reducida o absorbida: costo total dividido por toneladas. Sirve para comparar, pero no decide por sí solo: una acción cara puede traer beneficios de salud o sociales que el número no recoge, y una barata puede cargar costos en las personas con menos ingresos. Por eso se evalúan varios criterios, se explican los supuestos y se considera a las comunidades afectadas. Los datos de esta ficha son de ejemplo.',
    ],
    vocab=[("acuerdo internacional", "compromiso entre países para actuar frente a un problema común"), ("subsidio", "ayuda económica del Estado para facilitar una acción"), ("impuesto a las emisiones", "pago que se cobra por cada cantidad de gases emitidos"), ("fiscalizar", "controlar que se cumpla una norma"), ("costo por tonelada", "costo total dividido por las toneladas reducidas")],
    worked=[
        ("Costo por tonelada", "Una acción de ejemplo cuesta 400 y reduce 80 toneladas. ¿Cuál es el costo por tonelada?", ["Se divide el costo total por las toneladas.", "400 ÷ 80 = 5."], "5"),
        ("Revisar quién paga", "Un impuesto de ejemplo a las emisiones puede subir el precio de la energía. ¿Qué efecto social hay que mirar?", ["Los hogares con menos ingresos gastan una parte mayor en energía.", "Se podría compensar con ayudas."], "Impacto en hogares con menos ingresos"),
    ],
    mistakes=[("Elegir la acción de menor costo sin mirar quién paga.", "Puede cargar los costos en personas con menos ingresos.", "Incluye la equidad entre los criterios."),
              ("Creer que un acuerdo internacional cumple solo el problema.", "Un acuerdo necesita acciones nacionales y fiscalización.", "Revisa si hay medidas concretas para cumplirlo.")],
    T=[
        ('¿Qué es un subsidio?', 'Una ayuda económica del Estado para facilitar algo', 'Un impuesto que se cobra a quien contamina más', 'Una multa por no cumplir una norma ambiental', 'El subsidio es una ayuda; el impuesto y la multa son cobros.'),
        ('¿Qué significa fiscalizar una norma?', 'Controlar que la norma se cumpla en la práctica', 'Escribir una nueva norma en una ley', 'Eliminar la norma porque es difícil de cumplir', 'Fiscalizar es controlar el cumplimiento de la norma.'),
        ('¿Qué es un impuesto a las emisiones?', 'Un pago que se cobra según los gases emitidos', 'Un pago que se entrega a quien planta árboles', 'Un pago que se cobra por entrar a un parque protegido', 'Cobra por emitir; busca desincentivar la contaminación.'),
        ('=', '{F} ¿Cuál es el costo por tonelada de la Acción A?', '300//100', 'Se divide el costo total por las toneladas.', ' millones de u.m.'),
        ('=', '{F} ¿Cuál es el costo por tonelada de la Acción B?', '800//200', 'Se divide el costo total por las toneladas.', ' millones de u.m.'),
        ('=', '{F} ¿Cuál es el costo por tonelada de la Acción C?', '100//50', 'Se divide el costo total por las toneladas.', ' millones de u.m.'),
        ('{F} Si solo se mira el costo por tonelada, ¿qué acción es la más barata?', 'La Acción C', 'La Acción A', 'La Acción B', 'C cuesta 2 por tonelada, A cuesta 3 y B cuesta 4.'),
        ('{F} ¿Qué beneficio adicional señala la ficha para la Acción B?', 'Mejora la salud de las personas en invierno', 'Aumenta las áreas protegidas', 'Genera ingresos para el Estado', 'La ficha indica que la Acción B mejora la salud en invierno.'),
        ('{F} ¿Qué riesgo social menciona la ficha para la Acción C?', 'Que los costos pasen a los precios', 'Que se cierren las grandes empresas', 'Que se pierdan áreas protegidas', 'El impuesto puede trasladarse a los precios que pagan los hogares.'),
        ('{F} Un funcionario dice: «La Acción C es la mejor, porque es la más barata». ¿Qué objeción es más sólida?', 'Reduce menos toneladas y puede afectar a hogares pobres', 'Es la que más cuesta por cada tonelada que logra reducir', 'No tiene ningún efecto sobre las emisiones de las empresas', 'Menor costo por tonelada no implica el mayor efecto ni el más equitativo.'),
        ('{F} ¿Qué acción da el mayor efecto ambiental anual según la ficha?', 'La Acción B, con 200 toneladas', 'La Acción A, con 100 toneladas', 'La Acción C, con 50 toneladas', 'B reduce 200 toneladas al año, más que A y C.'),
        ('{F} ¿Cómo podrían combinarse acciones para cumplir el acuerdo internacional y cuidar la equidad?', 'Combinar B y C, financiando el subsidio con el impuesto', 'Elegir solo la acción de menor costo sin otra medida', 'Esperar a que el acuerdo se cumpla solo', 'Una combinación puede ampliar el efecto y compensar a los hogares.'),
        ('{F} Antes de decidir, ¿qué dato nuevo aportaría más?', 'Quién paga y quién se beneficia con cada acción', 'El nombre del ministro que firmó el acuerdo internacional', 'La cantidad de reuniones que hubo sobre el tema en el último año', 'Los efectos distributivos permiten evaluar la equidad.'),
    ],
    ctx=('Una acción de ejemplo cuesta 600 y reduce 150 toneladas; otra cuesta 500 y reduce 100. ¿Cuál tiene menor costo por tonelada y cuánto es?', 'La primera, con 4 por tonelada', 'La segunda, con 5 por tonelada', 'La primera, con 6 por tonelada', 'Se calcula 600 ÷ 150 = 4 y 500 ÷ 100 = 5; la primera cuesta menos por tonelada.'),
    sc=[
        ('Nombra dos criterios para evaluar una acción ambiental del Estado.', 'Por ejemplo, el efecto ambiental y el costo', 'También sirven el plazo, la equidad y la capacidad de fiscalizar.'),
        ('=', 'Una acción de ejemplo cuesta 900 y reduce 300 toneladas. ¿Cuál es el costo por tonelada?', '900//300', 'Se divide el costo por las toneladas.', ' millones de u.m.'),
        ('¿Por qué un acuerdo internacional necesita acciones nacionales?', 'Porque los compromisos se cumplen con medidas concretas de cada país', 'Un acuerdo sin medidas ni fiscalización no reduce emisiones.'),
    ],
    op=("Usa la {F} Redacta una recomendación de seis líneas: qué acción o combinación elegirías, con su costo por tonelada; qué criterio pesó más; a quién podría afectar negativamente; cómo lo compensarías; y cómo se relaciona con el acuerdo internacional.",
        "Recomiendo combinar B y C. B cuesta 4 por tonelada y C cuesta 2. Pesó el efecto sobre la salud y la equidad. El impuesto podría afectar a hogares de menos ingresos si sube los precios. Usaría parte del impuesto para financiar el subsidio de B. Así el país avanza en el compromiso del acuerdo internacional de reducir emisiones.",
        ["calcula costos por tonelada", "reconoce a quién afecta", "relaciona con el acuerdo"], ["recomendación de seis líneas"], ["decidir solo por costo", "no mencionar la equidad"],
        "Pregunta cómo cambiaría tu decisión si el objetivo principal fuera proteger biodiversidad."),
    rx=("Calcula el costo por tonelada de dos acciones inventadas y compáralas.", "Averigua con tu docente si tu comuna tiene una norma ambiental local y cuál es."),
)

# ============================================================ OA 06, clase 1
F = ("Ficha 1 (países y organizaciones de ejemplo, inventados). Los países ficticios Alto Valle, Mar Claro y Sierra Verde forman un bloque llamado Unión del Sur. "
     "Acordaron que los productos que se venden entre ellos no pagan arancel (un impuesto a los productos importados) y que, a los de fuera del bloque, cobran un arancel común de 10 %. "
     "También firmaron un acuerdo de cooperación en salud para compartir vacunas e información, y uno de educación para reconocer títulos entre sus universidades. "
     "En la región existen organizaciones reales de integración, como Mercosur, la Comunidad Andina y la Alianza del Pacífico, y organismos como la CEPAL, que estudia temas económicos y sociales.")
build(
    O6, 1, F,
    use="Aprenderé a explicar qué son la integración y la cooperación entre Estados latinoamericanos, qué son los bloques económicos y qué acuerdos existen en economía, salud, educación, género y derechos humanos.",
    explain=[
        'La integración regional es el proceso por el cual los países de una región acuerdan trabajar juntos para lograr objetivos comunes. La cooperación internacional es la ayuda y la colaboración entre países u organismos en temas como economía, salud, educación, ciencia, género y derechos humanos. Un bloque económico es un grupo de países que acuerda reducir barreras al comercio entre ellos. Un arancel es un impuesto a los productos importados; en una zona de libre comercio los países bajan o eliminan los aranceles entre sí; en una unión aduanera, además, cobran un arancel común a los productos de países de fuera del bloque.',
        'En América Latina existen varios bloques y organismos regionales, como Mercosur, la Comunidad Andina y la Alianza del Pacífico, además de organismos como la CEPAL, que produce estudios y propuestas, y la Organización Panamericana de la Salud. También hay acuerdos y sistemas de protección de derechos humanos, de igualdad de género, de educación y de ciencia. Para analizarlos hay que ubicar actores (Estados, organismos), tiempo (cuándo se firmaron) y espacio (qué países participan), y reconocer que los objetivos no siempre se cumplen del todo. Los bloques de este cuaderno son ejemplos inventados.',
    ],
    vocab=[("integración regional", "proceso por el que países de una región acuerdan trabajar juntos"), ("bloque económico", "grupo de países que acuerda reducir barreras al comercio entre ellos"), ("arancel", "impuesto a los productos importados"), ("zona de libre comercio", "bloque en que los países eliminan o bajan los aranceles entre sí"), ("unión aduanera", "bloque que además cobra un arancel común a los países de fuera"), ("cooperación internacional", "colaboración entre países u organismos en temas de interés común")],
    worked=[
        ("Clasificar un acuerdo", "Tres países de ejemplo eliminan el arancel entre ellos, pero cada uno cobra el suyo a los de fuera. ¿Qué tipo de bloque es?", ["Eliminan aranceles entre sí.", "No tienen arancel común: es zona de libre comercio."], "Zona de libre comercio"),
        ("Calcular un arancel", "Un producto de ejemplo cuesta 200 u.m. y paga 10 % de arancel al entrar a un bloque. ¿Cuánto es el arancel?", ["10 % de 200 es 20.", "El arancel es el impuesto sobre el valor."], "20 u.m."),
    ],
    mistakes=[("Creer que un bloque económico solo trata de comercio.", "También hay cooperación en salud, educación, ciencia, género y derechos humanos.", "Revisa todos los ámbitos de los acuerdos."),
              ("Confundir zona de libre comercio con unión aduanera.", "En la unión aduanera hay arancel común hacia fuera.", "Pregunta si los países cobran un arancel común a los de fuera.")],
    T=[
        ('¿Qué es un arancel?', 'Un impuesto que se cobra a los productos importados', 'Un impuesto a los productos exportados', 'Un permiso para que una empresa venda en el país', 'Los aranceles se cobran a las importaciones; no son permisos.'),
        ('¿Qué es un bloque económico?', 'Un grupo de países que baja barreras al comercio entre ellos', 'Una organización que reúne solo a los países más grandes', 'Un acuerdo para que cada país produzca todo sin comerciar', 'Un bloque busca facilitar el comercio entre sus miembros.'),
        ('¿Qué es la cooperación internacional?', 'La colaboración entre países en temas de interés común', 'La decisión de un país de aislarse por completo del resto del mundo', 'La competencia entre países por vender más productos en otros mercados', 'Cooperar es colaborar, por ejemplo en salud o ciencia.'),
        ('{F} ¿Qué pagan los productos que se venden entre Alto Valle, Mar Claro y Sierra Verde?', 'No pagan arancel', 'Pagan 10 % de arancel', 'Pagan el doble del arancel común', 'La ficha dice que entre ellos no pagan arancel.'),
        ('{F} ¿Qué cobran a los productos de países de fuera del bloque?', 'Un arancel común de 10 %', 'Ningún arancel', 'Un arancel distinto en cada país', 'Cobran un arancel común de 10 %.'),
        ('=', '{F} Un producto de fuera del bloque cuesta 300 u.m. ¿Cuánto es el arancel al entrar a la Unión del Sur?', '300*10//100', 'Se calcula el 10 % del valor del producto.', ' u.m.'),
        ('{F} Por el arancel común, la Unión del Sur es un ejemplo de…', 'Unión aduanera, porque cobran arancel común hacia fuera', 'Zona de libre comercio sin arancel común', 'Un acuerdo solo de cooperación en salud', 'Eliminan aranceles entre sí y cobran un arancel común hacia fuera: unión aduanera.'),
        ('{F} ¿Qué tipo de cooperación incluye compartir vacunas e información?', 'Cooperación en salud', 'Cooperación en educación', 'Cooperación económica', 'La ficha menciona un acuerdo de cooperación en salud.'),
        ('{F} ¿Para qué sirve el acuerdo de educación entre las universidades?', 'Para reconocer los títulos universitarios entre los países', 'Para eliminar los aranceles entre los países del bloque', 'Para repartir vacunas entre los estudiantes', 'Reconocer títulos facilita estudiar y trabajar en otro país del bloque.'),
        ('{F} Alguien dice: «La Unión del Sur es solo un acuerdo comercial». ¿Qué corrección corresponde?', 'También incluye cooperación en salud y educación', 'Es correcto, porque los bloques solo comercian', 'Es incorrecto, porque no tiene acuerdo comercial', 'La ficha muestra acuerdos de salud y educación además del comercio.'),
        ('{F} ¿Qué ventaja puede tener para una empresa de Mar Claro vender a Sierra Verde en la Unión del Sur?', 'No paga arancel, lo que reduce el precio final', 'Debe pagar un arancel mayor que las empresas de fuera', 'Tiene prohibido vender en los demás países', 'Sin arancel, el producto llega más barato al país vecino.'),
        ('{F} ¿Qué dato de la ficha ayuda a ubicar espacio y actores de la integración en la región?', 'Que existen organizaciones como Mercosur y la Comunidad Andina', 'Que la Unión del Sur cobra aranceles a los productos de sus propios países miembros', 'Que la CEPAL fija los aranceles que cobra cada país de la región', 'La ficha nombra organizaciones de integración reales como parte del contexto regional.'),
        ('{F} Un estudiante afirma: «Si hay integración, los objetivos se cumplen siempre». ¿Qué respuesta es más prudente?', 'Pueden no cumplirse del todo; hay que revisar su aplicación', 'Es cierto, porque toda firma de un acuerdo garantiza su cumplimiento', 'Es falso, porque ningún acuerdo internacional se aplica jamás en la práctica', 'Hay que revisar si los compromisos se aplican y con qué resultados.'),
    ],
    ctx=('Dos países de ejemplo eliminan el arancel entre ellos y cada uno mantiene el suyo hacia el resto. ¿Qué tipo de acuerdo comercial es?', 'Una zona de libre comercio', 'Una unión aduanera', 'Un acuerdo solo de cooperación cultural', 'No hay arancel común hacia afuera, por lo que es una zona de libre comercio.'),
    sc=[
        ('En Chile y la región, ¿qué es la integración regional?', 'El proceso por el que países de una región acuerdan trabajar juntos', 'Incluye temas económicos y también sociales, de salud y de derechos.'),
        ('=', 'Un producto de ejemplo cuesta 500 u.m. y paga 10 % de arancel. ¿Cuánto es el arancel?', '500*10//100', 'Se calcula el 10 % del valor.', ' u.m.'),
        ('Nombra dos ámbitos de cooperación internacional distintos del comercio.', 'Por ejemplo, salud y educación', 'También hay cooperación en ciencia, género y derechos humanos.'),
    ],
    op=("Usa la {F} Escribe un cuadro con tres filas (comercio, salud, educación): qué acordaron los países de la Unión del Sur, quiénes se benefician y un límite o pregunta que habría que investigar.",
        "Comercio: sin arancel entre sí y 10 % hacia fuera; se benefician empresas exportadoras; pregunta: ¿suben los precios de los productos de fuera? Salud: comparten vacunas e información; se beneficia la población; pregunta: ¿llega a las zonas rurales? Educación: reconocen títulos; se benefician estudiantes y profesionales; pregunta: ¿se reconocen todos los títulos o solo algunos?",
        ["completa las tres filas", "identifica beneficiarios", "formula preguntas investigables"], ["cuadro de tres filas"], ["confundir tipos de bloque", "dar por cumplidos los acuerdos sin evidencia"],
        "Revisa que cada fila se apoye en la ficha."),
    rx=("Explica con tus palabras la diferencia entre zona de libre comercio y unión aduanera.", "Averigua con tu docente un acuerdo de cooperación de tu país con otros países de la región y anótalo."),
)
