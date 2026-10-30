"""Cuaderno del estudiante, 1.º básico Ciencias Naturales: OA 01 (seres vivos y cosas no vivas) y OA 02 (animales)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA1, OA2 = "CN01 OA 01", "CN01 OA 02"


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


# ---------------------------------------------------------------- OA 01
register(
    OA1, 1,
    materials="Este cuaderno con el registro de ejemplo del frijol y de la piedra, y un lápiz. Si quieres comprobarlo en casa: un frijol remojado una noche, algodón húmedo y un vaso transparente.",
    use="Aprenderé a buscar pistas para saber si algo está vivo. Sirve para no equivocarme cuando alguien dice «se mueve, entonces está vivo».",
    prior=["Sé nombrar plantas, animales y objetos de mi casa.", "Sé que medir es comparar con los centímetros de una regla."],
    explain=[
        "Un detective de lo vivo busca pistas. Una pista es que los seres vivos crecen: se hacen más grandes con el tiempo. Un frijol en algodón húmedo crece y una piedra no crece nunca, aunque pase mucho tiempo.",
        "Otra pista es que los seres vivos responden a lo que pasa a su alrededor, por ejemplo a la luz o al ruido. También se reproducen: de una semilla nace una planta nueva y de un huevo de gallina puede nacer un pollito.",
        "Moverse no basta para estar vivo. Un auto de juguete rueda y no está vivo. Un árbol casi no se mueve y sí está vivo. Por eso un buen detective junta varias pistas antes de decidir.",
    ],
    vocab=[("ser vivo", "algo que crece, responde a su entorno y se reproduce"), ("cosa no viva", "algo que no crece, no responde y no se reproduce"), ("pista", "dato que observo y que me ayuda a decidir"), ("crecer", "hacerse más grande con el tiempo"), ("registro", "tabla donde anoto lo que observo")],
    worked=[
        {"title": "Leer un registro de crecimiento", "problem": "Registro del frijol: día 0 mide 0 cm, día 2 mide 1 cm, día 4 mide 3 cm, día 6 mide 6 cm. ¿Es una pista de vida?", "steps": ["Miro los números en orden: 0, 1, 3, 6.", "Cada vez el número es mayor.", "Un objeto que se hace más grande con el tiempo está creciendo.", "Crecer es una pista de vida."], "answer": "Sí, el frijol creció y eso es una pista de que está vivo"},
        {"title": "Una pista que no basta", "problem": "Un auto de juguete avanza por el suelo. ¿Está vivo porque se mueve?", "steps": ["Pregunto: ¿crece? No, el auto mide siempre lo mismo.", "Pregunto: ¿tiene crías? No.", "Moverse es solo una pista y aquí faltan las otras."], "answer": "No está vivo; moverse solo no alcanza"},
    ],
    mistakes=[
        {"wrong": "Decir «la nube se mueve, entonces está viva».", "why": "Se usa una sola pista, el movimiento, y el viento también mueve cosas.", "fix": "Revisa también si crece y si se reproduce antes de decidir."},
        {"wrong": "Decir «el árbol no se mueve, entonces no está vivo».", "why": "Se piensa que todo ser vivo camina o salta.", "fix": "Busca otras pistas: el árbol crece, tiene hojas nuevas y da semillas."},
    ],
    tiers={
        "recovery": [
            arith("El frijol midió 0 cm el día 0 y 6 cm el día 6. ¿Cuántos centímetros creció?", "6-0", "Se resta lo que medía al comienzo a lo que mide al final.", " cm"),
            ex("La piedra midió 4 cm el lunes y 4 cm el viernes. ¿Creció la piedra?", "No", "El número no cambió, así que no creció."),
            ex("¿Qué pista de vida muestra un perro cuando pasa de cachorro a perro grande?", "Crece", "Se hace más grande con el tiempo."),
        ],
        "understand": [
            ex("¿Qué significa que un ser vivo «crece»?", "Que se hace más grande con el tiempo", "Es la definición de crecer en esta clase."),
            ex("Una semilla de girasol da origen a una planta nueva. ¿Qué pista de vida es esa?", "Se reproduce", "De una semilla nace otra planta."),
            ex("¿Por qué un registro con números ayuda a un detective?", "Porque permite comparar los datos en el tiempo", "Con los números se ve si algo cambió o no."),
        ],
        "apply": [
            ex("Registro de una planta de poroto: 2 cm, 5 cm, 9 cm, 14 cm (días 1, 3, 5, 7). ¿Es un ser vivo? Usa una pista.", "Sí, porque crece", "Los números suben cada vez."),
            ex("Registro de una tijera: 12 cm, 12 cm, 12 cm, 12 cm (días 1, 3, 5, 7). ¿Crece?", "No", "La medida es igual todos los días."),
            arith("Una lenteja brotó y el día 3 medía 2 cm. El día 7 medía 7 cm. ¿Cuántos centímetros creció entre el día 3 y el día 7?", "7-2", "Se compara la medida final con la inicial.", " cm"),
        ],
        "reason": [
            ex("Lucas dice: «El carrito de cuerda se mueve solo, así que está vivo». ¿Qué le respondes con una pista?", "Que no crece ni tiene crías, así que no está vivo", "Faltan pistas de vida aunque se mueva."),
            ex("Una semilla seca no se mueve. Puesta en algodón húmedo, en 6 días saca una raíz de 3 cm. ¿Qué se puede concluir y por qué?", "Que la semilla está viva, porque creció", "Antes no se notaba y después creció 3 cm."),
        ],
        "challenge": [
            ex("Escribe una cosa que se mueva y no esté viva, y una que casi no se mueva y esté viva.", "Por ejemplo un auto de juguete y un árbol", "Moverse no decide si algo está vivo."),
            ex("Un helado se hace más pequeño al sol. Una planta se hace más grande con agua. ¿Cuál muestra crecimiento y por qué?", "La planta, porque se hace más grande", "El helado cambia por derretirse, no por crecer."),
        ],
    },
    context=[ex("En la plaza ves un banco de madera, un pasto verde y una pelota que rueda. El pasto tenía 3 cm el domingo y 5 cm el sábado siguiente. ¿Cuál de los tres muestra crecimiento?", "El pasto", "Pasó de 3 cm a 5 cm; el banco y la pelota no cambian de tamaño.")],
    selfcheck=[ex("¿Una piedra crece?", "No", "Su tamaño no aumenta con el tiempo."), ex("¿Cuántas pistas conviene juntar antes de decidir si algo está vivo?", "Varias", "Una sola pista, como moverse, puede engañar."), ex("¿Qué es un registro?", "Una tabla donde anoto lo que observo", "Sirve para comparar datos.")],
    open_task=task("Mira este registro de dos objetos. Objeto 1: 10 cm, 10 cm, 10 cm. Objeto 2: 10 cm, 13 cm, 17 cm. Escribe cuál puede ser un ser vivo y qué número te lo mostró. Dibuja los dos.", "El objeto 2 puede ser un ser vivo porque pasó de 10 cm a 17 cm y creció. El objeto 1 siempre midió 10 cm.", ["dice cuál objeto crece", "cita los números del registro", "dibuja los dos objetos"], ["dibujo", "frase con números"], ["decidir sin usar los números", "decir que el objeto 1 está vivo por su forma"], "Reconoce el crecimiento y pide citar al menos dos números del registro para justificar."),
    reinforce="Mira un frijol que crece en un vaso y dibuja su tamaño cada dos días.",
    extend="Explica por qué crecer es una buena pista de vida pero no la única.",
)

register(
    OA1, 2,
    materials="Este cuaderno con la tabla de dos plantas de ejemplo (con agua y sin agua) y un lápiz. En casa, con ayuda de un adulto: dos plantas iguales y un vaso con agua.",
    use="Aprenderé que los seres vivos necesitan agua, alimento y aire. Sirve para saber cómo cuidar a una planta o a una mascota.",
    prior=["Sé que hay plantas y animales.", "Sé leer una tabla con números."],
    explain=[
        "Los seres vivos necesitan agua, alimento y aire para vivir. Tú tomas agua, comes y respiras. Un perro también. Una piedra no necesita nada de eso y por eso no se enferma ni se muere.",
        "Las plantas también necesitan agua y aire. Su alimento lo fabrican ellas con luz, agua y aire. Si una planta no recibe agua, sus hojas se ponen caídas. Si le das agua, sus hojas siguen firmes.",
        "Los peces no respiran como tú, pero toman el aire que hay mezclado en el agua. Por eso un pez necesita agua limpia. Cada ser vivo recibe lo que necesita de una manera distinta.",
    ],
    vocab=[("agua", "líquido que los seres vivos necesitan para vivir"), ("alimento", "lo que come un ser vivo para tener energía y crecer"), ("aire", "gas que está a nuestro alrededor y que se respira"), ("necesitar", "no poder vivir sin algo"), ("hoja caída", "hoja que perdió su firmeza por falta de agua")],
    worked=[
        {"title": "Dos plantas, una con agua", "problem": "Planta A recibe 2 cucharadas de agua al día. Planta B no recibe agua. Hojas firmes: día 1, A=6 y B=6; día 7, A=6 y B=1. ¿Qué pasó con B?", "steps": ["Al comienzo las dos tenían 6 hojas firmes.", "El día 7 A seguía con 6 y B quedó con 1.", "La única diferencia es el agua.", "Sin agua las hojas de B se pusieron caídas."], "answer": "B perdió hojas firmes porque no recibió agua"},
        {"title": "El aire y la respiración", "problem": "Sentada, Ema respira 12 veces en 30 segundos. Después de saltar, respira 20 veces en 30 segundos. ¿Qué muestra?", "steps": ["Comparo 12 con 20.", "20 es mayor que 12.", "Respirar es tomar aire y el cuerpo pide más cuando se mueve."], "answer": "Ema necesita aire y toma más aire al saltar"},
    ],
    mistakes=[
        {"wrong": "Pensar que las plantas no necesitan nada porque no comen como nosotros.", "why": "No se ve que fabrican su alimento.", "fix": "Recuerda que las plantas necesitan agua, aire y luz para fabricar su alimento."},
        {"wrong": "Creer que si una planta tiene mucha agua en la mesa, no necesita más.", "why": "Se mira una sola vez y no el tiempo.", "fix": "Los seres vivos necesitan agua cada cierto tiempo, no solo una vez."},
    ],
    tiers={
        "recovery": [
            ex("Nombra las tres cosas que necesitan los seres vivos para vivir.", "Agua, alimento y aire", "Son las tres necesidades de esta clase."),
            ex("¿Una piedra necesita agua para vivir?", "No", "La piedra no está viva."),
            ex("Un gato tiene hambre. ¿Qué necesita?", "Alimento", "El hambre indica que le falta comer."),
        ],
        "understand": [
            ex("¿Qué necesita una planta además de agua y aire para fabricar su alimento?", "Luz", "Fabrica su alimento con luz, agua y aire."),
            ex("¿Por qué un pez necesita agua limpia?", "Porque toma el aire que hay en el agua", "El pez respira aire mezclado con el agua."),
            ex("¿Qué se ve en una planta a la que le falta agua?", "Las hojas caídas", "Pierden firmeza sin agua."),
        ],
        "apply": [
            arith("En la tabla, la planta B tenía 6 hojas firmes el día 1 y 1 hoja firme el día 7. ¿Cuántas hojas firmes perdió?", "6-1", "Se resta lo que quedó a lo que había.", " hojas"),
            ex("Planta A tuvo agua los 7 días y mantuvo 6 hojas firmes. Planta B no tuvo agua. ¿Qué planta sigue mejor?", "La planta A", "Con agua sus hojas siguen firmes."),
            arith("Ema respiró 12 veces en 30 segundos sentada y 20 veces después de saltar. ¿Cuántas respiraciones más hizo después de saltar?", "20-12", "Se resta la cantidad de reposo a la del salto.", " respiraciones"),
        ],
        "reason": [
            ex("Nico olvidó regar su planta durante 7 días y las hojas se cayeron. Dice «la planta se murió de pena». ¿Qué falta explicar?", "Que le faltó agua", "La causa observable es que no recibió agua."),
            ex("Una pecera con 4 peces se tapa por completo con una tapa sin agujeros. ¿Qué necesidad puede faltarles?", "Aire", "Los peces toman el aire mezclado en el agua y una tapa muy cerrada lo limita."),
        ],
        "challenge": [
            ex("Dos plantas iguales: una junto a la ventana con agua y otra en un clóset oscuro con agua. ¿Qué necesidad cambia entre las dos?", "La luz", "Las dos tienen agua; solo cambia la luz."),
            ex("Escribe una necesidad que tengan en común una planta y un perro.", "Agua o aire", "Ambos los necesitan para vivir."),
        ],
    },
    context=[ex("En casa hay una maceta con albahaca y un canario en su jaula. El canario no tiene agua desde ayer y la maceta sí. ¿Qué ser vivo está en peligro primero y por qué?", "El canario, porque le falta agua", "Un animal necesita agua cada día y hoy no la tiene.")],
    selfcheck=[ex("¿Qué toma el cuerpo cuando respiras?", "Aire", "Respirar es tomar aire."), ex("¿Qué necesidad cubre comer una manzana?", "El alimento", "La manzana es alimento."), ex("¿Una planta a la que le falta agua tiene hojas firmes o caídas?", "Caídas", "Sin agua pierde firmeza.")],
    open_task=task("Imagina que cuidas un conejo y una maceta de lavanda. Escribe en una tabla de dos columnas qué agua, alimento y aire recibe cada uno en un día. Usa dibujos si quieres.", "Conejo: agua limpia en su bebedero, pasto y zanahoria, aire fresco de una jaula ventilada. Lavanda: riego con una taza de agua, luz y tierra, aire de la ventana abierta.", ["nombra agua, alimento y aire para el conejo", "nombra agua y aire para la planta", "usa una tabla ordenada"], ["tabla", "dibujos rotulados"], ["decir que la planta come como el conejo", "olvidar el aire"], "Reconoce las necesidades y pide aclarar cómo cada ser vivo recibe lo que necesita."),
    reinforce="Mide cuántos vasos de agua tomas en un día y anótalos.",
    extend="Explica por qué una planta en un clóset oscuro y con agua también se pone débil.",
)

register(
    OA1, 3,
    materials="Este cuaderno con los registros de ejemplo (planta hacia la ventana, talla de Lía, huevos), lápiz y colores. En casa: una planta junto a una ventana y una regla.",
    use="Aprenderé tres pistas de vida: responder a lo que pasa, crecer y reproducirse. Sirve para explicar por qué un animal o una planta están vivos.",
    prior=["Sé que los seres vivos necesitan agua, alimento y aire.", "Sé restar números pequeños."],
    explain=[
        "Los seres vivos responden a estímulos. Un estímulo es algo que pasa en su entorno, como la luz o un ruido. Si hay un ruido fuerte, el gato salta. Si hay luz en una ventana, la planta crece hacia esa luz.",
        "Los seres vivos crecen. Un cachorro pasa a ser un perro grande y tú mides más cada año. Los seres vivos también se reproducen: la gallina pone huevos, de los huevos salen pollitos y una semilla da una planta nueva.",
        "Las cosas no vivas no hacen esas tres cosas. Un juguete no crece, no responde por sí mismo y no tiene crías. Si algo cumple las tres pistas, puedes decir con seguridad que es un ser vivo.",
    ],
    vocab=[("estímulo", "algo que pasa en el entorno, como luz o ruido"), ("responder", "cambiar lo que hago cuando hay un estímulo"), ("crecer", "hacerse más grande con el tiempo"), ("reproducirse", "tener crías o semillas que son nuevos seres vivos"), ("cría", "ser vivo recién nacido")],
    worked=[
        {"title": "Una planta que responde a la luz", "problem": "Una planta junto a la ventana. Su punta se movió hacia la ventana 0 cm el día 1, 2 cm el día 3 y 5 cm el día 5. ¿Qué estímulo hubo y cómo respondió?", "steps": ["Los números suben: 0, 2, 5.", "La punta se mueve hacia la ventana.", "En la ventana entra luz.", "El estímulo es la luz y la planta respondió girando su punta."], "answer": "El estímulo fue la luz y la planta respondió inclinándose hacia ella"},
        {"title": "Crecer y reproducirse", "problem": "Lía midió 110 cm en marzo y 114 cm en diciembre. Una gallina puso 3 huevos y salieron 3 pollitos. ¿Qué pistas son?", "steps": ["Lía pasó de 110 a 114: creció.", "De cada huevo salió un pollito.", "Tener crías es reproducirse."], "answer": "Lía creció y la gallina se reprodujo"},
    ],
    mistakes=[
        {"wrong": "Decir que una puerta que se abre con el viento «responde» como un ser vivo.", "why": "Se confunde moverse con responder.", "fix": "Un ser vivo cambia lo que hace por sí mismo; la puerta solo es empujada."},
        {"wrong": "Pensar que un juguete tiene crías porque viene en caja con otros juguetes.", "why": "No se distingue fabricar de reproducirse.", "fix": "Reproducirse es que el propio ser vivo tenga crías."},
    ],
    tiers={
        "recovery": [
            ex("Un perro dormido despierta cuando suena un portazo. ¿Cuál fue el estímulo?", "El ruido", "El portazo es lo que pasó en su entorno."),
            arith("Lía midió 110 cm en marzo y 114 cm en diciembre. ¿Cuántos centímetros creció?", "114-110", "Se resta la medida inicial a la final.", " cm"),
            ex("De una semilla de zapallo nace una planta nueva. ¿Qué pista de vida es?", "Reproducirse", "La semilla da un ser vivo nuevo."),
        ],
        "understand": [
            ex("¿Qué es un estímulo?", "Algo que pasa en el entorno, como luz o ruido", "Es lo que provoca una respuesta."),
            ex("¿Qué hace la planta cuando la luz viene solo por un lado?", "Se inclina hacia la luz", "Responde al estímulo luz."),
            ex("¿Reproducirse es lo mismo que comer?", "No", "Reproducirse es tener crías o semillas; comer es alimentarse."),
        ],
        "apply": [
            arith("La punta de la planta se movió 5 cm hacia la ventana en 5 días. Si se movió 2 cm en los primeros 3 días, ¿cuántos cm se movió en los últimos 2 días?", "5-2", "Se resta lo movido al comienzo del total.", " cm"),
            arith("La gallina puso 3 huevos y otra gallina puso 2. ¿Cuántos huevos hay en total?", "3+2", "Se juntan los huevos de las dos gallinas.", " huevos"),
            ex("Las flores de un jardín se cierran en la noche y se abren en el día. ¿Qué estímulo cambia entre el día y la noche?", "La luz", "Hay luz de día y poca luz de noche."),
        ],
        "reason": [
            ex("Una pelota rueda cuando la empujas y se detiene sola. ¿Responde como un ser vivo? Justifica.", "No, solo fue empujada", "No cambia lo que hace por sí misma y no crece ni se reproduce."),
            ex("Un caracol esconde sus cuernitos cuando lo tocas. ¿Qué pista de vida muestra?", "Responde a un estímulo", "Reacciona al toque."),
        ],
        "challenge": [
            ex("Un huevo fértil recién puesto todavía no tiene pollito formado. Si la gallina lo empolla unos 21 días, sale un pollito. ¿Qué pista de vida aparece después de ese tiempo?", "Nace un pollito, o sea se reproduce", "De un huevo fértil sale una cría."),
            ex("Escribe un estímulo y la respuesta de un animal.", "Por ejemplo ruido fuerte y el gato salta", "Un estímulo provoca una respuesta."),
        ],
    },
    context=[ex("Juan puso un frijol en un vaso junto a una ventana. A los 6 días la punta de la planta se inclinaba 4 cm hacia la ventana. ¿Qué estímulo y qué respuesta ves?", "Estímulo: la luz; respuesta: se inclina hacia ella", "La planta cambió su dirección por la luz.")],
    selfcheck=[ex("¿Qué tres pistas de vida vimos hoy?", "Responder, crecer y reproducirse", "Son las tres pistas de la clase."), ex("¿El viento que mueve una puerta es un estímulo que ella siente?", "No", "La puerta no es un ser vivo."), ex("¿Una semilla que da una planta nueva se reproduce?", "Sí", "Da un ser vivo nuevo.")],
    open_task=task("Mira estas tres historias y escribe qué pista de vida muestra cada una. Historia 1: un gato cierra los ojos cuando le dan luz fuerte. Historia 2: un pino de 10 cm pasa a medir 25 cm. Historia 3: una perra tiene 4 cachorros.", "Historia 1: responde a la luz. Historia 2: crece de 10 cm a 25 cm. Historia 3: se reproduce porque tiene 4 crías.", ["une cada historia con su pista", "usa las palabras responder, crecer o reproducirse", "cita un dato de la historia"], ["frases cortas", "dibujo de una de las historias"], ["confundir crecer con reproducirse", "no citar datos"], "Reconoce las tres pistas y pide citar un dato de cada historia."),
    reinforce="Observa a una mascota o a una planta y anota una respuesta a un estímulo.",
    extend="Explica por qué las cosas no vivas no se reproducen aunque haya muchas parecidas.",
)

register(
    OA1, 4,
    materials="Este cuaderno con la tabla de ocho objetos y cuatro pistas, un lápiz y colores. En casa: nada especial.",
    use="Aprenderé a clasificar objetos en seres vivos y cosas no vivas usando pistas. Sirve para decidir con evidencia y no por lo que parece.",
    prior=["Sé las pistas de vida: crecer, responder y reproducirse.", "Sé que los seres vivos necesitan agua, alimento y aire."],
    explain=[
        "Clasificar es poner las cosas en grupos. Hoy haremos dos grupos: seres vivos y cosas no vivas. Para cada objeto revisas las pistas: ¿crece?, ¿responde?, ¿se reproduce?, ¿necesita agua, alimento y aire?",
        "Mira una tabla con Sí y No. Si un objeto tiene Sí en todas las pistas, es un ser vivo. Si tiene No en todas las pistas, es una cosa no viva. Así decides con evidencia y no porque algo se ve bonito o se mueve.",
        "Algunos casos engañan. El champiñón no se mueve ni parece animal, pero crece, se reproduce y necesita alimento, así que es un ser vivo. Una pelota rueda, pero no tiene ninguna pista de vida.",
    ],
    vocab=[("clasificar", "poner objetos en grupos según una regla"), ("evidencia", "dato que observo y apoya mi decisión"), ("ser vivo", "tiene todas las pistas de vida"), ("cosa no viva", "no tiene las pistas de vida"), ("criterio", "regla que uso para formar los grupos")],
    worked=[
        {"title": "Clasificar con una tabla", "problem": "Perro: crece Sí, responde Sí, se reproduce Sí, necesita agua y alimento Sí. Piedra: No, No, No, No. ¿En qué grupo va cada uno?", "steps": ["Perro tiene Sí en las cuatro pistas.", "Piedra tiene No en las cuatro pistas.", "Un ser vivo cumple las pistas y una cosa no viva no."], "answer": "Perro: ser vivo. Piedra: cosa no viva"},
        {"title": "Un caso que engaña", "problem": "Champiñón: crece Sí, responde Sí (cambia con la humedad y el ambiente), se reproduce Sí, necesita alimento Sí. No se mueve. ¿Es un ser vivo?", "steps": ["No camina ni salta, pero eso no es una pista de vida.", "Tiene Sí en las cuatro pistas.", "Por la evidencia, va en seres vivos."], "answer": "El champiñón es un ser vivo"},
    ],
    mistakes=[
        {"wrong": "Poner el auto de juguete en seres vivos porque rueda.", "why": "Se usa solo el movimiento.", "fix": "Revisa la tabla: el auto tiene No en crecer, responder y reproducirse."},
        {"wrong": "Poner el árbol en cosas no vivas porque no se mueve.", "why": "Se mira lo que se ve de lejos.", "fix": "Revisa la tabla: el árbol crece, responde a la luz y da semillas."},
    ],
    tiers={
        "recovery": [
            ex("Objeto: reloj. Crece No, responde No, se reproduce No, necesita agua y alimento No. ¿Ser vivo o cosa no viva?", "Cosa no viva", "Tiene No en todas las pistas."),
            ex("Objeto: mariposa. Crece Sí, responde Sí, se reproduce Sí, necesita alimento Sí. ¿Ser vivo o cosa no viva?", "Ser vivo", "Tiene Sí en todas las pistas."),
            ex("Al clasificar objetos en seres vivos y cosas no vivas, ¿qué estás haciendo?", "Poner las cosas en grupos según una regla", "Se separan en grupos con un criterio."),
        ],
        "understand": [
            ex("¿Qué dos grupos usamos hoy?", "Seres vivos y cosas no vivas", "Son los grupos de la clase."),
            ex("¿Qué es una evidencia?", "Un dato que observo y apoya mi decisión", "Sirve para justificar."),
            ex("¿Por qué el champiñón es un ser vivo si no se mueve?", "Porque crece, se reproduce y necesita alimento", "Tiene las pistas aunque no camine."),
        ],
        "apply": [
            ex("Tabla: manzano Sí, Sí, Sí, Sí. Taza de loza No, No, No, No. Mochila No, No, No, No. ¿Cuál es el único ser vivo?", "El manzano", "Es el único con Sí en todas."),
            ex("Tabla: pez Sí, Sí, Sí, Sí. Pelota No, No, No, No. Nube No, No, No, No. ¿Cuántas cosas no vivas hay?", "2", "La pelota y la nube tienen No en todas."),
            ex("Clasifica estas cuatro: vaca, lápiz, flor, bicicleta. Escribe los seres vivos.", "Vaca y flor", "Crecen, responden y se reproducen; el lápiz y la bicicleta no."),
        ],
        "reason": [
            ex("Sofía dice que la bicicleta es un ser vivo porque se mueve rápido. ¿Qué evidencia de la tabla la contradice?", "Tiene No en crecer, responder y reproducirse", "No cumple ninguna pista de vida."),
            ex("Tomás dice que el cactus no es un ser vivo porque casi no se mueve. Si el cactus crece 2 cm al año y da flores con semillas, ¿tiene razón?", "No", "Crece y se reproduce, así que es un ser vivo."),
        ],
        "challenge": [
            ex("Hay 6 objetos: gato, roca, rosa, lápiz, hormiga, vaso. ¿Cuántos son seres vivos?", "3", "Gato, rosa y hormiga son seres vivos."),
            ex("Escribe un objeto que sea una cosa no viva y explica con una pista.", "Por ejemplo una silla porque no crece", "No tiene pistas de vida."),
        ],
    },
    context=[ex("En una mesa hay una planta de menta, un vaso de vidrio, una piedra de río y un hongo champiñón. ¿Cuáles son los seres vivos?", "La menta y el champiñón", "Crecen, responden y se reproducen.")],
    selfcheck=[ex("¿Qué grupo tiene todas las pistas de vida?", "Seres vivos", "Cumplen las pistas."), ex("¿Una tijera es un ser vivo?", "No", "No crece ni se reproduce."), ex("Si algo se mueve, ¿ya es un ser vivo?", "No", "Falta revisar las otras pistas.")],
    open_task=task("Con esta lista de seis cosas: abeja, cuchara, tulipán, nube, perro, sombrero. Haz dos columnas, seres vivos y cosas no vivas, y escribe una pista de vida junto a cada ser vivo.", "Seres vivos: abeja (crece y tiene crías), tulipán (da semillas), perro (crece). Cosas no vivas: cuchara, nube, sombrero.", ["clasifica las seis cosas", "da una pista por cada ser vivo", "usa dos columnas"], ["tabla de dos columnas", "frase con pistas"], ["clasificar por el movimiento", "no justificar con una pista"], "Reconoce los dos grupos y pide una pista para justificar cada ser vivo."),
    reinforce="Haz una tabla de cuatro cosas de tu casa y clasifícalas.",
    extend="Explica qué otra pista de vida usarías para decidir sobre un hongo.",
)

# ---------------------------------------------------------------- OA 02
register(
    OA2, 1,
    materials="Este cuaderno con la ficha de cinco animales (nombre, tamaño, cubierta, desplazamiento y hábitat), lápiz y colores.",
    use="Aprenderé a mirar un animal como un naturalista. Sirve para describir cómo es y dónde vive.",
    prior=["Sé nombrar animales que conozco.", "Sé comparar tamaños con las palabras grande y pequeño."],
    explain=[
        "Un naturalista mira con cuidado a los animales y anota lo que ve. Hoy anotamos cuatro datos: el tamaño, con qué está cubierto su cuerpo, cómo se mueve y dónde vive.",
        "La cubierta del cuerpo puede ser pelo, plumas, escamas, piel suave o un caparazón. El perro tiene pelo, la gallina tiene plumas y la trucha tiene escamas. Cada cubierta protege al animal de una forma distinta.",
        "El tamaño se compara: una hormiga mide cerca de 1 cm, un gato mide unos 25 cm de alto y un caballo unos 150 cm. Son medidas aproximadas. Anotar estos datos en una ficha permite comparar sin equivocarse.",
    ],
    vocab=[("naturalista", "persona que observa y anota cómo son los seres vivos"), ("cubierta del cuerpo", "lo que cubre la piel del animal, como pelo o plumas"), ("tamaño", "qué tan grande o pequeño es"), ("hábitat", "lugar donde vive un animal"), ("ficha", "hoja donde anoto datos")],
    worked=[
        {"title": "Llenar una ficha", "problem": "Gallina: mide unos 40 cm, tiene plumas, camina con dos patas, vive en un gallinero en el campo. Escribe su ficha.", "steps": ["Tamaño: unos 40 cm.", "Cubierta: plumas.", "Cómo se mueve: camina con dos patas.", "Dónde vive: gallinero en el campo."], "answer": "Gallina: 40 cm, plumas, camina, vive en el campo"},
        {"title": "Comparar dos fichas", "problem": "Gato: 25 cm, pelo. Caballo: 150 cm, pelo. ¿Cuál es más alto y qué tienen igual?", "steps": ["150 es mayor que 25.", "El caballo es más alto.", "Los dos tienen pelo."], "answer": "El caballo es más alto y los dos tienen pelo"},
    ],
    mistakes=[
        {"wrong": "Decir «el animal es lindo» en lugar de anotar un dato.", "why": "Se da una opinión y no una observación.", "fix": "Anota un dato que se pueda comprobar, como tamaño o cubierta."},
        {"wrong": "Escribir «es grande» sin comparar.", "why": "Grande depende de con qué se compare.", "fix": "Escribe un número, por ejemplo 150 cm, o compara con otro animal."},
    ],
    tiers={
        "recovery": [
            ex("Ficha: trucha, escamas, nada con aletas, vive en el río. ¿Qué cubierta tiene?", "Escamas", "La ficha lo dice."),
            ex("Ficha: perro, pelo, camina con cuatro patas. ¿Cómo se mueve?", "Camina con cuatro patas", "Dato de la ficha."),
            ex("Ficha: canario, plumas, vuela con alas. ¿Qué cubierta tiene?", "Plumas", "La ficha lo dice."),
        ],
        "understand": [
            ex("¿Qué es el hábitat de un animal?", "El lugar donde vive", "Es su casa en la naturaleza."),
            ex("¿Qué cuatro datos anotamos en una ficha?", "Tamaño, cubierta, cómo se mueve y hábitat", "Son los datos de la clase."),
            ex("¿Es «bonito» un dato de una ficha de naturalista?", "No", "Es una opinión, no una observación."),
        ],
        "apply": [
            arith("Una hormiga mide 1 cm y un gato mide 25 cm de alto. ¿Cuántos centímetros más alto es el gato?", "25-1", "Se resta la medida pequeña a la grande.", " cm"),
            arith("Un caballo mide 150 cm y un gato 25 cm de alto. ¿Cuántos centímetros más alto es el caballo?", "150-25", "Se resta la medida del gato a la del caballo.", " cm"),
            ex("Un animal tiene pelo, camina con cuatro patas y vive en el campo. ¿Podría ser un caballo o un pez?", "Un caballo", "El pez no tiene pelo ni patas."),
        ],
        "reason": [
            ex("Ana dijo «el sapo es pequeño». Mide 8 cm. ¿Por qué un dato con número es mejor?", "Porque se puede comprobar con una regla", "Pequeño depende de con qué se compare."),
            ex("Ficha A: 40 cm, plumas. Ficha B: 40 cm, escamas. ¿Qué dato las diferencia?", "La cubierta del cuerpo", "El tamaño es igual; cambia plumas por escamas."),
        ],
        "challenge": [
            ex("Escribe tres datos de un animal que conozcas: tamaño, cubierta y hábitat.", "Por ejemplo gato, pelo y casa", "Son datos observables."),
            ex("Una vaca tiene pelo y mide 140 cm. Un caballo tiene pelo y mide 150 cm. ¿Cuál es más alto y por cuántos centímetros?", "El caballo, por 10 cm", "150 menos 140 es 10."),
        ],
    },
    context=[ex("En el parque ves un picaflor de 10 cm con plumas que vuela y una paloma de 30 cm con plumas que vuela. ¿Cuántos centímetros más grande es la paloma?", "20 cm", "30 menos 10 es 20.")],
    selfcheck=[ex("¿Qué cubierta tiene una gallina?", "Plumas", "Las aves tienen plumas."), ex("¿Qué hace un naturalista con lo que observa?", "Lo anota en una ficha", "Registra datos para comparar."), ex("¿Qué cubierta tiene un pez?", "Escamas", "Los peces suelen tener escamas.")],
    open_task=task("Completa una ficha de naturalista con estos cuatro animales (datos de ejemplo aproximados): perro (50 cm, pelo, camina con cuatro patas, casa), pingüino (60 cm, plumas, nada con aletas, costa), lagartija (10 cm, escamas, camina con cuatro patas, piedras), trucha (30 cm, escamas, nada con aletas, río). Después dibuja uno.", "Ficha del perro: tamaño 50 cm, cubierta pelo, se mueve caminando con cuatro patas, vive en una casa. Dibujo: un perro con pelo.", ["escribe los cuatro datos", "usa números para el tamaño", "dibuja un animal"], ["tabla", "dibujo"], ["escribir opiniones", "olvidar la unidad cm"], "Reconoce datos observables y pide agregar la unidad en cada tamaño."),
    reinforce="Mira una mascota y anota sus cuatro datos.",
    extend="Compara dos animales con una ficha y escribe una diferencia y una semejanza.",
)

register(
    OA2, 2,
    materials="Este cuaderno con la tabla de seis animales y cómo se desplazan, lápiz y colores.",
    use="Aprenderé cómo se desplazan los animales y qué partes del cuerpo usan. Sirve para entender por qué cada animal vive donde vive.",
    prior=["Sé la ficha de naturalista.", "Sé nombrar partes como patas, alas y aletas."],
    explain=[
        "Los animales se desplazan de distintas maneras. Algunos caminan con patas, como el perro. Otros vuelan con alas, como el cóndor. Otros nadan con aletas, como el pez. Otros reptan, como la serpiente y el caracol.",
        "La parte del cuerpo que usan se llama estructura de desplazamiento. Las patas sirven para caminar y saltar. Las alas sirven para volar. Las aletas sirven para nadar. Algunos animales no tienen patas y se arrastran.",
        "Un mismo animal puede usar más de una estructura. El pato camina con patas, nada con patas con membrana y vuela con alas. Para describirlo, escribe cada forma de moverse que observas.",
    ],
    vocab=[("desplazarse", "moverse de un lugar a otro"), ("patas", "estructuras para caminar o saltar"), ("alas", "estructuras para volar"), ("aletas", "estructuras para nadar"), ("reptar", "moverse arrastrando el cuerpo por el suelo")],
    worked=[
        {"title": "Unir animal y estructura", "problem": "Cóndor, trucha, perro, caracol. ¿Qué estructura usa cada uno?", "steps": ["Cóndor vuela: alas.", "Trucha nada: aletas.", "Perro camina: patas.", "Caracol repta: su pie, que se arrastra."], "answer": "Cóndor alas, trucha aletas, perro patas, caracol repta"},
        {"title": "Más de una forma", "problem": "El pato camina en la orilla, nada en el agua y vuela al cielo. ¿Cuántas formas de moverse tiene?", "steps": ["Camina: una.", "Nada: dos.", "Vuela: tres."], "answer": "Tiene tres formas de moverse"},
    ],
    mistakes=[
        {"wrong": "Decir que todas las aves vuelan.", "why": "Se generaliza desde las aves que se ven más.", "fix": "El pingüino tiene alas, pero las usa para nadar."},
        {"wrong": "Decir que los animales sin patas no se mueven.", "why": "Se piensa que mover es solo caminar.", "fix": "La serpiente y el caracol se desplazan reptando."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué estructura usa un pez para nadar?", "Aletas", "Las aletas empujan en el agua."),
            ex("¿Qué estructura usa una gaviota para volar?", "Alas", "Las alas sostienen en el aire."),
            ex("¿Qué estructura usa un conejo para saltar?", "Patas", "Salta con las patas."),
        ],
        "understand": [
            ex("¿Qué significa «desplazarse»?", "Moverse de un lugar a otro", "Es cambiar de lugar."),
            ex("¿Cómo se desplaza una serpiente?", "Reptando", "Arrastra su cuerpo."),
            ex("¿Cuántas formas de moverse tiene el pato?", "Tres: caminar, nadar y volar", "Camina con patas, nada con patas con membrana y vuela con alas."),
        ],
        "apply": [
            ex("Une: caballo, delfín, mariposa. Estructuras: patas, aletas, alas. Escribe las parejas.", "Caballo patas, delfín aletas, mariposa alas", "Cada animal usa la estructura de su forma de moverse."),
            ex("Un animal vive en el mar, no tiene patas y se mueve con aletas. ¿Se parece más a una vaca o a un tiburón?", "Un tiburón", "Nada con aletas."),
            ex("Tabla: tortuga camina, gaviota vuela, salmón nada. ¿Cuántos animales usan patas?", "1", "Solo la tortuga camina con patas."),
        ],
        "reason": [
            ex("Pedro dice que el pingüino no es un ave porque no vuela. Si el pingüino tiene plumas y alas, ¿qué le respondes?", "Que sí es un ave: tiene plumas y alas, aunque use las alas para nadar", "Las plumas y las alas son características de las aves."),
            ex("Un gusano no tiene patas ni alas ni aletas, pero se mueve. ¿Cómo lo hace?", "Reptando, arrastra su cuerpo", "Algunos animales se mueven sin patas."),
        ],
        "challenge": [
            ex("Escribe un animal que use dos formas de moverse y nómbralas.", "Por ejemplo la rana: nada y salta", "Tiene dos formas."),
            ex("Hay 4 gaviotas volando y 3 caminando en la orilla. ¿Cuántos animales hay?", "7", "Cuatro más tres son siete."),
        ],
    },
    context=[ex("En una laguna ves 5 patos nadando, 2 caminando por la orilla y 1 volando. ¿Cuántos patos ves en total?", "8", "Cinco más dos más uno son ocho.")],
    selfcheck=[ex("¿Qué estructura sirve para volar?", "Alas", "Las alas permiten volar."), ex("¿Qué estructura sirve para nadar?", "Aletas", "Las aletas empujan el agua."), ex("¿Cómo se mueve un caracol?", "Repta", "Arrastra su cuerpo.")],
    open_task=task("Mira esta lista de animales y escribe cómo se desplaza cada uno: rana, cóndor, delfín, culebra, conejo, pingüino. Usa las palabras caminar, saltar, volar, nadar o reptar.", "Rana: saltar y nadar. Cóndor: volar. Delfín: nadar. Culebra: reptar. Conejo: saltar. Pingüino: nadar y caminar.", ["escribe una forma de moverse por cada animal", "usa las palabras de la lista", "nombra la estructura"], ["lista", "dibujo de dos animales"], ["decir que el pingüino vuela", "olvidar que algunos reptan"], "Reconoce los tipos de desplazamiento y pide nombrar la estructura que usan."),
    reinforce="Observa dos animales de tu barrio y anota cómo se mueven.",
    extend="Explica por qué la forma de moverse ayuda a un animal a vivir en su lugar.",
)

register(
    OA2, 3,
    materials="Este cuaderno con tarjetas de animales y de lugares donde viven (bosque, desierto, río, mar, cordillera), lápiz y colores.",
    use="Aprenderé que cada animal vive en un hábitat que le da lo que necesita. Sirve para entender por qué un pez no vive en un desierto.",
    prior=["Sé cómo se desplazan los animales.", "Sé que los seres vivos necesitan agua, alimento y aire."],
    explain=[
        "El hábitat es el lugar donde vive un animal y donde encuentra alimento, agua y refugio. Hay hábitats de tierra, como un bosque o un desierto, y hábitats de agua, como un río o el mar.",
        "El cuerpo de cada animal se parece a su hábitat. El pez tiene aletas y escamas para vivir en el agua. El cóndor tiene alas muy grandes para volar sobre la cordillera. El guanaco tiene pelo grueso para el frío de la cordillera.",
        "Si sacas un animal de su hábitat, puede tener problemas. Un pez fuera del agua no puede respirar bien. Por eso cuidamos el lugar donde viven los animales.",
    ],
    vocab=[("hábitat", "lugar donde vive un animal y encuentra lo que necesita"), ("refugio", "lugar donde se protege"), ("desierto", "lugar muy seco con poca agua"), ("bosque", "lugar con muchos árboles"), ("mar", "gran cantidad de agua salada")],
    worked=[
        {"title": "Animal y hábitat", "problem": "Pingüino de Humboldt: plumas, nada con aletas, come peces, hace nidos en las rocas de la costa. ¿Cuál es su hábitat?", "steps": ["Come peces: busca comida en el mar.", "Nida en rocas junto al mar.", "Su hábitat está en la costa y el mar."], "answer": "Su hábitat es la costa y el mar"},
        {"title": "Cuerpo y lugar", "problem": "El guanaco vive en la cordillera, donde hace frío. Tiene pelo grueso. ¿Para qué le sirve?", "steps": ["En la cordillera hace frío.", "El pelo grueso da abrigo.", "Le ayuda a mantenerse tibio."], "answer": "El pelo grueso lo abriga del frío"},
    ],
    mistakes=[
        {"wrong": "Decir que el hábitat de un perro es solo la casa.", "why": "Se piensa en las mascotas y no en los animales silvestres.", "fix": "El hábitat natural de un animal silvestre es el lugar de la naturaleza donde vive; la casa es el lugar de una mascota."},
        {"wrong": "Pensar que un pez puede vivir fuera del agua un rato largo.", "why": "No se relaciona el cuerpo con el hábitat.", "fix": "El pez necesita estar en el agua para respirar."},
    ],
    tiers={
        "recovery": [
            ex("¿Dónde vive un pez: en el agua o en el desierto?", "En el agua", "Su cuerpo está hecho para nadar."),
            ex("¿Qué animal vive en el mar: el delfín o el guanaco?", "El delfín", "El guanaco vive en la cordillera."),
            ex("¿Qué animal vuela sobre la cordillera: el cóndor o la trucha?", "El cóndor", "El cóndor tiene alas muy grandes."),
        ],
        "understand": [
            ex("¿Qué encuentra un animal en su hábitat?", "Alimento, agua y refugio", "Eso necesita para vivir."),
            ex("¿Por qué el guanaco tiene pelo grueso?", "Porque en la cordillera hace frío", "El pelo lo abriga."),
            ex("¿Qué es un refugio?", "Un lugar donde el animal se protege", "Lo cuida del frío o de otros animales."),
        ],
        "apply": [
            ex("Une cada animal con su hábitat: lobo de mar, guanaco, rana. Hábitats: costa, cordillera, laguna.", "Lobo de mar costa, guanaco cordillera, rana laguna", "Cada uno vive donde encuentra lo que necesita."),
            arith("En una roca de la costa hay 4 lobos de mar. Llegan 3 más. ¿Cuántos hay ahora?", "4+3", "Se suman los que llegaron.", " lobos de mar"),
            ex("Un animal tiene aletas y escamas y no puede vivir fuera del agua. ¿Su hábitat es el mar o el desierto?", "El mar", "Su cuerpo está hecho para el agua."),
        ],
        "reason": [
            ex("Si un pez se saca del agua durante un minuto largo, ¿qué le pasa y por qué?", "Le cuesta respirar, porque su cuerpo está hecho para respirar en el agua", "Su hábitat es el agua."),
            ex("¿Por qué un camello puede vivir en el desierto y una rana de laguna no?", "Porque el camello resiste la falta de agua y la rana necesita agua cerca", "Cada cuerpo se adapta a su hábitat."),
        ],
        "challenge": [
            ex("Escribe un animal y su hábitat con una razón.", "Por ejemplo el pingüino vive en la costa porque come peces", "La razón une el cuerpo con el lugar."),
            ex("En un bosque viven 6 pájaros y 5 ardillas. ¿Cuántos animales hay?", "11", "Seis más cinco son once."),
        ],
    },
    context=[ex("En la costa de Chile ves lobos de mar tomando sol sobre rocas y pingüinos nadando cerca. ¿Cuál es el hábitat de los dos?", "La costa y el mar", "Descansan en las rocas y buscan peces en el mar.")],
    selfcheck=[ex("¿Dónde vive un delfín?", "En el mar", "Es un animal marino."), ex("¿Qué es el hábitat?", "El lugar donde vive un animal", "Ahí encuentra lo que necesita."), ex("¿Qué tipo de hábitat tiene un río?", "De agua", "Es un lugar con agua.")],
    open_task=task("Une cada animal con su hábitat y escribe una razón: cóndor (cordillera), pingüino de Humboldt (costa), trucha (río), zorro culpeo (campo y cerros). Elige uno y dibuja su hábitat con tres elementos.", "Pingüino: costa, porque nada y hace nidos en rocas. Dibujo: mar, rocas y un pingüino.", ["une los cuatro animales", "da una razón", "dibuja el hábitat con tres elementos"], ["lista de parejas", "dibujo"], ["poner un animal marino en el desierto", "no dar razón"], "Reconoce la relación animal y hábitat y pide la razón con un dato de su cuerpo."),
    reinforce="Mira un animal de tu barrio y anota dónde lo ves.",
    extend="Explica qué le pasaría a un guanaco si viviera en la playa tropical.",
)

register(
    OA2, 4,
    materials="Este cuaderno con la tabla de ocho animales (tamaño, cubierta, desplazamiento y hábitat), lápiz y colores.",
    use="Aprenderé a agrupar animales con un criterio y a explicar por qué. Sirve para ordenar lo que observo en la naturaleza.",
    prior=["Sé la ficha de naturalista.", "Sé cómo se desplazan los animales y cuál es su hábitat."],
    explain=[
        "Clasificar animales es formar grupos con una regla. Una regla puede ser la cubierta del cuerpo: pelo, plumas, escamas. Otra regla puede ser cómo se mueven: vuelan, nadan, caminan. Otra, dónde viven.",
        "Cuando elijas una regla, todos los animales de un grupo deben cumplirla. Si la regla es «tiene plumas», el grupo tiene la gallina y el cóndor. Si la regla cambia a «nada», el grupo tiene el pez y el pingüino.",
        "Un buen grupo se explica con una frase: «Este grupo tiene escamas». Otra persona debe poder decir en qué grupo va un animal nuevo. Si alguien no puede, la regla es poco clara.",
    ],
    vocab=[("criterio", "regla que sirve para formar grupos"), ("grupo", "animales que cumplen la misma regla"), ("semejanza", "algo que se parece"), ("diferencia", "algo que no se parece"), ("clasificación", "grupos formados con una regla")],
    worked=[
        {"title": "Agrupar por cubierta", "problem": "Gallina (plumas), perro (pelo), trucha (escamas), cóndor (plumas), gato (pelo). Agrupa por cubierta.", "steps": ["Plumas: gallina y cóndor.", "Pelo: perro y gato.", "Escamas: trucha."], "answer": "Plumas: gallina y cóndor. Pelo: perro y gato. Escamas: trucha"},
        {"title": "Cambiar el criterio", "problem": "Con los mismos animales, agrupa por si vuelan o no: gallina (no vuela casi), cóndor (vuela), trucha (no), perro (no), gato (no).", "steps": ["Vuela: cóndor.", "No vuela: los otros cuatro."], "answer": "Vuela: cóndor. No vuela: gallina, trucha, perro y gato"},
    ],
    mistakes=[
        {"wrong": "Mezclar dos reglas en un mismo grupo: «tiene pelo y vive en el agua».", "why": "Se usa más de una regla a la vez.", "fix": "Usa una sola regla por vez y escribe una frase que la diga."},
        {"wrong": "Dejar un animal sin grupo.", "why": "No se revisa que la regla incluya a todos.", "fix": "Revisa cada animal de la lista y pregúntate si cumple la regla."},
    ],
    tiers={
        "recovery": [
            ex("Regla: tiene plumas. ¿El gato entra en el grupo?", "No", "El gato tiene pelo."),
            ex("Regla: nada con aletas. ¿La trucha entra?", "Sí", "La trucha nada con aletas."),
            ex("Regla: tiene pelo. ¿El perro entra?", "Sí", "El perro tiene pelo."),
        ],
        "understand": [
            ex("En Ciencias: ¿Qué es un criterio?", "Una regla para formar grupos", "Dice qué cumple cada grupo."),
            ex("¿Cuántas reglas usamos a la vez en un grupo?", "Una", "Una sola regla hace el grupo claro."),
            ex("¿Cómo se explica un grupo?", "Con una frase que diga la regla", "Así otra persona entiende."),
        ],
        "apply": [
            ex("Animales: loro (plumas), delfín (piel lisa), conejo (pelo), cóndor (plumas). Agrupa por cubierta y escribe el grupo de plumas.", "Loro y cóndor", "Los dos tienen plumas."),
            ex("Animales: pez, delfín, tortuga marina, lobo de mar. Regla: vive en el mar. ¿Cuántos entran?", "4", "Todos viven en el mar."),
            ex("Animales: caballo, caracol, pato, pez. Regla: no tiene patas. ¿Cuáles entran?", "El pez y el caracol", "Ninguno de los dos tiene patas."),
        ],
        "reason": [
            ex("Marta formó un grupo con perro, gato y gallina y dijo «tienen pelo». ¿Qué animal no cumple?", "La gallina", "La gallina tiene plumas."),
            ex("Con perro, gallina y trucha, ¿qué criterio permite tres grupos de un animal cada uno?", "La cubierta del cuerpo", "Pelo, plumas y escamas son tres cubiertas distintas."),
        ],
        "challenge": [
            ex("Inventa una regla para separar a estos cuatro animales en dos grupos: perro, gato, loro, canario.", "Pelo o plumas", "Perro y gato tienen pelo; loro y canario tienen plumas."),
            ex("Hay 3 animales con pelo y 4 con plumas. ¿Cuántos animales son?", "7", "Tres más cuatro son siete."),
        ],
    },
    context=[ex("En una granja hay vaca, oveja, gallina, pato y conejo. Si agrupas por plumas, ¿cuántos animales entran?", "2", "La gallina y el pato tienen plumas.")],
    selfcheck=[ex("¿Qué se necesita para formar un grupo?", "Una regla", "Un criterio define el grupo."), ex("¿Cuántos grupos salen si separas por pelo o plumas con perro, gato y loro?", "2", "Pelo: perro y gato; plumas: loro."), ex("¿Una regla puede cambiar?", "Sí", "Con otra regla salen otros grupos.")],
    open_task=task("Agrupa estos seis animales de dos maneras distintas: caballo (pelo, camina), loro (plumas, vuela), trucha (escamas, nada), conejo (pelo, salta), gaviota (plumas, vuela), pez dorado (escamas, nada). Escribe la regla de cada clasificación.", "Por cubierta: pelo (caballo, conejo), plumas (loro, gaviota), escamas (trucha, pez dorado). Por movimiento: vuela (loro, gaviota), nada (trucha, pez dorado), camina o salta (caballo, conejo).", ["forma dos clasificaciones", "escribe la regla de cada una", "ningún animal queda sin grupo"], ["dos tablas", "frases con la regla"], ["usar dos reglas en un grupo", "olvidar un animal"], "Reconoce las dos reglas y pide revisar que cada animal tenga grupo."),
    reinforce="Agrupa cuatro animales de tu casa o tu barrio por una regla.",
    extend="Explica por qué dos personas pueden clasificar bien los mismos animales de maneras distintas.",
)
