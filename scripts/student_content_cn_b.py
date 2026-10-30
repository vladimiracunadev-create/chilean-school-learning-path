"""Cuaderno del estudiante, 1.º básico Ciencias Naturales: OA 03 (estructuras de las plantas) y OA 04 (clasificar semillas, frutos, flores y tallos)."""
from __future__ import annotations

from student_content_cn_a import task
from student_lessons import arith, ex, register

OA3, OA4 = "CN01 OA 03", "CN01 OA 04"

# ---------------------------------------------------------------- OA 03
register(
    OA3, 1,
    materials="Este cuaderno con el registro de una planta de poroto (raíz, tallo, hojas y flores), lápiz y colores. En casa: una planta de maceta o de jardín, una regla y, si tienes, una lupa. Lávate las manos al terminar.",
    use="Aprenderé a reconocer las cuatro estructuras principales de una planta: raíz, tallo, hojas y flores. Sirve para describir una planta con palabras exactas.",
    prior=["Sé que las plantas son seres vivos.", "Sé medir con una regla en centímetros."],
    explain=[
        "Una planta tiene estructuras, que son sus partes. Las cuatro principales son la raíz, el tallo, las hojas y las flores. La raíz casi siempre está bajo la tierra. El tallo sube y sostiene la planta.",
        "Las hojas salen del tallo y casi siempre son verdes. Las flores salen en la parte de arriba y tienen pétalos de colores. No todas las plantas tienen flores al mismo tiempo, pero muchas las tienen en alguna época del año.",
        "Para observar bien, mira de abajo hacia arriba: primero la raíz, luego el tallo, después las hojas y al final las flores. Mide lo que puedas y anótalo con su unidad, por ejemplo 12 cm.",
    ],
    vocab=[("raíz", "parte de la planta que está bajo la tierra"), ("tallo", "parte que sostiene la planta"), ("hoja", "parte verde que sale del tallo"), ("flor", "parte con pétalos de colores"), ("estructura", "una parte de la planta")],
    worked=[
        {"title": "Leer el registro de una planta", "problem": "Planta de poroto: raíz 8 cm, tallo 12 cm, 6 hojas, 2 flores. ¿Qué parte mide más: la raíz o el tallo?", "steps": ["Comparo 8 cm con 12 cm.", "12 es mayor que 8.", "El tallo mide más."], "answer": "El tallo mide más; 4 cm más que la raíz"},
        {"title": "Nombrar las partes", "problem": "Señala la parte que está bajo la tierra y la parte con pétalos.", "steps": ["Bajo la tierra está la raíz.", "Los pétalos están en la flor."], "answer": "Raíz y flor"},
    ],
    mistakes=[
        {"wrong": "Llamar «tallo» a la raíz porque también es larga y delgada.", "why": "Se mira la forma y no el lugar.", "fix": "La raíz está bajo la tierra; el tallo sube por el aire."},
        {"wrong": "Decir que la hoja es lo mismo que el pétalo.", "why": "Ambos son planos y de colores parecidos en algunas plantas.", "fix": "La hoja sale del tallo y casi siempre es verde; los pétalos forman la flor."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué parte de la planta está bajo la tierra?", "La raíz", "Es la parte que se oculta en el suelo."),
            ex("¿Qué parte de la planta tiene pétalos de colores?", "La flor", "Los pétalos forman la flor."),
            ex("¿Qué parte de la planta sale del tallo y casi siempre es verde?", "La hoja", "Las hojas salen del tallo."),
        ],
        "understand": [
            ex("¿Cuáles son las cuatro estructuras principales de una planta?", "Raíz, tallo, hojas y flores", "Son las partes de la clase."),
            ex("¿Para qué sirve el tallo?", "Para sostener la planta", "Mantiene la planta parada."),
            ex("¿En qué orden se observa una planta en esta clase?", "De abajo hacia arriba", "Se parte por la raíz y se termina en la flor."),
        ],
        "apply": [
            arith("La raíz del poroto mide 8 cm y el tallo 12 cm. ¿Cuántos centímetros mide más el tallo?", "12-8", "Se resta lo que mide la raíz a lo que mide el tallo.", " cm"),
            arith("Una planta tiene 6 hojas y le salen 3 hojas nuevas. ¿Cuántas hojas tiene ahora?", "6+3", "Se juntan las hojas que había y las nuevas.", " hojas"),
            ex("Una planta tiene raíz de 5 cm, tallo de 20 cm y 8 hojas. ¿Qué parte mide 20 cm?", "El tallo", "Cada medida corresponde a su estructura."),
        ],
        "reason": [
            ex("Clara arrancó una planta y vio que no tenía raíz. Dice que no era una planta. ¿Qué respuesta es más probable?", "La raíz se cortó al arrancarla", "Casi todas las plantas tienen raíz bajo la tierra."),
            ex("Tomás dice que el tallo del girasol es una raíz porque es largo. ¿Cómo lo corriges?", "Es un tallo porque sube sobre la tierra y sostiene las hojas y la flor", "El tallo sube desde la raíz."),
        ],
        "challenge": [
            ex("Una planta tiene 2 flores y 5 hojas. ¿Cuántas hojas y flores hay en total?", "7", "Dos flores más cinco hojas son siete."),
            ex("Escribe una planta que conozcas y una estructura que se coma.", "Por ejemplo la lechuga y sus hojas", "Algunas plantas se comen en hojas, raíz o tallo."),
        ],
    },
    context=[ex("En el jardín ves un girasol con un tallo de 150 cm y un clavel con un tallo de 40 cm. ¿Cuántos centímetros más largo es el tallo del girasol?", "110 cm", "150 menos 40 es 110.")],
    selfcheck=[ex("¿Cuál de estas partes está bajo la tierra: la raíz o la flor?", "La raíz", "Está dentro de la tierra."), ex("¿Qué parte sostiene a la planta?", "El tallo", "Mantiene las hojas arriba."), ex("¿Cuántas estructuras principales vimos hoy?", "4", "Raíz, tallo, hojas y flores.")],
    open_task=task("Mira esta planta de ejemplo: raíz 6 cm, tallo 15 cm, 4 hojas y 1 flor roja. Dibújala con las cuatro partes, ponles nombre y escribe una medida junto a cada una que tenga centímetros.", "Dibujo con raíz (6 cm) bajo la tierra, tallo (15 cm), cuatro hojas verdes y una flor roja arriba.", ["dibuja las cuatro partes en su lugar", "escribe los nombres", "usa las medidas con cm"], ["dibujo rotulado", "medidas"], ["dibujar la raíz fuera de la tierra", "olvidar la unidad"], "Reconoce las partes y pide dibujar la raíz bajo la tierra."),
    reinforce="Observa una planta de tu casa y nombra sus cuatro partes.",
    extend="Compara dos plantas distintas y di qué parte es más larga en cada una.",
)

register(
    OA3, 2,
    materials="Este cuaderno con la tabla del experimento del apio con agua coloreada (datos de ejemplo), lápiz y colores. En casa, con ayuda de un adulto: un tallo de apio, un vaso, agua y colorante de cocina.",
    use="Aprenderé para qué sirven la raíz y el tallo. Sirve para entender cómo el agua llega a las hojas.",
    prior=["Sé nombrar raíz, tallo, hojas y flores.", "Sé que las plantas necesitan agua."],
    explain=[
        "La raíz sujeta la planta a la tierra y absorbe agua. Sin raíz, la planta se cae y no puede tomar el agua del suelo. Hay raíces largas y finas, y también raíces gruesas, como la zanahoria.",
        "El tallo sostiene las hojas y las flores. Además, por dentro tiene tubitos muy finos que llevan el agua desde la raíz hasta las hojas. Puedes verlo con un apio puesto en agua con colorante: el color sube por el tallo.",
        "El experimento muestra que el tallo transporta el agua. En la tabla, a las 0 horas el apio no tiene hojas teñidas, a las 6 horas hay 2 hojas teñidas y a las 24 horas hay 5. El color subió porque el agua subió.",
    ],
    vocab=[("absorber", "tomar el agua del suelo"), ("sujetar", "mantener firme en un lugar"), ("transportar", "llevar de un lugar a otro"), ("tallo", "parte que sostiene y lleva agua"), ("colorante", "tinta de cocina que tiñe el agua")],
    worked=[
        {"title": "Leer el experimento del apio", "problem": "Hojas teñidas de un apio con 6 hojas: 0 horas = 0, 6 horas = 2, 24 horas = 5. ¿Qué pasó con el color?", "steps": ["El número de hojas teñidas sube: 0, 2, 5.", "El color llegó a más hojas con el tiempo.", "El agua con color subió por el tallo."], "answer": "El color subió por el tallo y llegó a más hojas"},
        {"title": "Para qué sirve la raíz", "problem": "Una planta sin raíz se cae al soltarla y no toma agua. ¿Para qué sirve la raíz?", "steps": ["Sin raíz se cae: la raíz la sujeta.", "Sin raíz no toma agua: la raíz absorbe agua."], "answer": "La raíz sujeta la planta y absorbe agua"},
    ],
    mistakes=[
        {"wrong": "Decir que las hojas toman el agua directamente del suelo.", "why": "No se ve el camino del agua.", "fix": "El agua entra por la raíz y sube por el tallo hasta las hojas."},
        {"wrong": "Creer que el colorante hace crecer el apio.", "why": "Se confunde el cambio de color con crecer.", "fix": "El colorante solo muestra por dónde sube el agua."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué parte de la planta absorbe agua del suelo?", "La raíz", "Está en la tierra."),
            ex("¿Qué parte de la planta lleva el agua hasta las hojas?", "El tallo", "Tiene tubitos finos por dentro."),
            ex("¿Para qué sirve el tallo además de llevar agua?", "Para sostener la planta", "Mantiene las hojas arriba."),
        ],
        "understand": [
            ex("¿Qué dos trabajos hace la raíz?", "Sujeta la planta y absorbe agua", "Son sus dos funciones."),
            ex("En el experimento del apio, ¿qué muestra el color?", "Por dónde sube el agua", "El colorante viaja con el agua."),
            ex("¿Qué significa transportar?", "Llevar de un lugar a otro", "El tallo lleva agua de la raíz a las hojas."),
        ],
        "apply": [
            arith("A las 6 horas había 2 hojas teñidas y a las 24 horas había 5. ¿Cuántas hojas más se tiñeron entre las 6 y las 24 horas?", "5-2", "Se resta lo que había a las 6 horas.", " hojas"),
            arith("El apio tiene 6 hojas y a las 24 horas hay 5 teñidas. ¿Cuántas hojas siguen sin color?", "6-5", "Se resta lo teñido al total.", " hoja"),
            ex("Una planta se cayó al viento porque su raíz era muy corta. ¿Para qué le faltó raíz?", "Para sujetarse", "La raíz mantiene firme la planta."),
        ],
        "reason": [
            ex("Si el agua con colorante sube solo por el tallo, ¿por qué las hojas se tiñeron?", "Porque el tallo llevó el agua hasta las hojas", "El color viaja con el agua por los tubitos."),
            ex("Si cortas el tallo de un apio y dejas un hueco entre las dos partes, ¿llegará color a las hojas de arriba? Explica.", "No, porque se corta el camino del agua", "El agua sube por el tallo."),
        ],
        "challenge": [
            ex("Escribe una planta con raíz gruesa que se coma y una con tallo que se coma.", "Por ejemplo la zanahoria (raíz) y el espárrago (tallo)", "Hay raíces y tallos comestibles."),
            ex("El apio estuvo 24 horas en agua con colorante y 5 de sus 6 hojas se tiñeron. ¿Qué podrías hacer para ver si se tiñen las 6?", "Esperar más tiempo", "El color puede seguir subiendo con el tiempo."),
        ],
    },
    context=[ex("Un jardinero mueve un arbolito con la raíz cortada. Pasan unos días: el arbolito se cayó y sus hojas se secaron. ¿Qué dos funciones perdió la raíz?", "Sujetar y absorber agua", "Sin raíz no se sostiene ni toma agua.")],
    selfcheck=[ex("¿Qué parte absorbe el agua?", "La raíz", "Absorbe del suelo."), ex("¿Qué parte lleva el agua por dentro?", "El tallo", "Tiene tubitos finos por dentro."), ex("¿Qué muestra el colorante en el apio?", "El camino del agua", "Sube con ella.")],
    open_task=task("Mira esta tabla de ejemplo de dos tallos con colorante. Apio A: 0 horas = 0 hojas con color, 12 horas = 3, 24 horas = 6. Apio B (su tallo se cortó en dos partes y se dejó un hueco entre ellas, así que el agua no puede seguir subiendo): 0 horas = 0, 12 horas = 0, 24 horas = 0. Escribe qué muestra cada tabla y qué concluyes sobre el tallo.", "En el apio A el color llegó a 6 hojas en 24 horas porque el agua subió por el tallo entero. En el apio B no llegó color porque el camino del agua estaba cortado. Concluyo que el tallo lleva el agua.", ["describe cada tabla con números", "dice que el tallo lleva agua", "usa los datos como evidencia"], ["frases con números", "dibujo del apio"], ["decir que el colorante hace crecer", "no usar los números"], "Reconoce la evidencia y pide citar al menos un número de cada tabla."),
    reinforce="Con ayuda de un adulto, pon un tallo de apio en agua con colorante y mira cada hora.",
    extend="Explica por qué una flor blanca cortada puede teñirse con colorante.",
)

register(
    OA3, 3,
    materials="Este cuaderno con la tabla de cuatro hojas (largo, forma y borde) y la tabla de tres flores, lápiz y colores. En casa: una hoja y una flor de jardín (no arranques plantas de parques).",
    use="Aprenderé para qué sirven las hojas y las flores y en qué se parecen y diferencian. Sirve para entender de dónde salen los frutos y las semillas.",
    prior=["Sé nombrar las cuatro partes de una planta.", "Sé que la raíz y el tallo llevan agua."],
    explain=[
        "Las hojas fabrican el alimento de la planta. Lo hacen con luz, agua y aire. Por eso las plantas necesitan luz para vivir. Las hojas pueden ser largas, anchas, redondas o con bordes lisos o con dientes.",
        "Las flores sirven para que la planta tenga semillas. Después de la flor, muchas veces aparece un fruto y dentro del fruto están las semillas. Una semilla, si cae en tierra húmeda, puede dar una planta nueva.",
        "Para describir una hoja anota su largo en cm, su forma y su borde. Para describir una flor anota su color y cuántos pétalos tiene. Así puedes comparar sin equivocarte.",
    ],
    vocab=[("hoja", "parte que fabrica el alimento con luz, agua y aire"), ("pétalo", "parte de colores de la flor"), ("fruto", "parte que guarda las semillas"), ("semilla", "parte de la que puede nacer otra planta"), ("borde", "orilla de la hoja")],
    worked=[
        {"title": "Describir una hoja", "problem": "Hoja de laurel: 8 cm de largo, forma alargada, borde liso. ¿Cómo la describes?", "steps": ["Largo: 8 cm.", "Forma: alargada.", "Borde: liso."], "answer": "Hoja de 8 cm, alargada y de borde liso"},
        {"title": "Para qué sirve la flor", "problem": "Un manzano florece en primavera y más tarde tiene manzanas con semillas. ¿Qué papel tuvo la flor?", "steps": ["La flor apareció primero.", "Después apareció el fruto.", "Dentro del fruto hay semillas."], "answer": "La flor permitió que se formara el fruto con semillas"},
    ],
    mistakes=[
        {"wrong": "Decir que las flores son solo para decorar.", "why": "Se mira la belleza y no la función.", "fix": "La flor ayuda a formar frutos con semillas."},
        {"wrong": "Pensar que las plantas comen tierra como alimento.", "why": "No se sabe que las hojas fabrican el alimento.", "fix": "Las plantas fabrican su alimento en las hojas con luz, agua y aire."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué parte de la planta fabrica el alimento?", "La hoja", "Allí se fabrica con luz, agua y aire."),
            ex("¿Qué parte de la planta tiene pétalos?", "La flor", "Los pétalos forman la flor."),
            ex("¿Dentro de qué parte de la planta suele haber semillas?", "Dentro del fruto", "El fruto guarda las semillas."),
        ],
        "understand": [
            ex("¿Con qué fabrica su alimento una hoja?", "Con luz, agua y aire", "Son los tres elementos de la clase."),
            ex("¿Para qué sirve la flor?", "Para que la planta tenga semillas", "Después de la flor aparece el fruto."),
            ex("¿Qué puede nacer de una semilla en tierra húmeda?", "Una planta nueva", "La semilla da una planta."),
        ],
        "apply": [
            ex("Tabla de ejemplo de hojas: laurel 8 cm, menta 4 cm, higuera 20 cm, aloe 30 cm. ¿Cuál es la hoja más larga?", "La del aloe", "30 cm es mayor que las otras."),
            arith("La hoja de higuera mide 20 cm y la de menta 4 cm. ¿Cuántos centímetros más larga es la de higuera?", "20-4", "Se resta la medida de la menta a la de la higuera.", " cm"),
            ex("Datos de ejemplo. Flores: rosa roja 30 pétalos, margarita blanca 20 pétalos, diente de león amarillo 100 pétalos. ¿Cuál tiene más pétalos?", "El diente de león", "100 es mayor que 30 y 20."),
        ],
        "reason": [
            ex("Rosa dice que si arranca las flores de su planta de frutilla, igual tendrá frutillas. ¿Qué le advertirías?", "Que sin flores no se forman frutos", "El fruto aparece después de la flor."),
            ex("Una planta de albahaca crece en un clóset oscuro y sus hojas se ponen pálidas. ¿Qué le falta a las hojas para fabricar alimento?", "Luz", "Las hojas necesitan luz."),
        ],
        "challenge": [
            ex("Escribe una planta cuyo fruto comas y nombra su flor o su hoja.", "Por ejemplo el tomate con flor amarilla", "El fruto sale de la flor."),
            ex("Una margarita tiene 20 pétalos y se le cayeron 5. ¿Cuántos quedan?", "15", "Veinte menos cinco son quince."),
        ],
    },
    context=[ex("En un huerto una rama de tomate tiene 4 flores. Supón que se forma un fruto por cada flor. ¿Cuántos tomates habrá en esa rama?", "4", "Cada flor forma un fruto.")],
    selfcheck=[ex("¿Qué fabrica el alimento de la planta?", "La hoja", "Allí se produce."), ex("¿Qué necesita la hoja de la luz?", "Fabricar alimento", "La luz es necesaria."), ex("¿Qué hay dentro de un fruto?", "Semillas", "El fruto las guarda.")],
    open_task=task("Con esta tabla de dos plantas escribe qué hojas y qué flores tiene cada una. Planta 1: hojas de 6 cm, borde liso; flor amarilla con 8 pétalos. Planta 2: hojas de 3 cm, borde con dientes; flor rosada con 5 pétalos. Después escribe una diferencia de hojas y una de flores.", "Diferencia de hojas: la planta 1 tiene hojas de 6 cm y la planta 2 de 3 cm. Diferencia de flores: la planta 1 tiene 8 pétalos y la 2 tiene 5.", ["compara hojas con números", "compara flores con números", "usa palabras como más, menos o diferente"], ["tabla de comparación", "dibujo"], ["describir sin medida", "mezclar hoja con flor"], "Reconoce diferencias y pide usar un número en cada comparación."),
    reinforce="Mira una hoja y una flor y anota su color y su forma.",
    extend="Explica por qué las plantas de interior necesitan estar cerca de una ventana.",
)

register(
    OA3, 4,
    materials="Este cuaderno con la lista de materiales para un modelo (palito de helado, papel verde, lana, papel de colores) y una tabla de partes con su función. Lápiz y colores. En casa: papel, lana o hilo, palitos y tijeras con adulto.",
    use="Aprenderé a hacer un modelo de una planta con sus cuatro partes. Sirve para explicar cómo funciona cada parte.",
    prior=["Sé nombrar raíz, tallo, hojas y flores.", "Sé para qué sirve cada una."],
    explain=[
        "Un modelo es una forma de mostrar algo. Puedes hacer un modelo de una planta con materiales sencillos: un palito para el tallo, papel verde para las hojas, papel de colores para la flor y lana para las raíces.",
        "Un buen modelo muestra las cuatro partes y deja claro para qué sirve cada una. Escribe un rótulo, que es un nombre pegado, junto a cada parte: «raíz: sujeta y absorbe agua» o «hoja: fabrica alimento».",
        "Los modelos tienen límites. Tu modelo de papel no crece ni necesita agua. Cuando lo uses, di qué muestra bien y qué no muestra. Eso es parte de pensar como científico.",
    ],
    vocab=[("modelo", "forma de representar algo real"), ("rótulo", "nombre escrito que se pega a una parte"), ("función", "para qué sirve una parte"), ("límite del modelo", "algo que el modelo no muestra"), ("representar", "mostrar algo con otra cosa")],
    worked=[
        {"title": "Elegir materiales", "problem": "Quieres un modelo con raíz, tallo, hojas y flor. Tienes lana, palito, papel verde y papel rosado. ¿Qué usas para cada parte?", "steps": ["Lana: se parece a la raíz fina.", "Palito: sostiene como el tallo.", "Papel verde: las hojas.", "Papel rosado: la flor."], "answer": "Raíz con lana, tallo con palito, hojas con papel verde, flor con papel rosado"},
        {"title": "Decir un límite", "problem": "Tu modelo no crece. ¿Es un problema?", "steps": ["Un modelo muestra algunas cosas.", "No muestra el crecimiento.", "Hay que decirlo."], "answer": "Es un límite del modelo: no muestra el crecimiento"},
    ],
    mistakes=[
        {"wrong": "Hacer el modelo sin rótulos.", "why": "Se piensa que se entiende solo.", "fix": "Escribe cada parte y su función junto al modelo."},
        {"wrong": "Decir que el modelo es una planta de verdad.", "why": "Se olvida que representa algo.", "fix": "Di «mi modelo representa una planta» y nombra un límite."},
    ],
    tiers={
        "recovery": [
            ex("En un modelo de planta, ¿qué material se parece al tallo: un palito o una hoja de papel?", "Un palito", "Sostiene y es largo."),
            ex("¿Qué parte representa el papel verde?", "Las hojas", "Las hojas son verdes."),
            ex("¿Qué parte representa la lana en el modelo?", "La raíz", "Es fina y larga como la raíz."),
        ],
        "understand": [
            ex("¿Qué es un modelo?", "Una forma de representar algo real", "Muestra cómo es algo."),
            ex("¿Para qué sirve un rótulo?", "Para ponerle nombre a cada parte", "Aclara qué es cada cosa."),
            ex("¿Qué es un límite del modelo?", "Algo que el modelo no muestra", "Por ejemplo, que no crece."),
        ],
        "apply": [
            ex("Escribe el rótulo de la raíz con su función.", "Raíz: sujeta y absorbe agua", "El rótulo une nombre y función."),
            ex("Tienes 1 palito, 3 papeles verdes y 1 papel rosado. ¿Cuántas partes de la planta puedes representar sin la raíz?", "3", "Tallo, hojas y flor."),
            arith("Un modelo tiene 4 hojas de papel. Le pegas 2 hojas más. ¿Cuántas hojas tiene?", "4+2", "Se suman las hojas nuevas.", " hojas"),
        ],
        "reason": [
            ex("Sara hizo un modelo con flor, tallo y hojas, pero sin raíz. ¿Qué función no muestra?", "Sujetar y absorber agua", "Es lo que hace la raíz."),
            ex("¿Por qué tu modelo de papel no necesita agua aunque represente una planta?", "Porque no es un ser vivo", "Es de papel y no está vivo."),
        ],
        "challenge": [
            ex("Escribe un material de tu casa que sirva para la flor del modelo y explica por qué.", "Por ejemplo papel rojo porque se parece a pétalos", "Tiene color y forma de pétalo."),
            ex("Dos modelos tienen 3 hojas cada uno. ¿Cuántas hojas hay entre los dos?", "6", "Tres más tres son seis."),
        ],
    },
    context=[ex("En una feria de ciencias, Luis muestra un modelo con raíz de lana, tallo de palito, 4 hojas verdes y 1 flor. ¿Cuántas estructuras distintas representa?", "4", "Raíz, tallo, hojas y flor.")],
    selfcheck=[ex("¿Qué representa el palito?", "El tallo", "Sostiene la planta."), ex("¿Un modelo es lo mismo que la cosa real?", "No", "Solo la representa."), ex("¿Qué escribe un rótulo?", "El nombre de una parte", "Ayuda a entender el modelo.")],
    open_task=task("Planifica un modelo de planta con esta lista de materiales: lana amarilla, palito de helado, cuatro círculos de papel verde y un círculo de papel rojo. Dibuja el modelo, rotula las cuatro partes con su función y escribe un límite del modelo.", "Modelo: lana amarilla bajo el palito (raíz: sujeta y absorbe agua), palito (tallo: sostiene), círculos verdes (hojas: fabrican alimento), círculo rojo (flor: forma semillas). Límite: no crece.", ["dibuja las cuatro partes", "rotula nombre y función", "dice un límite del modelo"], ["dibujo con rótulos", "frase del límite"], ["no escribir la función", "olvidar el límite"], "Reconoce el uso del modelo y pide escribir un límite."),
    reinforce="Con papel y lana, haz una planta pequeña y rotula sus partes.",
    extend="Compara tu modelo con una planta de verdad y escribe dos cosas que tiene la planta y tu modelo no.",
)

# ---------------------------------------------------------------- OA 04
register(
    OA4, 1,
    materials="Este cuaderno con la tabla de seis semillas (tamaño, forma, textura y color), lápiz y colores. En casa, si quieres comprobarlo: legumbres y cereales de la cocina sobre un plato, sin probarlas.",
    use="Aprenderé a describir semillas con cuatro criterios: tamaño, forma, textura y color. Sirve para poder compararlas y agruparlas.",
    prior=["Sé que una semilla puede dar una planta.", "Sé medir en centímetros."],
    explain=[
        "Las semillas son distintas entre sí. Para describirlas usamos criterios: el tamaño, que se mide en cm; la forma, como redonda, alargada o de riñón; la textura, que es cómo se siente, lisa o arrugada; y el color.",
        "En la tabla de semillas de hoy: la lenteja mide cerca de 1 cm, es redonda y aplanada, lisa y café. El poroto mide cerca de 2 cm, tiene forma de riñón, es liso y blanco. El arroz mide cerca de 1 cm, es alargado, liso y blanco. Son medidas de ejemplo, redondeadas a centímetros enteros.",
        "Cuando describes con los cuatro criterios puedes compararlas sin verlas. Por ejemplo, el poroto es más grande que la lenteja, pero las dos son lisas. Siempre anota la unidad, cm.",
    ],
    vocab=[("criterio", "característica que uso para describir o agrupar"), ("textura", "cómo se siente algo al tocarlo"), ("forma", "figura de un objeto"), ("tamaño", "qué tan grande es"), ("semilla", "parte de la planta que puede dar otra planta")],
    worked=[
        {"title": "Describir con cuatro criterios", "problem": "Garbanzo: 1 cm, redondo, arrugado, beige. Descríbelo con los cuatro criterios.", "steps": ["Tamaño: 1 cm.", "Forma: redondo.", "Textura: arrugado.", "Color: beige."], "answer": "Tamaño 1 cm, redondo, arrugado y beige"},
        {"title": "Comparar dos semillas", "problem": "Poroto 2 cm y lenteja 1 cm. ¿Cuál es mayor y cuánto?", "steps": ["2 es mayor que 1.", "La diferencia es 1 cm."], "answer": "El poroto es 1 cm más grande"},
    ],
    mistakes=[
        {"wrong": "Describir solo con el color.", "why": "Un solo criterio no distingue semillas del mismo color.", "fix": "Usa tamaño, forma, textura y color."},
        {"wrong": "Escribir «grande» en lugar del número.", "why": "Grande depende de con qué se compare.", "fix": "Mide y anota el número con cm."},
    ],
    tiers={
        "recovery": [
            ex("Tabla: lenteja 1 cm, poroto 2 cm. ¿Cuál mide menos?", "La lenteja", "1 es menor que 2."),
            ex("Tabla: arveja, redonda y lisa, verde. ¿Qué color tiene?", "Verde", "El color está en la ficha."),
            ex("Tabla: garbanzo, arrugado. ¿Qué criterio describe «arrugado»?", "La textura", "La textura es cómo se siente."),
        ],
        "understand": [
            ex("¿Cuáles son los cuatro criterios para describir una semilla?", "Tamaño, forma, textura y color", "Son los de la clase."),
            ex("¿Qué es la textura?", "Cómo se siente algo al tocarlo", "Puede ser lisa o arrugada."),
            ex("¿Por qué conviene medir en lugar de decir «grande»?", "Porque el número se puede comprobar", "La palabra grande depende de la comparación."),
        ],
        "apply": [
            ex("El poroto mide 2 cm y la lenteja 1 cm. ¿Cuántos centímetros más mide el poroto?", "1 cm", "Dos menos uno es uno."),
            ex("Tabla de semillas: lenteja café, poroto blanco, maíz amarillo, arveja verde. ¿Cuál es amarilla?", "El maíz", "El color está en la tabla."),
            ex("Tabla: arroz alargado, lenteja redonda, poroto con forma de riñón. ¿Cuál es alargado?", "El arroz", "La forma está en la tabla."),
        ],
        "reason": [
            ex("Pablo dice que la lenteja y el arroz son iguales porque son pequeños. Si la lenteja es redonda y café y el arroz es alargado y blanco, ¿tiene razón?", "No", "Se diferencian en forma y color."),
            ex("Si dos semillas son lisas y blancas, ¿qué criterio mirarías para distinguirlas?", "El tamaño o la forma", "El color y la textura ya son iguales."),
        ],
        "challenge": [
            ex("Escribe una semilla y descríbela con los cuatro criterios.", "Por ejemplo poroto: 2 cm, riñón, liso, blanco", "Incluye tamaño, forma, textura y color."),
            ex("Hay 5 semillas lisas y 3 arrugadas. ¿Cuántas semillas hay?", "8", "Cinco más tres son ocho."),
        ],
    },
    context=[ex("Para una siembra, el abuelo tiene un frasco con 12 porotos y otro con 20 lentejas. ¿Cuántas lentejas más que porotos hay?", "8", "Veinte menos doce son ocho.")],
    selfcheck=[ex("¿Cómo es una semilla «arrugada»: lisa o con pliegues?", "Con pliegues", "La textura arrugada tiene pliegues."), ex("¿Qué unidad se usa para el tamaño?", "Centímetros", "Se mide con regla."), ex("¿Cuántos criterios vimos?", "4", "Tamaño, forma, textura y color.")],
    open_task=task("Describe con cuatro criterios estas dos semillas de ejemplo: A mide 2 cm, es redonda, arrugada y beige. B mide 1 cm, es alargada, lisa y blanca. Después escribe una semejanza y una diferencia.", "A: 2 cm, redonda, arrugada, beige. B: 1 cm, alargada, lisa, blanca. Semejanza: las dos miden menos de 3 cm. Diferencia: A es arrugada y B es lisa.", ["usa los cuatro criterios", "escribe una semejanza", "escribe una diferencia"], ["tabla de dos semillas", "frases"], ["olvidar un criterio", "no usar números"], "Reconoce los criterios y pide una semejanza con un dato."),
    reinforce="Describe dos semillas de tu cocina con los cuatro criterios.",
    extend="Ordena tres semillas de menor a mayor tamaño.",
)

register(
    OA4, 2,
    materials="Este cuaderno con la tabla de seis frutos (color y tamaño), lápiz y colores. En casa: frutas de la cocina, sin cortarlas.",
    use="Aprenderé a clasificar frutos con un solo criterio a la vez. Sirve para agrupar sin mezclar reglas.",
    prior=["Sé describir con tamaño, forma, textura y color.", "Sé qué es un criterio."],
    explain=[
        "Un fruto es la parte de la planta que guarda las semillas. La manzana, el limón, el tomate y la palta son frutos. Para clasificarlos, elige un criterio y úsalo con todos.",
        "Si el criterio es el color, haces grupos de rojos, amarillos y verdes. Si el criterio es el tamaño, haces grupos de pequeños y grandes con una medida clara, por ejemplo menos de 5 cm y 5 cm o más.",
        "Cada fruto va en un solo grupo. Si la manzana va en rojos, no puede ir también en verdes. Cuando termines, cuenta los frutos de cada grupo y comprueba que sumen el total.",
    ],
    vocab=[("fruto", "parte de la planta que guarda las semillas"), ("clasificar", "poner en grupos con un criterio"), ("criterio", "regla para formar los grupos"), ("grupo", "conjunto de frutos que cumplen la regla"), ("total", "cantidad que resulta de juntar todo")],
    worked=[
        {"title": "Clasificar por color", "problem": "Manzana roja, plátano amarillo, limón amarillo, frutilla roja, uva morada, palta verde. Clasifica por color.", "steps": ["Rojo: manzana y frutilla.", "Amarillo: plátano y limón.", "Morado: uva.", "Verde: palta."], "answer": "Rojo 2, amarillo 2, morado 1, verde 1"},
        {"title": "Clasificar por tamaño", "problem": "Con estas medidas de ejemplo: manzana 8 cm, plátano 18 cm, limón 7 cm, frutilla 3 cm, uva 2 cm, palta 12 cm. Regla: menos de 5 cm o 5 cm y más.", "steps": ["Menos de 5 cm: frutilla y uva.", "5 cm y más: manzana, plátano, limón y palta."], "answer": "Menos de 5 cm: 2 frutos. 5 cm y más: 4 frutos"},
    ],
    mistakes=[
        {"wrong": "Poner la manzana en rojos y también en pequeños.", "why": "Se usan dos reglas a la vez.", "fix": "Usa un criterio por vez y haz una clasificación aparte con el otro."},
        {"wrong": "Dejar un fruto sin grupo.", "why": "No se revisa el total.", "fix": "Cuenta los grupos y comprueba que sumen 6."},
    ],
    tiers={
        "recovery": [
            ex("Fruto: frutilla roja de 3 cm. Criterio: color. ¿A qué grupo va?", "Al rojo", "Su color es rojo."),
            ex("Fruto: palta verde de 12 cm. Criterio: color. ¿A qué grupo va?", "Al verde", "Su color es verde."),
            ex("Fruto: uva de 2 cm. Regla: menos de 5 cm. ¿Entra?", "Sí", "Dos es menor que cinco."),
        ],
        "understand": [
            ex("¿Cuántos criterios se usan a la vez al clasificar?", "Uno", "Así los grupos son claros."),
            ex("¿Qué es un fruto?", "La parte de la planta que guarda las semillas", "Dentro hay semillas."),
            ex("Si clasificas seis frutos, ¿cuánto deben sumar todos los grupos?", "6", "Cada fruto va en un solo grupo."),
        ],
        "apply": [
            ex("Clasifica por color: limón amarillo, plátano amarillo, tomate rojo. ¿Cuántos van en amarillo?", "2", "El limón y el plátano son amarillos."),
            ex("Regla: 5 cm y más. Frutos: frutilla 3 cm, manzana 8 cm, limón 7 cm, uva 2 cm. ¿Cuántos entran?", "2", "La manzana y el limón miden 5 cm o más."),
            arith("Grupo rojo: 2 frutos. Grupo amarillo: 2. Grupo morado: 1. Grupo verde: 1. ¿Cuántos frutos son en total?", "2+2+1+1", "Se suman todos los grupos.", " frutos"),
        ],
        "reason": [
            ex("Ema puso el limón en amarillos y el plátano en alargados. ¿Qué error cometió?", "Usó dos criterios distintos", "Los dos deben usar el mismo criterio."),
            ex("Con la regla «menos de 10 cm», ¿van juntos la manzana de 8 cm y la palta de 12 cm?", "No", "La manzana entra y la palta no."),
        ],
        "challenge": [
            ex("Escribe un criterio distinto del color y del tamaño para clasificar frutos.", "Por ejemplo textura: lisos o con pelitos", "Es otro criterio observable."),
            ex("Hay 2 grupos: 4 frutos pequeños y 3 grandes. ¿Cuántos frutos hay?", "7", "Cuatro más tres son siete."),
        ],
    },
    context=[ex("En una feria hay 10 manzanas rojas y 6 manzanas verdes en un cajón. ¿Cuántas manzanas son rojas más que verdes?", "4", "Diez menos seis son cuatro.")],
    selfcheck=[ex("¿La uva es un fruto?", "Sí", "La uva guarda semillas dentro."), ex("¿Qué se hace para formar grupos?", "Elegir un criterio", "Define el grupo."), ex("¿Un fruto puede estar en dos grupos con el mismo criterio?", "No", "Cada uno va solo en un grupo.")],
    open_task=task("Clasifica estos frutos con la medida dada, dos veces. Frutos: sandía (verde, 30 cm), frutilla (roja, 3 cm), naranja (naranja, 8 cm), cereza (roja, 2 cm), plátano (amarillo, 18 cm). Primero por color y luego por tamaño con la regla menos de 10 cm o 10 cm y más.", "Por color: verde (sandía), rojo (frutilla, cereza), naranja (naranja), amarillo (plátano). Por tamaño: menos de 10 cm (frutilla, naranja, cereza), 10 cm y más (sandía, plátano).", ["hace dos clasificaciones", "usa un criterio por vez", "ningún fruto queda sin grupo"], ["dos tablas", "dibujo"], ["mezclar criterios", "olvidar un fruto"], "Reconoce que usa un criterio por clasificación y pide contar los totales."),
    reinforce="Clasifica cuatro frutas de tu cocina por color.",
    extend="Haz una segunda clasificación con un criterio distinto y compara los grupos.",
)

register(
    OA4, 3,
    materials="Este cuaderno con la tabla de seis flores y cuatro tallos (color, tamaño, textura), lápiz y colores.",
    use="Aprenderé a clasificar flores y tallos con otro criterio y a comparar dos clasificaciones. Sirve para ver que una misma colección se puede agrupar de varias maneras.",
    prior=["Sé clasificar con un criterio.", "Sé describir tamaño, forma, textura y color."],
    explain=[
        "Las flores se pueden clasificar por color, por tamaño o por cantidad de pétalos. Los tallos se pueden clasificar por textura, es decir, si son lisos, rugosos o con espinas, y por si son duros o blandos.",
        "Tabla de hoy (medidas de ejemplo, aproximadas). Flores: rosa roja (6 cm), margarita blanca (4 cm), girasol amarillo (20 cm), clavel rojo (5 cm), diente de león amarillo (3 cm), aromo amarillo (1 cm). Tallos: margarita (verde, blando), pino (café, rugoso, duro), rosa (verde, con espinas), junco (verde, liso y delgado).",
        "Probar otro criterio puede cambiar los grupos. Por color, la rosa y el clavel van juntos. Si la regla es «menos de 10 cm», la rosa va con la margarita y el clavel. Ninguna clasificación es la única; lo importante es que la regla sea clara.",
    ],
    vocab=[("flor", "parte de la planta con pétalos"), ("tallo", "parte que sostiene la planta"), ("pétalo", "parte de colores de la flor"), ("rugoso", "áspero al tocarlo"), ("espina", "punta dura que pincha")],
    worked=[
        {"title": "Flores por color", "problem": "Rosa roja, margarita blanca, girasol amarillo, clavel rojo, diente de león amarillo, aromo amarillo. Clasifica por color.", "steps": ["Rojo: rosa y clavel.", "Blanco: margarita.", "Amarillo: girasol, diente de león y aromo."], "answer": "Rojo 2, blanco 1, amarillo 3"},
        {"title": "Tallos por espinas", "problem": "Margarita (blando), pino (duro y rugoso), rosa (con espinas), junco (liso y delgado). Clasifica por si tienen espinas o no.", "steps": ["Con espinas: rosa.", "Sin espinas: margarita, pino y junco."], "answer": "Con espinas: rosa. Sin espinas: margarita, pino y junco"},
    ],
    mistakes=[
        {"wrong": "Pensar que si cambian los grupos, la primera clasificación estaba mala.", "why": "Se cree que hay una sola manera correcta.", "fix": "Si la regla es clara, dos clasificaciones distintas pueden estar correctas."},
        {"wrong": "Decir «tallo bonito» como criterio.", "why": "Bonito es una opinión.", "fix": "Usa criterios que se puedan observar, como la textura."},
    ],
    tiers={
        "recovery": [
            ex("Flor: clavel rojo. Criterio: color. ¿A qué grupo va?", "Al rojo", "Su color es rojo."),
            ex("Tallo: pino, café, rugoso. ¿Qué textura tiene?", "Rugosa", "Está en la ficha."),
            ex("Flor: girasol amarillo de 20 cm. Regla: más de 10 cm. ¿Entra?", "Sí", "Veinte es mayor que diez."),
        ],
        "understand": [
            ex("¿Por qué dos clasificaciones distintas pueden estar bien?", "Porque cada una usa una regla clara", "Cambian los criterios, no el cuidado."),
            ex("¿Qué es un tallo rugoso?", "Uno áspero al tocarlo", "Rugoso es áspero."),
            ex("¿Qué es una espina?", "Una punta dura que pincha", "La rosa las tiene en el tallo."),
        ],
        "apply": [
            ex("Flores amarillas de la tabla: girasol, diente de león y aromo. ¿Cuántas son?", "3", "Son las tres amarillas."),
            arith("El girasol mide 20 cm y la margarita 4 cm. ¿Cuántos centímetros más grande es el girasol?", "20-4", "Se resta la medida de la margarita.", " cm"),
            ex("Tallos: margarita, pino, rosa, junco. ¿Cuál tiene espinas?", "La rosa", "Está en la ficha."),
        ],
        "reason": [
            ex("Luz agrupó la rosa y el clavel porque son rojos. Beto las agrupó porque miden menos de 10 cm. ¿Quién está equivocado?", "Ninguno", "Cada uno usa una regla clara."),
            ex("Si clasificas el aromo y el diente de león por tamaño, ¿quién va en el grupo de menos de 5 cm?", "Los dos", "Miden 1 cm y 3 cm."),
        ],
        "challenge": [
            ex("Propón un criterio para clasificar tallos que no sea duro o blando.", "Por ejemplo con espinas o sin espinas", "Se puede observar mirando el tallo."),
            ex("Hay 3 flores rojas y 3 amarillas. ¿Cuántas flores hay?", "6", "Tres más tres son seis."),
        ],
    },
    context=[ex("Una florería tiene 5 claveles rojos y 8 claveles blancos. ¿Cuántos claveles hay en total?", "13", "Cinco más ocho son trece.")],
    selfcheck=[ex("¿Una flor tiene pétalos?", "Sí", "Los pétalos forman la flor."), ex("¿Cómo se llama la parte que pincha en un tallo?", "Espina", "Es una punta dura."), ex("¿Puedes clasificar las mismas flores de dos maneras?", "Sí", "Cambiando el criterio.")],
    open_task=task("Con la tabla de seis flores de esta clase, haz dos clasificaciones: una por color y otra por si miden menos de 5 cm o 5 cm y más. Compara las dos y escribe una frase que diga qué cambió.", "Por color: rojo (rosa, clavel), blanco (margarita), amarillo (girasol, diente de león, aromo). Por tamaño: menos de 5 cm (margarita, diente de león, aromo), 5 cm y más (rosa, girasol, clavel). Cambió que la rosa y el clavel siguen juntos pero la margarita pasa a otro grupo.", ["hace dos clasificaciones", "escribe la regla de cada una", "compara los grupos"], ["dos tablas", "frase de comparación"], ["mezclar reglas", "no comparar"], "Reconoce que dos reglas dan grupos distintos y pide comparar con un ejemplo."),
    reinforce="Clasifica cuatro flores o tallos de un jardín (sin arrancarlos) por color.",
    extend="Inventa un tercer criterio para tus flores y haz la clasificación.",
)

register(
    OA4, 4,
    materials="Este cuaderno con una clasificación para revisar (con un error), una pauta de revisión y una tabla de cuatro plantas. Lápiz y colores.",
    use="Aprenderé a presentar una clasificación y a explicarla. Sirve para que otra persona entienda mis grupos y los pueda usar.",
    prior=["Sé clasificar con un criterio.", "Sé hacer más de una clasificación."],
    explain=[
        "Una clasificación se presenta con tres partes: la regla, los grupos y el total. Por ejemplo: «Regla: color. Grupos: rojo 2, amarillo 3. Total: 5». Así otra persona entiende rápido.",
        "Antes de presentarla, revisa con una pauta: ¿la regla es clara?, ¿cada objeto está en un solo grupo?, ¿los grupos suman el total?, ¿usé números con unidad? Si algo falla, corrígelo.",
        "Escuchar a los demás también ayuda. Si alguien pregunta «¿por qué la rosa va en ese grupo?», puedes mostrar el dato de la tabla. Así tu explicación se apoya en evidencia.",
    ],
    vocab=[("presentar", "mostrar mi trabajo a otras personas"), ("pauta", "lista de cosas para revisar"), ("evidencia", "dato que apoya mi respuesta"), ("regla", "criterio que usé"), ("total", "suma de todos los grupos")],
    worked=[
        {"title": "Revisar con la pauta", "problem": "Clasificación: regla color; rojo: rosa, clavel; amarillo: girasol, aromo; la margarita no quedó en ningún grupo. Total dicho: 4 de 5 flores. ¿Qué falla?", "steps": ["La regla es clara.", "La margarita no está en un grupo.", "El total no cuenta las 5 flores."], "answer": "Falta la margarita; debe ir en un grupo blanco"},
        {"title": "Presentar en tres partes", "problem": "Regla: tamaño. Menos de 5 cm: margarita, aromo. 5 cm y más: rosa, clavel, girasol. Presenta la clasificación.", "steps": ["Regla: tamaño.", "Grupos: 2 y 3.", "Total: 2 + 3 = 5."], "answer": "Regla tamaño; grupos de 2 y 3 flores; total 5"},
    ],
    mistakes=[
        {"wrong": "Presentar la clasificación sin decir la regla.", "why": "Se piensa que los demás la adivinan.", "fix": "Escribe la regla al comienzo, por ejemplo «regla: color»."},
        {"wrong": "Defender un grupo con «porque sí».", "why": "No se usa evidencia.", "fix": "Cita el dato de la tabla, por ejemplo «mide 3 cm»."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué primera parte lleva una buena presentación de una clasificación?", "La regla", "Se parte diciendo el criterio."),
            ex("Una clasificación tiene grupos de 2 y de 3 objetos. ¿Cuál es el total?", "5", "Dos más tres son cinco."),
            ex("¿Para qué sirve una pauta de revisión?", "Para revisar si mi trabajo está bien", "Es una lista de cosas a comprobar."),
        ],
        "understand": [
            ex("¿Por qué debes apoyar tu explicación en un dato?", "Para que otros me crean con evidencia", "El dato comprueba mi decisión."),
            ex("¿Qué falla si un objeto no quedó en ningún grupo?", "El total no coincide", "Falta contar ese objeto."),
            ex("¿Qué haces si alguien pregunta por qué un objeto está en un grupo?", "Muestro el dato de la tabla", "La evidencia responde."),
        ],
        "apply": [
            ex("Clasificación por color con 6 flores: rojo 2, amarillo 3, blanco 1. ¿Suman bien con el total de 6?", "Sí", "Dos más tres más uno son seis."),
            ex("Clasificación de 5 frutos: pequeños 2, grandes 2. ¿Suman bien con el total de 5?", "No", "Dos más dos son cuatro y falta uno."),
            arith("Regla: textura. Lisos: 3. Rugosos: 4. Con espinas: 1. ¿Cuántos objetos hay en total?", "3+4+1", "Se suman los tres grupos.", " objetos"),
        ],
        "reason": [
            ex("Lía dice que su clasificación es perfecta, pero no escribió la regla. ¿Qué le falta?", "Decir la regla", "Sin regla nadie entiende los grupos."),
            ex("Ana dice que las 3 flores amarillas miden menos de 5 cm, pero el girasol amarillo mide 20 cm. ¿Qué dato la contradice?", "El girasol de 20 cm", "Veinte cm no es menos de cinco."),
        ],
        "challenge": [
            ex("Revisa: regla color; rojos: manzana, tomate; verdes: palta; faltan limón y plátano. ¿Qué grupo falta crear?", "Amarillo", "El limón y el plátano son amarillos."),
            ex("Escribe una pregunta que podría hacerte un compañero sobre tu clasificación.", "Por ejemplo por qué la rosa va en rojo", "Se responde con un dato."),
        ],
    },
    context=[ex("En la feria del curso, Sofía muestra una clasificación de 8 hojas en 3 grupos: 3, 3 y 2. ¿Cuántas hojas clasificó en total?", "8", "Tres más tres más dos son ocho.")],
    selfcheck=[ex("¿Qué debe decir una presentación al comienzo?", "La regla", "Es lo primero."), ex("¿Cuántas partes tiene una buena presentación?", "3", "Regla, grupos y total."), ex("¿Cómo se defiende un grupo?", "Con un dato de la tabla", "La evidencia lo apoya.")],
    open_task=task("Prepara una presentación de 3 frases con esta tabla de ejemplo: lenteja (café, 1 cm), poroto (blanco, 2 cm), semilla de palta (café, 4 cm), maíz (amarillo, 1 cm). Clasifica por tamaño: menos de 2 cm y 2 cm o más. Di la regla, los grupos y el total.", "Regla: tamaño. Grupos: menos de 2 cm (lenteja y maíz, 2) y 2 cm o más (poroto y semilla de palta, 2). Total: 4 semillas.", ["dice la regla", "nombra los dos grupos con su cantidad", "dice el total"], ["tres frases", "tabla"], ["omitir la regla", "olvidar una semilla"], "Reconoce las tres partes y pide comprobar que el total sea 4."),
    reinforce="Cuéntale a alguien de tu casa cómo clasificaste cuatro objetos.",
    extend="Prepara una pregunta que podrían hacerte sobre tu clasificación y su respuesta.",
)
