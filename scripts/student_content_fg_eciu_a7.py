"""Educación Ciudadana 4.º medio FG: OA 05 (libertad, igualdad y solidaridad ante desafíos democráticos) y OA 06 (medios, tecnologías, participación y vida privada). Casos y cifras de ejemplo inventados."""
from __future__ import annotations

from fg_eciu_common import build

O5 = "FG-ECIU-4M-OAC-05"
O6 = "FG-ECIU-4M-OAC-06"

# ============================================================ OA 05, clase 1
F = ("Ficha 58 (casos de ejemplo): (1) Una familia con ingresos bajos no puede pagar transporte para que su hija asista al liceo. "
     "(2) En un taller de ejemplo, a las estudiantes se les asignan solo tareas de cuidado y a los estudiantes, tareas técnicas. "
     "(3) Un liceo no tiene rampa ni intérprete de lengua de señas para un estudiante sordo. "
     "(4) Una vecina de ejemplo, hablante de una lengua originaria, recibe burlas por su forma de hablar.")
build(
    O5, 1, F,
    use="Aprenderé a relacionar los conceptos de libertad, igualdad y solidaridad con desafíos como la desigualdad, la pobreza, la equidad de género, la inclusión y la diversidad.",
    prior=["Sé los principios de los derechos humanos.", "Sé qué es discriminar.", "Sé qué es la justicia social."],
    explain=[
        "La libertad es poder elegir y actuar sin coacciones injustas, pero también tener condiciones reales para hacerlo: una persona sin recursos ni acceso a educación tiene menos libertad efectiva. La igualdad es que todas las personas tengan la misma dignidad y derechos, igual trato ante la ley e igualdad de oportunidades. La solidaridad es la responsabilidad de apoyarnos y cuidarnos mutuamente, especialmente a quienes enfrentan mayores dificultades.",
        "Los desafíos de la democracia muestran cómo se relacionan estos conceptos. La pobreza y la desigualdad limitan la libertad real. La equidad de género busca que mujeres, hombres y personas de géneros diversos tengan las mismas oportunidades, sin estereotipos. La inclusión busca que personas con discapacidad u otras condiciones puedan participar plenamente. La diversidad étnica, cultural y sexual se respeta como parte de la igualdad de dignidad.",
        "La equidad significa dar a cada persona lo que necesita para estar en igualdad de condiciones; es distinta de dar a todos lo mismo. Por ejemplo, una rampa no da más a una persona, le permite entrar. Cuando se habla de pueblos originarios, sus propias comunidades y educadores tradicionales explican su cultura y su lengua.",
    ],
    vocab=[("libertad efectiva", "posibilidad real de elegir porque se cuenta con las condiciones para hacerlo"), ("equidad", "dar a cada persona lo que necesita para participar en igualdad de condiciones"), ("solidaridad", "responsabilidad mutua de apoyarnos, sobre todo a quienes tienen más dificultades"), ("estereotipo", "idea simplificada y rígida sobre un grupo de personas"), ("inclusión", "medidas para que todas las personas participen plenamente")],
    worked=[
        ("Igualdad y equidad", "En un liceo de ejemplo se entrega el mismo libro de letra pequeña a todos, pero un estudiante tiene baja visión. ¿Es equitativo?", ["Se da lo mismo a todos.", "No se considera lo que necesita."], "No; falta una adaptación"),
        ("Libertad efectiva", "Una joven de ejemplo quiere estudiar, pero no puede pagar el transporte. ¿Qué limita su libertad?", ["Falta de recursos.", "No cuenta con condiciones reales."], "La falta de recursos"),
    ],
    mistakes=[("Creer que igualdad es dar lo mismo a todos.", "Las personas tienen necesidades distintas.", "Pregunta qué necesita cada una para participar."),
              ("Pensar que la solidaridad es solo caridad.", "Es una responsabilidad compartida.", "Busca soluciones que cambien las condiciones.")],
    T=[
        ('abc', '¿Qué es la libertad efectiva?', 'Poder elegir y actuar teniendo condiciones reales para hacerlo, no solo permiso formal', 'Poder hacer lo que se quiera sin ninguna regla ni límite alguno', 'Tener un derecho escrito en la ley, aunque no pueda ejercerse en la práctica', 'La libertad real exige recursos y acceso, no solo que la ley la permita.'),
        ('abc', '¿Qué es la equidad?', 'Dar a cada persona lo que necesita para estar en igualdad de condiciones', 'Dar exactamente lo mismo a todas las personas, sin mirar su situación', 'Dar más a quienes ya tienen más oportunidades para que avancen', 'Equidad no es igualdad de trato idéntico, sino atender necesidades distintas.'),
        ('abc', '¿Qué es la solidaridad?', 'La responsabilidad mutua de apoyarnos, sobre todo a quienes enfrentan más dificultades', 'Ayudar solo a las personas que conocemos o que están cerca de nosotros', 'Entregar ayuda a cambio de algo, como un favor o un pago', 'La solidaridad es una responsabilidad compartida con quienes más lo necesitan.'),
        ('abc', '{F} ¿Qué desafío muestra el caso 1?', 'Pobreza, que limita la libertad efectiva de asistir al liceo', 'Falta de inclusión por una discapacidad que impide participar', 'Estereotipos de género en la asignación de las tareas', 'Sin recursos para transporte, la hija no puede ejercer su derecho a estudiar.'),
        ('abc', '{F} ¿Qué desafío muestra el caso 2?', 'Equidad de género y estereotipos en las tareas', 'Pobreza que limita el acceso al liceo', 'Falta de accesibilidad en el edificio del taller', 'Se asignan tareas según el género y no según intereses o habilidades.'),
        ('abc', '{F} ¿Qué desafío muestra el caso 3?', 'Inclusión: faltan condiciones para que participe plenamente', 'Pobreza: la familia no tiene recursos para pagar el transporte', 'Estereotipos de género en la asignación de las tareas', 'La falta de rampa e intérprete impide su participación en igualdad.'),
        ('abc', '{F} ¿Qué desafío muestra el caso 4?', 'Respeto a la diversidad cultural y lingüística', 'Pobreza y desigualdad de ingresos entre familias', 'Inclusión de personas con discapacidad en el liceo', 'Las burlas por su forma de hablar desconocen su cultura y su lengua.'),
        ('abc', '{F} ¿Qué sería equidad en el caso 3?', 'Proveer la rampa y el intérprete que el estudiante necesita para participar', 'Darle lo mismo que a los demás, sin cambios ni ajustes', 'Pedirle que asista solo a algunas clases en las que no haya barreras', 'La equidad atiende su necesidad para que participe en igualdad.'),
        ('abc', '{F} ¿Qué sería solidaridad en el caso 1?', 'Buscar apoyos para el transporte y cambiar las condiciones que limitan su asistencia', 'Dejar que la familia resuelva sola el problema del transporte', 'Ofrecer ayuda solo si la familia la pide con mucha gratitud', 'La solidaridad es responsabilidad mutua frente a quien enfrenta dificultades.'),
        ('abc', '{F} Un compañero dice: «Todos tienen los mismos derechos, así que no hay que hacer nada». ¿Qué corresponde?', 'Recordar que las condiciones reales importan para poder ejercer los derechos', 'Aceptarlo, porque la igualdad ante la ley basta para ejercerlos', 'Rechazarlo, porque en realidad los derechos no son iguales para todos', 'Sin condiciones, un derecho existe en el papel pero no se ejerce.'),
        ('abc', '{F} ¿Qué medida corrige el estereotipo del caso 2?', 'Rotar las tareas entre todas y todos según intereses y habilidades', 'Mantener la asignación porque ya funciona y nadie reclama', 'Asignar solo tareas técnicas a las estudiantes para equilibrar', 'Elimina la división de tareas por género.'),
        ('abc', '{F} ¿Qué relación hay entre la igualdad y la libertad efectiva?', 'Sin condiciones de igualdad, la libertad se ejerce menos', 'No tienen relación: la libertad es siempre plena', 'La igualdad reduce la libertad de elegir', 'La falta de recursos y oportunidades limita las elecciones reales.'),
        ('abc', 'Un estudiante con baja visión necesita letra más grande en las pruebas. ¿Qué concepto justifica ese ajuste?', 'Equidad, porque atiende su necesidad para estar en igualdad de condiciones', 'Privilegio, porque recibe una ventaja injusta frente a los demás', 'Estereotipo, porque supone que el estudiante no puede hacerlo', 'El ajuste le permite competir en las mismas condiciones, no le da una ventaja.'),
    ],
    ctx=('abc', 'Una vecina recibe burlas por hablar una lengua originaria. ¿Quién puede explicar esa lengua y su cultura?', 'Sus propias comunidades y educadores tradicionales', 'Cualquier persona que haya leído sobre el tema', 'Un compañero que quiera investigar', 'Son quienes conocen su cultura y su lengua.'),
    sc=[
        ('¿Qué es la inclusión?', 'Que personas con discapacidad u otras condiciones puedan participar plenamente', 'Busca eliminar las barreras que dejan a personas fuera.'),
        ('abc', '¿Qué es un estereotipo?', 'Una idea simplificada y rígida sobre un grupo de personas', 'Un dato comprobado con evidencia sobre un grupo', 'Una norma que fija una ley para un grupo', 'Generaliza sin considerar a cada persona.'),
        ('En Educación Ciudadana: ¿qué es la igualdad?', 'Que todas las personas tengan la misma dignidad y derechos', 'Incluye igual trato ante la ley e igualdad de oportunidades.'),
    ],
    op=("Con la {F} haz una tabla con los cuatro casos: concepto en juego (libertad, igualdad o solidaridad), desafío y una medida que sea equitativa. Escribe además una frase sobre cómo cambiaría el trato a una persona en tu liceo.",
        "Caso 1: libertad efectiva; pobreza; apoyo con transporte. Caso 2: igualdad; equidad de género; rotar tareas. Caso 3: igualdad e inclusión; rampa e intérprete. Caso 4: igualdad de dignidad; respeto a la diversidad; sancionar burlas y valorar las lenguas. Frase: invitaría a que todas y todos participen en las tareas.",
        ["relaciona concepto y desafío", "propone medida equitativa", "no estereotipa"], ["tabla de cuatro casos", "frase"], ["confundir igualdad con trato idéntico", "asignar tareas por género"],
        "Pregunta qué caso le resulta más cercano y por qué."),
    reinforce="Explica con tus palabras la diferencia entre igualdad y equidad.",
    extend="Anota una barrera para participar que veas en tu entorno y una forma de eliminarla.",
)

# ============================================================ OA 05, clase 2
F = ("Ficha 59 (caso de ejemplo): el programa ficticio «Camino Abierto» entrega ayuda económica y apoyo escolar a familias de bajos ingresos en una comuna. "
     "Datos de ejemplo: 500 familias reciben el programa; antes, 300 tenían a algún hijo o hija fuera del liceo por razones económicas; ahora 120. "
     "Una evaluación (de ejemplo) también muestra que 80 familias que necesitaban la ayuda no se enteraron. Fuentes: informe del programa, testimonio de una madre y nota de prensa.")
build(
    O5, 2, F,
    use="Aprenderé a investigar un caso de superación de la pobreza e inclusión, a calcular su alcance y a identificar a quiénes quedan fuera.",
    prior=["Sé qué son libertad, igualdad y solidaridad.", "Sé calcular diferencias y porcentajes.", "Sé interrogar fuentes."],
    explain=[
        "La pobreza es la carencia de recursos para cubrir necesidades básicas y desarrollar un proyecto de vida. Superarla requiere ingresos, pero también educación, salud, vivienda y oportunidades. Un programa social se evalúa por su alcance (a cuántos llega), su efecto (cuánto cambia la situación) y su equidad (si llega a quienes más lo necesitan).",
        "En el caso de ejemplo se calcula la diferencia entre antes y después: de 300 a 120 familias con hijos o hijas fuera del liceo. También se revisa quiénes quedan fuera: 80 familias que necesitaban la ayuda no se enteraron. Esto es un problema de acceso a la información y de inclusión.",
        "Las fuentes aportan distinto: el informe del programa da cifras; el testimonio muestra una experiencia; la nota informa. Se evita concluir que el programa «resolvió la pobreza»: reduce un problema específico. Se piden más datos, como el tiempo que permanecen en el liceo. Se respeta la dignidad de las familias y no se las expone.",
    ],
    vocab=[("pobreza", "carencia de recursos para cubrir necesidades básicas y desarrollar un proyecto de vida"), ("alcance", "cantidad de personas a las que llega un programa"), ("efecto", "cambio que produce un programa en la situación de las personas"), ("focalización", "dirigir una ayuda a quienes más la necesitan"), ("brecha de acceso", "diferencia entre quienes pueden y no pueden acceder a algo")],
    worked=[
        ("Calcular un cambio", "En un programa de ejemplo, 200 estudiantes faltaban por razones económicas y ahora son 50. ¿Cuántos menos?", ["Se resta 50 a 200.", "Son 150."], "150 estudiantes menos"),
        ("Brecha de acceso", "Una beca de ejemplo se difunde solo por internet. ¿A quiénes puede dejar fuera?", ["A quienes no tienen internet.", "Hay una brecha de acceso."], "A quienes no tienen internet"),
    ],
    mistakes=[("Concluir que el programa resolvió la pobreza.", "Solo mejora un aspecto.", "Habla del efecto en un aspecto específico."),
              ("No revisar a quienes quedan fuera.", "Se pierde la equidad.", "Calcula cuántos necesitaban y no accedieron.")],
    T=[
        ('abc', '¿Qué es la pobreza?', 'La carencia de recursos para cubrir necesidades básicas y desarrollar un proyecto de vida', 'La falta de ingresos de una persona durante un mes determinado', 'La situación de quienes no tienen trabajo ni estudios', 'La pobreza afecta varias dimensiones y no solo un ingreso momentáneo.'),
        ('abc', '¿Qué criterios se usan para evaluar un programa social?', 'Alcance, efecto y equidad', 'Costo, rapidez y publicidad', 'Popularidad, tamaño y antigüedad', 'Se mira a cuántos llega, cuánto cambia y si llega a quienes más lo necesitan.'),
        ('=', '{F} ¿Qué porcentaje de las 300 familias dejó de tener hijos o hijas fuera del liceo?', '(300-120)*100//300', 'Se compara la mejora (180 familias) con el valor inicial.', ' %'),
        ('=', '{F} ¿Qué porcentaje de las 500 familias del programa tiene todavía algún hijo o hija fuera del liceo?', '120*100//500', 'Se compara la parte con el total de familias.', ' %'),
        ('abc', '{F} ¿Qué problema muestra el dato de las 80 familias?', 'Una brecha de acceso a la información: la ayuda no les llegó', 'Un exceso de ayuda que recibieron algunas familias', 'Un problema de costos del programa para el municipio', 'Familias que necesitaban la ayuda quedaron fuera por no enterarse.'),
        ('abc', '{F} ¿Qué es el alcance del programa?', 'A cuántas familias llega', 'Cuánto cambia la situación de las familias', 'Si llega a quienes más lo necesitan', 'Mide la cobertura, no el cambio ni la equidad.'),
        ('abc', '{F} ¿Qué mide el efecto del programa?', 'Cuánto cambia la situación de las familias', 'A cuántas familias llega', 'Cuánto cuesta cada familia atendida', 'Compara la situación antes y después.'),
        ('abc', '{F} Alguien dice: «El programa resolvió la pobreza». ¿Qué corresponde?', 'Señalar que mejoró un aspecto específico, pero faltan datos sobre otros', 'Aceptarlo, porque bajó de 300 a 120 familias con jóvenes fuera', 'Rechazarlo, porque ningún programa social logra cambiar nada', 'Reduce un problema específico, sin resolver la pobreza en general.'),
        ('abc', '{F} ¿Qué medida reduce la brecha de acceso a la información?', 'Difundir el programa por varios medios, incluso en persona', 'Difundirlo solo en un sitio web que pueden leer pocas familias', 'Esperar a que las familias lo busquen por su cuenta', 'Varios canales alcanzan a más personas.'),
        ('abc', '{F} ¿Qué dato falta para evaluar mejor el efecto?', 'Cuánto tiempo permanecen los jóvenes en el liceo después de recibir la ayuda', 'Cómo se llama el director del liceo y desde cuándo trabaja', 'Qué opinan quienes no necesitan la ayuda sobre el programa', 'Muestra el efecto en el tiempo, no solo al inicio.'),
        ('abc', '{F} ¿Cómo se respeta la dignidad de las familias al comunicar el programa?', 'Sin exponer sus nombres ni su situación', 'Publicando una lista de familias beneficiadas', 'Contando casos reales con nombres, con autorización verbal', 'Se protege su privacidad y se evita estigmatizar.'),
        ('abc', 'Una beca de ejemplo se entrega por orden de llegada y los jóvenes de zonas rurales llegan tarde. ¿Qué principio falla?', 'Equidad, porque no considera la dificultad de acceso', 'Pluralismo, porque hay pocas opciones', 'Solidaridad, porque ayuda a todos por igual', 'Tratar igual a quienes parten con barreras distintas mantiene la desigualdad.'),
        ('abc', '{F} ¿Qué aporta el testimonio de una madre?', 'Una experiencia personal que ilustra, pero no mide el efecto en todas las familias', 'Cifras exactas del programa en toda la comuna', 'Un análisis de toda la situación del país', 'Un testimonio muestra una vivencia, no una medición.'),
    ],
    ctx=('abc', 'Un servicio se ofrece solo en el centro de la comuna y no llega a familias rurales. ¿Qué problema aparece?', 'Una brecha de acceso', 'Un exceso de cobertura', 'Un error de cálculo del efecto', 'La ayuda existe, pero no todas las personas pueden acceder a ella.'),
    sc=[
        ('abc', '¿Qué es la focalización?', 'Dirigir una ayuda a quienes más la necesitan', 'Repartir la ayuda sin criterio', 'Dar la ayuda solo a quien la pida', 'Se concentra en el grupo que más necesita.'),
        ('¿Qué es una brecha de acceso?', 'La diferencia entre quienes pueden y no pueden acceder a algo', 'Mide cuántas personas pueden acceder frente a cuántas quedan sin acceso.'),
        ('En un programa social, ¿qué es la equidad?', 'Que llegue a quienes más lo necesitan', 'Mira quién queda fuera y quién necesita más apoyo.'),
    ],
    op=("Con la {F} escribe un informe de cinco puntos: efecto del programa en números, alcance, quiénes quedan fuera, una medida para llegar a ellos y una conclusión prudente. Respeta la dignidad de las familias.",
        "Efecto: 180 familias menos con hijos fuera del liceo. Alcance: 500 familias. Fuera: 80 que no se enteraron. Medida: difusión en persona y en el liceo. Conclusión: el programa mejora un aspecto y se debe ampliar su difusión.",
        ["calcula bien", "identifica brecha", "conclusión prudente"], ["informe de cinco puntos"], ["decir que resolvió la pobreza", "exponer a familias"],
        "Pregunta qué otro dato pediría."),
    reinforce="Calcula la diferencia entre 400 y 150 y explica qué significa en un programa.",
    extend="Anota una ayuda social que conozcas y cómo se informa a las personas.",
)

# ============================================================ OA 05, clase 3
F = ("Ficha 60 (perspectivas de ejemplo sobre ayudas sociales en un país ficticio). "
     "Perspectiva 1: «Las ayudas deben ir solo a quienes más las necesitan (focalizadas), para usar bien los recursos». "
     "Perspectiva 2: «Las ayudas deben ser para todas las personas (universales), para que nadie quede fuera por errores de selección». "
     "Perspectiva 3: «Conviene un sistema mixto: base para todos y apoyo adicional a quienes más lo necesitan». "
     "Dato de ejemplo: de 1.000 familias elegibles, un sistema focalizado deja fuera por error a 100; un sistema universal cuesta el doble.")
build(
    O5, 3, F,
    use="Aprenderé a contrastar posturas sobre cómo aplicar la igualdad y la solidaridad en políticas sociales, con ventajas, costos y valores en juego.",
    prior=["Sé qué es la equidad y la solidaridad.", "Sé comparar perspectivas.", "Sé calcular proporciones."],
    explain=[
        "Una ayuda universal se entrega a todas las personas que cumplen un criterio amplio (por ejemplo, todas las familias con hijos). Una ayuda focalizada se entrega solo a quienes cumplen un criterio más estricto, como bajos ingresos. Ambas buscan la justicia social, pero priorizan valores diferentes: la universalidad destaca la igualdad de derechos y la facilidad de acceso; la focalización destaca el uso eficiente de los recursos.",
        "Cada enfoque tiene riesgos. La focalización puede dejar fuera por error a quienes necesitan la ayuda y puede estigmatizar. La universalidad puede costar más y entregar ayuda a quienes no la necesitan. Un enfoque mixto intenta equilibrar. Para decidir se examinan datos como el porcentaje de error y el costo, y se discute qué riesgos son más aceptables.",
        "Estas posturas no pertenecen a un partido ni son «correctas» o «incorrectas» por sí solas: expresan valores. Una discusión cuidadosa presenta cada postura con sus mejores argumentos y evita caricaturas como «quiere quitar ayudas» o «quiere gastar sin control».",
    ],
    vocab=[("ayuda universal", "ayuda que se entrega a todas las personas que cumplen un criterio amplio"), ("ayuda focalizada", "ayuda dirigida a quienes cumplen un criterio estricto, como bajos ingresos"), ("error de exclusión", "dejar fuera a alguien que sí necesitaba la ayuda"), ("estigmatizar", "marcar a una persona o grupo de manera negativa"), ("sistema mixto", "sistema que combina ayuda universal y focalizada")],
    worked=[
        ("Calcular exclusión", "De 200 familias elegibles de ejemplo, un sistema deja fuera por error a 20. ¿Qué porcentaje es?", ["20 entre 200 son 10 de cada 100.", "Es el 10 %."], "10 %"),
        ("Clasificar", "Una ayuda de ejemplo se entrega a todas las familias con hijos pequeños. ¿Es universal o focalizada?", ["Su criterio es amplio.", "Es universal."], "Universal"),
    ],
    mistakes=[("Pensar que focalizar siempre es más justo.", "Puede dejar fuera por error.", "Revisa el error de exclusión."),
              ("Caricaturizar al otro enfoque.", "Se ignora su valor.", "Explica su mejor argumento.")],
    T=[
        ('abc', '¿Qué es una ayuda universal?', 'Una que se entrega a todas las personas que cumplen un criterio amplio', 'Una que se entrega solo a quienes tienen los ingresos más bajos', 'Una que se entrega solo a quienes la piden en una oficina', 'Lo universal se define por un criterio amplio, no por el ingreso.'),
        ('abc', '¿Qué es una ayuda focalizada?', 'Una que se entrega solo a quienes cumplen un criterio estricto, como bajos ingresos', 'Una que se entrega a todas las personas sin excepción', 'Una que se entrega por sorteo entre las familias postulantes', 'La focalización dirige la ayuda a un grupo más acotado.'),
        ('=', '{F} ¿Cuántas familias elegibles quedan cubiertas en el sistema focalizado?', '1000-100', 'Se resta las excluidas al total de elegibles.', ' familias'),
        ('=', '{F} ¿Qué porcentaje de las familias elegibles queda excluido por error en el sistema focalizado?', '100*100//1000', 'Se compara la parte excluida con el total.', ' %'),
        ('=', '{F} Si el sistema focalizado cuesta 500 millones de pesos, ¿cuánto cuesta el universal?', '500*2', 'El dato dice que el universal cuesta el doble.', ' millones'),
        ('abc', '{F} ¿Qué valor defiende la perspectiva 1?', 'El uso eficiente de los recursos', 'Que nadie quede fuera por errores', 'La igualdad de trato sin importar el ingreso', 'Dirige la ayuda a quienes más la necesitan para usar bien los recursos.'),
        ('abc', '{F} ¿Qué valor defiende la perspectiva 2?', 'Que nadie quede fuera por errores de selección', 'El uso eficiente de los recursos del Estado', 'La reducción del presupuesto de las ayudas', 'Su razón es evitar el error de exclusión.'),
        ('abc', '{F} ¿Qué propone la perspectiva 3?', 'Una base para todos y un apoyo adicional para quienes más lo necesitan', 'Eliminar la ayuda focalizada y dejar solo una ayuda universal', 'Entregar la ayuda solo a quienes la soliciten por escrito', 'Es el sistema mixto que busca equilibrar ambos valores.'),
        ('abc', '{F} ¿Qué riesgo tiene el sistema focalizado?', 'Dejar fuera por error a quienes la necesitan y estigmatizar', 'Costar el doble que el sistema universal en la prueba', 'Entregar ayuda a quienes no la necesitan de verdad', 'Según el dato, deja fuera por error a 100 de 1.000 familias.'),
        ('abc', '{F} ¿Qué riesgo tiene el sistema universal?', 'Costar más y entregar ayuda a quienes no la necesitan', 'Dejar fuera por error a muchas familias que sí la necesitan', 'Estigmatizar a quienes la reciben ante sus vecinos', 'Según el dato, cuesta el doble.'),
        ('abc', '{F} Alguien dice: «El enfoque 1 quiere quitar ayudas». ¿Qué error comete?', 'Una caricatura: deforma lo que propone la perspectiva 1', 'Un dato verificable que se puede comprobar en la ficha', 'Un argumento con evidencia que responde a la objeción', 'La perspectiva 1 busca usar bien los recursos, no quitar ayudas.'),
        ('abc', '{F} ¿Qué dato falta para decidir mejor?', 'Cuánto aumentaría el presupuesto y qué otras necesidades quedarían sin atender', 'El nombre del ministerio que administra las ayudas', 'Cuántas personas opinan en redes sociales sobre el tema', 'Aporta el costo de oportunidad de elegir un sistema.'),
        ('abc', '{F} ¿Qué medida reduce el error de exclusión en un sistema focalizado?', 'Difusión amplia y un procedimiento de reclamo para quienes quedaron fuera', 'Pedir más requisitos para postular a la ayuda', 'Reducir el plazo de postulación para ordenar el sistema', 'Facilita el acceso y corrige exclusiones.'),
    ],
    ctx=('abc', 'Una escuela de ejemplo ofrece almuerzo gratuito a todos los estudiantes. ¿Qué tipo de ayuda es?', 'Universal', 'Focalizada', 'Ninguna, porque no es dinero', 'Se entrega a todas las personas del grupo, sin criterio de ingreso.'),
    sc=[
        ('abc', '¿Qué es un error de exclusión?', 'Dejar fuera a alguien que sí necesitaba la ayuda', 'Dar ayuda de más a alguien que no la necesitaba', 'Cobrar por una ayuda gratuita', 'Es el riesgo principal de la focalización.'),
        ('abc', '¿Qué es estigmatizar?', 'Marcar a una persona o grupo de manera negativa', 'Ayudar a un grupo con prioridad por su situación', 'Registrar los datos de una persona en un listado', 'Puede ocurrir cuando solo ciertas personas reciben una ayuda.'),
        ('¿Qué es un sistema mixto?', 'Uno que combina una base para todos con apoyo adicional focalizado', 'Busca equilibrar el acceso de todos con el apoyo extra a quienes más lo necesitan.'),
    ],
    op=("Con la {F} haz una tabla con las tres perspectivas: valor, ventaja y riesgo. Escribe luego una propuesta mixta de cuatro líneas que reduzca el error de exclusión y cuide los recursos, sin tomar partido.",
        "Perspectiva 1: eficiencia; ahorra recursos; riesgo de excluir. Perspectiva 2: universalidad; no excluye; cuesta más. Perspectiva 3: equilibrio; combina; requiere diseño. Propuesta: base universal pequeña, apoyo extra por necesidad y difusión amplia con revisión de reclamos.",
        ["identifica valores", "reconoce riesgos", "propone sin partido"], ["tabla", "propuesta de cuatro líneas"], ["caricaturizar", "tomar partido"],
        "Pregunta qué valor le parece más importante."),
    reinforce="Explica con tus palabras la diferencia entre ayuda universal y focalizada.",
    extend="Anota un beneficio escolar y si es universal o focalizado.",
)

# ============================================================ OA 05, clase 4
F = ("Ficha 61 (tema de deliberación de ejemplo): el centro de estudiantes ficticio del liceo Las Vertientes debate si exigir que su directiva tenga al menos 3 de 6 cargos para cada género (paridad), para promover la equidad de género. "
     "A favor: asegura que haya voces diversas. En contra: podría limitar la libertad de votar por quien se prefiera. "
     "Dato de ejemplo: en los últimos años, en 3 elecciones de 4, la directiva tuvo 5 hombres y 1 mujer. Alternativa: capacitación y apoyo para postular, sin exigencia.")
build(
    O5, 4, F,
    use="Aprenderé a deliberar sobre medidas que promueven la igualdad y la inclusión, equilibrando libertad, igualdad y solidaridad, con razones y evidencia.",
    prior=["Sé qué es la equidad de género.", "Sé estructurar un argumento.", "Sé leer datos simples."],
    explain=[
        "Las medidas de acción afirmativa buscan corregir desigualdades de oportunidades. Una exigencia de paridad asegura una representación mínima de cada género; una alternativa es capacitar y apoyar a quienes tienen menos oportunidades de postular. Ambas buscan equidad, pero con medios distintos.",
        "Al deliberar se pesan los valores: la igualdad (que todas las personas tengan oportunidades reales), la libertad (que cada votante elija) y la solidaridad (apoyar a quienes enfrentan barreras). Un dato como «3 de 4 elecciones» muestra una tendencia, pero no explica la causa. Es útil preguntar por qué hay menos postulantes mujeres y si existen barreras.",
        "Una propuesta sólida combina medidas: apoyo, difusión, revisión de barreras y, si es necesario, una exigencia temporal con evaluación. Se escuchan todas las voces con respeto, se evita atribuir intenciones y se reconoce el valor de las posturas diferentes. Cualquier medida se acompaña de indicadores y de un plazo de revisión.",
    ],
    vocab=[("acción afirmativa", "medida temporal para corregir desigualdades de oportunidades"), ("paridad", "igual número de cargos para cada género"), ("barrera", "obstáculo que dificulta la participación de ciertas personas"), ("representación", "presencia de distintos grupos en las instancias de decisión"), ("medida temporal", "medida que se aplica por un tiempo determinado y se evalúa")],
    worked=[
        ("Leer una tendencia", "En 4 elecciones de ejemplo, 3 tuvieron mayoría de hombres. ¿Qué parte es?", ["3 de 4.", "Tres cuartas partes."], "Tres cuartas partes"),
        ("Medida temporal", "Un liceo de ejemplo aplica una cuota por dos años y luego evalúa. ¿Qué tipo de medida es?", ["Se aplica por un tiempo.", "Es temporal."], "Temporal"),
    ],
    mistakes=[("Atribuir mala intención a quienes votaron.", "No hay evidencia de intención.", "Pregunta por las barreras."),
              ("Decidir sin evaluar la medida después.", "No se sabe si funciona.", "Define indicadores y plazo.")],
    T=[
        ('abc', '¿Qué es una acción afirmativa?', 'Una medida temporal para corregir desigualdades de oportunidades', 'Una norma permanente que da ventajas a un grupo para siempre', 'Una campaña de publicidad para promover la igualdad', 'Busca corregir desigualdades y se acompaña de evaluación y plazo.'),
        ('abc', '¿Qué es la paridad?', 'Igual número de cargos para cada género', 'Un voto doble para las minorías', 'Una lista con un solo género', 'Equilibra el número de cargos entre géneros.'),
        ('=', '{F} En 3 de las 4 últimas elecciones la directiva tuvo 5 hombres y 1 mujer. ¿Qué porcentaje de las elecciones fue?', '3*100//4', 'Se compara la parte con el total de elecciones.', ' %'),
        ('=', '{F} Con paridad, ¿qué porcentaje de los 6 cargos corresponde a cada género?', '3*100//6', 'Se compara los cargos de un género con el total.', ' %'),
        ('abc', '{F} ¿Qué ventaja menciona la ficha para la paridad?', 'Asegura que haya voces diversas', 'Aumenta la libertad de elegir', 'Reduce el número de postulantes', 'Es el argumento a favor que registra la ficha.'),
        ('abc', '{F} ¿Qué objeción menciona la ficha?', 'Podría limitar la libertad de votar por quien se prefiera', 'Reduce la participación de las mujeres en la directiva', 'Cuesta mucho dinero y no hay presupuesto para aplicarla', 'Es la objeción registrada en la ficha.'),
        ('abc', '{F} ¿Qué valor defiende la paridad?', 'Igualdad de oportunidades y de representación', 'Libertad de elegir a cualquier candidato sin límites', 'Ahorro de recursos en la elección de la directiva', 'Busca que todas las personas tengan oportunidades reales.'),
        ('abc', '{F} ¿Qué valor defiende la objeción?', 'Libertad de elegir', 'Igualdad de representación', 'Solidaridad', 'Se centra en el voto libre.'),
        ('abc', '{F} ¿Qué dato falta para entender la causa de la tendencia?', 'Cuántas mujeres postularon y qué barreras enfrentaron', 'Cuántos estudiantes asisten al liceo', 'Cuántos años tiene el centro de estudiantes', 'Explica si falta de postulantes o barreras causan la tendencia.'),
        ('abc', '{F} ¿Qué propuesta combinada es más sólida?', 'Apoyo y difusión para postular, y una exigencia temporal evaluada', 'No hacer ninguna acción hasta que cambie la situación', 'Una exigencia permanente sin ninguna evaluación posterior', 'Combina medios y revisión del efecto.'),
        ('abc', '{F} Alguien dice: «Si pocos votan por mujeres, es porque no quieren». ¿Qué corresponde?', 'Pedir evidencia, pues podrían existir barreras', 'Aceptarlo, porque el voto muestra la voluntad', 'Rechazarlo, porque nunca hay preferencia por género', 'No se atribuye intención sin datos.'),
        ('abc', '{F} ¿Qué indicador mostraría el efecto de la medida?', 'Cantidad de postulantes de cada género y composición de la directiva', 'Cantidad de afiches pegados sobre la medida en el liceo', 'Cantidad de reuniones realizadas por la directiva', 'Mide el resultado de la medida y no solo actividades.'),
        ('abc', '{F} ¿Qué haces si una compañera recibe burlas por postular?', 'Apoyarla y avisar a una persona adulta de confianza', 'Reírte para no ser blanco de las burlas de otros', 'Pedirle que no postule para evitar problemas', 'Se protege a la persona y se pide ayuda.'),
    ],
    ctx=('abc', 'Un liceo establece que los grupos de trabajo tengan integrantes de ambos géneros. ¿Qué busca?', 'Representación y diversidad de voces', 'Reducir el tamaño de los grupos', 'Evitar que las personas trabajen con amigos', 'Es el objetivo de la medida.'),
    sc=[
        ('¿Qué es una medida temporal?', 'Una medida que se aplica por un plazo y se evalúa para decidir si continúa', 'Evita que una acción afirmativa se vuelva permanente sin revisión.'),
        ('abc', '¿Qué es una barrera?', 'Un obstáculo que dificulta la participación', 'Una norma que protege la participación', 'Un cargo en la directiva', 'Impide que ciertas personas participen en igualdad.'),
        ('¿Qué es la representación en una directiva?', 'Que las distintas personas y grupos estén presentes en la toma de decisiones', 'Se relaciona con la paridad y la diversidad.'),
    ],
    op=("Con la {F} escribe una propuesta de siete líneas: tu postura o combinación, un argumento con el dato, una objeción, tu respuesta, una medida de apoyo, un indicador y un plazo de revisión.",
        "Propongo apoyo para postular y una exigencia temporal de paridad con revisión. Argumento: en 3 de 4 elecciones la directiva fue casi masculina. Objeción: limita la libertad de voto. Respuesta: se limita por un tiempo y se evalúa. Apoyo: talleres de liderazgo. Indicador: postulantes y composición. Revisión: en dos años.",
        ["usa el dato", "responde objeción", "incluye indicador y plazo"], ["propuesta de siete líneas"], ["atribuir intenciones", "no fijar plazo"],
        "Pregunta cómo escucharía a quienes no están de acuerdo."),
    reinforce="Explica por qué una medida temporal debe evaluarse.",
    extend="Observa quiénes participan en las instancias de tu liceo y qué barreras podría haber.",
)

# ============================================================ OA 05, clase 5
F = ("Ficha 62 (diagnóstico de ejemplo en el liceo ficticio Rayén): en una encuesta a 100 estudiantes, 40 dicen haber visto burlas por origen, acento o apariencia; "
     "25 creen que su liceo no tiene formas de participar para estudiantes con discapacidad; 60 conocen poco las lenguas y culturas originarias. "
     "Recursos: 14 voluntarios, 4 semanas, apoyo de dos docentes. Idea: una «semana de la inclusión y la diversidad» con actividades seguras, invitados y exposición de trabajos. Las costumbres y lenguas de pueblos originarios las presentan sus propias comunidades o educadores tradicionales.")
build(
    O5, 5, F,
    use="Aprenderé a diseñar una acción escolar que promueva la inclusión y el respeto a la diversidad con libertad, igualdad y solidaridad.",
    prior=["Sé qué es la inclusión y la equidad.", "Sé diseñar una acción con indicador.", "Sé cuidar la privacidad."],
    explain=[
        "Una semana de la inclusión y la diversidad es una acción colectiva que informa, sensibiliza y propone cambios concretos. Parte de un diagnóstico (burlas, falta de formas de participar, desconocimiento de culturas) y define objetivos: reducir burlas, abrir formas de participar y conocer mejor las culturas. Cada objetivo tiene un indicador.",
        "El diseño incluye actividades seguras: exposiciones, charlas con invitados, juegos cooperativos, revisión de barreras en el liceo. Para temas de pueblos originarios, no se inventan costumbres ni palabras: se invita a sus comunidades o educadores tradicionales. Se evita exponer a personas concretas: se usan casos ficticios y se pide consentimiento para cualquier testimonio.",
        "También se prevén riesgos: que una actividad incomode o excluya a alguien, o que se reproduzcan estereotipos. Se define cómo se actuará (por ejemplo, avisar a una persona adulta de confianza ante burlas o acoso) y cómo se evaluará el resultado con una encuesta final. Los resultados se comunican con honestidad y se proponen mejoras.",
    ],
    vocab=[("sensibilizar", "ayudar a que las personas tomen conciencia de un tema"), ("consentimiento", "autorización libre de una persona para usar su testimonio"), ("juego cooperativo", "juego en que se gana colaborando"), ("barrera arquitectónica", "obstáculo físico que dificulta el acceso"), ("educador tradicional", "persona de una comunidad que enseña su cultura y lengua")],
    worked=[
        ("Objetivo medible", "En un liceo de ejemplo, 30 de 100 dicen haber visto burlas y se quiere bajar a 15. ¿Cuánto debe disminuir?", ["Se resta 15 a 30.", "Son 15."], "15 estudiantes"),
        ("Respetar la privacidad", "Un grupo de ejemplo quiere mostrar la historia de una compañera. ¿Qué hace?", ["Pide su consentimiento.", "O usa un caso ficticio."], "Pedir consentimiento o usar un caso ficticio"),
    ],
    mistakes=[("Inventar costumbres o palabras de un pueblo originario.", "Se deforma una cultura.", "Invita a sus comunidades o educadores tradicionales."),
              ("Exponer a una compañera como ejemplo.", "Se vulnera su privacidad.", "Usa casos ficticios o pide consentimiento.")],
    T=[
        ('abc', '¿Qué significa sensibilizar?', 'Ayudar a que las personas tomen conciencia de un tema', 'Obligar a que las personas cambien de opinión', 'Informar solo a quienes ya conocen el tema', 'Busca comprensión y empatía, no imposición.'),
        ('=', '{F} Si el objetivo es bajar las burlas observadas de 40 a 20, ¿en qué porcentaje se reducirían?', '(40-20)*100//40', 'Se compara la reducción con el valor inicial.', ' %'),
        ('=', '{F} Si cada una de 4 actividades necesita 3 voluntarios, ¿cuántos de los 14 voluntarios quedan libres?', '14-4*3', 'Se calcula cuántos se necesitan y se resta del total.', ' voluntarios'),
        ('abc', '{F} ¿Quién presenta las costumbres de un pueblo originario?', 'Sus propias comunidades o educadores tradicionales', 'Cualquier persona que haya investigado en internet', 'Un grupo de estudiantes que dramatice sus costumbres', 'Ellos conocen su cultura; no se inventan costumbres ni palabras.'),
        ('abc', '{F} ¿Qué actividad es segura?', 'Una exposición y un juego cooperativo', 'Una competencia con riesgo físico', 'Un debate en que se apunta a compañeros concretos', 'No hay riesgos físicos ni exposición de personas.'),
        ('abc', '{F} ¿Qué indicador mide la reducción de burlas?', 'Estudiantes que reportan haber visto burlas en la encuesta final', 'Afiches pegados en el diario mural y en los pasillos', 'Asistentes a las charlas durante la semana', 'Mide el resultado frente al punto de partida.'),
        ('abc', '{F} ¿Qué es el consentimiento?', 'La autorización libre de una persona para usar su testimonio', 'Una orden de una autoridad para que se use un testimonio', 'Un permiso del curso para publicar cualquier testimonio', 'Protege la privacidad y la decisión de cada persona.'),
        ('abc', '{F} ¿Qué hace un estudiante que presencia burlas durante la semana?', 'Apoyar a la persona y avisar a una persona adulta de confianza', 'Reírse para integrarse al grupo y no quedar afuera', 'Grabar la escena para subirla a redes sociales', 'Se protege a quien sufre y se busca ayuda adecuada.'),
        ('abc', '{F} ¿Qué actividad responde al problema de participación?', 'Revisar barreras y abrir formas de participar para estudiantes con discapacidad', 'Pedir a esos estudiantes que se adapten a las condiciones actuales', 'Ignorar el dato, porque son pocos los afectados', 'Responde al dato de 25 estudiantes que no ven formas de participar.'),
        ('abc', '{F} Si la encuesta final muestra pocos cambios, ¿qué corresponde?', 'Revisar qué falló y ajustar', 'Cancelar la iniciativa', 'Declarar un éxito total', 'Se aprende de la evaluación para mejorar.'),
        ('abc', 'Un curso organiza una feria de comidas del mundo. ¿Qué cuidado es necesario?', 'Evitar estereotipos y pedir ayuda a personas que conozcan cada cultura', 'Inventar las costumbres para que la feria sea más atractiva', 'Presentar una sola cultura como representativa de todas', 'Se respeta la cultura sin deformarla.'),
        ('abc', '{F} ¿Qué riesgo debe prever el equipo?', 'Que una actividad incomode o excluya a alguien, o reproduzca estereotipos', 'Que haya demasiados invitados y falte espacio en el liceo', 'Que las exposiciones sean muy largas para el público', 'Una acción sobre diversidad también puede dañar si se diseña sin cuidado.'),
        ('abc', '{F} ¿Qué medida responde a que 60 estudiantes conocen poco las culturas originarias?', 'Invitar a comunidades o educadores tradicionales para que presenten su cultura', 'Presentar trabajos hechos solo con información de internet', 'Dramatizar costumbres que los estudiantes imaginan', 'Las propias comunidades explican su cultura.'),
    ],
    ctx=('abc', 'Un liceo quiere hacer un mural sobre diversidad. ¿Cómo evitar exponer a personas concretas?', 'Usar casos ficticios y pedir consentimiento para cualquier testimonio', 'Pintar rostros reales de compañeros sin avisarles ni pedir permiso', 'Escribir sus nombres y su situación personal en el mural', 'Se protege la privacidad y la decisión de las personas.'),
    sc=[
        ('En Educación Ciudadana: ¿Qué es un juego cooperativo?', 'Un juego en que se gana colaborando', 'En un juego cooperativo todos dependen de todos, lo que fomenta la solidaridad.'),
        ('abc', '¿Qué es un educador tradicional?', 'Una persona de una comunidad que enseña su cultura y lengua', 'Cualquier docente de historia que haya estudiado el tema', 'Un investigador externo que visita el liceo', 'Es quien transmite los saberes de su comunidad.'),
        ('¿Qué es una barrera arquitectónica?', 'Un obstáculo físico en un edificio, como escaleras sin rampa', 'Limita la participación de personas con discapacidad.'),
    ],
    op=("Con la {F} diseña la semana: objetivo medible, tres actividades, roles para 14 voluntarios, a quién invitarías para presentar culturas, un cuidado de privacidad, un indicador y qué harías ante una situación de burlas.",
        "Objetivo: bajar de 40 a 20 los estudiantes que ven burlas. Actividades: exposición, juego cooperativo, revisión de barreras. Roles: 5 por actividad y 4 de apoyo. Invitados: educadores tradicionales. Privacidad: casos ficticios. Indicador: encuesta final. Ante burlas: apoyar y avisar a un adulto de confianza.",
        ["objetivo medible", "respeta culturas y privacidad", "incluye aviso a un adulto"], ["diseño de la semana"], ["inventar costumbres", "exponer a una persona"],
        "Pregunta cómo seguirían después de la semana."),
    reinforce="Escribe tres normas para una semana de la diversidad.",
    extend="Averigua con una persona adulta qué comunidades originarias o migrantes hay cerca de tu comuna.",
)

# ============================================================ OA 06, clase 1
F = ("Ficha 63 (situaciones de ejemplo): (1) Un diario digital de ejemplo publica el debate de un concejo municipal en directo. (2) Una cuenta anónima difunde un rumor falso sobre una candidata a delegada. "
     "(3) Una aplicación municipal pide el nombre, el rut y la ubicación de la persona que reclama por un bache. (4) Un grupo de estudiantes organiza una campaña por redes y consigue 500 firmas.")
build(
    O6, 1, F,
    use="Aprenderé qué son los medios de comunicación masiva y las nuevas tecnologías de la información, qué oportunidades y riesgos tienen para la democracia y cómo se protege la vida privada.",
    prior=["Sé qué es participar.", "Sé qué es una fuente.", "Sé qué es un dato personal."],
    explain=[
        "Los medios de comunicación masiva (prensa, radio, televisión y medios digitales) y las redes sociales difunden información a muchas personas. Las tecnologías de la información y la comunicación (TIC) incluyen internet, aplicaciones y redes. Son importantes para la democracia porque permiten informarse, debatir, organizarse y vigilar al poder.",
        "Ofrecen oportunidades: acceso rápido a información, transparencia (por ejemplo, transmitir debates públicos), participación y organización de campañas. También tienen riesgos: desinformación (información falsa o engañosa), noticias falsas que se viralizan, burbujas informativas donde solo se ve lo que ya se cree, ciberacoso, concentración de la propiedad de medios y recolección excesiva de datos personales.",
        "La vida privada es el ámbito de la persona que merece protección: sus datos, su imagen, sus mensajes. Un dato personal solo debe pedirse si es necesario y con consentimiento. Para cuidarse: verificar fuentes, no difundir rumores, no compartir información íntima de otros y avisar a una persona adulta de confianza ante acoso o amenazas.",
    ],
    vocab=[("medio de comunicación masiva", "canal que difunde información a muchas personas, como prensa, radio, televisión o medios digitales"), ("desinformación", "información falsa o engañosa que se difunde"), ("burbuja informativa", "situación en que solo se recibe información que coincide con lo que ya se cree"), ("dato personal", "información que identifica a una persona"), ("consentimiento", "autorización libre para usar información propia")],
    worked=[
        ("Clasificar una oportunidad", "Un canal de ejemplo transmite en directo una sesión del municipio. ¿Qué oportunidad es?", ["Muestra lo que hacen las autoridades.", "Es transparencia."], "Transparencia"),
        ("Clasificar un riesgo", "Una cuenta de ejemplo difunde una noticia falsa para desprestigiar a alguien. ¿Qué riesgo es?", ["Es información falsa.", "Es desinformación."], "Desinformación"),
    ],
    mistakes=[("Compartir una noticia sin verificarla porque «ya la tiene mucha gente».", "Que sea viral no la hace verdadera.", "Revisa la fuente antes de compartir."),
              ("Entregar datos personales sin preguntar para qué se usarán.", "Se pierde el control de la información.", "Pide el motivo y el consentimiento.")],
    T=[
        ('abc', '¿Qué son los medios de comunicación masiva?', 'Canales que difunden información a muchas personas, como prensa, radio y medios digitales', 'Conversaciones privadas entre dos personas por mensajería', 'Sistemas que solo almacenan datos sin difundir información', 'Se distinguen por llegar a muchas personas a la vez.'),
        ('abc', '{F} ¿Qué oportunidad muestra el caso 1?', 'Transparencia: se pueden ver las decisiones públicas', 'Desinformación: se difunde información falsa', 'Concentración de medios en pocas manos', 'Transmitir un debate permite que la ciudadanía vigile las decisiones.'),
        ('abc', '{F} ¿Qué riesgo muestra el caso 2?', 'Desinformación', 'Transparencia', 'Participación', 'Un rumor falso puede dañar la honra de una persona.'),
        ('abc', '{F} ¿Qué oportunidad muestra el caso 4?', 'Organización y participación', 'Pérdida de privacidad', 'Desinformación', 'Reunir firmas es una forma de participar y organizarse.'),
        ('abc', '{F} ¿Qué riesgo puede tener el caso 3?', 'Recolección excesiva de datos personales', 'Falta de campaña para difundir el reclamo', 'Exceso de transparencia en las decisiones', 'Se piden datos que quizás no son necesarios para reclamar por un bache.'),
        ('abc', '¿Qué es la desinformación?', 'Información falsa o engañosa que se difunde', 'Una opinión con la que no estamos de acuerdo', 'Una noticia que todavía no se ha publicado', 'Engaña a las personas, aunque se presente como noticia.'),
        ('abc', '¿Qué es una burbuja informativa?', 'Recibir solo información que coincide con lo que ya se cree', 'Un buscador que muestra todos los resultados sin filtrar', 'Una red social con pocos usuarios registrados', 'La persona ve solo lo que ya cree, lo que limita la diversidad de información.'),
        ('abc', '{F} ¿Qué haces antes de compartir el rumor del caso 2?', 'Verificar quién lo dice y con qué evidencia', 'Compartirlo rápido para advertir a los demás', 'Comentar que parece verdad', 'Comprobar la fuente antes de compartir evita difundir falsedades.'),
        ('abc', '{F} ¿Qué pregunta conviene hacer a la aplicación del caso 3?', '¿Para qué necesitan estos datos y quién los verá?', '¿Cuántas personas ya la descargaron en la comuna?', '¿Cuánto tarda en cargar la aplicación en el teléfono?', 'Protege la vida privada al exigir que el dato sea necesario.'),
        ('abc', '{F} Alguien dice: «Si algo circula en redes es verdad». ¿Qué corresponde?', 'Aclarar que ser viral no prueba que sea verdad', 'Aceptarlo, porque muchas personas no se equivocarían', 'Rechazarlo, porque nada de lo que circula en redes es verdad', 'Viral no es sinónimo de verdadero.'),
        ('abc', '{F} ¿Qué haces si recibes mensajes de acoso por redes?', 'Guardar la evidencia, no responder y avisar a una persona adulta de confianza', 'Responder con ofensas para que dejen de escribirte', 'Borrar los mensajes y no contárselo a nadie', 'Se busca ayuda y se conservan pruebas.'),
        ('abc', '{F} Un grupo difunde una foto de una compañera sin su permiso. ¿Qué derecho se vulnera?', 'La vida privada y la imagen', 'La libertad de culto', 'La libertad de reunión', 'No hubo consentimiento para usar su imagen.'),
        ('abc', '¿Qué es un dato personal?', 'Información que identifica a una persona, como nombre, rut o ubicación', 'Cualquier información que publica un medio de comunicación', 'Información que ya es pública para todos en internet', 'Debe pedirse solo si es necesario y con consentimiento.'),
    ],
    ctx=('abc', 'Una página muestra a una persona solo las noticias que coinciden con lo que ya piensa. ¿Qué riesgo es?', 'Burbuja informativa, por ver solo lo que ya se cree', 'Transparencia, por mostrar las decisiones públicas', 'Ciberacoso, por mensajes ofensivos hacia una persona', 'Limita el acceso a información distinta.'),
    sc=[
        ('¿Qué es la vida privada?', 'El ámbito de la persona que merece protección: sus datos, su imagen y sus mensajes', 'Se protege frente a medios y tecnologías.'),
        ('abc', '¿Qué es el consentimiento?', 'La autorización libre para usar información propia', 'Un trámite obligatorio que se completa una sola vez', 'Una orden de una autoridad para entregar datos', 'Es la base del respeto a la vida privada.'),
        ('En Educación Ciudadana: ¿Qué son las TIC?', 'Las tecnologías de la información y la comunicación: internet, aplicaciones y redes', 'Estas tecnologías permiten informarse, debatir, organizarse y vigilar al poder.'),
    ],
    op=("Con la {F} haz una tabla de cuatro filas (una por situación): oportunidad o riesgo, derecho o valor involucrado y una acción responsable. Agrega una frase sobre qué harías si recibes una imagen íntima de alguien: no la guardas ni la reenvías, no borras el chat y avisas a una persona adulta de confianza.",
        "Caso 1: oportunidad; transparencia; compartir con fuente. Caso 2: riesgo; honra; verificar y no difundir. Caso 3: riesgo; privacidad; preguntar para qué se usan los datos. Caso 4: oportunidad; participación; firmar y difundir con datos veraces. Imagen íntima: no la guardo ni la reenvío, no borro el chat y aviso a un adulto de confianza.",
        ["clasifica oportunidades y riesgos", "relaciona con derechos", "incluye el protocolo de seguridad"], ["tabla de cuatro filas", "frase de seguridad"], ["reenviar la imagen", "borrar el chat"],
        "Pregunta cómo verificaría una noticia antes de compartirla."),
    reinforce="Escribe tres oportunidades y tres riesgos de las redes sociales para la democracia.",
    extend="Observa una noticia que veas hoy y anota qué fuente la respalda.",
)

# ============================================================ OA 06, clase 2
F = ("Ficha 64 (caso de ejemplo): en la ciudad ficticia de Puerto Luz circula un mensaje: «El municipio cerrará todas las escuelas públicas el próximo año». "
     "Fuentes: (1) el mensaje, sin autor; (2) un comunicado del municipio que dice que se cierra una escuela con 25 estudiantes y se traslada a una escuela vecina; (3) una nota de un diario local que cita el comunicado; (4) un video con comentarios que dicen que es verdad. "
     "Datos de ejemplo: la ciudad tiene 20 escuelas públicas.")
build(
    O6, 2, F,
    use="Aprenderé a investigar un caso de desinformación: verificar fuentes, comparar versiones y comunicar con responsabilidad.",
    prior=["Sé qué es la desinformación.", "Sé interrogar fuentes.", "Sé calcular partes de un total."],
    explain=[
        "Verificar una información significa comprobar quién la dice, con qué fuente, cuándo y con qué evidencia. Un mensaje sin autor ni fuente es una señal de alerta. Un comunicado oficial es una fuente primaria, es decir, proviene directamente de quien decide. Una nota de prensa que cita el comunicado es una fuente secundaria.",
        "Se comparan versiones: el mensaje dice «todas las escuelas», pero el comunicado dice «una escuela» con 25 estudiantes. La diferencia es grande. Se calcula la proporción: 1 de 20 escuelas es el 5 %. Los comentarios de un video no son evidencia; solo muestran lo que algunas personas piensan. Un titular exagerado puede apelar a emociones para ser compartido.",
        "Después de verificar, se comunica con responsabilidad: se corrige con fuentes, se evita ridiculizar a quien compartió el rumor y se explica por qué es falso o impreciso. Si el rumor daña la honra de alguien, se avisa a una persona adulta de confianza. La democracia necesita ciudadanos que verifiquen antes de difundir.",
    ],
    vocab=[("fuente primaria", "documento o testimonio que proviene directamente de quien decide o vivió el hecho"), ("fuente secundaria", "fuente que comenta o resume otra fuente"), ("verificar", "comprobar quién dice algo, con qué fuente y con qué evidencia"), ("señal de alerta", "indicio de que una información puede ser falsa"), ("apelar a las emociones", "intentar convencer provocando miedo o enojo en vez de dar evidencia")],
    worked=[
        ("Calcular una proporción", "Se cierra 1 de 10 escuelas de ejemplo. ¿Qué porcentaje es?", ["1 de 10 es una décima parte.", "Es el 10 %."], "10 %"),
        ("Fuente primaria", "Un comunicado del hospital de ejemplo, publicado por el propio hospital, ¿qué tipo de fuente es?", ["Proviene de quien decide.", "Es primaria."], "Primaria"),
    ],
    mistakes=[("Creer una información porque muchos comentan que es verdad.", "Los comentarios no son evidencia.", "Busca la fuente primaria."),
              ("Ridiculizar a quien compartió un rumor.", "Daña la convivencia y no corrige.", "Explica con fuentes y con respeto.")],
    T=[
        ('abc', '¿Qué significa verificar una información?', 'Comprobar quién la dice, con qué fuente, cuándo y con qué evidencia', 'Compartirla con quienes confían en nosotros para que la verifiquen', 'Buscar a otras personas que opinen igual que nosotros', 'Verificar es contrastar, no buscar coincidencias.'),
        ('abc', '¿Qué es una fuente primaria?', 'La que proviene directamente de quien decide o vivió el hecho', 'La que repite lo que dijo otra fuente en su propio texto', 'La que tiene más comentarios y reacciones en redes', 'Una fuente primaria está más cerca del hecho.'),
        ('abc', '{F} ¿Qué tipo de fuente es cada una?', 'El comunicado es primaria y la nota del diario es secundaria', 'El comunicado es secundaria y la nota del diario es primaria', 'Ambas son fuentes primarias', 'El comunicado viene de quien decide; la nota lo cita.'),
        ('=', '{F} ¿Qué porcentaje de las 20 escuelas públicas se cierra?', '1*100//20', 'Se compara una escuela con el total de veinte.', ' %'),
        ('=', '{F} ¿Cuántas escuelas seguirían funcionando?', '20-1', 'Se resta la escuela que se cierra al total.', ' escuelas'),
        ('abc', '{F} ¿Qué señal de alerta tiene el mensaje original?', 'No tiene autor ni fuente', 'Es muy corto', 'Menciona al municipio', 'Un mensaje sin autor no permite saber quién se hace responsable.'),
        ('abc', '{F} ¿Por qué los comentarios del video no son evidencia?', 'Muestran lo que piensan algunas personas, no un hecho comprobado', 'Porque son demasiado largos para leerlos todos', 'Porque están en un video y no en un texto escrito', 'Opinar que algo es verdad no lo prueba.'),
        ('abc', '{F} ¿Qué diferencia hay entre el mensaje y el comunicado?', 'El mensaje dice que se cierran todas las escuelas; el comunicado, una con 25 estudiantes', 'El mensaje habla de una escuela; el comunicado de todas las escuelas', 'No hay diferencia, solo cambia el estilo del lenguaje', 'La diferencia entre «todas» y «una» es grande.'),
        ('abc', '{F} ¿Qué conclusión es más ajustada?', 'El mensaje exagera lo que dice el comunicado', 'El mensaje es verdadero', 'El comunicado oculta una decisión mayor', 'Los datos oficiales no respaldan la afirmación del mensaje.'),
        ('abc', '{F} ¿Qué acción es responsable?', 'Compartir el comunicado como respuesta al rumor', 'Compartir el rumor con una advertencia', 'Ignorarlo sin decir nada', 'Corrige con una fuente en lugar de ampliar la falsedad.'),
        ('abc', '{F} Un compañero compartió el rumor sin mala intención. ¿Qué haces?', 'Explicarle con fuentes y con respeto', 'Burlarte de él en el grupo de mensajería', 'Bloquearlo sin explicarle el motivo', 'Corrige sin dañar a la persona.'),
        ('abc', '{F} ¿Qué dato falta para entender el efecto del traslado de los 25 estudiantes?', 'A qué escuela vecina irían y cómo llegarían', 'Cuántos años tiene el municipio', 'Cuántos comentarios tiene el video', 'Aclara el impacto real de la decisión sobre las familias.'),
        ('abc', 'Un mensaje dice: «¡URGENTE! ¡Comparte antes de que lo borren!». ¿Qué señal de alerta tiene?', 'Apela a la urgencia y a las emociones para que se comparta sin verificar', 'Es demasiado corto para contener una noticia verdadera', 'Usa mayúsculas, lo que prueba que es completamente falso', 'Busca que se difunda antes de que alguien lo revise.'),
    ],
    ctx=('abc', 'Un titular dice «¡Escándalo total!» y no entrega datos. ¿Qué señal de alerta tiene?', 'Apela a las emociones en vez de entregar evidencia', 'Es breve y no tiene datos que lo respalden', 'Tiene fecha de publicación y lugar de origen', 'Un titular exagerado puede inducir a compartir sin comprobar.'),
    sc=[
        ('En Educación Ciudadana: ¿Qué es una señal de alerta?', 'Un indicio de que una información puede ser falsa', 'Invita a verificar antes de difundir.'),
        ('abc', '¿Qué es una fuente secundaria?', 'Una que comenta o cita lo que dijo otra fuente', 'Una que proviene directamente de quien decide', 'Una que no tiene autor', 'Una nota que cita un comunicado es secundaria.'),
        ('¿Qué significa apelar a las emociones?', 'Usar sentimientos como miedo o rabia para que se comparta sin pensar', 'Es una táctica frecuente de la desinformación.'),
    ],
    op=("Con la {F} escribe un informe de cinco puntos: mensaje, qué dice la fuente primaria, qué proporción es, por qué los comentarios no son evidencia y cómo responderías al grupo que compartió el rumor.",
        "Mensaje: cierre de todas las escuelas. Fuente primaria: el comunicado dice una escuela con 25 estudiantes. Proporción: 5 %. Los comentarios no son evidencia. Respuesta: compartiría el comunicado y explicaría con respeto.",
        ["compara versiones", "calcula la proporción", "responde con respeto"], ["informe de cinco puntos"], ["compartir el rumor", "ridiculizar"],
        "Pregunta qué otro dato verificaría."),
    reinforce="Explica con un ejemplo la diferencia entre fuente primaria y secundaria.",
    extend="Elige un mensaje que hayas recibido y anota si tenía autor, fecha y fuente.",
)

# ============================================================ OA 06, clase 3
F = ("Ficha 65 (perspectivas de ejemplo sobre moderar contenido en redes). "
     "Perspectiva 1 (periodista): «Las plataformas deben retirar rápido la desinformación peligrosa». "
     "Perspectiva 2 (defensora de la libertad de expresión): «Retirar contenido sin reglas claras puede censurar opiniones legítimas». "
     "Perspectiva 3 (investigador): «Hay que combinar reglas transparentes, verificación de datos y educación en medios». "
     "Dato de ejemplo: en una prueba, de 100 mensajes retirados por un sistema automático, 20 fueron retirados por error.")
build(
    O6, 3, F,
    use="Aprenderé a contrastar posturas sobre el rol de los medios y las plataformas en la democracia, equilibrando libertad de expresión, protección frente a la desinformación y vida privada.",
    prior=["Sé qué es la desinformación.", "Sé que la libertad de expresión tiene límites.", "Sé comparar perspectivas."],
    explain=[
        "Los medios y las plataformas digitales cumplen un papel central en el debate público. Se les pide que informen con veracidad y que respeten derechos. Al mismo tiempo, las decisiones de retirar contenidos pueden afectar la libertad de expresión. El desafío es proteger a las personas de la desinformación y el acoso sin censurar opiniones legítimas.",
        "Las posturas destacan valores distintos: la rapidez para evitar daños, la libertad para opinar, la transparencia de las reglas y la educación de las personas usuarias. Un dato, como «20 errores en 100 retiros», muestra que los sistemas automáticos pueden equivocarse, por lo que se necesitan procedimientos de reclamo y revisión humana.",
        "Contrastar implica identificar el valor y la evidencia de cada postura, distinguir entre opiniones y desinformación peligrosa, y proponer medidas combinadas: reglas públicas, apelación, etiquetas de verificación, protección de datos y alfabetización mediática. Se evita presentar el tema como «censura o libertad total».",
    ],
    vocab=[("moderación de contenido", "decisión de retirar, limitar o etiquetar contenidos en una plataforma"), ("censura", "prohibición arbitraria de expresar una opinión"), ("alfabetización mediática", "capacidad de analizar críticamente los medios y la información"), ("apelación", "posibilidad de reclamar y pedir revisión de una decisión"), ("etiqueta de verificación", "aviso que indica que un dato fue comprobado o es dudoso")],
    worked=[
        ("Calcular errores", "Un sistema de ejemplo retira 50 mensajes y 5 fueron por error. ¿Qué porcentaje es?", ["5 entre 50 es una décima parte.", "Es el 10 %."], "10 %"),
        ("Medida combinada", "¿Qué medida protege contra la desinformación sin censurar: etiquetar un dato dudoso o borrar toda opinión crítica?", ["Etiquetar informa y deja opinar.", "Borrar toda crítica es censura."], "Etiquetar un dato dudoso"),
    ],
    mistakes=[("Pensar que moderar contenido siempre es censura.", "Retirar acoso o amenazas protege derechos.", "Distingue opinión de daño."),
              ("Pensar que no hace falta ninguna regla.", "Se facilitaría la desinformación y el acoso.", "Busca reglas claras y transparentes.")],
    T=[
        ('abc', '¿Qué es la moderación de contenido?', 'Revisar y retirar contenidos de una plataforma según sus reglas', 'Prohibir toda opinión crítica que aparezca en la plataforma', 'Elegir qué personas pueden registrarse en la plataforma', 'Es la aplicación de reglas sobre lo que se publica.'),
        ('abc', '¿Qué es la censura?', 'La prohibición arbitraria de expresar una opinión', 'Retirar una amenaza según reglas públicas', 'Pedir pruebas antes de publicar', 'La palabra clave es arbitraria: sin reglas claras ni razones.'),
        ('=', '{F} ¿Cuántos mensajes fueron retirados correctamente?', '100-20', 'Se resta los errores al total de retirados.', ' mensajes'),
        ('=', '{F} Si el sistema retira 5.000 mensajes con el mismo porcentaje de error, ¿cuántos retiros serían erróneos?', '5000*20//100', 'Se aplica la proporción de error al nuevo total.', ' mensajes'),
        ('abc', '{F} ¿Qué valor defiende el periodista?', 'La rapidez para evitar los daños de la desinformación', 'La libertad total de expresión sin ninguna restricción', 'La transparencia de las reglas de la plataforma', 'Pide retirar rápido la desinformación peligrosa.'),
        ('abc', '{F} ¿Qué valor defiende la defensora de la libertad de expresión?', 'La libertad de expresión, con reglas claras', 'La rapidez de los retiros de contenido', 'El uso de sistemas automáticos de retiro', 'Teme que retirar sin reglas censure opiniones legítimas.'),
        ('abc', '{F} ¿Qué combina el investigador?', 'Reglas transparentes, verificación de datos y educación en medios', 'Solo retirar contenidos más rápido para evitar daños', 'Solo educar a los usuarios, sin ninguna regla', 'Es su propuesta de combinar medidas.'),
        ('abc', '{F} ¿Qué muestra el dato de 20 errores en 100 retiros?', 'Que los sistemas automáticos pueden equivocarse', 'Que la mayoría de los retiros son injustos', 'Que los retiros nunca se equivocan', '20 de 100 es una parte, no la mayoría, pero es un error relevante.'),
        ('abc', '{F} ¿Qué necesita un sistema que puede equivocarse?', 'Apelación y revisión humana', 'Menos reglas públicas', 'Más retiros automáticos', 'Permite corregir errores y proteger la libertad de expresión.'),
        ('abc', '{F} Alguien dice: «Moderar es siempre censura». ¿Qué error comete?', 'No distingue una opinión legítima de un daño como el acoso o la amenaza', 'Usa evidencia de otro caso para generalizar el problema', 'Confunde la apelación con la revisión de una decisión', 'No todo retiro es censura: hay contenidos que dañan derechos.'),
        ('abc', '{F} ¿Qué medida combinada es más equilibrada?', 'Reglas públicas, etiquetas de verificación, apelación y alfabetización mediática', 'Eliminar toda regla y dejar que cada persona publique libremente', 'Retirar contenidos sin explicar las razones a las personas', 'Une protección frente a daños y libertad de expresión.'),
        ('abc', '{F} ¿Qué contenido debe retirarse con más urgencia?', 'Amenazas e incitación a la violencia', 'Una opinión crítica con la autoridad', 'Un comentario irónico sobre un político', 'Las amenazas y la incitación a la violencia dañan derechos de otras personas.'),
        ('abc', '{F} ¿Qué dato falta para evaluar la propuesta del investigador?', 'Cuánto cuesta aplicarla y qué resultados tuvo en pruebas', 'El nombre del investigador y su lugar de trabajo', 'Cuántos seguidores tiene el periodista en redes sociales', 'Permite evaluar su efecto y su viabilidad.'),
    ],
    ctx=('abc', 'Un sitio de ejemplo elimina comentarios críticos hacia la administración sin explicar las reglas. ¿Qué falla?', 'La transparencia de las reglas', 'La velocidad del retiro', 'Las etiquetas de verificación', 'Sin reglas explicadas, el retiro puede ser arbitrario.'),
    sc=[
        ('¿Qué es una etiqueta de verificación?', 'Una marca que indica que un contenido fue revisado o es dudoso', 'Ayuda a informarse sin retirar el contenido.'),
        ('abc', '¿Qué es la alfabetización mediática?', 'La capacidad de analizar críticamente los medios y la información', 'Aprender a leer y escribir en los primeros años de escuela', 'Usar muchas redes sociales y estar conectado todo el día', 'Enseña a analizar los medios, por lo que forma usuarios críticos.'),
        ('¿Qué es la apelación?', 'La posibilidad de reclamar y pedir revisión de una decisión', 'La apelación permite corregir los errores de una decisión de moderación.'),
    ],
    op=("Con la {F} haz una tabla con las tres perspectivas: valor, evidencia y riesgo. Escribe después una política de moderación de cinco líneas con reglas públicas, un procedimiento de apelación y una medida de educación. Sin tomar partido.",
        "Periodista: rapidez; daño de la desinformación; riesgo, retirar de más. Defensora: libertad; temor a la censura; riesgo, dejar pasar el acoso. Investigador: combinación; dato de 20 errores; riesgo, costo. Política: reglas públicas, retiro de amenazas, apelación humana, etiquetas de verificación y talleres de educación mediática.",
        ["identifica valores", "incluye apelación", "propone educación"], ["tabla", "política de cinco líneas"], ["decir que moderar es censura", "eliminar reglas"],
        "Pregunta qué medida protegería más a quienes sufren acoso."),
    reinforce="Explica por qué un sistema de moderación necesita apelación.",
    extend="Averigua qué reglas de convivencia tiene una red que uses y cómo se reclama.",
)

# ============================================================ OA 06, clase 4
F = ("Ficha 66 (tema de deliberación de ejemplo): el municipio ficticio de Valle Hondo propone una aplicación para recibir reclamos y ofrecer votaciones vecinales. "
     "Para votar, la aplicación pediría el nombre completo, el rut, la dirección y el teléfono. "
     "A favor: facilita la participación y evita fraudes. En contra: reúne muchos datos personales que podrían filtrarse o usarse para otros fines. "
     "Alternativa: pedir solo el rut para comprobar que la persona vive en la comuna, guardar los datos cifrados y borrarlos al terminar la votación. "
     "Dato de ejemplo: en una prueba, 400 de 2.000 vecinos usaron la aplicación.")
build(
    O6, 4, F,
    use="Aprenderé a deliberar sobre tecnologías de participación, equilibrando facilidad de participar y protección de la vida privada, con razones y evidencia.",
    prior=["Sé qué es un dato personal.", "Sé estructurar un argumento.", "Sé calcular porcentajes."],
    explain=[
        "Las tecnologías pueden facilitar la participación: votar a distancia, reclamar en línea, informarse. Pero cada dato personal que se pide es un riesgo: puede filtrarse, usarse con otros fines o permitir seguimiento. Un principio útil es la minimización de datos: pedir solo lo necesario, guardarlo protegido y borrarlo cuando ya no hace falta.",
        "Al deliberar se pregunta qué dato es necesario para el objetivo (por ejemplo, comprobar que alguien vive en la comuna), qué riesgos tiene y qué alternativas existen. También se pregunta por la inclusión: si solo participa quien tiene teléfono y conexión, se excluye a otras personas, y habrá que mantener opciones presenciales.",
        "Una propuesta sólida combina facilidad y protección: datos mínimos, cifrado, plazos de borrado, información clara sobre el uso, consentimiento y opciones sin tecnología. Se evalúa con indicadores como participación y número de incidentes de seguridad. Quien disiente tiene derecho a objetar y a que se registre su postura.",
    ],
    vocab=[("minimización de datos", "principio de pedir solo los datos necesarios para un objetivo"), ("cifrado", "protección de datos para que no puedan leerse sin autorización"), ("filtración", "salida de datos a personas no autorizadas"), ("brecha digital", "diferencia entre quienes tienen y no tienen acceso a tecnología"), ("consentimiento informado", "autorización dada con información clara sobre el uso de los datos")],
    worked=[
        ("Aplicar minimización", "Para comprobar que una persona vive en una comuna, ¿qué dato es necesario: su identificación o también su historial de compras?", ["Basta la identificación.", "El historial no es necesario."], "Solo la identificación"),
        ("Calcular participación", "En una prueba de ejemplo, 300 de 1.500 vecinos usaron una aplicación. ¿Qué porcentaje es?", ["300 entre 1.500 son 20 de cada 100.", "Es el 20 %."], "20 %"),
    ],
    mistakes=[("Pedir todos los datos por si acaso.", "Aumenta el riesgo de filtración.", "Pide solo lo necesario."),
              ("Ofrecer solo la vía digital.", "Se excluye a quien no tiene acceso.", "Mantén opciones presenciales.")],
    T=[
        ('abc', '¿Qué es la minimización de datos?', 'Pedir solo los datos necesarios para un objetivo', 'Pedir todos los datos posibles por si se necesitan', 'Guardar los datos sin plazo', 'Reduce los riesgos de filtración y de uso indebido.'),
        ('abc', '¿Qué es el cifrado?', 'Proteger datos para que no se lean sin autorización', 'Borrar los datos después de usarlos en la votación', 'Publicar los datos en una lista pública del municipio', 'Hace ilegible la información para quien no tiene autorización.'),
        ('=', '{F} ¿Qué porcentaje de los 2.000 vecinos usó la aplicación?', '400*100//2000', 'Se compara la parte que la usó con el total.', ' %'),
        ('=', '{F} ¿Cuántos vecinos no usaron la aplicación?', '2000-400', 'Se resta los usuarios al total.', ' vecinos'),
        ('abc', '{F} ¿Qué ventaja menciona la ficha?', 'Facilita la participación y evita fraudes', 'Reúne pocos datos y nadie se preocupa por ellos', 'Elimina la necesidad de votar en persona', 'Es el argumento a favor registrado en la ficha.'),
        ('abc', '{F} ¿Qué riesgo menciona la ficha?', 'Que los datos se filtren o se usen para otros fines', 'Que haya demasiada participación de los vecinos', 'Que la votación sea más lenta que en papel', 'Es la objeción registrada en la ficha.'),
        ('abc', '{F} ¿Qué principio aplica la alternativa de pedir solo el rut?', 'Minimización de datos: pide solo lo necesario para comprobar que vive en la comuna', 'Máxima recolección, para evitar fraudes en la votación', 'Anonimato total, sin comprobar nada sobre quien vota', 'Limita el dato pedido al fin que se persigue.'),
        ('abc', '{F} ¿Qué medida protege los datos?', 'Cifrarlos y borrarlos al terminar la votación', 'Guardarlos indefinidamente por si se necesitan', 'Compartirlos con otras reparticiones', 'Reduce el tiempo y la exposición a riesgos.'),
        ('abc', '{F} ¿Qué problema puede tener una aplicación como única vía?', 'Excluir a quienes no tienen acceso a tecnología (brecha digital)', 'Facilitar la participación de todos por igual en la comuna', 'Reducir el fraude en las votaciones a cero', 'Quien no tiene teléfono o conexión queda fuera.'),
        ('abc', '{F} Alguien dice: «Entreguemos todos los datos, así participamos más fácil». ¿Qué corresponde?', 'Pedir solo los datos necesarios y mantener opciones sin tecnología', 'Aceptarlo, porque la participación es lo más importante en democracia', 'Rechazar toda aplicación y volver al sistema anterior', 'Equilibra facilidad con privacidad e inclusión.'),
        ('abc', '{F} ¿Qué indicador mostraría si la medida funciona?', 'Participación y cantidad de incidentes de seguridad', 'Cantidad de afiches pegados en la comuna', 'Número de descargas de la aplicación', 'Mide a la vez la participación y la protección.'),
        ('abc', '{F} ¿Qué haces si descubres que un dato tuyo se difundió sin permiso?', 'Avisar a una persona adulta de confianza y reportarlo a la institución', 'Callar para que no se note que sus datos se difundieron', 'Responder difundiendo datos de quien lo hizo', 'Se busca ayuda y se reporta a quien puede actuar.'),
        ('abc', 'Una app escolar de ejemplo pide acceso a los contactos del teléfono para votar por el delegado. ¿Qué corresponde?', 'Preguntar si es necesario y negarse si no lo es', 'Aceptar sin leer porque es del liceo', 'Dar acceso solo a medias', 'Es un dato innecesario para el objetivo de votar.'),
    ],
    ctx=('abc', 'Un liceo ofrece votar en línea y también en un puesto en el liceo. ¿Qué evita?', 'Excluir a quienes no tienen acceso a internet', 'Que haya demasiados votantes en el liceo', 'Que se protejan los datos de los estudiantes', 'Mantener una opción presencial reduce la brecha digital.'),
    sc=[
        ('¿Qué es una filtración de datos?', 'La salida no autorizada de datos personales a manos de terceros', 'Es uno de los riesgos de reunir muchos datos.'),
        ('abc', '¿Qué es el consentimiento informado?', 'Aceptar el uso de los datos sabiendo para qué se usarán', 'Aceptar sin leer las condiciones de uso de la aplicación', 'Aceptar porque otros ya lo hicieron antes', 'Requiere información clara sobre el uso.'),
        ('En Educación Ciudadana: ¿Qué es la brecha digital?', 'La diferencia entre quienes tienen y no tienen acceso a tecnología', 'Puede excluir a personas de la participación.'),
    ],
    op=("Con la {F} escribe una propuesta de siete líneas: qué datos pedirías y por qué, una medida de seguridad, una opción para quien no tiene tecnología, el uso del dato, un indicador y un plazo de revisión.",
        "Pediría solo el rut para comprobar la residencia. Seguridad: cifrado y borrado al terminar. Opción: urnas en la sede vecinal. Uso: solo para la votación. Indicador: participación e incidentes. Revisión: tras la primera votación. Consentimiento informado antes de votar.",
        ["aplica minimización", "incluye opción inclusiva", "incluye consentimiento"], ["propuesta de siete líneas"], ["pedir más datos de los necesarios", "excluir a quien no tiene tecnología"],
        "Pregunta cómo informaría el uso de los datos."),
    reinforce="Explica con un ejemplo qué datos son necesarios y cuáles no.",
    extend="Revisa qué datos pide una aplicación que uses y si todos son necesarios.",
)

# ============================================================ OA 06, clase 5
F = ("Ficha 67 (diagnóstico de ejemplo en el liceo ficticio Alto Palena): en una encuesta a 80 estudiantes, 50 comparten noticias sin revisar la fuente, 30 sí la revisan. "
     "Además, 20 dicen haber recibido mensajes ofensivos en redes. Recursos: 12 voluntarios, 4 semanas, un docente de apoyo. "
     "Idea: una campaña «Verifica antes de compartir» con afiches, un taller de verificación de fuentes y un espacio para avisar a un adulto de confianza ante acoso.")
build(
    O6, 5, F,
    use="Aprenderé a diseñar una campaña escolar de verificación de información y cuidado de la vida privada, con metas, actividades, inclusión y evaluación.",
    prior=["Sé verificar una fuente.", "Sé qué es la vida privada.", "Sé diseñar una acción con indicador."],
    explain=[
        "Una campaña de verificación busca que más personas revisen la fuente antes de compartir una información. Parte de un diagnóstico (50 de 80 comparten sin revisar), plantea un objetivo medible (por ejemplo, que 60 de 80 revisen la fuente), asigna roles y define actividades: un taller con pasos simples (¿quién lo dice?, ¿cuándo?, ¿qué evidencia hay?, ¿lo confirma otra fuente?), afiches y ejercicios con casos ficticios.",
        "La campaña cuida la privacidad: no usa mensajes reales ni nombres de compañeros; usa ejemplos inventados. También considera el bienestar: se enseña a no responder a mensajes ofensivos, a guardar la evidencia, a no reenviar imágenes íntimas y a avisar a una persona adulta de confianza.",
        "Se evalúa con una encuesta antes y después, y se comunica con honestidad. Una campaña escolar tiene un alcance limitado, pero fortalece hábitos. Se pueden planear nuevas acciones: un panel de verificación mensual, o un acuerdo de curso sobre cómo usar los grupos de mensajería.",
    ],
    vocab=[("campaña", "conjunto de actividades coordinadas para lograr un cambio"), ("taller de verificación", "actividad práctica para aprender a comprobar fuentes"), ("encuesta previa y posterior", "preguntas antes y después de una acción para medir cambios"), ("acuerdo de curso", "norma que el curso decide en conjunto"), ("evidencia digital", "mensajes o capturas que muestran lo ocurrido")],
    worked=[
        ("Medir un cambio", "En un curso de ejemplo, 15 de 40 revisaban la fuente y luego lo hacen 30. ¿Cuántos más?", ["Se resta 15 a 30.", "Son 15."], "15 estudiantes más"),
        ("Qué hacer ante un mensaje ofensivo", "Un estudiante de ejemplo recibe un mensaje ofensivo. ¿Qué paso es adecuado?", ["No responde.", "Guarda la evidencia y avisa a un adulto de confianza."], "Guardar la evidencia y avisar a un adulto de confianza"),
    ],
    mistakes=[("Usar mensajes reales de compañeros como ejemplos.", "Se vulnera su privacidad.", "Usa casos inventados."),
              ("Prometer que la campaña eliminará la desinformación.", "Su alcance es limitado.", "Plantea metas realistas.")],
    T=[
        ('abc', '¿Qué es una campaña?', 'Un conjunto de actividades coordinadas para lograr un cambio', 'Un mensaje publicado una sola vez en el diario mural', 'Una encuesta final que se aplica al terminar el semestre', 'Combina varias acciones con un mismo objetivo.'),
        ('=', '{F} Si el objetivo es que 60 de los 80 estudiantes revisen la fuente, ¿qué porcentaje es?', '60*100//80', 'Se compara la meta con el total de estudiantes.', ' %'),
        ('=', '{F} Si el objetivo es que 60 revisen la fuente, ¿cuántos más que los 30 actuales?', '60-30', 'Se resta los actuales a la meta.', ' estudiantes'),
        ('=', '{F} ¿Qué porcentaje de los 80 estudiantes dice haber recibido mensajes ofensivos?', '20*100//80', 'Se compara la parte con el total.', ' %'),
        ('abc', '{F} ¿Qué preguntas incluye el taller de verificación?', '¿Quién lo dice, cuándo y con qué evidencia? ¿Lo confirma otra fuente?', '¿Cuántos likes tiene y cuántas veces se compartió esa noticia?', '¿Quién lo compartió primero entre mis amigos cercanos?', 'Son pasos que comprueban la fuente y la evidencia.'),
        ('abc', '{F} ¿Qué tipo de ejemplos usa la campaña?', 'Casos ficticios', 'Mensajes reales de compañeros con sus nombres', 'Mensajes reales sin nombres, pero con capturas', 'Protege la privacidad de las personas.'),
        ('abc', '{F} ¿Qué indicador mide la meta?', 'Estudiantes que dicen revisar la fuente en la encuesta posterior a la campaña', 'Afiches impresos durante las cuatro semanas', 'Asistentes a la presentación de la campaña', 'Mide el cambio de hábito frente al punto de partida.'),
        ('abc', '{F} ¿Qué se enseña ante mensajes ofensivos?', 'No responder, guardar la evidencia y avisar a una persona adulta de confianza', 'Responder con ofensas para defenderse de quien escribe', 'Borrar el mensaje y no decir nada a nadie', 'Es un protocolo seguro porque conserva pruebas y busca ayuda de un adulto.'),
        ('abc', '{F} ¿Qué haces con una imagen íntima que recibes de alguien?', 'No la reenvías ni la compartes y avisas a una persona adulta de confianza', 'La reenvías solo a quienes ya la conocen para que opinen', 'La borras y no cuentas nada a nadie por vergüenza', 'Se protege a la persona afectada y se pide ayuda.'),
        ('abc', '{F} Si después de la campaña solo 40 revisan la fuente, ¿qué corresponde?', 'Reconocer el avance y ajustar las actividades', 'Declarar fracaso total y abandonar la campaña', 'Declarar la meta cumplida aunque no lo esté', '40 supera los 30 iniciales, pero no alcanza los 60.'),
        ('abc', '{F} ¿Qué acción de continuidad es realista?', 'Un panel mensual con una verificación de ejemplo', 'Una promesa de eliminar la desinformación', 'Repetir el mismo afiche cada mes', 'Es una acción concreta y sostenible.'),
        ('abc', 'Un curso acuerda reglas para su grupo de mensajería. ¿Qué regla protege la privacidad?', 'No reenviar fotos de otras personas sin su permiso', 'Reenviar todo lo que llegue para estar informados', 'Compartir capturas de conversaciones privadas con el curso', 'Respeta la imagen y la privacidad de las demás personas.'),
        ('abc', '¿Qué es una encuesta previa y posterior?', 'Preguntas antes y después de una acción para medir cambios', 'Un examen final de conocimientos sobre verificación', 'Una encuesta que se aplica solo al terminar la campaña', 'Permite comparar con el punto de partida.'),
    ],
    ctx=('abc', 'Antes de compartir una noticia llamativa, ¿cuál es el primer paso?', 'Revisar quién la publica y si otra fuente la confirma', 'Compartirla para ver si alguien la desmiente', 'Fijarse en cuántas personas la compartieron', 'Antes de difundir una información se verifica su fuente y su evidencia.'),
    sc=[
        ('¿Qué es un taller de verificación?', 'Una actividad donde se practica comprobar fuentes y evidencia con casos ficticios', 'Enseña pasos simples para revisar una información.'),
        ('abc', '¿Qué es la evidencia digital?', 'Mensajes o capturas que muestran lo ocurrido', 'Una opinión publicada en redes sin respaldo', 'Un archivo borrado que ya no se puede recuperar', 'Ayuda a documentar casos de acoso o desinformación.'),
        ('¿Qué es un acuerdo de curso?', 'Una norma compartida que el curso decide para convivir mejor', 'Por ejemplo, reglas sobre cómo usar el grupo de mensajería.'),
    ],
    op=("Con la {F} diseña la campaña: objetivo medible, tres actividades, roles para 12 voluntarios, pasos de verificación, un cuidado de privacidad, un protocolo de seguridad ante mensajes ofensivos o imágenes íntimas, y un indicador.",
        "Objetivo: 60 de 80 revisan la fuente. Actividades: afiches, taller, ejercicios con casos ficticios. Roles: 4 por actividad. Pasos: ¿quién lo dice?, ¿cuándo?, ¿evidencia?, ¿otra fuente? Privacidad: casos inventados. Protocolo: no responder, guardar evidencia, no reenviar imágenes íntimas, no borrar el chat y avisar a un adulto de confianza. Indicador: encuesta posterior.",
        ["objetivo medible", "protocolo de seguridad completo", "privacidad"], ["diseño de la campaña"], ["usar casos reales", "no incluir el aviso a un adulto"],
        "Pregunta cómo sabrá si la campaña cambió los hábitos."),
    reinforce="Escribe cuatro pasos para verificar una información.",
    extend="Haz un acuerdo de tres normas para un grupo de mensajería de tu curso.",
)

# ============================================================ OA 06, clase 6
F = ("Ficha 68 (evaluación de ejemplo): tras la campaña «Verifica antes de compartir» del liceo ficticio Alto Palena, una encuesta posterior mostró: de 80 estudiantes, 60 dicen revisar la fuente (antes eran 30). "
     "Sin embargo, solo 25 asistieron al taller completo; 15 dicen que lo hacen «a veces»; los mensajes ofensivos reportados bajaron de 20 a 14. Costo de ejemplo: 40.000 pesos (afiches y fotocopias). "
     "Limitaciones: la encuesta es de autoinforme (cada persona dice lo que hace) y no hay observación directa.")
build(
    O6, 6, F,
    use="Aprenderé a evaluar los efectos y límites de una acción de verificación y de protección de la vida privada, con datos, costo y honestidad.",
    prior=["Sé qué es un indicador.", "Sé calcular diferencias y porcentajes.", "Sé qué es el autoinforme."],
    explain=[
        "Evaluar una campaña de comunicación es comparar los resultados con el punto de partida y con la meta, y estimar costos. Aquí, las personas que dicen revisar la fuente subieron de 30 a 60 de 80. Pero un autoinforme puede exagerar: la gente puede decir lo que cree que es correcto. Por eso se complementa con una prueba práctica, por ejemplo verificar un caso ficticio.",
        "Los efectos pueden ser diversos. Algunos son buscados (más verificación), otros son parciales (el taller lo siguió una parte) y otros no previstos (más conciencia sobre la privacidad o, quizás, desconfianza excesiva hacia cualquier noticia). Los mensajes ofensivos reportados bajaron, pero eso no prueba que la campaña lo causó: pudieron intervenir otros factores.",
        "La evaluación honesta señala logros, límites y próximos pasos. Se informa a la comunidad sin exagerar. Se agradece a quienes participaron, se reconoce a quienes no pudieron asistir y se propone una mejora concreta, como repetir el taller en otro horario. Se mantiene el protocolo de avisar a una persona adulta de confianza ante acoso.",
    ],
    vocab=[("autoinforme", "dato que cada persona entrega sobre su propia conducta"), ("prueba práctica", "actividad que comprueba lo que la persona realmente hace"), ("efecto parcial", "resultado que se logra solo en parte"), ("causalidad", "relación en que una cosa produce otra"), ("próximo paso", "acción concreta para mejorar o continuar")],
    worked=[
        ("Calcular mejora", "Una campaña de ejemplo pasó de 20 a 35 estudiantes que verifican. ¿Cuántos más?", ["Se resta 20 a 35.", "Son 15."], "15 estudiantes más"),
        ("Autoinforme", "«Digo que reviso las fuentes siempre». ¿Qué limitación tiene este dato?", ["Es lo que la persona dice.", "No es observación directa."], "Es autoinforme"),
    ],
    mistakes=[("Atribuir toda mejora a la campaña.", "Pudieron influir otros factores.", "Habla de relación y pide más datos."),
              ("Ignorar el costo.", "Un resultado se compara con lo invertido.", "Calcula el costo por persona.")],
    T=[
        ('abc', '¿Qué es un autoinforme?', 'Un dato que cada persona entrega sobre su propia conducta', 'Un dato medido por observadores externos sin preguntar a nadie', 'Un registro automático de una aplicación o programa', 'Es lo que la persona dice hacer, no lo que se observa.'),
        ('=', '{F} ¿En qué porcentaje aumentó la cantidad de estudiantes que dicen revisar la fuente?', '(60-30)*100//30', 'Se compara el aumento con el valor inicial.', ' %'),
        ('=', '{F} ¿En qué porcentaje bajaron los mensajes ofensivos reportados?', '(20-14)*100//20', 'Se compara la baja con el valor inicial.', ' %'),
        ('=', '{F} ¿Cuántos pesos costó la campaña por estudiante, entre los 80 estudiantes?', '40000//80', 'Se divide el costo total entre los estudiantes.', ' pesos'),
        ('=', '{F} ¿Cuántos estudiantes más que los que asistieron al taller completo dicen revisar la fuente?', '60-25', 'Se resta los asistentes al taller a los que dicen revisar la fuente.', ' estudiantes'),
        ('abc', '{F} ¿Qué limitación señala la ficha?', 'La encuesta es de autoinforme: cada persona dice lo que hace', 'La encuesta fue demasiado larga para los estudiantes', 'No se preguntó a ningún estudiante sobre su conducta', 'Está en las limitaciones de la ficha.'),
        ('abc', '{F} ¿Qué prueba complementaría el autoinforme?', 'Una prueba práctica en que verifiquen un caso ficticio', 'Otra encuesta con las mismas preguntas', 'Una votación sobre si la campaña fue buena', 'Comprueba la conducta en vez de lo que cada persona declara.'),
        ('abc', '{F} Alguien dice: «Los mensajes ofensivos bajaron por la campaña». ¿Qué corresponde?', 'Señalar que pudo haber otros factores y que falta evidencia de causa', 'Aceptarlo, porque los mensajes bajaron después de la campaña', 'Rechazarlo, porque una campaña no puede influir en las conductas', 'Que algo ocurra después no prueba que sea consecuencia.'),
        ('abc', '{F} ¿Qué conclusión es prudente?', 'Mejoró lo que dicen hacer, pero se necesita comprobarlo con pruebas prácticas', 'La campaña eliminó la desinformación del liceo por completo', 'La campaña no sirvió porque pocos asistieron al taller', 'Reconoce el avance logrado sin exagerar sus alcances ni minimizarlo.'),
        ('abc', '{F} ¿Qué efecto parcial muestra la ficha?', 'Solo 25 estudiantes siguieron el taller completo', 'Todos asistieron al taller', 'Los mensajes ofensivos desaparecieron', 'Solo una parte de los estudiantes siguió el taller completo.'),
        ('abc', '{F} ¿Qué próximo paso es concreto?', 'Repetir el taller en otro horario para quienes no pudieron asistir', 'Dar por terminada la iniciativa sin hacer más cambios', 'Culpar a quienes no asistieron por falta de interés', 'Mejora la inclusión y es una acción concreta.'),
        ('abc', 'Un curso evalúa una campaña solo con una encuesta que cada persona responde de memoria. ¿Qué límite tiene?', 'Es autoinforme y puede exagerar lo que se hace', 'No tiene límites, porque todos responden con la verdad', 'Es demasiado exacta para ser considerada una estimación', 'No hay observación directa de la conducta.'),
        ('abc', '{F} ¿Qué sería un efecto no previsto de la campaña?', 'Desconfianza excesiva hacia cualquier noticia', 'Más estudiantes que verifican las fuentes', 'Menos mensajes ofensivos en el liceo', 'Es una consecuencia que no se buscaba.'),
    ],
    ctx=('abc', 'Un liceo ve que, tras una charla, bajan los atrasos. ¿Qué cautela corresponde?', 'Puede haber otros factores; hace falta comparar antes de afirmar que la charla lo causó', 'Concluir que la charla fue la causa y repetirla cada año', 'Concluir que la charla no influyó en los atrasos', 'Que algo ocurra después no prueba causalidad.'),
    sc=[
        ('¿Qué es la causalidad?', 'La relación en que una cosa produce otra', 'Para afirmarla se necesita evidencia, no solo coincidencia.'),
        ('abc', '¿Qué es una prueba práctica?', 'Una actividad que comprueba lo que la persona realmente hace', 'Una opinión sobre lo que debería hacerse en cada caso', 'Una pregunta de memoria sobre los contenidos del taller', 'Mide la conducta real de la persona en una situación concreta.'),
        ('¿Qué es un efecto parcial?', 'Un resultado que se logra solo en una parte de lo esperado', 'Por ejemplo, que solo parte del grupo siguió el taller.'),
    ],
    op=("Con la {F} escribe una evaluación de seis líneas: dos logros con números, dos límites, un efecto parcial, un costo por estudiante, una recomendación y una frase honesta para informar al liceo.",
        "Logros: de 30 a 60 estudiantes que revisan la fuente; mensajes ofensivos de 20 a 14. Límites: autoinforme; sin prueba práctica. Efecto parcial: 25 asistieron al taller. Costo: 500 pesos por estudiante. Recomendación: repetir el taller y hacer una prueba práctica. Mensaje: mejoramos, pero seguimos verificando y cuidándonos.",
        ["usa números", "reconoce límites", "propone recomendación"], ["evaluación de seis líneas"], ["atribuir causa sin evidencia", "omitir el costo"],
        "Pregunta qué nueva medición haría."),
    reinforce="Explica por qué un autoinforme no basta para evaluar.",
    extend="Anota un hábito digital propio que podrías mejorar y cómo lo medirías.",
)
