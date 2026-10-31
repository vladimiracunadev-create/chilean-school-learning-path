"""Cuaderno del estudiante, 6.º básico Ciencias Naturales: OA 16 (capas de la Tierra) y OA 17 (el suelo)."""
from __future__ import annotations

from student_content_cn6_b import task
from student_lessons import arith, ex, register

OA16 = "CN06 OA 16"
OA17 = "CN06 OA 17"

# ================================================================ OA 16, clase 1
register(
    OA16, 1,
    materials="Papel y lápiz. Los datos están escritos en el cuaderno.",
    use="Aprenderé a describir la atmósfera, la litósfera y la hidrósfera con datos y a separar lo que muestran los datos de lo que yo opino. Sirve para entender de dónde vienen el aire, el agua y los minerales que usamos.",
    prior=["Sé que el agua del planeta está en océanos, glaciares, ríos y lagos.", "Sé que el aire es una mezcla de gases."],
    explain=[
        "La Tierra tiene tres capas que estudiamos aquí. La atmósfera es la capa de gases que rodea al planeta. La litósfera es la capa rocosa y sólida de la superficie: las rocas, los minerales y el suelo. La hidrósfera es toda el agua del planeta: océanos, ríos, lagos, hielo y aguas subterráneas.",
        "Los datos describen cada capa. Atmósfera: de cada 100 partes de aire seco, cerca de 78 son nitrógeno, 21 son oxígeno y 1 es de otros gases. Hidrósfera: el agua cubre cerca de 71 de cada 100 partes de la superficie de la Tierra. Litósfera: es la parte donde viven las plantas y de donde sacamos minerales, como el cobre, y rocas para construir.",
        "Una observación es un dato como «el aire tiene 21 partes de oxígeno por cada 100». Una interpretación es una idea que agregamos, como «por eso la atmósfera es la capa más importante». Las tres capas permiten la vida y entregan recursos, es decir, materiales que usamos las personas.",
    ],
    vocab=[("atmósfera", "capa de gases que rodea la Tierra"), ("litósfera", "capa rocosa y sólida de la Tierra, con rocas, minerales y suelo"), ("hidrósfera", "conjunto de toda el agua del planeta"), ("recurso", "material de la naturaleza que las personas usamos"), ("mineral", "sustancia sólida natural que se encuentra en las rocas")],
    worked=[
        {"title": "Leer una proporción", "problem": "De cada 100 partes de aire, 21 son oxígeno y 78 son nitrógeno. ¿Cuántas partes entre los dos suman?", "steps": ["Se suman los dos datos.", "21 + 78 = 99."], "answer": "99 partes de 100"},
        {"title": "Observación o interpretación", "problem": "Frase A: «El agua cubre cerca de 71 de cada 100 partes de la superficie». Frase B: «Por eso el planeta debería llamarse Océano». ¿Cuál es la observación?", "steps": ["La frase A es un dato.", "La frase B es una idea que agrega una persona."], "answer": "La frase A es observación; la B es interpretación"},
    ],
    mistakes=[
        {"wrong": "Decir que el aire es solo oxígeno.", "why": "Se confunde el gas que respiramos con todo el aire.", "fix": "El aire tiene cerca de 78 partes de nitrógeno y 21 de oxígeno por cada 100."},
        {"wrong": "Pensar que la litósfera es solo las montañas.", "why": "Se piensa solo en lo que se ve alto.", "fix": "Incluye rocas, minerales y suelo en cualquier lugar."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué capa de la Tierra es una mezcla de gases que rodea al planeta?", "La atmósfera", "Está formada por gases como nitrógeno y oxígeno."),
            ex("¿Qué capa incluye océanos, ríos, lagos y hielo?", "La hidrósfera", "Es toda el agua del planeta."),
            ex("¿En qué capa están las rocas y el suelo donde crecen las plantas?", "En la litósfera", "Es la capa rocosa y sólida."),
        ],
        "understand": [
            ex("Frase: «El oxígeno es 21 de cada 100 partes del aire». ¿Observación o interpretación?", "Observación", "Es un dato."),
            ex("Frase: «La capa más importante es la hidrósfera». ¿Observación o interpretación?", "Interpretación", "Es una opinión que los datos no muestran."),
            ex("El cobre que se extrae de una mina, ¿qué recurso es: del aire, del agua o de las rocas?", "De las rocas", "Los minerales están en la litósfera."),
        ],
        "apply": [
            arith("De cada 100 partes de la superficie de la Tierra, 71 están cubiertas por agua. ¿Cuántas partes no están cubiertas por agua?", "100-71", "Se resta del total la parte con agua.", " partes"),
            arith("En el aire, 78 partes son nitrógeno y 21 son oxígeno. ¿Cuántas partes más de nitrógeno que de oxígeno hay?", "78-21", "Se resta el dato menor al mayor.", " partes"),
            ex("Clasifica en orden estos tres recursos: aire para respirar, agua de un río, cobre de una mina. Escribe la capa de cada uno.", "Atmósfera, hidrósfera, litósfera", "Cada recurso viene de una capa distinta."),
        ],
        "reason": [
            ex("Ema dice: «En el aire hay 21 partes de oxígeno y 79 de nada». ¿Qué dato corrige su error?", "Las otras 79 partes son nitrógeno y otros gases", "El aire no es solo oxígeno, hay otros gases."),
            ex("Un compañero afirma que la litósfera es el recurso más valioso y lo apoya con «porque yo creo». ¿Qué le falta a esa frase?", "Un dato que lo muestre", "Una afirmación necesita evidencia."),
        ],
        "challenge": [
            arith("En 1.000 litros de aire, ¿cuántos litros de oxígeno hay si por cada 100 litros hay 21?", "(1000//100)*21", "1.000 litros son diez veces 100 litros, así que hay 10 grupos de 21 litros.", " litros"),
            ex("¿Cuál es una limitación de la tabla «71 partes de agua, 29 partes de tierra»: que simplifica el planeta o que entrega un dato?", "Que simplifica el planeta", "No dice cuánta agua dulce hay ni dónde está."),
        ],
    },
    context=[ex("Una persona de tu casa dice «el agua que tomamos viene de un río o de un pozo». ¿A qué capa pertenecen el agua del río y el agua del pozo?", "A la hidrósfera", "Los ríos y las aguas subterráneas son parte del agua del planeta.")],
    selfcheck=[
        ex("¿Qué gas es 78 de cada 100 partes del aire?", "El nitrógeno", "Es el gas más abundante."),
        ex("¿De qué capa son parte los minerales?", "De la litósfera", "Están en las rocas."),
        ex("Una interpretación, ¿es un dato o una idea agregada?", "Una idea agregada", "No sale directo de la tabla."),
    ],
    open_task=task(
        "Dibuja una tabla con tres columnas (capa, qué contiene, un recurso que usamos). Complétala con la atmósfera, la litósfera y la hidrósfera. Agrega una fila de datos: aire (78 de nitrógeno, 21 de oxígeno, 1 de otros gases por cada 100) y agua (71 de cada 100 partes de la superficie). Escribe dos observaciones y una interpretación.",
        "Atmósfera: gases; aire para respirar. Hidrósfera: océanos y ríos; agua para beber. Litósfera: rocas y suelo; cobre. O: el oxígeno es 21 de cada 100. O: el agua cubre 71 de cada 100 partes de la superficie. I: el agua es lo más importante.",
        ["tres capas con contenido y recurso", "dos observaciones con datos", "una interpretación marcada"],
        ["tabla completa", "frases rotuladas"],
        ["poner el mismo recurso en dos capas", "escribir una opinión como dato"],
        "Pregunta cuál de sus frases no se podría comprobar con una medición.",
    ),
    reinforce="Escribe tres frases: una sobre cada capa, y marca si es observación o interpretación.",
    extend="Averigua con una persona de tu casa qué recursos de la litósfera usan todos los días, como la sal o los materiales de construcción.",
)

# ================================================================ OA 16, clase 2
register(
    OA16, 2,
    materials="Papel y lápiz. Los datos están escritos en el cuaderno.",
    use="Aprenderé a formular preguntas comprobables y predicciones sobre cómo usamos los recursos de las capas de la Tierra. Sirve para anticipar el efecto de proteger una capa.",
    prior=["Sé qué contienen la atmósfera, la litósfera y la hidrósfera.", "Sé que una predicción usa «Si…, entonces…»."],
    explain=[
        "Una pregunta comprobable relaciona un dato con otro. Por ejemplo: «¿cuántos litros de agua puede ahorrar una familia si cada persona usa 20 litros menos por día?». Se responde con una cuenta y con datos de ejemplo, como que una casa tiene 4 personas.",
        "Una predicción usa la proporción conocida. Si en 100 litros de aire hay 21 litros de oxígeno, entonces en 500 litros hay 105 litros de oxígeno, porque 500 es cinco veces 100. Si una persona gasta 150 litros de agua al día, entonces 4 personas gastan 600 litros al día.",
        "Proteger una capa también se puede predecir: si disminuye la basura que va a un río, entonces el agua del río estará menos contaminada. Los datos de esta clase son de ejemplo: sirven para practicar a predecir, no para afirmar cifras reales de tu ciudad.",
    ],
    vocab=[("proporción", "relación entre dos cantidades que cambian juntas"), ("ahorrar", "usar menos de algo para que dure más"), ("contaminación", "presencia de sustancias que dañan el ambiente"), ("predicción", "resultado esperado apoyado en datos"), ("datos de ejemplo", "datos inventados para practicar")],
    worked=[
        {"title": "Predecir con proporción", "problem": "En 100 litros de aire hay 21 litros de oxígeno. ¿Cuántos litros de oxígeno predices en 300 litros de aire?", "steps": ["300 es 3 veces 100.", "3 × 21 = 63."], "answer": "63 litros"},
        {"title": "Predecir un ahorro", "problem": "Una casa tiene 4 personas. Si cada una ahorra 20 litros de agua al día, ¿cuántos litros ahorra la casa en un día?", "steps": ["Cada persona ahorra 20 litros.", "4 × 20 = 80."], "answer": "80 litros al día"},
    ],
    mistakes=[
        {"wrong": "Usar datos de ejemplo como si fueran cifras reales de tu ciudad.", "why": "Se pierde la diferencia entre ejemplo y medición.", "fix": "Escribe «datos de ejemplo» y no los uses como hechos."},
        {"wrong": "Predecir sin decir en qué dato te apoyas.", "why": "Parece una adivinanza.", "fix": "Usa «Si… entonces…» y nombra el dato."},
    ],
    tiers={
        "recovery": [
            ex("¿Cuál es una pregunta comprobable: «¿Cuántos litros de agua ahorra una casa si cada persona usa menos?» o «¿Qué capa es más bonita?»?", "¿Cuántos litros de agua ahorra una casa si cada persona usa menos?", "Se responde con una cuenta."),
            ex("Si en 100 litros de aire hay 21 litros de oxígeno, ¿cuántos hay en 200 litros?", "42 litros", "200 es el doble de 100, así que también se duplica el oxígeno."),
            ex("Si disminuye la basura que cae a un río, ¿el agua del río estará más contaminada o menos contaminada?", "Menos contaminada", "Hay menos desechos en el agua."),
        ],
        "understand": [
            ex("¿Cuál es una predicción bien escrita: (a) «El agua es importante» o (b) «Si cada persona ahorra 10 litros, entonces una casa de 3 personas ahorrará 30 litros»?", "(b)", "Tiene «si… entonces» y se puede calcular."),
            ex("En Ciencias, ¿qué significa un dato de ejemplo?", "Un dato inventado para practicar", "No es una medición real."),
            ex("¿Para qué sirve usar la proporción de 21 litros de oxígeno en 100 litros de aire?", "Para predecir cuánto oxígeno hay en otra cantidad de aire", "La proporción se mantiene."),
        ],
        "apply": [
            arith("Si en 100 litros de aire hay 21 litros de oxígeno, ¿cuántos litros de oxígeno predices en 500 litros de aire?", "5*21", "500 es cinco veces 100.", " litros"),
            arith("Una persona gasta 150 litros de agua al día. ¿Cuántos litros gastan 4 personas?", "4*150", "Se multiplica el consumo por el número de personas.", " litros"),
            arith("Una casa de 5 personas ahorra 15 litros de agua por persona al día. ¿Cuántos litros ahorra la casa en un día?", "5*15", "Se multiplica el ahorro por persona por el número de personas.", " litros"),
        ],
        "reason": [
            ex("Mario predijo que 300 litros de aire tendrían 42 litros de oxígeno. Con la proporción de 21 litros por cada 100 litros, ¿qué debe corregir?", "La predicción, que debía ser 63 litros", "300 litros son 3 grupos de 21 litros."),
            ex("Ana dice: «Los datos de ejemplo prueban que mi ciudad gasta 150 litros por persona». ¿Qué error comete?", "Usa datos de ejemplo como si fueran reales", "Los datos de ejemplo no sirven para afirmar cifras de una ciudad."),
        ],
        "challenge": [
            arith("Una casa gasta 600 litros de agua al día. Si logra ahorrar 90 litros por día, ¿cuántos litros gastará en un día?", "600-90", "Se resta el ahorro al consumo.", " litros"),
            arith("Con ese ahorro de 90 litros por día, ¿cuántos litros ahorra la casa en 7 días?", "7*90", "Se multiplica el ahorro diario por los días.", " litros"),
        ],
    },
    context=[ex("Una persona de tu casa quiere medir cuántos litros de agua usa lavando la loza en un balde de 10 litros llenado 3 veces al día. ¿Cuántos litros usa en un día?", "30 litros", "Se multiplica el balde por las veces.")],
    selfcheck=[
        ex("Si en 100 litros de aire hay 21 de oxígeno, ¿cuántos hay en 400 litros?", "84 litros", "400 es cuatro veces 100."),
        ex("¿Con qué palabras empieza una predicción?", "Si", "Se escribe «Si…, entonces…»."),
        ex("¿Los datos de ejemplo son mediciones reales?", "No", "Son datos de práctica."),
    ],
    open_task=task(
        "Usa estos datos de ejemplo: una persona gasta 150 litros de agua al día; en 100 litros de aire hay 21 litros de oxígeno. Escribe dos preguntas comprobables y dos predicciones con «Si…, entonces…», una sobre el agua de una casa de 3 personas y otra sobre el oxígeno de 400 litros de aire. Calcula los resultados.",
        "Si una casa de 3 personas gasta 150 litros por persona, entonces gastará 450 litros al día. Si hay 21 litros de oxígeno en 100 litros de aire, entonces en 400 litros habrá 84 litros.",
        ["dos preguntas comprobables", "dos predicciones con «si»", "cálculos correctos"],
        ["preguntas", "predicciones", "cuentas"],
        ["usar los datos como reales", "no calcular el resultado"],
        "Pregunta qué cambiaría si la casa tuviera 6 personas.",
    ),
    reinforce="Haz otra predicción sobre el ahorro de agua usando un número de personas distinto.",
    extend="Averigua con una persona de tu casa cuántas veces al día usan un balde o una manguera y cuántos litros caben, y calcula el uso diario.",
)

# ================================================================ OA 16, clase 3
register(
    OA16, 3,
    materials="Papel y lápiz. Dibuja el modelo con flechas.",
    use="Aprenderé a modelar las capas de la Tierra y cómo interactúan, y a ubicar en ellas los recursos y las amenazas. Sirve para entender que cuidar una capa ayuda a las demás.",
    prior=["Sé qué contiene cada capa.", "Sé que el agua se evapora y vuelve como lluvia."],
    explain=[
        "Un modelo de las tres capas puede ser un dibujo con tres recuadros: arriba la atmósfera, en el centro la hidrósfera y abajo la litósfera. Las flechas muestran que las capas se relacionan. El agua de los mares y ríos (hidrósfera) se evapora y llega a la atmósfera. En las nubes se condensa y cae como lluvia sobre la litósfera.",
        "Los seres vivos usan las tres capas. Una planta toma agua de la hidrósfera, nutrientes del suelo de la litósfera y dióxido de carbono de la atmósfera. Las personas usamos aire, agua y minerales. Las amenazas también conectan las capas: el humo contamina la atmósfera, y la lluvia puede llevar esos contaminantes al suelo y a los ríos.",
        "El modelo tiene límites. En la realidad las capas no están separadas por líneas: hay aire disuelto en el agua, agua dentro del suelo y polvo en el aire. Por eso un buen modelo se acompaña de una frase que dice qué simplifica.",
    ],
    vocab=[("interacción", "relación en que un cambio en una capa afecta a otra"), ("evaporación", "paso del agua líquida a gas"), ("nutriente", "sustancia del suelo que las plantas necesitan"), ("contaminante", "sustancia que daña el ambiente"), ("modelo", "representación simplificada de algo")],
    worked=[
        {"title": "Ubicar en el modelo", "problem": "¿En qué capa está cada cosa: nube, océano, roca de cobre?", "steps": ["La nube está en el aire: atmósfera.", "El océano es agua: hidrósfera.", "El cobre está en las rocas: litósfera."], "answer": "Atmósfera, hidrósfera, litósfera"},
        {"title": "Seguir una flecha", "problem": "Una flecha va de «lluvia» a «río». ¿Entre qué capas se mueve el agua?", "steps": ["La lluvia cae desde la atmósfera.", "El río es parte de la hidrósfera."], "answer": "De la atmósfera a la hidrósfera"},
    ],
    mistakes=[
        {"wrong": "Dibujar las capas como si no se tocaran.", "why": "Se olvida que interactúan.", "fix": "Agrega flechas que muestren intercambios, como la evaporación y la lluvia."},
        {"wrong": "Pensar que contaminar el aire no afecta al agua ni al suelo.", "why": "No se consideran las conexiones.", "fix": "Sigue las flechas: la lluvia lleva contaminantes del aire al suelo y los ríos."},
    ],
    tiers={
        "recovery": [
            ex("¿En qué capa está el viento: atmósfera, hidrósfera o litósfera?", "Atmósfera", "El viento es aire en movimiento."),
            ex("¿En qué capa está un lago?", "Hidrósfera", "Es parte del agua del planeta."),
            ex("¿En qué capa está una piedra?", "Litósfera", "Es parte de la capa rocosa."),
        ],
        "understand": [
            ex("En el modelo, ¿qué muestra una flecha entre dos capas?", "Que se relacionan e intercambian algo", "Por ejemplo, agua o contaminantes."),
            ex("¿Por qué cuidar el aire también ayuda a cuidar el agua?", "Porque la lluvia lleva contaminantes del aire a los ríos", "Las capas están conectadas."),
            ex("¿Cuál es una limitación del dibujo de tres recuadros: que separa las capas con líneas o que usa un rótulo?", "Que separa las capas con líneas", "En la realidad hay agua en el suelo y aire en el agua."),
        ],
        "apply": [
            ex("Una planta toma agua, nutrientes del suelo y dióxido de carbono. Escribe en orden la capa de donde viene cada uno.", "Hidrósfera, litósfera, atmósfera", "El agua es hidrósfera, el suelo es litósfera y el dióxido de carbono es un gas del aire."),
            ex("Una flecha en el modelo va de «océano» a «nube». ¿Qué cambio de estado representa?", "Evaporación", "El agua líquida pasa a gas."),
            ex("Escribe la capa de origen de cada ítem, en este orden: oxígeno que respira un perro, sal de una mina, agua de un estanque.", "Atmósfera, litósfera, hidrósfera", "El oxígeno es un gas del aire, la sal de mina es mineral y el estanque es agua."),
        ],
        "reason": [
            ex("Rosa dice que si se contamina el suelo, el agua del río no se afecta. Con el modelo, ¿qué conexión la contradice?", "La lluvia o el agua subterránea puede llevar contaminantes del suelo al río", "El agua conecta litósfera e hidrósfera."),
            ex("Un compañero dice que el modelo de tres cajas es una copia exacta de la Tierra. ¿Qué responderías?", "Que es un modelo simplificado con límites", "No muestra todas las mezclas entre capas."),
        ],
        "challenge": [
            ex("Sigue la cadena: humo de una fábrica, suelo del cerro donde cae la ceniza, agua de un río. Escribe la capa de cada elemento en orden.", "Atmósfera, litósfera, hidrósfera", "El humo viaja por el aire, el suelo es parte de la litósfera y el río es agua."),
            ex("Una mina de cobre amenaza con contaminar el agua del suelo. ¿Qué dos capas están en conflicto en esa situación?", "Litósfera e hidrósfera", "El mineral viene de la litósfera y el agua es hidrósfera."),
        ],
    },
    context=[ex("Una persona de tu casa dice «el basural de la comuna contamina el río». ¿Qué capa se contamina primero y qué capa recibe después la contaminación?", "Primero la litósfera y después la hidrósfera", "El basural está en el suelo y el agua lleva los residuos al río.")],
    selfcheck=[
        ex("El humo de una fábrica, ¿contamina primero la atmósfera o la litósfera?", "La atmósfera", "El humo sale al aire."),
        ex("¿Qué capa aporta nutrientes a una planta?", "La litósfera", "El suelo tiene los nutrientes."),
        ex("¿Las capas están completamente separadas?", "No", "Se relacionan entre sí."),
    ],
    open_task=task(
        "Dibuja tres recuadros (atmósfera, hidrósfera, litósfera) con flechas entre ellos. Rotula al menos tres flechas (por ejemplo, evaporación, lluvia, planta toma agua). Escribe un recurso en cada recuadro y una amenaza que conecte dos capas. Termina con una limitación de tu modelo.",
        "Atmósfera: aire. Hidrósfera: agua del río. Litósfera: suelo. Flecha: evaporación de hidrósfera a atmósfera; lluvia de atmósfera a litósfera. Amenaza: humo que cae con la lluvia. Limitación: no muestra las mezclas.",
        ["tres recuadros con flechas rotuladas", "un recurso en cada capa y una amenaza", "una limitación"],
        ["dibujo", "rótulos"],
        ["dibujar capas sin conexiones", "no escribir la limitación"],
        "Pregunta qué pasaría en su modelo si desaparece una flecha.",
    ),
    reinforce="Explica con una flecha de tu modelo por qué cuidar el suelo también ayuda a un río cercano.",
    extend="Averigua con una persona de tu casa qué tipo de residuos se separan para reciclar y a qué capa evitan contaminar.",
)

# ================================================================ OA 16, clase 4
register(
    OA16, 4,
    materials="Papel y lápiz. Los datos están escritos en el cuaderno.",
    use="Aprenderé a comparar medidas de protección de las capas de la Tierra con un criterio y a escoger la mejor con evidencia. Sirve para proponer acciones realistas.",
    prior=["Sé qué contiene cada capa y cómo se conectan.", "Sé comparar usando una tabla."],
    explain=[
        "Proteger las capas de la Tierra significa evitar su contaminación y usar sus recursos con cuidado. Para atmósfera: usar menos transporte con humo y plantar árboles. Para litósfera: reciclar, evitar basurales y cuidar el suelo. Para hidrósfera: no botar basura a ríos y mares, y ahorrar agua.",
        "Para decidir cuál medida es mejor usamos criterios. Los tres que usaremos son: cuánto ayuda a proteger (de 1 a 3 puntos), cuán fácil es hacerla (de 1 a 3) y a cuántas personas alcanza (de 1 a 3). Sumamos los puntos de cada medida: la que suma más es la mejor según esos criterios.",
        "Ejemplo con datos de ejemplo. Medida A, ahorrar agua en casa: ayuda 2, facilidad 3, alcance 2, total 7. Medida B, plantar árboles en el barrio: ayuda 3, facilidad 2, alcance 3, total 8. Según los criterios, B es mejor que A. Pero los puntajes son una opinión informada, y otro grupo podría usar otros criterios. Eso es una limitación.",
    ],
    vocab=[("medida de protección", "acción para evitar daños a una capa de la Tierra"), ("criterio", "regla para comparar"), ("puntaje", "número que se da según un criterio"), ("alcance", "cuántas personas o lugares abarca una medida"), ("reciclar", "convertir residuos en materiales para usar de nuevo")],
    worked=[
        {"title": "Sumar puntajes", "problem": "Una medida tiene ayuda 3, facilidad 2 y alcance 1. ¿Cuántos puntos suma?", "steps": ["Se suman los tres puntajes.", "3 + 2 + 1 = 6."], "answer": "6 puntos"},
        {"title": "Elegir la mejor", "problem": "La medida A suma 7 y la B suma 8. ¿Cuál es mejor según los criterios?", "steps": ["Se compara el total.", "8 es mayor que 7."], "answer": "La medida B"},
    ],
    mistakes=[
        {"wrong": "Elegir la medida que más le gusta a uno sin usar los puntajes.", "why": "No se aplicó el criterio.", "fix": "Suma los puntajes y compara los totales."},
        {"wrong": "Pensar que el puntaje final es una verdad absoluta.", "why": "Los puntajes son una decisión de las personas.", "fix": "Anota que podría cambiar con otros criterios."},
    ],
    tiers={
        "recovery": [
            ex("Usar menos los vehículos que echan humo, ¿protege principalmente la atmósfera, la litósfera o la hidrósfera?", "La atmósfera", "El humo contamina el aire."),
            ex("No botar basura al río, ¿protege principalmente la atmósfera, la litósfera o la hidrósfera?", "La hidrósfera", "El río es agua."),
            ex("Reciclar y evitar basurales, ¿protege principalmente la atmósfera, la litósfera o la hidrósfera?", "La litósfera", "Los residuos se acumulan en el suelo."),
        ],
        "understand": [
            ex("En esta clase, ¿qué es un criterio de comparación?", "Una regla para comparar las medidas", "Con el mismo criterio se juzga cada medida."),
            ex("¿Por qué los puntajes de las medidas son una limitación?", "Porque son una opinión informada y otro grupo podría poner otros puntajes", "No son mediciones exactas."),
            ex("Una medida que ayuda mucho, pero que casi nadie puede hacer, ¿obtiene buen puntaje en alcance?", "No", "Su alcance es bajo."),
        ],
        "apply": [
            arith("La medida C tiene ayuda 2, facilidad 3 y alcance 3. ¿Cuántos puntos suma?", "2+3+3", "Se suman los tres puntajes.", " puntos"),
            arith("La medida D tiene ayuda 3, facilidad 1 y alcance 2. ¿Cuántos puntos suma?", "3+1+2", "Se suman los tres puntajes.", " puntos"),
            ex("Ordena de mayor a menor según su total: C suma 8, D suma 6, E suma 7.", "C, E, D", "8 es mayor que 7 y 7 es mayor que 6."),
        ],
        "reason": [
            ex("Luis dice que una medida con total 6 es mejor que una con total 8 porque «es más fácil». ¿Qué criterio olvidó considerar?", "Los otros dos criterios, ayuda y alcance", "El total considera los tres criterios."),
            ex("Dos grupos puntúan la misma medida con 8 y con 5. ¿Qué indica eso sobre los puntajes?", "Que dependen de quién los pone", "Son una opinión informada."),
        ],
        "challenge": [
            arith("Un curso de 30 estudiantes propone una medida y 24 se comprometen a hacerla. ¿Cuántos estudiantes no se comprometen?", "30-24", "Se resta del total los que sí se comprometen.", " estudiantes"),
            ex("Si dos medidas empatan en total, ¿qué puedes hacer para decidir sin inventar datos: agregar un nuevo criterio o lanzar una moneda?", "Agregar un nuevo criterio", "Un nuevo criterio permite diferenciar las medidas."),
        ],
    },
    context=[ex("Tu barrio propone dos medidas: A (puntaje total 7), poner basureros de reciclaje, y B (puntaje total 9), plantar árboles con ayuda de los vecinos. ¿Cuál escogerías con el criterio de los puntajes?", "La medida B", "Su total es mayor.")],
    selfcheck=[
        ex("¿Cuántos puntos suma una medida con 2, 2 y 3?", "7", "2 + 2 + 3 = 7."),
        ex("¿Qué capa protege no botar basura a los ríos?", "La hidrósfera", "El agua es hidrósfera."),
        ex("¿Los puntajes son una verdad exacta?", "No", "Son una opinión informada."),
    ],
    open_task=task(
        "Compara estas tres medidas con puntajes de ayuda, facilidad y alcance (1 a 3): Medida X, separar la basura en casa: 2, 3, 2. Medida Y, no tirar aceite usado por el desagüe: 3, 3, 2. Medida Z, usar menos el auto en un barrio: 3, 1, 3. Calcula el total de cada una, escoge la mejor y escribe una limitación.",
        "X suma 7, Y suma 8, Z suma 7. La mejor es Y porque tiene el total más alto. Limitación: los puntajes son una opinión informada.",
        ["tres totales correctos", "decisión justificada", "limitación escrita"],
        ["cálculos", "decisión"],
        ["calcular mal los totales", "no justificar la decisión"],
        "Pregunta qué otro criterio agregaría para desempatar.",
    ),
    reinforce="Inventa una cuarta medida con tres puntajes y calcula su total.",
    extend="Averigua con una persona de tu casa qué medida de protección ambiental ya hacen en casa y a qué capa ayuda.",
)

# ================================================================ OA 17, clase 1
register(
    OA17, 1,
    materials="Papel y lápiz. Si quieres, tres puñados de tierra de un jardín, arena de una plaza y arcilla o barro (lávate las manos al terminar). Los datos están escritos en el cuaderno.",
    use="Aprenderé a describir el suelo con color, textura y retención de agua, y a separar lo que observo de lo que interpreto. Sirve para comparar suelos con evidencia.",
    prior=["Sé que las plantas crecen en el suelo.", "Sé separar observación e interpretación."],
    explain=[
        "El suelo es la capa superior de la litósfera donde crecen las plantas. Está formado por pequeños trozos de roca, restos de plantas y animales descompuestos, agua y aire. Sus propiedades son rasgos que se pueden observar: el color, la textura y la capacidad de retención de agua.",
        "El color puede ser oscuro, rojizo o claro. Un suelo oscuro suele tener más restos de plantas descompuestos. La textura es qué tan finas o gruesas son sus partículas: la arena tiene granos grandes y ásperos, el limo es suave como harina y la arcilla tiene partículas muy finas y se pega cuando está mojada. La retención de agua es cuánta agua queda en el suelo en lugar de pasar.",
        "Observación: «Muestra A: color café oscuro, granos finos, se pega a los dedos». Interpretación: «Es un suelo muy fértil». La interpretación no sale solo de lo observado. Para describir un suelo, primero escribe el color, la textura y el dato de retención y después tu explicación.",
    ],
    vocab=[("suelo", "capa superior de la litósfera donde crecen las plantas"), ("textura", "qué tan finos o gruesos son los granos del suelo"), ("arcilla", "partículas muy finas que se pegan cuando están mojadas"), ("arena", "granos grandes y ásperos"), ("retención de agua", "cantidad de agua que el suelo guarda sin dejarla pasar")],
    worked=[
        {"title": "Describir una muestra", "problem": "Muestra A: color café oscuro, granos muy finos, se pega a los dedos cuando está mojada. ¿Qué textura tiene?", "steps": ["Los granos muy finos que se pegan indican arcilla.", "Es textura arcillosa."], "answer": "Arcillosa"},
        {"title": "Observación o interpretación", "problem": "Frase A: «La muestra B es clara y de granos grandes». Frase B: «La muestra B no sirve para cultivar». ¿Cuál es la observación?", "steps": ["La frase A describe lo que se ve.", "La frase B es una valoración que no sale solo de esa observación."], "answer": "La frase A es observación; la B es interpretación"},
    ],
    mistakes=[
        {"wrong": "Decir que un suelo oscuro es siempre mejor.", "why": "Se saca una conclusión de un solo rasgo.", "fix": "Describe color, textura y retención y compara."},
        {"wrong": "Mezclar la observación con una opinión: «tierra fea y seca».", "why": "Se usan juicios.", "fix": "Describe con rasgos: color café claro, granos grandes."},
    ],
    tiers={
        "recovery": [
            ex("Granos grandes y ásperos que no se pegan: ¿es arena o arcilla?", "Arena", "La arena tiene granos grandes."),
            ex("Partículas muy finas que se pegan cuando están mojadas: ¿es arena o arcilla?", "Arcilla", "La arcilla es muy fina."),
            ex("¿Qué propiedad del suelo se refiere a la cantidad de agua que guarda?", "La retención de agua", "Es cuánta agua queda en el suelo."),
        ],
        "understand": [
            ex("Frase: «La muestra de tierra de maceta es café oscuro». ¿Observación o interpretación?", "Observación", "Se ve directamente."),
            ex("Frase: «Esa tierra es perfecta para todas las plantas». ¿Observación o interpretación?", "Interpretación", "Es una valoración sin dato."),
            ex("En Ciencias, ¿qué es la textura de un suelo?", "Qué tan finos o gruesos son sus granos", "Se nota al frotar la tierra entre los dedos."),
        ],
        "apply": [
            ex("Muestra C: color rojizo, granos medianos que se sienten suaves como harina. Entre arena, limo y arcilla, ¿qué textura es la más probable?", "Limo", "El limo es suave como harina."),
            ex("Una muestra oscura tiene muchos restos de hojas descompuestas. ¿Qué parte del suelo explica ese color oscuro: los restos de plantas o las rocas grandes?", "Los restos de plantas", "La materia orgánica oscurece el suelo."),
            arith("Una muestra de suelo de 100 g tiene 60 g de arena. ¿Cuántos gramos NO son arena?", "100-60", "Se resta la arena del total.", " g"),
        ],
        "reason": [
            ex("Ema dice que la muestra A es fértil porque es oscura y la B no lo es porque es clara. ¿Qué le falta para concluir?", "Datos de textura y retención de agua", "Un solo rasgo no basta."),
            ex("Dos compañeros describen la misma tierra: uno dice «café oscuro, granos finos» y otro «fea y sucia». ¿Cuál descripción es mejor para comparar suelos?", "La primera", "Usa rasgos observables."),
        ],
        "challenge": [
            arith("En 200 g de una muestra hay 120 g de arena, 50 g de limo y el resto es arcilla. ¿Cuántos gramos de arcilla hay?", "200-120-50", "Se resta al total la arena y el limo.", " g"),
            ex("¿Cuál es una limitación de describir un suelo solo con tus manos: que es difícil repetir la sensación igual otro día o que es muy seguro?", "Que es difícil repetir la sensación igual otro día", "Depende de la persona y del momento."),
        ],
    },
    context=[ex("Una persona de tu casa dice «mi jardín tiene tierra negra y suelta, y en la plaza hay arena clara». ¿Cuál rasgo de color describe al jardín?", "Oscuro o negro", "Se refiere al color de la muestra.")],
    selfcheck=[
        ex("¿Qué granos son más grandes: los de arena o los de arcilla?", "Los de arena", "La arcilla es muy fina."),
        ex("¿La retención de agua es una propiedad del suelo?", "Sí", "Se mide por el agua que guarda."),
        ex("«Esa tierra se ve café oscuro» y «esa tierra es la mejor». ¿Cuál frase es la interpretación?", "La segunda", "Es una valoración sin dato."),
    ],
    open_task=task(
        "Observa tres muestras (si no tienes tierra, usa estas descripciones de ejemplo). Muestra 1: café oscuro, granos finos, se pega al mojarla. Muestra 2: color claro, granos grandes y ásperos. Muestra 3: color rojizo, suave como harina. Haz una tabla con color, textura y una interpretación para cada una, y marca con O las observaciones y con I las interpretaciones.",
        "Muestra 1: O, café oscuro, granos finos. I, probablemente retiene bastante agua. Muestra 2: O, clara y áspera. I, el agua pasa rápido. Muestra 3: O, rojiza y suave. I, textura de limo.",
        ["tres muestras con color y textura", "marcas O e I", "interpretaciones razonables"],
        ["tabla completa"],
        ["usar juicios como «fea»", "no marcar O e I"],
        "Pregunta cómo comprobaría la interpretación con una prueba de agua.",
    ),
    reinforce="Describe con color y textura la tierra de una maceta o del patio usando solo palabras observables.",
    extend="Averigua con una persona de tu casa qué tipo de suelo tiene el lugar donde viven: arenoso, arcilloso o de jardín.",
)

# ================================================================ OA 17, clase 2
register(
    OA17, 2,
    materials="Papel y lápiz. Los datos están escritos en el cuaderno. Para la tarea abierta puedes usar un colador, un vaso medidor y tierra o arena de la plaza.",
    use="Aprenderé a hacer una pregunta comprobable y una predicción sobre cuánta agua retiene cada suelo, y a diseñar una prueba justa. Sirve para comparar suelos sin adivinar.",
    prior=["Conozco las texturas arena, limo y arcilla.", "Sé qué es una prueba justa."],
    explain=[
        "Una pregunta comprobable sobre el suelo puede ser: «¿qué suelo deja pasar más agua: arena o arcilla?». Para responderla hay que usar la misma cantidad de suelo (por ejemplo, 200 g), la misma cantidad de agua (100 mL), el mismo recipiente y el mismo tiempo (5 minutos). Solo cambia el tipo de suelo.",
        "Una predicción usa lo que sabemos de la textura. La arena tiene granos grandes con espacios entre ellos, así que el agua pasa fácil. La arcilla tiene partículas finas y espacios muy pequeños, así que el agua pasa lento. Entonces: «Si uso arena, entonces saldrá más agua por abajo que con arcilla, y la arena retendrá menos agua».",
        "La retención se calcula así: agua puesta menos agua que salió. Por ejemplo, si se ponen 100 mL y salen 70 mL, el suelo retuvo 30 mL. Una parte del agua queda pegada a las partículas, y esa es el agua retenida. Si el resultado contradice la predicción, se corrige la predicción.",
    ],
    vocab=[("retener", "guardar el agua en el suelo"), ("filtrar", "dejar pasar el agua a través del suelo"), ("variable que cambia", "condición que se modifica a propósito"), ("constante", "condición que se mantiene igual"), ("prueba justa", "prueba en que cambia solo una condición")],
    worked=[
        {"title": "Calcular la retención", "problem": "Se echan 100 mL de agua sobre arena y salen 70 mL. ¿Cuántos mL retuvo la arena?", "steps": ["Agua puesta: 100 mL.", "Agua que salió: 70 mL.", "Retuvo 100 − 70 = 30."], "answer": "30 mL"},
        {"title": "Reconocer la variable que cambia", "problem": "Se echan 100 mL de agua sobre 200 g de arena y sobre 200 g de arcilla, y se mide el agua que sale en 5 minutos. ¿Qué cambia y qué se mantiene?", "steps": ["Cambia el tipo de suelo.", "Se mantienen la cantidad de suelo, el agua y el tiempo."], "answer": "Cambia el tipo de suelo; son constantes 200 g, 100 mL y 5 minutos"},
    ],
    mistakes=[
        {"wrong": "Comparar 200 g de arena con 100 g de arcilla.", "why": "Cambian dos condiciones.", "fix": "Usa la misma cantidad de suelo en todas las muestras."},
        {"wrong": "Predecir que la arena retiene más porque «es más seca».", "why": "No se usa la textura.", "fix": "Piensa en el tamaño de los granos y los espacios entre ellos."},
    ],
    tiers={
        "recovery": [
            ex("Se echan 100 mL de agua sobre un suelo y salen 40 mL. ¿Cuántos mL retuvo?", "60 mL", "100 menos 40 son 60."),
            ex("¿Qué suelo deja pasar el agua más fácil: arena o arcilla?", "Arena", "Sus granos grandes dejan espacios grandes."),
            ex("En la prueba de la arena y la arcilla, ¿cuántas condiciones cambian a propósito?", "Una", "Solo cambia el tipo de suelo."),
        ],
        "understand": [
            ex("¿Cuál es una pregunta comprobable: «¿Qué suelo es más bonito?» o «¿Cuántos mL de agua salen de arena y de arcilla en 5 minutos?»?", "¿Cuántos mL de agua salen de arena y de arcilla en 5 minutos?", "Se responde midiendo."),
            ex("Predicción: «Si uso arcilla, entonces saldrá menos agua». ¿Qué propiedad de la arcilla la apoya?", "Sus partículas finas dejan espacios muy pequeños", "Por eso el agua pasa lento."),
            ex("Si el resultado contradice la predicción, ¿qué se corrige?", "La predicción", "Los resultados son la evidencia."),
        ],
        "apply": [
            arith("Se echan 100 mL de agua sobre arcilla y salen 15 mL. ¿Cuántos mL retuvo la arcilla?", "100-15", "Se resta el agua que salió del agua puesta.", " mL"),
            arith("Se echan 120 mL de agua sobre tierra de jardín y salen 50 mL. ¿Cuántos mL retuvo?", "120-50", "Se resta el agua que salió del agua puesta.", " mL"),
            ex("Una prueba usa 200 g de arena, 150 g de arcilla y 100 mL de agua en cada una. ¿Qué condición no es constante?", "La cantidad de suelo", "Debe ser igual en todas las muestras."),
        ],
        "reason": [
            ex("Inés predijo que la arena retendría 90 mL de 100 mL y midió 30 mL. ¿Qué debe corregir?", "La predicción", "La medición es la evidencia."),
            ex("Beto usa arena mojada y arcilla seca. Dice que la arena retiene menos. ¿Qué error tiene su prueba?", "No empezaron en las mismas condiciones", "Un suelo ya estaba mojado, así que la comparación no es justa."),
        ],
        "challenge": [
            arith("En una prueba justa se miden 5 minutos. Se repite 3 veces con arena y salen 70, 72 y 68 mL. ¿Cuál es el promedio? Suma y divide por 3.", "(70+72+68)//3", "El promedio resume pruebas repetidas.", " mL"),
            ex("Si la arcilla retiene más agua que la arena, ¿en cuál de los dos suelos esperas que el agua tarde más en bajar por el suelo?", "En la arcilla", "Sus espacios pequeños frenan el paso del agua."),
        ],
    },
    context=[ex("Una persona de tu casa quiere elegir entre arena y tierra de jardín para una maceta y no quiere que el agua se escape rápido. ¿Qué predicción puedes hacer sobre cuál retiene más agua?", "La tierra de jardín retiene más agua que la arena", "La arena deja pasar el agua con facilidad.")],
    selfcheck=[
        ex("Si se ponen 100 mL y salen 55 mL, ¿cuántos mL retuvo el suelo?", "45 mL", "100 menos 55 son 45."),
        ex("¿Qué suelo predices que deja pasar menos agua?", "La arcilla", "Sus espacios son muy pequeños."),
        ex("¿Qué debe mantenerse igual en una prueba justa?", "Las demás condiciones", "Solo cambia el tipo de suelo."),
    ],
    open_task=task(
        "Diseña una prueba justa para comparar arena y tierra de jardín. Escribe: la pregunta comprobable, la variable que cambia, la que mides, tres constantes y una predicción con «Si…, entonces…». Si puedes, hazla con un colador y un vaso medidor, con 200 g de cada suelo y 100 mL de agua.",
        "Pregunta: ¿qué suelo retiene más agua? Cambia: tipo de suelo. Mido: mL que salen en 5 minutos. Constantes: 200 g de suelo, 100 mL de agua y 5 minutos. Predicción: si uso tierra de jardín, entonces saldrá menos agua que con arena.",
        ["pregunta comprobable", "variable que cambia y variable que mide", "tres constantes y una predicción"],
        ["diseño escrito"],
        ["cambiar más de una condición", "olvidar una constante"],
        "Pregunta qué haría para repetir la prueba y estar más segura o seguro.",
    ),
    reinforce="Escribe otra predicción sobre un suelo con textura de limo y justifícala con el tamaño de sus granos.",
    extend="Averigua con una persona de tu casa qué hace en las macetas para que la tierra no se seque tan rápido.",
)

# ================================================================ OA 17, clase 3
register(
    OA17, 3,
    materials="Papel y lápiz. Dibuja los esquemas.",
    use="Aprenderé a modelar cómo se forma el suelo y cómo se ordenan sus capas. Sirve para entender por qué el suelo tarda tanto en formarse y por qué hay que protegerlo.",
    prior=["Sé que el suelo es parte de la litósfera.", "Conozco color, textura y retención de agua."],
    explain=[
        "El suelo se forma muy lento a partir de la roca. Primero el viento, el agua, los cambios de temperatura y las raíces de las plantas rompen la roca en trozos cada vez más pequeños. A ese desgaste de la roca se le llama meteorización. Los trozos pequeños son la base del suelo.",
        "Luego llegan los seres vivos. Las plantas, los animales y los microorganismos aportan hojas, restos y desechos que se descomponen y forman una materia oscura llamada humus. El humus se mezcla con los trozos de roca y forma el suelo. Este proceso toma cientos de años o más, y por eso el suelo es un recurso que se pierde mucho más rápido de lo que se forma.",
        "Un modelo de capas del suelo, de arriba hacia abajo: capa superficial oscura y con humus, subsuelo con más minerales, roca fragmentada y roca madre (roca sin cambios). El modelo tiene límites: muestra capas ordenadas, pero en la realidad el espesor cambia de un lugar a otro y las capas se mezclan.",
    ],
    vocab=[("meteorización", "desgaste y ruptura de la roca por viento, agua, temperatura o raíces"), ("humus", "materia oscura formada por restos de seres vivos descompuestos"), ("roca madre", "roca de la que se origina un suelo"), ("subsuelo", "capa bajo la capa superficial del suelo"), ("descomposición", "proceso en que los restos de seres vivos se desintegran")],
    worked=[
        {"title": "Ordenar la formación", "problem": "Ordena: (1) se forma el suelo, (2) la roca se rompe en trozos, (3) se agregan restos de seres vivos. ¿En qué orden ocurren?", "steps": ["Primero se rompe la roca.", "Luego se agregan los restos descompuestos.", "Finalmente se forma el suelo."], "answer": "2, 3, 1"},
        {"title": "Sumar capas", "problem": "Un corte de suelo tiene una capa superficial de 8 cm, un subsuelo de 20 cm y roca fragmentada de 12 cm. ¿Cuántos cm tiene en total?", "steps": ["Se suman los tres espesores.", "8 + 20 + 12 = 40."], "answer": "40 cm"},
    ],
    mistakes=[
        {"wrong": "Creer que el suelo se forma en pocos días.", "why": "Se confunde con mezclar tierra.", "fix": "El suelo se forma en cientos de años o más."},
        {"wrong": "Pensar que la capa superficial es roca.", "why": "Se mezclan las capas.", "fix": "La capa superficial es oscura y con humus; la roca está más abajo."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué se rompe primero en la formación del suelo: la roca o las hojas?", "La roca", "Su ruptura es el primer paso."),
            ex("¿Cómo se llama la materia oscura formada por restos descompuestos de seres vivos?", "Humus", "Aporta nutrientes al suelo."),
            ex("¿Qué capa está más abajo: la roca madre o la capa superficial?", "La roca madre", "Está bajo todas las demás."),
        ],
        "understand": [
            ex("En Ciencias, ¿qué es la meteorización?", "El desgaste y ruptura de la roca", "El viento, el agua y las raíces la rompen en trozos."),
            ex("¿Por qué el suelo se considera un recurso que se forma muy lento?", "Porque demora cientos de años o más", "Se pierde más rápido de lo que se forma."),
            ex("¿Cuál es una limitación del modelo de capas: que son siempre del mismo espesor o que tiene cuatro capas?", "Que son siempre del mismo espesor", "En la realidad el espesor cambia."),
        ],
        "apply": [
            arith("Un corte de suelo tiene capa superficial de 10 cm, subsuelo de 25 cm y roca fragmentada de 15 cm. ¿Cuántos cm mide en total?", "10+25+15", "Se suman los tres espesores.", " cm"),
            ex("Ordena de arriba hacia abajo: roca madre, capa superficial con humus, subsuelo, roca fragmentada.", "Capa superficial, subsuelo, roca fragmentada, roca madre", "Es el orden del modelo."),
            arith("Un corte tiene 50 cm de profundidad y la capa superficial mide 12 cm. ¿Cuántos cm miden las otras capas juntas?", "50-12", "Se resta la capa superficial del total.", " cm"),
        ],
        "reason": [
            ex("Sofi dice que si se pierde 1 cm de suelo, mañana vuelve a estar. Con el modelo, ¿qué la contradice?", "Que el suelo demora cientos de años en formarse", "La formación es muy lenta."),
            ex("Mateo dice que el humus viene de la roca. ¿De dónde viene realmente según la clase?", "De restos descompuestos de seres vivos", "El humus es materia orgánica."),
        ],
        "challenge": [
            ex("Un lugar tiene roca madre casi al descubierto y sin humus. ¿Qué predices sobre la vida de las plantas ahí: pocas o muchas?", "Pocas", "Sin suelo con humus hay pocos nutrientes."),
            arith("En un lugar imaginario, cada 1 cm de suelo demora 200 años en formarse. ¿Cuántos años demoran 8 cm?", "8*200", "Se multiplican los centímetros por los años de cada uno.", " años"),
        ],
    },
    context=[ex("En una excavación se ve una capa oscura arriba y una capa de piedras más abajo. ¿Cuál de las dos capas tiene más humus?", "La capa oscura de arriba", "El humus oscurece la capa superficial.")],
    selfcheck=[
        ex("Nombra un agente que rompe la roca en trozos más pequeños.", "El viento, el agua, los cambios de temperatura o las raíces (cualquiera de ellos)", "Esos agentes provocan la meteorización."),
        ex("¿Qué capa tiene humus: la superficial o la roca madre?", "La superficial", "Ahí están los restos descompuestos."),
        ex("¿El suelo se forma rápido o lento?", "Lento", "Demora cientos de años."),
    ],
    open_task=task(
        "Dibuja un corte de suelo con cuatro capas rotuladas (superficial con humus, subsuelo, roca fragmentada y roca madre) y pon un espesor a cada una que sume 60 cm. Agrega flechas que muestren la meteorización y los restos de plantas que forman el humus. Escribe una limitación de tu dibujo.",
        "Superficial 10 cm, subsuelo 25 cm, roca fragmentada 15 cm, roca madre 10 cm (total 60 cm). Limitación: en la realidad los espesores cambian de un lugar a otro.",
        ["cuatro capas rotuladas", "espesores que suman 60 cm", "flechas y una limitación"],
        ["dibujo", "suma"],
        ["poner la roca madre arriba", "espesores que no suman 60 cm"],
        "Pregunta qué parte del dibujo muestra la formación más lenta.",
    ),
    reinforce="Escribe en tres pasos cómo se forma el suelo a partir de la roca.",
    extend="Averigua con una persona de tu casa qué hace con las cáscaras de verduras y cómo se relacionan con el humus.",
)

# ================================================================ OA 17, clase 4
register(
    OA17, 4,
    materials="Papel y lápiz. Los datos están escritos en el cuaderno; son datos de ejemplo.",
    use="Aprenderé a comparar resultados de retención de agua de tres suelos con un criterio. Sirve para decidir qué suelo es mejor para cierto uso.",
    prior=["Sé calcular el agua retenida: puesta menos salida.", "Sé qué es una prueba justa."],
    explain=[
        "Se hizo una prueba justa con tres suelos. En cada embudo se pusieron 200 g de suelo y 100 mL de agua. Después de 5 minutos se midió el agua que salió. Datos de ejemplo: arena, 70 mL; tierra de jardín, 40 mL; arcilla, 15 mL.",
        "El criterio de comparación es el agua retenida, que se calcula como 100 mL menos el agua que salió. Arena: 100 − 70 = 30 mL. Tierra de jardín: 100 − 40 = 60 mL. Arcilla: 100 − 15 = 85 mL. El orden de mayor a menor retención es arcilla, tierra de jardín y arena.",
        "Los datos permiten concluir: «La arcilla retuvo 85 mL, la tierra de jardín 60 mL y la arena 30 mL, entonces la arcilla retiene más». Como limitación, se hizo una sola prueba por suelo y la arcilla en la realidad puede dejar el agua tan pegada que las raíces no la aprovechan. Retener mucha agua no siempre es mejor para una planta.",
    ],
    vocab=[("agua retenida", "agua puesta menos agua que salió"), ("criterio", "regla para comparar"), ("conclusión", "idea final apoyada en datos"), ("limitación", "aspecto que reduce la confianza en los resultados"), ("prueba repetida", "prueba que se hace otra vez para comprobar")],
    worked=[
        {"title": "Comparar dos retenciones", "problem": "La tierra de jardín retuvo 60 mL y la arena 30 mL. ¿Cuántos mL más retuvo la tierra de jardín?", "steps": ["Los dos datos están en mL.", "60 − 30 = 30."], "answer": "30 mL más"},
        {"title": "Ordenar con el criterio", "problem": "Con retenciones de arena 30 mL, tierra de jardín 60 mL y arcilla 85 mL, ¿cuál retiene menos?", "steps": ["Se busca el menor valor.", "30 mL es el menor."], "answer": "La arena"},
    ],
    mistakes=[
        {"wrong": "Decir que la arcilla es mejor para todo porque retiene más agua.", "why": "Se usa un solo criterio.", "fix": "Considera para qué se usa el suelo; las raíces también necesitan aire."},
        {"wrong": "Usar el agua que salió como si fuera la retenida.", "why": "Se confunden los dos datos.", "fix": "La retenida es la puesta menos la que salió."},
    ],
    tiers={
        "recovery": [
            ex("Salieron 20 mL de 100 mL que se echaron. ¿Cuánta agua retuvo el suelo?", "80 mL", "100 menos 20 son 80."),
            ex("Entre un suelo que retiene 45 mL y otro que retiene 70 mL, ¿cuál retiene más?", "El de 70 mL", "70 es mayor que 45."),
            ex("En una prueba justa con tres suelos, ¿qué debe cambiar: el tipo de suelo o la cantidad de agua?", "El tipo de suelo", "La cantidad de agua es constante."),
        ],
        "understand": [
            ex("¿Qué es el agua retenida?", "El agua puesta menos el agua que salió", "Es la que queda en el suelo."),
            ex("¿Cuál conclusión usa evidencia: (a) «La arcilla es mejor» o (b) «La arcilla retuvo 85 mL y la arena 30 mL»?", "(b)", "Cita datos medidos."),
            ex("¿Por qué una sola prueba es una limitación?", "Porque el resultado puede ser casual y no se sabe si se repetiría", "Falta repetir para tener confianza."),
        ],
        "apply": [
            arith("Un suelo retuvo 85 mL y otro 30 mL. ¿Cuántos mL de diferencia hay?", "85-30", "Se resta el menor al mayor.", " mL"),
            arith("En otra prueba justa se echaron 150 mL de agua y salieron 90 mL. ¿Cuántos mL retuvo el suelo?", "150-90", "Se resta el agua que salió de la puesta.", " mL"),
            ex("Ordena de menos a más retención: tierra de jardín 60 mL, arcilla 85 mL, arena 30 mL.", "Arena, tierra de jardín, arcilla", "Se ordenan por los mL retenidos."),
        ],
        "reason": [
            ex("Laura dice que la arena retiene más porque dejó pasar más agua. ¿Qué error comete?", "Confunde el agua que salió con el agua retenida", "Más agua que salió significa menos retención."),
            ex("Hugo afirma que la arcilla es siempre el mejor suelo para cultivar. ¿Qué dato de la clase lo contradice?", "Que retener mucha agua no siempre es mejor para una planta", "Un solo criterio no basta para decidir."),
        ],
        "challenge": [
            arith("Tres pruebas con tierra de jardín retuvieron 58, 60 y 62 mL. ¿Cuál es el promedio? Suma y divide por 3.", "(58+60+62)//3", "El promedio resume pruebas repetidas.", " mL"),
            ex("Un suelo retuvo 85 mL de 100 mL en una prueba y 40 mL de 100 mL en otra prueba justa con el mismo suelo. ¿Los resultados son parecidos o muy distintos?", "Muy distintos", "La diferencia es grande y habría que revisar la prueba."),
        ],
    },
    context=[ex("Una persona de tu casa quiere una maceta para una planta que necesita que el agua pase rápido. Con los datos de la clase, ¿qué suelo conviene más: arena o arcilla?", "Arena", "Retiene menos agua y la deja pasar.")],
    selfcheck=[
        ex("¿Cuánta agua retuvo la arena en los datos de la clase?", "30 mL", "100 menos 70."),
        ex("¿Qué suelo retuvo más?", "La arcilla", "Retuvo 85 mL."),
        ex("La conclusión «la arcilla retuvo 85 mL» ¿cita un dato medido?", "Sí", "Incluye un valor en mL."),
    ],
    open_task=task(
        "Con los datos de ejemplo (100 mL de agua en cada suelo, 5 minutos, salieron: arena 70 mL, tierra de jardín 40 mL, arcilla 15 mL), haz una tabla con el agua que salió y la retenida, escribe una conclusión que cite dos datos y una limitación. Luego escribe qué suelo recomendarías para una planta de desierto.",
        "Retenida: arena 30 mL, jardín 60 mL, arcilla 85 mL. Conclusión: la arcilla retuvo 85 mL y la arena 30 mL. Limitación: una sola prueba. Recomendación para planta de desierto: arena, porque deja pasar el agua.",
        ["tabla con retenciones correctas", "conclusión con dos datos", "limitación y recomendación"],
        ["tabla", "conclusión"],
        ["confundir agua que salió con retenida", "no citar datos"],
        "Pregunta qué cambiaría si las pruebas fueran de 10 minutos.",
    ),
    reinforce="Calcula la retención de un suelo del que salieron 55 mL de los 100 mL echados.",
    extend="Averigua con una persona de tu casa qué suelo usan para plantas que necesitan mucha agua y cuál para plantas que necesitan poca.",
)

# ================================================================ OA 17, clase 5
register(
    OA17, 5,
    materials="Papel y lápiz. Los datos están escritos en el cuaderno; son datos de ejemplo.",
    use="Aprenderé a explicar con evidencia y límites por qué es importante proteger el suelo de la contaminación y a comunicar mis resultados. Sirve para convencer con datos.",
    prior=["Sé que el suelo se forma muy lento.", "Sé que una explicación tiene afirmación, evidencia y razón."],
    explain=[
        "El suelo puede contaminarse con basura, aceite o combustible derramado y exceso de productos para controlar plagas. Un suelo contaminado no deja crecer bien a las plantas ni sirve para alimentar. Como el suelo tarda cientos de años en formarse, perderlo es muy grave.",
        "Veamos una prueba con datos de ejemplo. En dos macetas se plantaron 10 semillas de lenteja en cada una. La maceta A tenía tierra limpia y germinaron 8 semillas. La maceta B tenía tierra con aceite y germinaron 2. Con esto se explica: «La contaminación con aceite disminuyó la germinación». Evidencia: 8 contra 2. Razón: el aceite cubre las partículas y casi no deja pasar agua ni aire.",
        "Para comunicar los resultados se escribe un informe corto con la pregunta, los datos, la conclusión y las limitaciones. Limitaciones: pocas semillas, una sola repetición y datos de ejemplo. Solo se podría afirmar con certeza repitiendo la prueba muchas veces.",
    ],
    vocab=[("germinar", "empezar a crecer una semilla"), ("contaminación del suelo", "presencia de sustancias que dañan el suelo"), ("informe", "texto corto que comunica una investigación"), ("evidencia", "dato que apoya una conclusión"), ("limitación", "aspecto que reduce la confianza en los resultados")],
    worked=[
        {"title": "Comparar con datos", "problem": "En la maceta A germinaron 8 de 10 semillas y en la B germinaron 2 de 10. ¿Cuántas semillas más germinaron en A?", "steps": ["Ambos datos son semillas.", "8 − 2 = 6."], "answer": "6 semillas más"},
        {"title": "Armar la conclusión", "problem": "Escribe una conclusión con afirmación, evidencia y razón sobre el aceite en el suelo.", "steps": ["Afirmación: el aceite disminuyó la germinación.", "Evidencia: 8 semillas contra 2.", "Razón: el aceite casi no deja pasar agua ni aire."], "answer": "El aceite disminuyó la germinación: 8 contra 2, porque casi no deja pasar agua ni aire"},
    ],
    mistakes=[
        {"wrong": "Concluir que cualquier contaminante hace lo mismo que el aceite.", "why": "Solo se probó un contaminante.", "fix": "Limita la conclusión a lo que se probó."},
        {"wrong": "Escribir un informe sin los datos.", "why": "No se puede comprobar.", "fix": "Incluye la tabla o los números."},
    ],
    tiers={
        "recovery": [
            ex("En otra maceta con tierra limpia germinaron 9 semillas de 10. ¿Cuántas no germinaron?", "1", "10 menos 9 es 1."),
            ex("¿Qué maceta tuvo más germinación en los datos de la clase: la limpia o la con aceite?", "La limpia", "Tuvo 8 semillas contra 2."),
            ex("¿Cuál es un contaminante del suelo: una hoja seca o el aceite usado derramado?", "El aceite usado derramado", "La hoja se descompone; el aceite daña el suelo."),
        ],
        "understand": [
            ex("¿Qué debe llevar un informe corto: pregunta, datos, conclusión y limitaciones, o solo la conclusión?", "Pregunta, datos, conclusión y limitaciones", "Así otra persona puede revisarlo."),
            ex("¿Por qué perder el suelo es muy grave?", "Porque demora cientos de años en formarse", "No se recupera rápido."),
            ex("¿Cuál es una limitación de usar solo 10 semillas por maceta: que son pocas o que son lentejas?", "Que son pocas", "Con pocas semillas el resultado puede ser casual."),
        ],
        "apply": [
            arith("En un segundo ensayo, la maceta limpia tuvo 7 semillas germinadas y la maceta con aceite tuvo 3. ¿Cuántas semillas germinaron entre las dos macetas?", "7+3", "Se suman los dos datos.", " semillas"),
            arith("Otro grupo plantó 20 semillas en tierra limpia y germinaron 16. ¿Cuántas no germinaron?", "20-16", "Se resta lo que germinó del total.", " semillas"),
            ex("Escribe en orden las partes de una conclusión científica: razón, afirmación, evidencia.", "Afirmación, evidencia, razón", "Primero la idea, luego el dato y por último el porqué."),
        ],
        "reason": [
            ex("Pablo concluye: «Todo lo que se derrame sobre el suelo lo contamina para siempre». ¿Qué le falta?", "Que solo se probó el aceite en una prueba de ejemplo", "No se puede generalizar desde un solo ejemplo."),
            ex("Sandra dice que la prueba muestra que el aceite no importa porque germinaron 2 semillas. ¿Qué dato la contradice?", "En la tierra limpia germinaron 8", "Hubo mucha menos germinación con aceite."),
        ],
        "challenge": [
            arith("En otra tierra limpia germinaron 9 de cada 10 semillas. Si se plantan 50 semillas con la misma proporción, ¿cuántas se predice que germinarán?", "5*9", "50 semillas son 5 grupos de 10, y cada grupo da 9.", " semillas"),
            ex("Para proteger el suelo de un patio, ¿qué medida es adecuada: botar aceite usado en la tierra o llevarlo a un punto de reciclaje?", "Llevarlo a un punto de reciclaje", "Así no contamina."),
        ],
    },
    context=[ex("Una persona de tu casa cambió el aceite de un auto en un patio de tierra y se derramó un poco. ¿Qué advertencia basada en los datos de la clase puedes hacerle?", "Que el aceite en el suelo puede disminuir la germinación de las plantas", "Los datos muestran menos semillas germinadas con aceite.")],
    selfcheck=[
        ex("¿Qué maceta tuvo menos semillas germinadas?", "La que tenía aceite", "Germinaron solo 2."),
        ex("¿Cuántas partes tiene una explicación científica?", "Tres", "Afirmación, evidencia y razón."),
        ex("¿Qué debe incluir un informe para que se pueda comprobar?", "Los datos", "Con números otra persona lo revisa."),
    ],
    open_task=task(
        "Escribe un informe de cinco líneas con estos datos de ejemplo: 10 semillas en tierra limpia, germinaron 8; 10 semillas en tierra con aceite, germinaron 2. Debe tener pregunta, datos, conclusión (afirmación, evidencia y razón), dos limitaciones y una medida para proteger el suelo.",
        "Pregunta: ¿el aceite afecta la germinación? Datos: 8 de 10 con tierra limpia y 2 de 10 con aceite. Conclusión: el aceite disminuyó la germinación porque casi no deja pasar agua ni aire. Limitaciones: pocas semillas, una sola prueba. Medida: no botar aceite usado en el suelo.",
        ["pregunta y datos", "conclusión con evidencia y razón", "dos limitaciones y una medida"],
        ["informe escrito"],
        ["generalizar a todos los contaminantes", "olvidar los datos"],
        "Pregunta qué prueba haría para comprobar con otro contaminante.",
    ),
    reinforce="Escribe una conclusión corta con los datos 8 y 2 usando las palabras afirmación, evidencia y razón.",
    extend="Averigua con una persona de tu casa dónde se puede llevar el aceite de cocina usado en tu comuna y por qué no se bota al desagüe.",
)
