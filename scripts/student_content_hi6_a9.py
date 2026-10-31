"""Material del estudiante de 6.º básico, Historia, Geografía y Ciencias Sociales: OA 09 (continuidades y cambios de la sociedad chilena a lo largo de su historia)."""
from __future__ import annotations

from hi5_lib import build

OA9 = "HI06 OA 09"

# ---------------------------------------------------------------- clase 1
F = ("Ficha 38 (tres cortes en el tiempo, hecha para este cuaderno; datos generales y redondeados). "
     "Hacia 1850: votaban pocos hombres, los que sabían leer y tenían propiedades; la escuela no era obligatoria; se viajaba en carreta, mula o caballo y se inauguraba el primer ferrocarril; los mensajes se enviaban por carta y, desde 1852, por telégrafo; la economía se basaba en la agricultura y la minería. "
     "Hacia 1920: votaban hombres que supieran leer; las mujeres no votaban todavía; la escuela primaria pasó a ser obligatoria en 1920; había trenes y tranvías en las ciudades; el salitre era muy importante. "
     "Hoy: votan hombres y mujeres desde los 18 años; la educación es obligatoria durante 12 años; se viaja en bus, metro, auto y avión; se comunica por teléfono celular e internet; Chile es uno de los mayores productores de cobre del mundo.")
build(
    OA9, 1, F,
    use="Aprenderé a ubicar en el tiempo qué cambió y qué se mantuvo en la sociedad chilena. Sirve para describir la historia con cortes en 1850, 1920 y hoy.",
    prior=["Sé que el voto y la educación se ampliaron en los siglos XIX y XX.", "Sé qué fue el ferrocarril y el telégrafo.", "Sé comparar usando un criterio."],
    explain=[
        "Un cambio es algo que es distinto de antes. Una continuidad es algo que sigue igual o parecido a través del tiempo. La historia de Chile tiene cambios y continuidades, y para verlos conviene comparar tres cortes en el tiempo: hacia 1850, hacia 1920 y hoy.",
        "Cambiaron el voto, que se amplió a más personas; la educación, que pasó a ser obligatoria durante muchos años; el transporte, que pasó de carretas y mulas a metro y aviones; y la comunicación, que pasó de cartas a internet. También cambió la economía, de la agricultura y la minería del siglo XIX a una economía con mucha minería del cobre.",
        "Hay también continuidades. La minería sigue siendo importante, igual que en el siglo XIX. La agricultura continúa en el campo. Y en Chile siempre han existido pueblos originarios y una sociedad diversa. Reconocer cambios y continuidades evita pensar que todo cambió o que todo sigue igual.",
    ],
    vocab=[("cambio", "algo que es distinto de antes"), ("continuidad", "algo que sigue igual o parecido a través del tiempo"), ("corte en el tiempo", "momento elegido para comparar con otros momentos"), ("cobre", "metal que Chile produce en grandes cantidades, sobre todo en el norte"), ("obligatorio", "que todos deben cumplir")],
    worked=[
        ("Reconocer un cambio", "{F} ¿Cómo cambió la comunicación entre 1850 y hoy?", ["En 1850 se usaban cartas y, desde 1852, el telégrafo.", "Hoy se usa el teléfono celular y el internet."], "Pasó de cartas y telégrafo a celular e internet"),
        ("Reconocer una continuidad", "{F} ¿Qué actividad económica aparece en 1850 y también hoy?", ["Busco una actividad que se repita.", "La minería aparece en 1850 y hoy, con el cobre."], "La minería"),
    ],
    mistakes=[("Pensar que todo cambió con el tiempo.", "Se olvidan las continuidades.", "La minería, por ejemplo, sigue siendo importante."),
              ("Creer que todo sigue igual.", "Se ignoran los cambios.", "El voto, la educación y el transporte cambiaron mucho.")],
    T=[
        ("{F} ¿Qué transporte se usaba hacia 1850 según la ficha?", "carreta, mula o caballo", "La ficha lo indica."),
        ("{F} ¿Desde qué año la escuela primaria fue obligatoria?", "1920", "La ficha lo indica."),
        ("{F} ¿Cuántos años de educación obligatoria hay hoy?", "12 años", "La ficha lo dice."),
        ("{F} ¿Qué mineral importante produce Chile hoy?", "el cobre", "La ficha lo indica."),
        ("=", "{F} ¿Cuántos años pasaron entre 1850 y 1920?", "1920-1850", "Se resta el año menor al mayor.", " años"),
        ("{F} ¿Quiénes votaban hacia 1920?", "hombres que supieran leer", "La ficha lo indica."),
        ("{F} Clasifica como cambio (C) o continuidad (K) entre 1850 y hoy: a) la minería es importante; b) el voto es para hombres y mujeres desde los 18 años; c) el internet; d) la agricultura continúa.", "a: K; b: C; c: C; d: K", "La minería y la agricultura se mantienen."),
        ("{F} Ordena los cortes del más antiguo al más reciente: hoy, 1920, 1850.", "1850, 1920, hoy", "Se ordenan por año."),
        ("{F} Un compañero dice: «Hacia 1920 votaban las mujeres». Corrígelo.", "No: todavía no votaban", "La ficha lo indica."),
        ("{F} Una alumna dice: «En 1850 se usaba internet». ¿Qué error comete?", "el internet es de hoy; en 1850 se usaban cartas y telégrafo", "La ficha separa las épocas."),
        ("{F} ¿Qué cambio de la ficha se relaciona con la economía entre 1920 y hoy?", "el salitre dejó de ser el producto principal y hoy es el cobre", "La ficha menciona el salitre en 1920 y el cobre hoy."),
        ("{F} Una línea de tiempo usa 1 cm = 10 años y parte en 1850. ¿A cuántos cm queda el año 1920?", "7 cm", "(1920 − 1850) ÷ 10 = 7."),
        ("{F} ¿Qué actividad económica aparece en los tres cortes de la ficha?", "la minería", "Aparece en 1850, 1920 (salitre) y hoy (cobre)."),
    ],
    ctx=("Un compañero dice: «Antes todo era mejor y todo sigue igual». Usa dos datos de la ficha para responderle.", "cambió el voto, que se amplió, y cambió la comunicación, que pasó de cartas a internet", "La ficha muestra muchos cambios."),
    sc=[("¿Qué es una continuidad?", "algo que sigue igual o parecido a través del tiempo", "Es la definición de la clase."),
        ("{F} ¿Quiénes votan hoy?", "hombres y mujeres desde los 18 años", "La ficha lo indica."),
        ("¿Por qué conviene comparar tres cortes?", "porque muestra cambios y continuidades en el tiempo", "Permite ver el proceso.")],
    op=("Dibuja una tabla con tres columnas (1850, 1920, hoy) y cuatro filas (voto, educación, transporte, comunicación). Completa con la ficha. Debajo escribe un cambio y una continuidad. {F}",
        "Voto: pocos hombres / hombres que saben leer / hombres y mujeres desde 18 años. Cambio: más personas votan. Continuidad: la minería sigue siendo importante.",
        ["tabla completa", "datos de la ficha", "un cambio y una continuidad"], ["tabla comparativa", "dos oraciones"], ["mezclar épocas", "no anotar ninguna continuidad"],
        "Pide que explique cuál fila muestra el mayor cambio."),
    reinforce="Di en voz alta un cambio y una continuidad.",
    extend="Escribe una pregunta sobre qué crees que cambiará en Chile en los próximos años.",
)

# ---------------------------------------------------------------- clase 2
F = ("Ficha 39 (fuentes inventadas para este cuaderno, basadas en hechos conocidos). "
     "Fuente A, descripción de una fotografía de Santiago hacia 1900: calle con tranvías tirados por caballos, carretas y personas con sombrero. "
     "Fuente B, nota de un diario de 1950 (texto inventado): «Cada vez más familias del campo llegan a la ciudad en busca de trabajo». "
     "Fuente C, noticia de hoy (texto inventado): «Una mina de cobre del norte de Chile exporta su producción a otros países». "
     "Fuente D, tabla de práctica con cifras redondeadas: población que vive en ciudades; 1900: 4 de cada 10 personas; 1950: 6 de cada 10; hoy: 9 de cada 10.")
build(
    OA9, 2, F,
    use="Aprenderé a usar fuentes para mostrar qué cambió y qué siguió igual en Chile. Sirve para apoyar una explicación con evidencia de distintas épocas.",
    prior=["Sé qué es un cambio y una continuidad.", "Sé analizar fuentes primarias y secundarias.", "Sé leer tablas simples."],
    explain=[
        "Para mostrar un cambio o una continuidad, necesitamos fuentes de diferentes épocas. Una fotografía muestra cómo era un lugar. Una nota de diario cuenta un hecho de su tiempo. Una tabla con datos permite medir cuánto cambió algo. Cada fuente tiene un punto de vista, y debemos preguntar quién la hizo, cuándo y para qué.",
        "La fotografía de 1900 muestra transporte con caballos y carretas. La nota de 1950 cuenta que más familias llegaban a la ciudad. La noticia de hoy muestra que la minería del cobre sigue siendo importante. La tabla indica que el porcentaje de población en ciudades creció: de 4 de cada 10 en 1900 a 9 de cada 10 hoy. Estas fuentes se pueden combinar.",
        "Los datos sirven para describir un cambio, pero no explican por sí solos por qué ocurrió. Además, cada fuente muestra solo un aspecto. Por eso conviene usar varias y reconocer sus límites. Por ejemplo, la tabla de ciudades no dice cómo vivían las familias del campo.",
    ],
    vocab=[("fuente", "documento, imagen o dato que sirve para conocer el pasado"), ("porcentaje", "parte de cada cien"), ("tabla", "cuadro de datos ordenados en filas y columnas"), ("urbano", "relacionado con la ciudad"), ("evidencia", "dato que apoya una afirmación")],
    worked=[
        ("Leer una tabla", "{F} ¿Qué cambió entre 1900 y hoy según la fuente D?", ["En 1900 vivían en ciudades 4 de cada 10 personas.", "Hoy viven 9 de cada 10."], "Creció la población que vive en ciudades"),
        ("Reconocer una continuidad", "{F} ¿Qué actividad económica aparece también en la fuente C?", ["La noticia habla de minería.", "La minería es una actividad que se mantiene."], "La minería del cobre"),
    ],
    mistakes=[("Creer que una fotografía muestra cómo era todo el país.", "Se generaliza desde un lugar.", "La fotografía muestra una calle de Santiago hacia 1900."),
              ("Pensar que una tabla explica por qué cambió algo.", "Se confunde descripción con explicación.", "La tabla mide cuánto cambió; hay que buscar otras fuentes para explicar por qué.")],
    T=[
        ("{F} ¿Qué transporte aparece en la fotografía de la fuente A?", "tranvías tirados por caballos y carretas", "La descripción lo indica."),
        ("{F} ¿Qué cuenta la fuente B?", "que más familias llegan del campo a la ciudad", "La nota lo dice."),
        ("{F} ¿Cuántas personas de cada 10 vivían en ciudades en 1950?", "6", "La tabla lo indica."),
        ("=", "{F} ¿Cuántas personas más de cada 10 viven en ciudades hoy comparado con 1900?", "9-4", "Se resta el valor menor al mayor.", " personas de cada 10"),
        ("{F} ¿Cuál de las fuentes es una tabla de datos?", "la fuente D", "La ficha la presenta así."),
        ("{F} ¿Qué fuente muestra una continuidad con el siglo XIX?", "la fuente C, porque habla de minería", "La minería existía en el siglo XIX."),
        ("{F} ¿Qué fuente sirve mejor para medir cuánto cambió la vida en ciudades?", "la fuente D", "Entrega números de tres épocas."),
        ("{F} Una alumna dice: «La fuente A prueba que todo Chile usaba tranvías». ¿Qué error comete?", "generaliza desde una fotografía de Santiago", "Una imagen no muestra todo el país."),
        ("{F} Un compañero dice: «La fuente D explica por qué las personas se fueron a la ciudad». ¿Qué error comete?", "la tabla mide el cambio, pero no explica por qué ocurrió", "Para explicar hay que usar fuentes como la B."),
        ("{F} ¿Qué fuente ayuda a explicar una causa del crecimiento de las ciudades?", "la fuente B, porque cuenta que familias llegan buscando trabajo", "Da una razón."),
        ("{F} Ordena las fuentes A, B y C por época, de la más antigua a la más reciente.", "A, B, C", "Las épocas son 1900, 1950 y hoy."),
        ("Según la explicación de la clase, ¿qué no dice la tabla de ciudades?", "cómo vivían las familias del campo", "La explicación lo señala como límite de esa fuente."),
        ("{F} ¿Qué dos fuentes combinarías para decir que las ciudades crecieron y por qué?", "la D y la B", "D da los datos y B una razón."),
    ],
    ctx=("Para una exposición sobre cómo cambió la vida en Chile, quieres un dato que muestre el crecimiento de las ciudades. ¿Qué fuente de la ficha eliges y por qué?", "la fuente D, porque tiene números de 1900, 1950 y hoy", "Los números permiten medir el cambio."),
    sc=[("¿Qué es un porcentaje?", "una parte de cada cien", "Es la definición de la clase."),
        ("{F} ¿Qué dato de la tabla muestra el mayor crecimiento?", "de 4 de cada 10 en 1900 a 9 de cada 10 hoy", "Es la comparación entre extremos."),
        ("¿Por qué una tabla no basta para explicar un cambio?", "porque mide, pero no dice por qué ocurrió", "Se necesitan otras fuentes.")],
    op=("Elige tres de las cuatro fuentes y haz una ficha para cada una: época, qué muestra, si apoya un cambio o una continuidad y qué límite tiene. Termina con una oración que combine dos fuentes. {F}",
        "D: tabla de práctica; apoya un cambio en la población urbana; no dice por qué. C: noticia de hoy; apoya la continuidad de la minería. Oración: Las ciudades crecieron, y las familias llegaban buscando trabajo.",
        ["tres fichas completas", "cambio o continuidad bien indicados", "oración que combina dos fuentes"], ["tres fichas", "una oración"], ["decir que la tabla explica las causas", "no indicar límites"],
        "Pide que explique por qué combinó esas dos fuentes."),
    reinforce="Con tus palabras, explica qué muestra cada fuente.",
    extend="Escribe una pregunta que puedas responder con una fotografía de tu barrio de hace 50 años.",
)

# ---------------------------------------------------------------- clase 3
F = ("Ficha 40 (causas de cambios y de continuidades, hecha para este cuaderno). "
     "Cambios y sus causas: el voto se amplió porque grupos como organizaciones de mujeres lo pidieron y se dictaron leyes; la educación se amplió porque se reconoció que era necesaria para participar y se crearon escuelas y leyes; las ciudades crecieron porque llegaron familias del campo buscando trabajo; el transporte y la comunicación cambiaron por nuevas tecnologías como el ferrocarril, el automóvil y el internet. "
     "Continuidades y sus causas: la minería sigue siendo importante porque Chile tiene grandes yacimientos de cobre; el campo sigue produciendo alimentos por la riqueza de su suelo y clima; el centralismo se mantiene porque muchas decisiones y servicios están concentrados en Santiago; los pueblos originarios continúan presentes y mantienen su cultura.")
build(
    OA9, 3, F,
    use="Aprenderé a explicar por qué algunas cosas cambiaron y otras se mantuvieron en la sociedad chilena. Sirve para relacionar causas, actores y consecuencias en el tiempo largo.",
    prior=["Sé qué es un cambio y una continuidad.", "Sé distinguir causa y consecuencia.", "Sé qué actores participaron en cambios del voto y la educación."],
    explain=[
        "Los cambios y las continuidades tienen causas. El voto y la educación cambiaron porque grupos de personas lo pidieron y se dictaron leyes. Las ciudades crecieron porque familias del campo buscaban trabajo. El transporte y la comunicación cambiaron por nuevas tecnologías como el ferrocarril, el automóvil y el internet.",
        "Las continuidades también tienen causas. La minería sigue siendo importante porque Chile tiene grandes yacimientos de cobre. El campo sigue produciendo alimentos por su suelo y clima. El centralismo, es decir, que muchas decisiones se tomen en Santiago, se mantiene porque servicios y poder se concentran allí.",
        "Los actores del cambio fueron muy variados: organizaciones de mujeres, trabajadores, el Estado, inventores y familias. Un mismo cambio puede beneficiar a unos más que a otros. Por eso es importante preguntar quién cambió algo, por qué y a quién benefició.",
    ],
    vocab=[("centralismo", "concentración de decisiones y servicios en la capital"), ("yacimiento", "lugar donde hay un mineral en cantidad"), ("tecnología", "conjunto de inventos y técnicas para hacer cosas"), ("actor", "persona o grupo que participa en un hecho"), ("beneficiar", "ayudar o favorecer a alguien")],
    worked=[
        ("Explicar una causa", "{F} ¿Por qué crecieron las ciudades según la ficha?", ["Busco el cambio de las ciudades.", "Llegaron familias del campo buscando trabajo."], "Porque llegaron familias del campo buscando trabajo"),
        ("Explicar una continuidad", "{F} ¿Por qué la minería sigue siendo importante?", ["Busco la continuidad.", "Chile tiene grandes yacimientos de cobre."], "Porque Chile tiene grandes yacimientos de cobre"),
    ],
    mistakes=[("Decir que las cosas cambian solas.", "Se olvidan los actores.", "Los cambios los impulsan personas, grupos y leyes."),
              ("Creer que las continuidades no tienen explicación.", "Se piensa que lo que sigue igual no necesita causas.", "También se explican, por ejemplo por la riqueza de recursos naturales.")],
    T=[
        ("{F} ¿Por qué se amplió el voto según la ficha?", "porque grupos como organizaciones de mujeres lo pidieron y se dictaron leyes", "La ficha lo indica."),
        ("{F} ¿Qué tecnología cambió el transporte?", "el ferrocarril y el automóvil", "La ficha los nombra."),
        ("{F} ¿Qué tecnología cambió la comunicación?", "el internet", "La ficha lo nombra."),
        ("{F} ¿Qué es el centralismo?", "que muchas decisiones y servicios se concentran en Santiago", "La explicación lo define."),
        ("{F} Clasifica como cambio (C) o continuidad (K): a) el internet; b) el cobre; c) más años de escuela obligatoria; d) el centralismo.", "a: C; b: K; c: C; d: K", "Lo que se mantiene es continuidad."),
        ("{F} ¿Qué cultura continúa presente en Chile según la ficha?", "la de los pueblos originarios", "La ficha lo indica."),
        ("{F} ¿Qué actor impulsó el voto femenino según la ficha?", "las organizaciones de mujeres", "La ficha lo indica."),
        ("{F} ¿Qué causa mantiene al campo produciendo alimentos?", "la riqueza de su suelo y clima", "La ficha lo dice."),
        ("{F} Un compañero dice: «El ferrocarril cambió la comunicación». Corrígelo.", "cambió el transporte; la comunicación cambió con tecnologías como el internet", "Son cambios de áreas distintas."),
        ("{F} Una alumna dice: «El centralismo desapareció». ¿Qué dato de la ficha lo contradice?", "que muchas decisiones y servicios siguen concentrados en Santiago", "La ficha lo presenta como continuidad."),
        ("{F} Según la ficha, ¿dónde se concentran hoy muchas decisiones y servicios: en la capital o en las regiones?", "en la capital (Santiago)", "La ficha lo presenta como la causa del centralismo."),
        ("{F} ¿Qué pregunta ayuda a no creer que los cambios beneficiaron a todos por igual?", "quién cambió algo, por qué y a quién benefició", "Muestra distintos efectos."),
        ("{F} Elige la mejor explicación. A) Las ciudades crecieron porque llegaron familias a buscar trabajo. B) Las ciudades crecieron porque sí.", "A", "A es una causa de la ficha."),
    ],
    ctx=("Una compañera dice: «La minería sigue en Chile por casualidad». Usa la ficha para responder.", "no: sigue porque Chile tiene grandes yacimientos de cobre", "Es una causa natural de la ficha."),
    sc=[("¿Qué es el centralismo?", "que muchas decisiones y servicios se concentran en la capital", "Es la definición de la clase."),
        ("{F} ¿Qué cambió en la educación?", "se amplió la educación obligatoria y se crearon escuelas", "La ficha lo dice."),
        ("¿Por qué hay que preguntar a quién benefició un cambio?", "porque no todos se benefician igual", "Cada grupo es afectado distinto.")],
    op=("Dibuja una tabla con tres columnas: «qué cambió o siguió igual», «causa» y «quién se benefició». Completa al menos cinco filas con la ficha (incluyendo dos continuidades). Debajo, escribe una oración sobre quién se benefició menos. {F}",
        "Las ciudades crecieron / llegaron familias buscando trabajo / quienes encontraron trabajo. La minería sigue / hay grandes yacimientos / el Estado y las empresas.",
        ["cinco filas completas", "dos continuidades incluidas", "oración final"], ["tabla de cinco filas", "una oración"], ["decir que el cambio benefició a todos", "no explicar la causa"],
        "Pide que explique una fila con sus palabras."),
    reinforce="Di en voz alta dos cambios y dos continuidades con su causa.",
    extend="Escribe una pregunta sobre cómo podría disminuir el centralismo.",
)

# ---------------------------------------------------------------- clase 4
F = ("Ficha 41 (comparación de territorios y de generaciones, hecha para este cuaderno). "
     "Santiago y la Región Metropolitana: concentra cerca de 4 de cada 10 personas del país; allí están el gobierno, muchas universidades y muchas empresas (el Congreso funciona en Valparaíso). "
     "Regiones: muchas tienen menos servicios especializados, pero cuentan con actividades propias, como minería en el norte, agricultura en el centro, bosques y turismo en el sur, y pesca en el extremo sur. "
     "Generaciones: una persona mayor recuerda que en su infancia se comunicaba con cartas y viajaba en tren; una niña de hoy usa mensajes por teléfono y viaja en bus o metro. "
     "Ambas comparten la importancia de aprender y de compartir con las personas queridas.")
build(
    OA9, 4, F,
    use="Aprenderé a comparar cambios y continuidades entre lugares y entre generaciones. Sirve para entender que el cambio no es igual para todos.",
    prior=["Sé qué es un cambio y una continuidad.", "Sé qué es el centralismo.", "Sé comparar con criterios."],
    explain=[
        "Los cambios no se viven igual en todos los lugares ni por todas las personas. Podemos comparar territorios, por ejemplo Santiago y las regiones, y generaciones, por ejemplo una persona mayor y una niña de hoy. Para comparar usamos criterios: transporte, comunicación, servicios y vida cotidiana.",
        "La Región Metropolitana concentra cerca de 4 de cada 10 personas y muchas instituciones, universidades y empresas. Las regiones tienen actividades propias, como minería, agricultura, turismo o pesca, pero a menudo menos servicios especializados. Esto es parte del centralismo, una continuidad histórica.",
        "Entre generaciones, la comunicación y el transporte cambiaron mucho: de las cartas y el tren a los mensajes por teléfono y el metro. Sin embargo, la importancia de aprender y de compartir con las personas queridas continúa. Comparar así permite ver diferencias, semejanzas y desafíos, como reducir las diferencias entre territorios.",
    ],
    vocab=[("generación", "grupo de personas que nacieron y crecieron en una misma época"), ("territorio", "espacio con características propias donde viven personas"), ("servicios especializados", "atenciones que requieren personal y equipos particulares, como algunos hospitales o universidades"), ("región", "una de las zonas político-administrativas de Chile"), ("desafío", "problema que hay que resolver")],
    worked=[
        ("Comparar dos territorios", "{F} ¿Qué diferencia hay entre la Región Metropolitana y las regiones en cuanto a servicios?", ["La RM concentra instituciones y servicios.", "Muchas regiones tienen menos servicios especializados."], "La RM concentra más servicios y muchas regiones tienen menos servicios especializados"),
        ("Comparar generaciones", "{F} ¿Qué continuidad comparten la persona mayor y la niña?", ["Leo la última frase de la ficha.", "Ambas valoran aprender y compartir con las personas queridas."], "La importancia de la familia y de la escuela"),
    ],
    mistakes=[("Pensar que las regiones no tienen actividades propias.", "Se mira solo la capital.", "Cada región tiene actividades propias, como minería, agricultura, turismo o pesca."),
              ("Creer que las generaciones no comparten nada.", "Se enfatiza solo el cambio.", "Ambas valoran aprender y compartir con las personas queridas.")],
    T=[
        ("{F} ¿Qué parte de la población vive en la Región Metropolitana según la ficha?", "cerca de 4 de cada 10 personas", "La ficha lo dice."),
        ("{F} ¿Qué actividad se menciona para el norte?", "la minería", "La ficha lo indica."),
        ("{F} ¿Qué actividad se menciona para el centro?", "la agricultura", "La ficha lo indica."),
        ("{F} ¿Cómo se comunicaba la persona mayor en su infancia?", "con cartas", "La ficha lo indica."),
        ("{F} ¿Cómo se comunica la niña de hoy?", "con mensajes por teléfono", "La ficha lo indica."),
        ("{F} Clasifica como territorio (T) o generación (G) la comparación: a) Santiago y regiones; b) una persona mayor y una niña de hoy.", "a: T; b: G", "Cada una compara un criterio distinto."),
        ("=", "{F} Si en una región viven 4 de cada 10 personas del país, ¿cuántas personas de un grupo de 100 viven allí?", "100*4//10", "Cada 10 personas incluyen 4 de esa región.", " personas"),
        ("{F} ¿Qué actividad se menciona en el sur?", "bosques y turismo", "La ficha lo dice."),
        ("{F} ¿Qué continuidad entre generaciones se menciona?", "la importancia de aprender y de compartir con las personas queridas", "La ficha lo indica."),
        ("{F} Un compañero dice: «En las regiones no hay actividades económicas». Corrígelo.", "sí hay: minería en el norte, agricultura en el centro, bosques y turismo en el sur, pesca en el extremo sur", "La ficha las enumera."),
        ("{F} Una alumna dice: «Las dos generaciones viajan igual». ¿Qué error comete?", "la persona mayor viajaba en tren y la niña viaja en bus o metro", "Cambió el transporte."),
        ("{F} ¿Qué desafío se menciona al comparar territorios?", "reducir las diferencias entre territorios", "La explicación lo señala."),
        ("{F} Elige la mejor conclusión. A) El cambio no se vive igual en todos los lugares. B) Todos los lugares son iguales.", "A", "La ficha muestra diferencias."),
    ],
    ctx=("Una familia vive en una región con pocos servicios especializados. ¿Qué dato de la ficha explica esa situación?", "el centralismo: muchos servicios están concentrados en la Región Metropolitana", "La ficha lo señala."),
    sc=[("¿Qué es una generación?", "un grupo de personas que nacieron y crecieron en una misma época", "Es la definición de la clase."),
        ("{F} ¿Qué cambió entre la persona mayor y la niña?", "la comunicación y el transporte", "La ficha lo indica."),
        ("¿Por qué es útil comparar territorios?", "porque muestra que el cambio no es igual en todos los lugares", "Hay diferencias entre lugares.")],
    op=("Dibuja una tabla con dos columnas, «Región Metropolitana» y «otra región de tu elección de la ficha: norte, centro, sur o extremo sur». Escribe tres criterios: servicios, actividad económica y población. Después escribe una oración que compare una persona mayor y una niña de hoy. {F}",
        "RM: concentra población y servicios. Norte: minería. Oración: Mientras la persona mayor escribía cartas, la niña de hoy envía mensajes, pero ambas valoran aprender y compartir con las personas queridas.",
        ["dos columnas completas", "tres criterios", "oración que compara generaciones"], ["tabla comparativa", "una oración"], ["decir que las regiones no tienen actividades", "mezclar generaciones"],
        "Pide que explique qué diferencia le pareció más importante."),
    reinforce="Di en voz alta una diferencia y una semejanza entre territorios y entre generaciones.",
    extend="Escribe una pregunta que le harías a una persona mayor sobre cómo era su infancia, para conversar solo si ella quiere.",
)
