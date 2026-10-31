"""Material del estudiante de 7.º básico, Historia, Geografía y Ciencias Sociales: OA 10 (sociedad medieval y orden estamental)."""
from __future__ import annotations

from hi5_lib import build

OA = "HI07 OA 10"

# ---------------------------------------------------------------- clase 1
F = ("Ficha 1 (resumen hecho para este cuaderno; las cifras de la aldea son de ejemplo). "
     "Visión cristiana: en la Europa medieval se creía que Dios estaba en el centro de la vida y que la vida en la Tierra era una preparación para la vida eterna. "
     "Tiempo: el domingo era día de misa y descanso; el año tenía fiestas religiosas, como Navidad y Pascua; la Cuaresma duraba 40 días antes de Pascua; las campanas del monasterio marcaban las horas de oración, que eran 8 al día. "
     "Se fue difundiendo una forma de contar los años desde el nacimiento de Cristo, propuesta por el monje Dionisio el Exiguo en el siglo VI. "
     "Aldea de ejemplo: 52 domingos al año y 30 fiestas de santos en que no se trabajaba en el campo.")
build(
    OA, 1, F,
    use="Aprenderé a comprender la visión cristiana del mundo y de la temporalidad en la Edad Media. Sirve para entender cómo organizaban el tiempo y qué sentido daban a la vida.",
    prior=["Sé qué papel tuvo la Iglesia en la formación de la Europa medieval.", "Sé que los años se cuentan antes y después de Cristo.", "Sé hacer sumas y restas simples."],
    explain=[
        "En la Europa medieval, la mayoría de las personas creía que Dios estaba en el centro de todo. La vida en la Tierra era una preparación para la vida eterna, y la Iglesia guiaba esa preparación con ceremonias, normas y enseñanzas. Esta visión del mundo se llama visión cristiana, y marcaba las decisiones y las costumbres.",
        "También organizaba el tiempo. El domingo era día de misa y descanso. El año tenía fiestas religiosas, como Navidad y Pascua, y la Cuaresma duraba 40 días antes de Pascua. Las campanas del monasterio marcaban las 8 horas de oración del día. Además, se fue difundiendo una forma de contar los años desde el nacimiento de Cristo, propuesta por el monje Dionisio el Exiguo en el siglo VI.",
        "Esta forma de ver el mundo no significa que todas las personas fueran iguales ni que no hubiera dudas o conflictos. Pero sirve para entender por qué los templos y los monasterios eran el centro de las aldeas. Para estudiar la mentalidad medieval se pregunta qué creían las personas y cómo esas creencias ordenaban su vida diaria.",
    ],
    vocab=[("visión cristiana", "forma de entender el mundo con Dios en el centro de la vida"), ("temporalidad", "forma en que una sociedad entiende y organiza el tiempo"), ("Cuaresma", "periodo de 40 días antes de Pascua"), ("liturgia", "conjunto de ceremonias religiosas"), ("mentalidad", "conjunto de ideas y creencias de una época")],
    worked=[
        ("Calcular días sin trabajo", "{F} ¿Cuántos días al año, entre domingos y fiestas de santos, no se trabajaba en el campo en la aldea de ejemplo?", ["Domingos: 52. Fiestas de santos: 30.", "Sumo: 52 + 30 = 82."], "82 días"),
        ("Interpretar una creencia", "{F} ¿Por qué se decía que la vida en la Tierra era una preparación?", ["La creencia era que había una vida eterna.", "La vida en la Tierra se veía como un paso previo."], "Porque se creía en una vida eterna después de esta"),
    ],
    mistakes=[("Pensar que toda la gente creía exactamente lo mismo.", "Se generaliza una visión del mundo.", "Había una visión cristiana dominante, pero también dudas, herejías y otras creencias."),
              ("Aplicar a la Edad Media ideas modernas sobre el tiempo, como el reloj.", "Se proyecta el presente al pasado.", "El tiempo se marcaba por campanas, fiestas y estaciones.")],
    T=[
        ("{F} ¿Cuántos días duraba la Cuaresma?", "40 días", "La ficha lo indica."),
        ("{F} ¿Cuántas horas de oración marcaban las campanas del monasterio?", "8 al día", "La ficha lo indica."),
        ("{F} ¿Desde qué hecho se fue difundiendo la forma de contar los años que propuso Dionisio el Exiguo?", "Desde el nacimiento de Cristo", "La ficha lo indica."),
        ("=", "{F} ¿Cuántos días al año no se trabajaba en el campo en la aldea de ejemplo, entre domingos y fiestas de santos, si hubiera 40 fiestas de santos en lugar de 30?", "52+40", "Se suman domingos y fiestas.", " días"),
        ("=", "{F} Si en la aldea de ejemplo se trabaja el resto del año de 365 días, ¿cuántos días se trabaja (con 52 domingos y 30 fiestas)?", "365-52-30", "Se resta lo no laborable al año.", " días"),
        ("{F} ¿Qué día era de misa y descanso?", "El domingo", "La ficha lo indica."),
        ("{F} ¿Qué se creía de la vida en la Tierra?", "Que era una preparación para la vida eterna", "La ficha lo indica."),
        ("{F} ¿En qué siglo propuso Dionisio el Exiguo contar los años desde el nacimiento de Cristo?", "En el siglo VI", "La ficha lo indica."),
        ("=", "{F} Si un monje reza las 8 horas de oración durante 5 días, ¿cuántas veces reza en total?", "8*5", "Se multiplican las horas diarias por los días.", " veces"),
        ("{F} Clasifica como práctica religiosa (R) o forma de medir el tiempo (T): 1) asistir a misa; 2) campanas que marcan las horas; 3) rezar una oración; 4) contar los 40 días de Cuaresma antes de Pascua.", "1 R, 2 T, 3 R, 4 T", "Asistir a misa y rezar son prácticas; las campanas y el conteo de días miden el tiempo."),
        ("{F} Ana dice: «En la Edad Media todos pensaban exactamente lo mismo». Corrígela.", "Había una visión cristiana dominante, pero también dudas, desacuerdos y otras creencias", "La ficha habla de una visión predominante."),
        ("{F} ¿Por qué las campanas eran importantes para el tiempo en una aldea sin relojes?", "Porque marcaban las horas de oración y ordenaban el día", "Servían como reloj para todos."),
        ("{F} Pedro dice: «Los medievales no tenían forma de organizar el año». ¿Qué datos de la ficha lo contradicen?", "El calendario de fiestas religiosas, la Cuaresma y los domingos organizaban el año", "La ficha da ejemplos."),
    ],
    ctx=("Un estudiante cuenta que su aldea de ejemplo tiene 52 domingos y 30 fiestas de santos libres de trabajo. Su compañero dice que eso sería flojera. ¿Qué respuesta histórica das? {F}", "Que esos días respondían a una visión cristiana que ordenaba el tiempo, no a flojera", "La mentalidad de la época explica el calendario."),
    sc=[("¿Qué es la visión cristiana?", "Una forma de entender el mundo con Dios en el centro de la vida", "Marcaba creencias y costumbres."),
        ("¿Cuántos días duraba la Cuaresma?", "40 días", "Eran los días antes de Pascua."),
        ("=", "{F} ¿Cuántos días hay en 3 semanas de Cuaresma si cada semana tiene 7 días?", "3*7", "Se multiplican semanas por días.", " días")],
    op=("Haz un calendario de una semana medieval de ejemplo con el domingo, una fiesta de un santo en martes y las 8 horas de oración marcadas por campanas. Escribe en dos líneas cómo cambia el trabajo del campo esa semana. {F}",
        "Domingo de misa y descanso; martes de fiesta de un santo sin trabajo; las campanas marcan la oración; trabajo de campo solo cuatro días.",
        ["incluye el domingo y la fiesta", "marca las campanas o las horas", "explica el efecto en el trabajo"], ["calendario dibujado", "dos líneas escritas"], ["pensar que se trabajaba todos los días", "usar relojes modernos"],
        "Pide que explique por qué la Iglesia tenía tanto peso en el calendario."),
    reinforce="Explica con tus palabras qué significa que la vida terrenal era una preparación.",
    extend="Escribe una pregunta sobre cómo se medían las horas en un monasterio de noche.",
)

# ---------------------------------------------------------------- clase 2
F = ("Ficha 2 (esquema hecho para este cuaderno; las cifras son de ejemplo). "
     "Los tres estamentos u órdenes: los que rezan (el clero: obispos, sacerdotes y monjes), los que combaten (la nobleza: caballeros y señores) y los que trabajan (los campesinos). "
     "Relaciones de dependencia: un señor entrega un feudo (tierra) a un vasallo, que a cambio le jura fidelidad y le presta servicio militar. Un siervo de la gleba trabaja la tierra del señor, no puede abandonarla sin permiso y entrega parte de su cosecha. "
     "Diezmo: la décima parte de la cosecha, que se entregaba a la Iglesia. "
     "Familia campesina de ejemplo: cosecha 50 sacos al año; entrega 5 de diezmo y 10 al señor.")
build(
    OA, 2, F,
    use="Aprenderé a analizar los estamentos y las relaciones de dependencia en la sociedad medieval. Sirve para entender quién debía qué a quién.",
    prior=["Sé qué es una jerarquía social.", "Sé que en la Edad Media había reinos y señores.", "Sé hacer restas y multiplicaciones simples."],
    explain=[
        "La sociedad medieval se explicaba con un esquema de tres estamentos: los que rezan (el clero), los que combaten (la nobleza) y los que trabajan (los campesinos). Cada grupo tenía una función y derechos distintos, y se creía que ese orden había sido querido por Dios. Era un orden estamental: se nacía en un estamento y era difícil cambiar.",
        "Entre las personas había relaciones de dependencia. Un señor entregaba un feudo (tierra) a un vasallo, que a cambio le juraba fidelidad y le prestaba servicio militar. Los campesinos, en particular los siervos de la gleba, trabajaban la tierra del señor, no podían irse sin permiso y entregaban parte de su cosecha. Además se pagaba el diezmo a la Iglesia: la décima parte de la cosecha.",
        "Este esquema simplifica la realidad. Había nobles pobres, campesinos libres con tierra propia y clérigos de origen campesino. El esquema muestra cómo se pensaba la sociedad, pero no describe la vida de cada persona. Para evaluarlo se compara con otras fuentes, como registros de cosechas y contratos.",
    ],
    vocab=[("estamento", "grupo social con función y derechos propios, al que se pertenecía por nacimiento"), ("feudo", "tierra entregada por un señor a un vasallo a cambio de fidelidad y servicio"), ("vasallo", "persona que jura fidelidad a un señor"), ("siervo de la gleba", "campesino sin libertad de abandonar la tierra del señor"), ("diezmo", "décima parte de la cosecha que se entregaba a la Iglesia")],
    worked=[
        ("Calcular lo que queda", "{F} ¿Cuántos sacos le quedan a la familia campesina después del diezmo y de lo que entrega al señor?", ["Cosecha: 50. Entrega 5 y 10.", "Resto: 50 − 5 − 10 = 35."], "35 sacos"),
        ("Identificar una dependencia", "{F} ¿Qué recibe un vasallo del señor y qué le da a cambio?", ["Recibe un feudo, es decir, tierra.", "A cambio da fidelidad y servicio militar."], "Recibe un feudo y da fidelidad y servicio militar"),
    ],
    mistakes=[("Pensar que todas las personas de un estamento vivían igual.", "Se toma el esquema como descripción de cada persona.", "Había nobles pobres y campesinos libres."),
              ("Creer que el siervo era un esclavo.", "Se confunden las dos situaciones.", "El siervo estaba ligado a la tierra, pero no era comprado y vendido como un esclavo.")],
    T=[
        ("{F} ¿Quiénes eran los que rezaban?", "El clero", "La ficha lo indica."),
        ("{F} ¿Qué entrega un señor a su vasallo?", "Un feudo, es decir, tierra", "La ficha lo indica."),
        ("{F} ¿Qué parte de la cosecha era el diezmo?", "La décima parte", "La ficha lo indica."),
        ("=", "{F} ¿Cuántos sacos de la cosecha se entregan en total, entre diezmo y señor?", "5+10", "Se suman las dos entregas.", " sacos"),
        ("=", "{F} Una familia cosecha 80 sacos y entrega la décima parte como diezmo. ¿Cuántos sacos son?", "80//10", "Se divide la cosecha entre 10.", " sacos"),
        ("{F} ¿Qué estamento era el de los que trabajan?", "Los campesinos", "La ficha lo indica."),
        ("=", "{F} Si 60 familias entregan 10 sacos cada una al señor, ¿cuántos sacos recibe en total?", "60*10", "Se multiplican las familias por los sacos de cada una.", " sacos"),
        ("{F} Relaciona cada función con su estamento: rezar, combatir, trabajar.", "Rezar: clero; combatir: nobleza; trabajar: campesinos", "Es el esquema de los tres estamentos."),
        ("{F} Clasifica cada obligación como del vasallo (V) o del siervo (S): 1) jurar fidelidad al señor; 2) trabajar la tierra del señor; 3) servicio militar; 4) no abandonar la tierra sin permiso.", "1 V, 2 S, 3 V, 4 S", "Cada obligación corresponde a una relación distinta."),
        ("{F} Ana dice: «Todos los campesinos eran siervos». Corrígela con un dato de la explicación de la clase.", "Había también campesinos libres con tierra propia", "Había variedad dentro del estamento."),
        ("{F} ¿Por qué se dice que el esquema de tres estamentos simplifica la realidad?", "Porque había nobles pobres, campesinos libres y clérigos de origen campesino", "El esquema no describe a cada persona."),
        ("{F} Pedro dice: «Un campesino podía abandonar fácilmente su tierra». ¿Qué relación de dependencia lo contradice?", "La del siervo de la gleba, que no podía irse sin permiso del señor", "La ficha la describe."),
        ("{F} ¿Qué fuente permitiría comprobar cuánto entregaba una familia campesina?", "Un registro de cosechas o un contrato del señorío", "Son fuentes de la época."),
    ],
    ctx=("En un juego de roles, un curso representa un señorío con un señor, un vasallo, un cura y familias campesinas. Si las familias deben entregar 2 de cada 10 sacos, ¿cuántos sacos entrega una familia que cosecha 50? {F}", "10 sacos", "50 ÷ 10 = 5, y 5 × 2 = 10."),
    sc=[("¿Qué es un feudo?", "Una tierra entregada por un señor a un vasallo a cambio de fidelidad y servicio", "Es la base del vasallaje."),
        ("¿Qué es el diezmo?", "La décima parte de la cosecha entregada a la Iglesia", "Se calcula dividiendo por 10."),
        ("=", "{F} ¿Cuántos sacos le quedan a una familia con 50 sacos si entrega 15 en total?", "50-15", "Se resta lo entregado a la cosecha.", " sacos")],
    op=("Dibuja un esquema con los tres estamentos y flechas que muestren qué da cada uno a los otros (por ejemplo, el campesino da trabajo y diezmo). Escribe una frase que explique por qué el esquema no describe la vida de cada persona. {F}",
        "Clero: oración y enseñanza; nobleza: protección; campesinos: trabajo y diezmo; el esquema no considera nobles pobres ni campesinos libres.",
        ["los tres estamentos con funciones", "flechas con lo que se da", "la frase señala un límite del esquema"], ["esquema dibujado", "frase escrita"], ["decir que todos vivían igual", "olvidar las relaciones de dependencia"],
        "Pide que explique qué diferencia hay entre un vasallo y un siervo."),
    reinforce="Nombra los tres estamentos y la función de cada uno.",
    extend="Escribe una pregunta sobre cómo se convertía un vasallo en señor de más tierras.",
)

# ---------------------------------------------------------------- clase 3
F = ("Ficha 3 (resumen hecho para este cuaderno; las cifras son de ejemplo). "
     "Vida rural: la gran mayoría de la población vivía en el campo. Un señorío tenía la casa o castillo del señor, la iglesia, el molino y las tierras de cultivo. Se usaba la rotación de tres campos: cada año uno se sembraba con trigo de invierno, otro con cebada o avena de primavera y el tercero descansaba. Señorío de ejemplo: cada campo mide 30 hectáreas. "
     "Vida urbana: tras la caída del Imperio de Occidente, muchas ciudades se redujeron o se despoblaron y el campo pasó a ser el centro de la vida; desde el siglo XI las ciudades volvieron a crecer, con murallas, mercados y ferias. Los burgueses eran habitantes de las ciudades dedicados al comercio y a oficios. Los gremios eran asociaciones de artesanos de un mismo oficio, con aprendices, oficiales y maestros. "
     "Taller de ejemplo: un maestro panadero con 2 oficiales y 3 aprendices.")
build(
    OA, 3, F,
    use="Aprenderé a examinar la vida rural y la vida urbana en la Edad Media. Sirve para comparar cómo vivían y trabajaban las personas en el campo y en la ciudad.",
    prior=["Sé qué son los estamentos.", "Sé qué es un siervo de la gleba.", "Sé multiplicar y restar con números pequeños."],
    explain=[
        "La mayoría de la gente vivía en el campo, en señoríos. Allí estaban la casa o castillo del señor, la iglesia, el molino y las tierras de cultivo. Para no agotar el suelo se usaba la rotación de tres campos: en cada año, uno se sembraba con trigo de invierno, otro con cebada o avena de primavera y el tercero descansaba.",
        "Tras la caída del Imperio de Occidente, muchas ciudades se redujeron o se despoblaron, y el campo pasó a ser el centro de la vida. Desde el siglo XI las ciudades volvieron a crecer, con murallas, mercados y ferias. Allí vivían los burgueses, dedicados al comercio y a oficios. Los artesanos de un mismo oficio se agrupaban en gremios, con aprendices, oficiales y maestros. En la ciudad había más movimiento de dinero que en el campo.",
        "Campo y ciudad estaban relacionados: la ciudad compraba alimentos del campo y el campo compraba productos de los artesanos. Aun así, la vida diaria era distinta: el ritmo del campo seguía las estaciones y el de la ciudad los mercados. No hay que verlos como mundos separados ni como lugares iguales en toda Europa.",
    ],
    vocab=[("señorío", "tierras y personas bajo la autoridad de un señor"), ("rotación de tres campos", "sistema en que un campo descansa cada año mientras se siembran los otros dos"), ("burgués", "habitante de la ciudad dedicado al comercio o a un oficio"), ("gremio", "asociación de artesanos de un mismo oficio"), ("feria", "mercado grande que se hacía en fechas fijas")],
    worked=[
        ("Calcular superficie cultivada", "{F} ¿Cuántas hectáreas se siembran cada año en el señorío de ejemplo?", ["Hay 3 campos de 30 hectáreas y uno descansa.", "Se siembran 2 × 30 = 60."], "60 hectáreas"),
        ("Contar personas de un taller", "{F} ¿Cuántas personas trabajan en el taller del maestro panadero?", ["Hay 1 maestro, 2 oficiales y 3 aprendices.", "Sumo: 1 + 2 + 3 = 6."], "6 personas"),
    ],
    mistakes=[("Pensar que todos vivían en ciudades.", "Se proyecta la vida actual al pasado.", "La gran mayoría vivía en el campo."),
              ("Creer que el campo y la ciudad eran mundos aislados.", "Se ignora el intercambio.", "La ciudad compraba alimentos y el campo compraba productos de los artesanos.")],
    T=[
        ("{F} ¿Qué pasó con muchas ciudades después de la caída del Imperio de Occidente y qué pasó a ser el centro de la vida?", "Se redujeron o se despoblaron; el campo pasó a ser el centro de la vida", "La ficha describe ese declive urbano."),
        ("{F} ¿Qué eran los gremios?", "Asociaciones de artesanos de un mismo oficio", "La ficha lo indica."),
        ("{F} ¿Desde qué siglo crecieron las ciudades?", "Desde el siglo XI", "La ficha lo indica."),
        ("=", "{F} ¿Cuántas hectáreas mide el total de los tres campos del señorío de ejemplo?", "3*30", "Se multiplican los campos por su superficie.", " hectáreas"),
        ("{F} El señorío de ejemplo siembra 60 hectáreas por año de un total de 90. ¿Qué parte del total descansa?", "Un tercio, es decir, 30 hectáreas", "Descansa uno de los tres campos."),
        ("{F} ¿Qué se sembraba cada año en los dos campos sembrados?", "Trigo de invierno y cebada o avena de primavera", "La ficha lo indica."),
        ("{F} ¿Quiénes eran los burgueses?", "Habitantes de las ciudades dedicados al comercio o a oficios", "La ficha lo indica."),
        ("=", "{F} Un taller de ejemplo tiene 1 maestro, 4 oficiales y 6 aprendices. ¿Cuántas personas trabajan en él?", "1+4+6", "Se suman las tres categorías.", " personas"),
        ("{F} Clasifica como vida rural (R) o urbana (U): 1) molino del señorío; 2) gremio de panaderos; 3) rotación de tres campos; 4) ferias en la ciudad.", "1 R, 2 U, 3 R, 4 U", "Cada elemento corresponde a un ámbito."),
        ("{F} ¿Por qué se usaba la rotación de tres campos?", "Para que el suelo no se agotara al dejar descansar un campo cada año", "La ficha dice que uno descansaba."),
        ("{F} Ana dice: «En la Edad Media todos vivían en ciudades». Corrígela.", "La gran mayoría de la población vivía en el campo", "La ficha lo indica."),
        ("{F} ¿Cómo se relacionaban el campo y la ciudad?", "La ciudad compraba alimentos del campo y el campo compraba productos de los artesanos", "Había intercambio entre ambos."),
        ("{F} ¿Qué diferencia había entre el ritmo de vida del campo y el de la ciudad?", "El campo seguía las estaciones y la ciudad, los mercados", "Cada ámbito marcaba el ritmo de otra manera."),
    ],
    ctx=("Un curso organiza una feria medieval con puestos de panadería, tejidos y herramientas. ¿Qué institución de la ciudad medieval representa esa feria y qué agrupaba a los artesanos de cada puesto? {F}", "Representa las ferias y los mercados; los gremios agrupaban a los artesanos", "La ficha nombra ambos."),
    sc=[("¿Qué es la rotación de tres campos?", "Un sistema donde un campo descansa cada año mientras se siembran los otros dos", "Evita agotar el suelo."),
        ("¿Qué era un gremio?", "Una asociación de artesanos de un mismo oficio", "Tenía aprendices, oficiales y maestros."),
        ("=", "{F} ¿Cuántas hectáreas se siembran en un señorío con tres campos de 40 hectáreas, si uno descansa?", "2*40", "Se multiplican los campos sembrados por su superficie.", " hectáreas")],
    op=("Haz un dibujo comparativo: a la izquierda, un señorío con casa del señor, iglesia, molino y tres campos; a la derecha, una ciudad con muralla, mercado y taller de gremio. Escribe tres semejanzas o diferencias en el ritmo de vida. {F}",
        "Señorío: casa del señor, iglesia, molino y campos con rotación; ciudad: muralla, mercado, taller; ritmo por estaciones frente a ritmo por mercados.",
        ["incluye elementos de ambos ámbitos", "escribe tres comparaciones", "las comparaciones usan la ficha"], ["dibujo comparativo", "tres líneas escritas"], ["mezclar elementos del campo y la ciudad", "no mencionar el ritmo de vida"],
        "Pide que explique por qué los gremios eran importantes en la ciudad."),
    reinforce="Nombra tres elementos de un señorío y tres de una ciudad.",
    extend="Escribe una pregunta sobre cómo llegaban los alimentos del campo a la ciudad.",
)

# ---------------------------------------------------------------- clase 4
F = ("Ficha 4 (resumen hecho para este cuaderno). "
     "Diversidad: las mujeres campesinas trabajaban en el campo y en tareas como hilar; algunas mujeres nobles administraban propiedades; Hildegarda de Bingen (1098 a 1179) fue abadesa, compositora y escritora; en muchas ciudades vivían comunidades judías y, en Hispania, también musulmanas. "
     "Movilidad limitada: un hijo de campesinos podía llegar a ser monje o sacerdote; en algunas ciudades, un siervo que vivía allí un año y un día quedaba libre; en un gremio se podía pasar de aprendiz a oficial y a maestro, pero llegar a maestro costaba dinero y años. "
     "Cambios: entre 1347 y 1351 la peste negra mató a una gran parte de la población de Europa, lo que hizo que faltaran trabajadores en el campo.")
build(
    OA, 4, F,
    use="Aprenderé a reconocer la diversidad de la sociedad medieval y cuán limitada era la movilidad social. Sirve para ver que no todos vivían igual ni podían cambiar de lugar social.",
    prior=["Sé qué eran los estamentos.", "Sé cómo vivían en el campo y la ciudad.", "Sé que un esquema simplifica la realidad."],
    explain=[
        "La sociedad medieval fue diversa. Las mujeres campesinas trabajaban en el campo y hilaban; algunas mujeres nobles administraban propiedades; otras, como Hildegarda de Bingen, fueron abadesas, compositoras y escritoras. En muchas ciudades vivían comunidades judías, y en Hispania también musulmanas. Cada región y cada época tuvo rasgos propios.",
        "La movilidad, es decir, la posibilidad de cambiar de lugar en la sociedad, era limitada pero no inexistente. Un hijo de campesinos podía llegar a ser monje o sacerdote; en algunas ciudades, un siervo que vivía allí un año y un día quedaba libre; en un gremio se podía pasar de aprendiz a oficial y a maestro, aunque costaba dinero y años.",
        "También hubo cambios. Entre 1347 y 1351 la peste negra mató a una gran parte de la población, y faltaron trabajadores en el campo. Esto muestra que la Edad Media no fue inmóvil. Al estudiar la sociedad medieval conviene evitar tanto la idea de un mundo oscuro e inmóvil como la de un mundo ideal.",
    ],
    vocab=[("diversidad", "existencia de personas y grupos distintos en una misma sociedad"), ("movilidad social", "posibilidad de cambiar de lugar en la sociedad"), ("abadesa", "mujer que dirige un monasterio"), ("peste negra", "epidemia que afectó a Europa entre 1347 y 1351"), ("aprendiz", "persona que aprende un oficio con un maestro")],
    worked=[
        ("Calcular una vida", "{F} ¿Cuántos años vivió Hildegarda de Bingen?", ["Nació en 1098 y murió en 1179.", "Resto: 1179 − 1098 = 81."], "81 años"),
        ("Identificar una vía de movilidad", "{F} ¿Qué camino tenía un hijo de campesinos para cambiar su situación?", ["La ficha dice que podía hacerse monje o sacerdote.", "Es una vía limitada, pero real."], "Hacerse monje o sacerdote"),
    ],
    mistakes=[("Decir que en la Edad Media era imposible cambiar de situación.", "Se ignoran las excepciones.", "Había vías de movilidad, aunque limitadas."),
              ("Creer que todas las mujeres de la Edad Media tenían la misma vida.", "Se generaliza.", "Había campesinas, nobles y abadesas, con vidas distintas.")],
    T=[
        ("{F} ¿Quién fue Hildegarda de Bingen?", "Una abadesa, compositora y escritora", "La ficha lo indica."),
        ("{F} ¿En qué años ocurrió la peste negra?", "Entre 1347 y 1351", "La ficha lo indica."),
        ("{F} ¿Cuánto tiempo debía vivir un siervo en una ciudad para quedar libre, en algunas ciudades?", "Un año y un día", "La ficha lo indica."),
        ("=", "{F} ¿Cuántos años duró la peste negra, de 1347 a 1351?", "1351-1347", "Se restan los años.", " años"),
        ("{F} ¿Qué comunidades vivían en muchas ciudades medievales, según la ficha?", "Comunidades judías", "La ficha lo indica."),
        ("{F} ¿Qué problema trajo la peste negra al campo?", "Faltaron trabajadores", "La ficha lo indica."),
        ("=", "{F} Un taller de gremio tiene 12 aprendices y de ellos 3 llegan a maestro. ¿Cuántos no llegan a maestro?", "12-3", "Se resta los que llegaron al total.", " aprendices"),
        ("{F} Clasifica como vía de movilidad (M) o límite (L): 1) hacerse monje; 2) llegar a maestro cuesta dinero y años; 3) vivir un año y un día en una ciudad; 4) nacer siervo de la gleba.", "1 M, 2 L, 3 M, 4 L", "Algunas opciones permitían cambiar y otras lo dificultaban."),
        ("{F} Ana dice: «Todas las mujeres de la Edad Media tenían la misma vida». Corrígela con dos ejemplos.", "Había mujeres campesinas que trabajaban en el campo y mujeres como Hildegarda, abadesa y escritora", "La ficha muestra distintas vidas."),
        ("{F} Pedro dice: «En la Edad Media nada cambió». Corrígelo con un dato.", "La peste negra, entre 1347 y 1351, redujo la población y faltaron trabajadores en el campo", "Hubo cambios importantes."),
        ("{F} ¿Por qué se dice que la movilidad era limitada y no inexistente?", "Porque había vías de cambio, como ser monje o maestro de gremio, pero costaban esfuerzo, dinero o suerte", "La ficha muestra ejemplos y condiciones."),
        ("{F} ¿Qué fuente permitiría saber cuántos siervos quedaron libres en una ciudad?", "Registros de la ciudad o documentos de liberación", "Se necesitan fuentes de la época."),
        ("{F} Un compañero dice: «Todos en la Edad Media tenían la misma religión». ¿Qué dato de la ficha lo contradice?", "Vivían comunidades judías y, en Hispania, musulmanas", "La ficha nombra otros grupos."),
    ],
    ctx=("Un museo exhibe la imagen de un taller de gremio con un maestro, dos oficiales y tres aprendices. Un visitante dice: «Todos llegaban a maestro». ¿Qué dato de la ficha le muestras? {F}", "Que llegar a maestro costaba dinero y años, así que no todos llegaban", "La movilidad era limitada."),
    sc=[("¿Qué es la movilidad social?", "La posibilidad de cambiar de lugar en la sociedad", "En la Edad Media era limitada."),
        ("¿Qué es un aprendiz?", "Una persona que aprende un oficio con un maestro", "Es el primer nivel del gremio."),
        ("=", "{F} ¿Cuántos años vivió una persona que nació en 1098 y murió en 1179?", "1179-1098", "Se restan los años.", " años")],
    op=("Escribe una carta imaginaria de 6 líneas de un joven de familia campesina que quiere cambiar su situación. Elige una vía de la ficha (monasterio, ciudad o gremio), explica qué necesita, qué obstáculo tiene y qué no sabe todavía. {F}",
        "Quiero hacerme aprendiz en la ciudad; necesito pagar y esperar años; mi señor puede no dejarme; no sé si lo lograré.",
        ["elige una vía real de la ficha", "nombra un obstáculo", "evita inventar hechos que contradigan la ficha"], ["carta escrita"], ["decir que cambiar era fácil", "ignorar los límites"],
        "Pide que explique por qué un siervo solo podía irse con permiso o por una vía especial."),
    reinforce="Nombra tres vías de movilidad y tres límites en la sociedad medieval.",
    extend="Escribe una pregunta sobre cómo se transmitían los oficios de padres a hijos.",
)
