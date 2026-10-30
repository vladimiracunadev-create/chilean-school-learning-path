"""Cuaderno del estudiante, 3.º básico Historia, Geografía y Ciencias Sociales: OA 10 (influencia geográfica en Grecia y Roma) y OA 11 (deberes y responsabilidades)."""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import ex, register

OA10, OA11 = "HI03 OA 10", "HI03 OA 11"


def W(title, problem, steps, answer):
    return {"title": title, "problem": problem, "steps": steps, "answer": answer}


def M(wrong, why, fix):
    return {"wrong": wrong, "why": why, "fix": fix}


def tiers(recovery, understand, apply, reason, challenge):
    return {"recovery": recovery, "understand": understand, "apply": apply, "reason": reason, "challenge": challenge}


# ================================================================ OA 10
register(
    OA10, 1,
    materials="Este cuaderno y un lápiz. La ficha del «mapa en palabras» está escrita en los ejercicios.",
    use="Aprenderé a leer un mapa para descubrir cuatro factores geográficos: ubicación, relieve, clima y recursos. Sirve para hacer buenas preguntas sobre Grecia y Roma.",
    prior=["Sé que Grecia y Roma fueron civilizaciones antiguas.", "Sé que un mapa muestra dónde están los lugares."],
    explain=[
        "Un factor geográfico es algo del lugar donde viven las personas que influye en su vida. La ubicación dice dónde está un lugar. El relieve son las formas de la tierra: montañas, valles, llanuras e islas. El clima es el calor, el frío y la lluvia que hay en un lugar durante el año. Los recursos naturales son lo que da la naturaleza: agua, tierra para cultivar, piedra, metales, madera.",
        "Un mapa no cuenta toda la historia, pero da pistas. Si el mapa muestra muchas montañas, podemos preguntar: ¿cómo se movían las personas entre ellas? Si muestra islas y mar, podemos preguntar: ¿viajaban en barco? Una buena pregunta histórica empieza con «¿Cómo...?» o «¿Por qué...?» y usa un dato del mapa.",
        "Grecia está en el sur de Europa, en una península con muchas montañas y muchas islas. Italia es otra península, con forma de bota, y Roma está en su parte central, junto a un río. Los dos lugares tienen costa en el mar Mediterráneo. En Grecia los veranos son secos y calurosos, y las lluvias llegan sobre todo en invierno. Estas pistas ayudan a imaginar cómo vivían, pero no lo explican todo.",
    ],
    vocab=[("factor geográfico", "algo del lugar que influye en la vida de las personas"), ("ubicación", "dónde está un lugar"), ("relieve", "formas de la tierra, como montañas y valles"), ("clima", "calor, frío y lluvia de un lugar durante el año"), ("recurso natural", "algo que da la naturaleza y las personas usan")],
    worked=[
        W("De un dato a una pregunta", "El mapa muestra que Grecia tiene muchas islas. ¿Qué pregunta histórica puedes hacer?",
          ["Leo el dato: muchas islas.", "Pienso qué necesitan las personas para ir de una isla a otra.", "Escribo una pregunta con «¿Cómo...?»: ¿Cómo viajaban los griegos entre las islas?"], "¿Cómo viajaban los griegos entre las islas?"),
        W("Clasificar un dato", "Una ficha dice: «Roma está junto al río Tíber». ¿Es ubicación, relieve, clima o recurso?",
          ["La frase dice dónde está Roma.", "Decir dónde está un lugar es ubicación.", "El río también podría servir como recurso, pero la frase solo señala el lugar."], "Ubicación"),
    ],
    mistakes=[
        M("Creer que el mapa ya explica lo que pasó.", "Un dato del mapa es una pista, no la respuesta completa.", "Usa el dato para hacer una pregunta y busca más información."),
        M("Mezclar relieve y clima, por ejemplo llamar «clima» a una montaña.", "Se confunden las formas de la tierra con el tiempo atmosférico.", "Las montañas son relieve; el calor y la lluvia son clima."),
    ],
    tiers=tiers(
        [ex("«Grecia tiene muchas montañas.» ¿Es un dato de relieve o de clima?", "De relieve", "Las montañas son una forma de la tierra."),
         ex("«Los veranos son secos y calurosos.» ¿Es un dato de clima o de recursos?", "De clima", "Habla del calor y la lluvia durante el año."),
         ex("«Cerca hay mármol, una piedra para construir.» ¿Es un recurso natural o una ubicación?", "Un recurso natural", "El mármol lo da la naturaleza y las personas lo usan.")],
        [ex("Con tus palabras, ¿qué es un recurso natural? Da un ejemplo.", "Algo que da la naturaleza y se usa, como agua, piedra o madera", "Un recurso viene de la naturaleza y sirve a las personas."),
         ex("¿Con cuál de estas palabras empieza una buena pregunta histórica: «¿Por qué...?» o «Sí o no»?", "«¿Por qué...?»", "Una pregunta histórica busca explicar, no solo decir sí o no."),
         ex("Un mapa muestra a Roma junto a un río. ¿Es esa información suficiente para saber toda la historia de Roma? Responde sí o no y explica.", "No; es solo una pista", "El mapa da un dato, y la historia necesita más información.")],
        [ex("Mapa en palabras: «Grecia es una península con muchas islas alrededor». Escribe la letra de la mejor pregunta: A) ¿Cuántos años tiene un olivo? B) ¿Cómo se comunicaban las personas de las islas?", "B", "Usa el dato de las islas; la A no se relaciona con el mapa."),
         ex("Mapa en palabras: «En Grecia hay pocas llanuras y muchas montañas». ¿Qué factor geográfico es: ubicación, relieve o clima?", "Relieve", "Llanuras y montañas son formas de la tierra."),
         ex("Une cada dato con su factor: 1) Está en el sur de Europa. 2) Llueve más en invierno. 3) Hay un valle largo. Factores: relieve, clima, ubicación.", "1 ubicación, 2 clima, 3 relieve", "Dónde está es ubicación; la lluvia es clima; el valle es una forma de la tierra.")],
        [ex("Tomás dice: «Como el mapa muestra montañas, ya sé todo sobre los griegos». ¿Qué le respondes?", "Que el mapa solo da una pista y falta más información", "Un solo dato no alcanza para explicar a una civilización."),
         ex("Ana confundió: «El clima de Grecia es muy montañoso». ¿Qué palabra corrige, clima o relieve?", "Relieve", "Montañoso habla de la forma de la tierra, no del tiempo atmosférico.")],
        [ex("Ficha: «Roma está en la parte central de la península de Italia, cerca del mar, junto a un río, con colinas alrededor». ¿Qué dato de la ficha es de relieve?", "Las colinas", "Las colinas son una forma de la tierra; el mar y el río dicen dónde está Roma."),
         ex("Ordena los pasos: A) hacer una pregunta, B) leer un dato del mapa, C) buscar más información.", "B, A, C", "Primero se observa, luego se pregunta y después se busca información.")],
    ),
    context=[ex("Sofía mira un mapa con las islas del mar Egeo y escribe: «¿Cómo hacían los griegos para llegar a otras islas?». ¿Su pregunta nace de un dato del mapa? Explica.", "Sí; nace del dato de que hay muchas islas", "Usa las islas, que son un dato del mapa.")],
    selfcheck=[ex("Nombra los cuatro factores geográficos de esta clase.", "Ubicación, relieve, clima y recursos naturales", "Son los cuatro que se explicaron."), ex("¿Una montaña es relieve o clima?", "Relieve", "Es una forma de la tierra."), ex("¿Un dato del mapa es una pista o la respuesta completa?", "Una pista", "Falta más información para explicar la historia.")],
    open_task=task("Mira esta ficha: «Grecia: península con montañas e islas, veranos secos, mar a su alrededor». Escribe dos preguntas históricas que empiecen con «¿Cómo...?» o «¿Por qué...?», cada una usando un dato distinto de la ficha.", "¿Cómo viajaban los griegos entre las islas? ¿Por qué las montañas podían separar a las personas?", ["cada pregunta usa un dato de la ficha", "empieza con «¿Cómo...?» o «¿Por qué...?»", "las dos preguntas son distintas"], ["dos preguntas escritas", "dato señalado en cada una"], ["escribir una pregunta que se responde con sí o no", "no usar ningún dato de la ficha"], "Pide a una persona que lea tus preguntas y te diga qué dato de la ficha reconoce en cada una."),
    reinforce="Mira un mapa de tu región y nombra un dato de relieve y uno de ubicación.",
    extend="Escribe una pregunta histórica sobre Roma que parta del dato «Roma está junto a un río».",
)

register(
    OA10, 2,
    materials="Este cuaderno y un lápiz. Las listas de productos están escritas en los ejercicios.",
    use="Aprenderé por qué el mar Egeo y sus islas fueron importantes para Grecia. Sirve para entender cómo viajaban y comerciaban los griegos.",
    prior=["Conozco los cuatro factores geográficos: ubicación, relieve, clima y recursos.", "Sé que Grecia tiene montañas e islas."],
    explain=[
        "El mar Egeo está al este de Grecia. Tiene muchas islas, y en esa época los barcos eran pequeños y navegaban cerca de la costa. Entre una isla y otra se podía ver tierra, así que viajar era más seguro. Por eso el mar unía los lugares en vez de separarlos, aunque las montañas dificultaban ir por tierra.",
        "Los griegos usaron el mar para el intercambio. Intercambiar es dar lo que sobra y recibir lo que falta. Producían aceite de oliva, vino y cerámica, y los guardaban en vasijas llamadas ánforas. A cambio traían productos como trigo y metales, que en su tierra eran escasos. Atenas tenía un puerto, el Pireo, que recibía muchos barcos.",
        "Navegar también permitió que algunos griegos fundaran ciudades nuevas en otras costas del Mediterráneo. Así llevaron sus ideas y costumbres. Pero el mar traía riesgos, como las tormentas. Los marinos conocían las estaciones y las costas para viajar con más cuidado, y si venía una tormenta buscaban un puerto donde refugiarse.",
    ],
    vocab=[("mar Egeo", "mar al este de Grecia, con muchas islas"), ("isla", "tierra rodeada de agua por todos lados"), ("navegación", "viajar en barco por el agua"), ("intercambio", "dar lo que sobra y recibir lo que falta"), ("ánfora", "vasija grande para guardar aceite o vino")],
    worked=[
        W("Qué ayuda el mar", "Una isla griega tiene poca tierra plana para cultivar trigo, pero tiene un buen puerto. ¿Cómo puede conseguir trigo?",
          ["Veo lo que falta: trigo.", "Veo lo que tiene: puerto y barcos.", "Puede navegar e intercambiar productos por trigo."], "Navegando e intercambiando sus productos por trigo"),
        W("Qué sobra y qué falta", "Un pueblo griego tiene mucho aceite de oliva y le falta metal. ¿Qué puede ofrecer y qué puede recibir?",
          ["Lo que sobra es el aceite.", "Lo que falta es el metal.", "Ofrece aceite y recibe metal."], "Ofrece aceite de oliva y recibe metal"),
    ],
    mistakes=[
        M("Pensar que el mar solo separaba a los griegos.", "Se olvida que las islas permitían viajar viendo tierra.", "El mar Egeo comunicaba islas y costas."),
        M("Creer que intercambiar es regalar.", "No se considera que cada parte da algo y recibe algo.", "En un intercambio las dos partes dan y reciben."),
    ],
    tiers=tiers(
        [ex("¿El mar Egeo está al este o al oeste de Grecia?", "Al este", "El texto de la clase lo ubica al este de Grecia."),
         ex("¿Una isla está rodeada de agua o de montañas?", "De agua", "Una isla es tierra rodeada de agua."),
         ex("¿En una ánfora se guardaba aceite o se cocinaba pan?", "Se guardaba aceite", "La ánfora era una vasija para aceite o vino.")],
        [ex("¿Por qué viajar entre islas era más seguro que cruzar mar abierto con barcos pequeños?", "Porque se veía tierra de una isla a otra", "Ver tierra ayudaba a orientarse."),
         ex("¿Qué es un intercambio? Responde con tus palabras.", "Dar lo que sobra y recibir lo que falta", "Las dos partes dan y reciben."),
         ex("Nombra un producto que los griegos vendían y uno que traían.", "Vendían aceite, vino o cerámica; traían trigo o metales", "El texto da esas listas.")],
        [ex("Lista de una isla: sobra vino y cerámica; falta trigo. ¿Qué ofrece y qué recibe?", "Ofrece vino y cerámica; recibe trigo", "Se ofrece lo que sobra y se recibe lo que falta."),
         ex("Un puerto recibe barcos con trigo y envía barcos con aceite en ánforas. ¿Es un intercambio? Responde sí o no y explica.", "Sí; sale aceite y entra trigo", "Hay algo que se da y algo que se recibe."),
         ex("Dos ciudades griegas están separadas por montañas muy altas, pero las dos tienen costa en el Egeo. ¿Qué camino puede comunicarlas mejor: el mar o las montañas?", "El mar", "Los barcos evitan cruzar montañas altas.")],
        [ex("Lola dice: «El mar Egeo era un problema, porque separaba las islas». ¿Qué parte falta en su idea?", "También las unía, porque permitía viajar en barco", "El mar separaba pero también comunicaba."),
         ex("Pedro dijo: «Los griegos regalaban su aceite». Según la clase, ¿qué hacían?", "Lo intercambiaban por productos que les faltaban", "Recibían algo a cambio.")],
        [ex("Una ciudad griega tiene un buen puerto, poco trigo y muchas ánforas de aceite. Escribe una decisión que podría tomar y por qué.", "Navegar e intercambiar aceite por trigo, porque tiene puerto y le falta trigo", "La decisión usa el puerto y lo que sobra y falta."),
         ex("Una tormenta fuerte se acerca. Un marino conoce la costa y sus puertos. ¿Qué es más prudente: refugiarse en un puerto cercano o salir a mar abierto?", "Refugiarse en un puerto cercano", "El puerto protege de la tormenta; el mar abierto es más riesgoso.")],
    ),
    context=[ex("Un mercader de una isla carga ánforas de vino. Su isla tiene poco trigo. Quiere llevar el vino a un puerto grande. ¿Qué conseguirá si el viaje sale bien y por qué le sirve el mar?", "Trigo; el mar permite llevar el vino al puerto", "Navega e intercambia lo que sobra por lo que falta.")],
    selfcheck=[ex("¿Qué mar está al este de Grecia?", "El mar Egeo", "Es el mar con muchas islas."), ex("¿Qué significa navegar?", "Viajar en barco", "Es moverse por el agua en una embarcación."), ex("Completa: en un intercambio doy lo que ____ y recibo lo que ____.", "Sobra; falta", "Así se define el intercambio.")],
    open_task=task("Imagina que eres un mercader griego. Elige una isla de esta lista: A) tiene mucho aceite y le falta trigo, B) tiene mucha cerámica y le faltan metales. Escribe un mensaje de tres líneas: qué lleva tu barco, a quién se lo ofrecerás y qué traerás de vuelta.", "Elegí la isla A. Llevo ánforas de aceite, se las ofrezco a una ciudad con trigo y traeré trigo de vuelta.", ["elige la isla A o la B", "nombra qué lleva y qué trae", "usa la idea de intercambio"], ["mensaje de tres líneas", "producto que sobra y producto que falta"], ["decir que se regala el producto", "traer lo mismo que se lleva"], "Pide a una persona que lea tu mensaje y diga qué sobraba y qué faltaba."),
    reinforce="Haz una lista de dos cosas que sobran en tu casa y dos que faltan, e inventa un intercambio.",
    extend="Explica con una frase por qué una ciudad con puerto pudo tener más contacto con otras que una ciudad rodeada de montañas.",
)

register(
    OA10, 3,
    materials="Este cuaderno y un lápiz. La ficha de Roma y las listas están escritas en los ejercicios.",
    use="Aprenderé por qué el mar Mediterráneo y el río Tíber fueron importantes para Roma. Sirve para entender cómo Roma se conectó con otros lugares.",
    prior=["Conozco los cuatro factores geográficos.", "Sé qué es un intercambio."],
    explain=[
        "Roma nació junto al río Tíber, en la parte central de la península de Italia, y cerca del mar. El río permitía llevar productos en barcos pequeños. En la desembocadura del río estaba Ostia, el puerto que conectaba a Roma con el mar. Alrededor de Roma había colinas, que servían para vigilar y defenderse.",
        "El mar Mediterráneo está rodeado por tres continentes: Europa, Asia y África. Por eso es un mar de caminos para llegar a muchos pueblos. Cuando Roma creció, los romanos viajaron por él, y lo llamaron «Mare Nostrum», que en latín significa «nuestro mar».",
        "Italia tiene llanuras donde se cultivan trigo, olivos y vides, y su clima mediterráneo es de veranos secos e inviernos suaves. Aun así, la ciudad crecía y necesitaba más alimentos. Traía trigo por mar desde otros lugares, como Egipto. Así el Mediterráneo ayudó a alimentar a Roma.",
    ],
    vocab=[("río Tíber", "río junto al cual nació Roma"), ("puerto", "lugar donde llegan y salen los barcos"), ("Mediterráneo", "mar rodeado por Europa, Asia y África"), ("Mare Nostrum", "«nuestro mar», nombre latino que Roma dio al Mediterráneo"), ("colina", "cerro bajo y redondeado")],
    worked=[
        W("Para qué sirve un río", "Roma está junto al río Tíber. ¿Qué ventaja da vivir cerca de un río?",
          ["Pienso en lo que un río permite.", "Da agua y permite navegar con barcos pequeños.", "Eso facilita llevar productos a la ciudad."], "Da agua y permite llevar productos en barcos"),
        W("Un mar con muchos caminos", "El Mediterráneo toca Europa, Asia y África. ¿Por qué eso ayudó a Roma?",
          ["Cuento los continentes: tres.", "Desde el mar se puede llegar a costas de los tres.", "Roma pudo comerciar con muchos pueblos."], "Porque desde el mar podía llegar a pueblos de tres continentes"),
    ],
    mistakes=[
        M("Decir que Roma estaba en la costa, justo en la orilla del mar.", "Se confunde la ciudad con su puerto.", "Roma está junto al río y cerca del mar; el puerto era Ostia."),
        M("Creer que Roma tenía todo lo que necesitaba en su propia tierra.", "Se olvida que traía alimentos por mar.", "Roma también traía trigo desde otros lugares."),
    ],
    tiers=tiers(
        [ex("¿Roma nació junto al río Tíber o junto al río Sena?", "Junto al río Tíber", "La clase indica que el Tíber está junto a Roma."),
         ex("¿Qué significa «Mare Nostrum»: «nuestro mar» o «gran montaña»?", "«Nuestro mar»", "Así llamaron los romanos al Mediterráneo."),
         ex("¿Ostia era un puerto o una colina?", "Un puerto", "Estaba en la desembocadura del río.")],
        [ex("Nombra los tres continentes que rodean el Mediterráneo.", "Europa, Asia y África", "Son los tres continentes de la clase."),
         ex("Menciona una ventaja de que Roma tuviera colinas alrededor.", "Servían para vigilar y defenderse", "Desde lo alto se ve a quien se acerca."),
         ex("¿Por qué Roma traía trigo por mar?", "Porque la ciudad crecía y necesitaba más alimentos", "Con más gente hacía falta más comida.")],
        [ex("Un barco pequeño sube por el Tíber hasta Roma. ¿Qué factor geográfico aprovecha: el río, el clima o el desierto?", "El río", "Es el Tíber el que permite navegar."),
         ex("Ficha: «En Italia hay llanuras donde se cultivan trigo y olivos». ¿Qué dato de la ficha es de relieve: llanuras o trigo?", "Llanuras", "Las llanuras son una forma de la tierra; el trigo es un cultivo."),
         ex("Un barco sale de Ostia hacia Egipto, en África, con aceite y vuelve con trigo. ¿Qué mar recorrió?", "El Mediterráneo", "Une Italia con África.")],
        [ex("Rosa dice: «Roma es una ciudad de playa». ¿Qué parte de la clase la corrige?", "Roma está junto a un río y cerca del mar, no en la playa", "El puerto estaba en Ostia."),
         ex("Dani afirma: «Roma solo comía lo que cultivaba cerca». Según la clase, ¿es correcto? Explica.", "No; también traía trigo por mar", "Se menciona el trigo traído desde otros lugares.")],
        [ex("Roma tenía un río para llevar productos y colinas para vigilar. Escribe una ventaja de cada uno.", "Río: llevar productos en barcos; colinas: vigilar y defenderse", "Cada elemento geográfico cumplía una función distinta."),
         ex("Ordena el viaje del trigo desde Egipto: A) barcos pequeños suben por el Tíber, B) cruza el Mediterráneo, C) llega al puerto de Ostia.", "B, C, A", "Primero el mar, luego el puerto y al final el río hasta Roma.")],
    ),
    context=[ex("Un mercader romano espera en Ostia un barco con trigo de Egipto. Cuando llega, se traslada el trigo en barcos pequeños por el Tíber hasta Roma. ¿Qué dos aguas usó para llegar el trigo a la ciudad?", "El mar Mediterráneo y el río Tíber", "Primero el mar, luego el río hasta la ciudad.")],
    selfcheck=[ex("¿Cómo se llama el puerto en la desembocadura del Tíber?", "Ostia", "Conectaba a Roma con el mar."), ex("¿Qué continentes rodean el Mediterráneo?", "Europa, Asia y África", "Así lo explica la clase."), ex("¿Para qué servían las colinas de Roma?", "Para vigilar y defenderse", "Desde lo alto se ve más lejos.")],
    open_task=task("Dibuja un mapa simple de Roma con estos elementos: el río Tíber, el puerto de Ostia en el mar y una colina. Escribe una frase que explique cómo llegaba el trigo desde el mar hasta Roma.", "Dibujé el río Tíber saliendo al mar con Ostia en su desembocadura. El trigo llegaba en barcos por el mar y subía por el Tíber hasta Roma.", ["incluye río, puerto y colina", "ubica Ostia en la desembocadura", "la frase explica el camino del trigo"], ["dibujo con tres elementos", "frase sobre el camino del trigo"], ["poner Roma en la orilla del mar", "olvidar el río"], "Compara tu dibujo con la ficha de la clase y revisa que Ostia esté donde el río llega al mar."),
    reinforce="Nombra un río o un lago de tu región y di para qué lo usa la gente.",
    extend="Escribe una frase que explique por qué un mar rodeado por varios continentes ayudó a comerciar.",
)

register(
    OA10, 4,
    materials="Este cuaderno y un lápiz. Los casos de Grecia y Roma están escritos en los ejercicios.",
    use="Aprenderé a relacionar los recursos naturales con las decisiones de las personas y a reconocer que la geografía también tiene límites. Sirve para no sacar conclusiones demasiado simples.",
    prior=["Sé qué factores geográficos influyeron en Grecia y en Roma.", "Sé qué es un intercambio."],
    explain=[
        "En Grecia hay mucho terreno de montaña y poca tierra plana para sembrar. En laderas y valles pequeños crecían bien los olivos y las vides, y se sembraba algo de trigo y cebada. Los griegos tenían también arcilla para hacer cerámica, mármol para construir y plata para fabricar monedas. El clima de veranos secos también ayudaba a los olivos y las vides. Con esos recursos, el clima y el mar, tomaron decisiones: comerciar y fundar ciudades en otras costas.",
        "En Italia había llanuras más amplias para cultivar. Roma usó esa tierra y además traía alimentos por mar. Un recurso no decide por sí solo. Las personas deciden cómo usarlo: pueden cultivar, comerciar, construir barcos o defenderse.",
        "La geografía influye, pero no lo determina todo. Atenas y Esparta, dos ciudades griegas, estaban en la misma región de montañas y costas. Atenas construyó una gran flota de barcos. Esparta se apoyó más en su ejército de tierra. El lugar fue parecido, pero las decisiones fueron distintas.",
    ],
    vocab=[("recurso", "algo que da la naturaleza y se puede usar"), ("decisión", "elección que hacen las personas"), ("influir", "ayudar a que algo pase, sin obligarlo"), ("límite", "lo que impide que una explicación sea completa"), ("flota", "conjunto de barcos")],
    worked=[
        W("Del recurso a la decisión", "En una ciudad griega abundan los olivos. Hay pocos campos de trigo. ¿Qué decisión puede tomar?",
          ["El recurso es el olivo.", "Falta trigo.", "Puede fabricar aceite e intercambiarlo por trigo."], "Hacer aceite y cambiarlo por trigo"),
        W("Mismo lugar, distintas decisiones", "Atenas y Esparta estaban en Grecia. Atenas hizo una gran flota; Esparta se apoyó en su ejército de tierra. ¿Qué enseña eso?",
          ["El lugar era parecido.", "Las decisiones fueron distintas.", "Entonces la geografía no decide todo."], "Que las personas también deciden; la geografía no lo determina todo"),
    ],
    mistakes=[
        M("Pensar que la geografía obliga a todos a hacer lo mismo.", "Se ignoran las decisiones de las personas.", "La geografía influye, pero las personas eligen."),
        M("Creer que tener un recurso basta para que una ciudad progrese.", "No se piensa en cómo se usa.", "Hay que decidir cómo cultivar, fabricar o comerciar."),
    ],
    tiers=tiers(
        [ex("El mármol, ¿es un recurso natural o una decisión?", "Un recurso natural", "Lo da la naturaleza."),
         ex("«Fundar una ciudad en otra costa», ¿es un recurso o una decisión?", "Una decisión", "La toman las personas."),
         ex("Una flota, ¿es un conjunto de barcos o de montañas?", "Un conjunto de barcos", "Así se definió en el vocabulario.")],
        [ex("Nombra dos recursos naturales de Grecia que menciona la clase.", "Arcilla, mármol, plata, olivos o vides", "Son recursos del texto."),
         ex("¿Qué significa que la geografía «influye» pero no «determina»?", "Ayuda a que algo pase, pero las personas también deciden", "No obliga a todos."),
         ex("¿En qué se parecen Atenas y Esparta, según la clase?", "Estaban en Grecia, con un relieve parecido", "Compartían la misma región de montañas y costas.")],
        [ex("Una ciudad tiene arcilla y mucha leña pero poca tierra. Escribe un producto que podría fabricar con la arcilla.", "Cerámica o vasijas", "La arcilla sirve para hacer cerámica."),
         ex("Una ciudad tiene llanuras fértiles. ¿Qué decisión usa mejor ese recurso: cultivar trigo o cerrar los campos?", "Cultivar trigo", "Usa la tierra fértil para alimentarse."),
         ex("Atenas hizo una gran flota. ¿Qué dos factores geográficos ayudaron a esa decisión?", "El mar y las costas con puertos", "Una flota se usa en el mar.")],
        [ex("Mía dice: «Como Grecia tenía montañas, todos los griegos hicieron lo mismo». ¿Qué ejemplo de la clase muestra que eso es falso?", "Atenas y Esparta tomaron decisiones distintas", "En el mismo país hubo caminos distintos."),
         ex("Un niño dijo: «Roma creció solo porque tenía un río». ¿Qué otras cosas intervinieron según la clase?", "Las llanuras para cultivar, el mar y las decisiones de las personas", "Hubo muchos factores, no solo el río.")],
        [ex("Escribe una frase que una un recurso de Grecia con una decisión de los griegos.", "Por ejemplo: como tenían olivos, hicieron aceite y lo intercambiaron", "Une recurso con decisión."),
         ex("Dos ciudades tienen el mismo mar y la misma tierra. Una construye barcos y otra se concentra en el ejército de tierra. ¿Se debe a la geografía o a decisiones de las personas?", "A decisiones de las personas", "El lugar es el mismo, así que cambia lo que decidieron.")],
    ),
    context=[ex("Un grupo de estudiantes lee: «Una ciudad de montaña tiene plata en sus cerros». Proponen usarla para hacer monedas y comprar trigo. ¿Qué recurso aprovechan y qué decisión toman?", "Aprovechan la plata; deciden hacer monedas y comprar trigo", "El recurso es la plata y la decisión es cómo usarla.")],
    selfcheck=[ex("¿Qué es una decisión?", "Una elección que hacen las personas", "Las personas deciden cómo usar los recursos."), ex("¿Influir es lo mismo que obligar?", "No", "Influir ayuda, pero no obliga."), ex("¿Qué ciudades griegas muestran decisiones distintas en un mismo lugar?", "Atenas y Esparta", "Una apostó por la flota y otra por el ejército de tierra.")],
    open_task=task("Elige una de estas ciudades inventadas: A) tiene puerto y poca tierra de cultivo; B) tiene llanuras fértiles y río. Escribe dos oraciones: una con un recurso o factor y otra con una decisión que podrían tomar.", "Elegí A. Tiene puerto. Puede decidir intercambiar productos por alimentos.", ["elige A o B", "nombra un factor o recurso", "nombra una decisión que lo use"], ["dos oraciones", "factor y decisión diferenciados"], ["decir que la ciudad está obligada a hacer una sola cosa", "no separar recurso y decisión"], "Subraya el recurso con un color y la decisión con otro para comprobar que los separaste."),
    reinforce="Piensa en un recurso de tu comuna y escribe qué decisión de la gente lo usa.",
    extend="Escribe por qué sería un error decir que una civilización se desarrolló solo por su geografía.",
)

register(
    OA10, 5,
    materials="Este cuaderno y un lápiz. Los textos para analizar están escritos en los ejercicios.",
    use="Aprenderé a explicar cómo influyó un factor geográfico sin decir que todo se debe a él. Sirve para escribir explicaciones claras y justas.",
    prior=["Sé qué factores geográficos influyeron en Grecia y Roma.", "Sé que las personas toman decisiones."],
    explain=[
        "Una buena explicación tiene cuatro partes. Primero, el factor geográfico, como el mar o el río. Segundo, cómo influyó: qué permitió o qué dificultó. Tercero, la decisión de las personas. Cuarto, un límite: algo que el factor no explica.",
        "Hay palabras que ayudan: «influyó», «facilitó», «permitió», «dificultó», «también» y «pero». Hay palabras que suenan demasiado seguras: «siempre», «todos», «obligó», «solo por». Con ellas la explicación se vuelve injusta, porque deja fuera las decisiones y otros factores.",
        "Un ejemplo: «El mar Egeo y sus islas facilitaron los viajes en barco. Por eso muchos griegos comerciaron. Pero no todas las ciudades eligieron lo mismo». Tiene factor, influencia, decisión y límite.",
    ],
    vocab=[("explicación", "texto que cuenta cómo o por qué pasó algo"), ("facilitar", "hacer más fácil"), ("dificultar", "hacer más difícil"), ("determinar", "decidir por completo, sin otra opción"), ("evidencia", "dato o ejemplo que apoya lo que digo")],
    worked=[
        W("Armar una explicación", "Factor: el río Tíber. Escribe una explicación con factor, influencia, decisión y límite.",
          ["Factor: el río Tíber.", "Influencia: permitió llevar productos en barcos.", "Decisión: los romanos usaron el río y el puerto de Ostia.", "Límite: el río no explica por sí solo el crecimiento de Roma."], "El río Tíber facilitó llevar productos en barcos. Los romanos usaron el río y el puerto, pero el río no explica por sí solo su crecimiento."),
        W("Detectar una frase demasiado segura", "«Las montañas obligaron a todos los griegos a ser pastores.» ¿Qué palabras están mal y por qué?",
          ["Busco palabras de seguridad total.", "«Obligaron» y «todos» no dejan lugar a decisiones.", "La clase mostró que hubo ciudades y decisiones distintas."], "«Obligaron» y «todos»; la geografía influye pero no decide todo"),
    ],
    mistakes=[
        M("Escribir «El mar hizo que los griegos fueran comerciantes» sin más.", "Se olvida que influyen decisiones y otros factores.", "Escribe «El mar facilitó el comercio y los griegos lo usaron»."),
        M("Dar solo el factor sin decir cómo influyó.", "La explicación queda incompleta.", "Agrega qué permitió o dificultó el factor."),
    ],
    tiers=tiers(
        [ex("¿«Facilitó» significa hacer más fácil o hacer más difícil?", "Hacer más fácil", "Así se definió en el vocabulario."),
         ex("¿Cuál palabra suena demasiado segura: «siempre» o «también»?", "«Siempre»", "«Siempre» no deja lugar a excepciones."),
         ex("¿El mar Egeo es un factor geográfico o una decisión?", "Un factor geográfico", "Es una parte del lugar.")],
        [ex("Nombra las cuatro partes de una buena explicación.", "Factor, cómo influyó, decisión de las personas y límite", "Son las cuatro partes de la clase."),
         ex("¿Para qué sirve el límite en una explicación?", "Para decir lo que el factor no explica", "Evita dar una idea demasiado simple."),
         ex("¿Cuál es una explicación más justa: A) «El mar obligó a los griegos a viajar» o B) «El mar facilitó los viajes de los griegos»?", "B", "«Obligó» quita el papel de las decisiones.")],
        [ex("Completa: «El Mediterráneo ____ el comercio de Roma, pero también influyeron las decisiones de los romanos». Elige: facilitó o prohibió.", "Facilitó", "El mar permitía llegar a otros pueblos."),
         ex("Texto: «Las llanuras de Italia permitieron cultivar trigo. Por eso los romanos sembraron. Pero también traían trigo de afuera». ¿Cuál es el límite?", "Que también traían trigo de afuera", "Muestra que las llanuras no alcanzaban para alimentar a todos."),
         ex("Marca las dos palabras demasiado seguras: «Todos los griegos viajaron en barco porque el mar los obligó».", "«Todos» y «obligó»", "No dejan lugar a otros casos ni decisiones.")],
        [ex("Ema escribió: «La geografía decidió toda la historia de Roma». ¿Qué le falta a su explicación?", "Las decisiones de las personas y otros factores", "La geografía influye pero no decide sola."),
         ex("Una explicación dice: «Grecia tenía islas». No dice cómo influyeron. ¿Qué parte falta?", "Cómo influyó", "Hay que explicar qué permitieron las islas.")],
        [ex("Escribe una explicación de dos oraciones sobre el mar Egeo que incluya un factor, una influencia, una decisión y un límite.", "Por ejemplo: el mar Egeo facilitó viajar entre islas; los griegos comerciaron, pero no todas las ciudades eligieron lo mismo", "Incluye las cuatro partes."),
         ex("Corrige con una palabra más justa: «Las montañas impidieron para siempre que los griegos se comunicaran».", "Dificultaron la comunicación, pero hubo contacto por mar", "«Impidieron para siempre» es demasiado seguro; el mar los comunicaba.")],
    ),
    context=[ex("Un estudiante quiere explicar por qué Roma tuvo contacto con muchos pueblos. Escribe: «Roma estaba cerca del Mediterráneo, que rodea tres continentes. Los romanos viajaron por él. Pero hubo otros motivos además del mar». ¿Qué parte es el límite?", "«Pero hubo otros motivos además del mar»", "Reconoce que el mar no lo explica todo.")],
    selfcheck=[ex("Escribe dos palabras demasiado seguras que conviene evitar.", "Por ejemplo: siempre, todos, obligó o solo por", "Cierran la explicación a una sola causa."), ex("¿Qué palabra une el factor con la decisión: «influyó» o «nunca»?", "«Influyó»", "Ayuda a explicar sin exagerar."), ex("¿Cuántas partes tiene la explicación de esta clase?", "Cuatro", "Factor, influencia, decisión y límite.")],
    open_task=task("Elige un factor: el mar Egeo, el río Tíber o las montañas de Grecia. Escribe una explicación de tres o cuatro oraciones con: el factor, cómo influyó, una decisión de las personas y un límite. Evita las palabras «siempre», «todos» y «obligó».", "Las montañas de Grecia dificultaron viajar por tierra. Por eso muchas ciudades se comunicaron por mar. Pero no todas las ciudades tomaron las mismas decisiones.", ["tiene las cuatro partes", "no usa palabras demasiado seguras", "usa datos vistos en la unidad"], ["texto de tres o cuatro oraciones", "palabras de las cuatro partes subrayadas"], ["decir que el factor decidió todo", "no incluir un límite"], "Subraya las cuatro partes con colores distintos para comprobar que no falta ninguna."),
    reinforce="Elige una frase de la unidad y cambia «siempre» o «todos» por una expresión más justa.",
    extend="Compara en dos oraciones cómo influyó el mar en Grecia y cómo influyó en Roma.",
)

# ================================================================ OA 11
register(
    OA11, 1,
    materials="Este cuaderno y un lápiz. Los casos están escritos en los ejercicios.",
    use="Aprenderé a distinguir un deber, un favor y un abuso. Sirve para saber qué me corresponde hacer, qué puedo elegir y cuándo debo pedir ayuda.",
    prior=["Sé que en mi casa y en mi escuela hay cosas que me toca hacer.", "Sé que puedo pedir ayuda a una persona adulta de confianza."],
    explain=[
        "Un deber es algo que me corresponde hacer por mi edad y mi rol. Por ejemplo, un deber de estudiante es llevar mis útiles y hacer mis tareas. Una responsabilidad es hacerme cargo de ese deber y de sus resultados. Cumplir un deber ayuda a las demás personas y también a mí.",
        "Un favor es una ayuda extra. Puedo decir que sí o que no, y no pasa nada si no puedo. Si el favor me gusta y puedo hacerlo con seguridad, es bueno ayudar. Un abuso es cuando me piden algo peligroso, injusto o que no corresponde a una niña o a un niño, o me presionan o me amenazan.",
        "Los niños y las niñas no deben hacer tareas riesgosas ni propias de personas adultas, como usar fuego, manejar herramientas filosas o cuidar solos durante mucho tiempo a alguien. Si algo me parece peligroso o injusto, digo «no» y se lo cuento a una persona adulta de confianza. Si me da miedo decir «no», igual se lo cuento.",
    ],
    vocab=[("deber", "algo que me corresponde hacer"), ("responsabilidad", "hacerme cargo de lo que me toca"), ("favor", "ayuda extra que puedo aceptar o no"), ("abuso", "pedir algo peligroso, injusto o que no corresponde"), ("consecuencia", "lo que pasa después de hacer o no hacer algo")],
    worked=[
        W("Deber o favor", "Una profesora dice: «Cada uno guarda sus lápices al terminar». Otro compañero pide: «¿Me ayudas a pegar mi afiche si tienes tiempo?». ¿Cuál es un deber y cuál un favor?",
          ["Guardar mis lápices es parte de mi trabajo.", "Ayudar a pegar el afiche del compañero es una ayuda extra.", "Puedo decir que no a esa ayuda."], "Guardar los lápices es un deber; ayudar con el afiche es un favor"),
        W("Detectar un abuso", "Alguien mayor le dice a Nico: «Sube a ese techo alto y me traes la pelota; si no, no te hablo más». ¿Qué es?",
          ["La tarea es peligrosa.", "Lo presionan con no hablarle más.", "Es un abuso: Nico debe decir que no y avisar a un adulto de confianza."], "Un abuso; debe decir que no y avisar a un adulto de confianza"),
    ],
    mistakes=[
        M("Creer que todo lo que me piden es un deber.", "Se confunde obedecer con cumplir lo que me corresponde.", "Pregúntate si es seguro, justo y propio de mi edad."),
        M("Pensar que decir «no» a un favor es una falta.", "Un favor es una ayuda voluntaria.", "Puedes decir «no puedo ahora» con respeto."),
    ],
    tiers=tiers(
        [ex("Hacer mis tareas escolares, ¿es un deber o un favor?", "Un deber", "Es parte de mi rol de estudiante."),
         ex("Prestar un lápiz extra si me lo piden, ¿es un deber o un favor?", "Un favor", "Es una ayuda que puedo dar o no."),
         ex("Que me pidan usar fuego sin supervisión, ¿es un abuso o un deber?", "Un abuso", "Es una tarea peligrosa que no corresponde a un niño.")],
        [ex("Explica con tus palabras qué es una responsabilidad.", "Hacerme cargo de lo que me corresponde", "Incluye cumplir y aceptar las consecuencias."),
         ex("Menciona una consecuencia de no llevar mis útiles a clases.", "No poder trabajar bien o tener que pedir prestado", "Cada acción tiene un resultado."),
         ex("¿A quién avisa una niña si le piden algo peligroso: a una persona adulta de confianza o a nadie?", "A una persona adulta de confianza", "Puede ayudarla y protegerla.")],
        [ex("Caso: Ana debe traer su cuaderno todos los días. Hoy lo olvidó. ¿Qué responsabilidad no cumplió y qué puede hacer?", "Traer su cuaderno; puede avisar y buscar cómo recuperar la tarea", "Reconoce la falta y busca arreglarla."),
         ex("Caso: Un compañero pide: «¿Me prestas tu goma, si no la necesitas?». ¿Es deber, favor o abuso?", "Un favor", "Pide algo opcional y razonable."),
         ex("Caso: Piden a un niño de 8 años que cuide solo a un bebé toda la noche. ¿Es un deber, un favor o un abuso?", "Un abuso: no corresponde a un niño", "Cuidar solo a un bebé toda la noche es una tarea propia de una persona adulta.")],
        [ex("Lalo dice: «Tengo que hacer todo lo que me pidan». ¿Qué parte de la clase lo corrige?", "No debo hacer lo peligroso ni lo injusto", "Existen pedidos que no corresponden a un niño."),
         ex("Sara cree que decir «no» a un favor es siempre una falta. ¿Qué le explicas?", "Que un favor es voluntario", "Se puede decir que no con respeto.")],
        [ex("Elige un deber de estudiante y un favor que puedes hacer a un compañero. Escríbelos.", "Por ejemplo: deber, hacer mis tareas; favor, prestar un lápiz", "Cada uno cumple su definición."),
         ex("Clasifica cada caso como deber, favor o abuso: A) ordenar mi mochila, B) ayudar a un amigo con su dibujo si puedo, C) subir a un árbol muy alto porque me lo exigen.", "A deber, B favor, C abuso", "A me corresponde, B es voluntario, C es peligroso.")],
    ),
    context=[ex("En el recreo, un grupo le dice a Pía: «Si no nos das tu colación, no juegas con nosotros». ¿Qué debe hacer Pía y por qué?", "Decir que no y avisar a una persona adulta de confianza", "La están presionando.")],
    selfcheck=[ex("Escribe una diferencia entre deber y favor.", "El deber me corresponde; el favor es voluntario", "Esa es la diferencia clave."), ex("¿Qué haces si te piden algo peligroso?", "Digo no y aviso a una persona adulta de confianza", "Así me protejo."), ex("¿Una consecuencia es lo que pasa antes o después de actuar?", "Después", "Es el resultado de lo que hago.")],
    open_task=task("Escribe una lista con un deber, un favor y una situación que sería un abuso. Usa estos casos o los tuyos: ordenar mi puesto, prestar un borrador, subir a un lugar muy alto si me lo exigen. Escribe qué harías en el abuso.", "Deber: ordenar mi puesto. Favor: prestar un borrador. Abuso: subir a un lugar muy alto si me lo exigen; diría que no y avisaría a una persona adulta de confianza.", ["clasifica correctamente los tres casos", "explica qué haría en el abuso", "usa palabras de la clase"], ["lista de tres casos", "frase de acción ante el abuso"], ["decir que un favor es obligatorio", "no avisar a una persona adulta de confianza"], "Muestra tu lista a un adulto de confianza y comenta con él si estás de acuerdo."),
    reinforce="Haz una lista de dos deberes que cumples en tu casa o en tu escuela.",
    extend="Escribe un caso en el que decir «no» sea lo correcto.",
)

register(
    OA11, 2,
    materials="Este cuaderno y un lápiz. La lista de útiles y el horario están escritos en los ejercicios.",
    use="Aprenderé cuáles son mis responsabilidades como estudiante y qué pasa cuando las cumplo. Sirve para trabajar mejor en clases y colaborar con mi curso.",
    prior=["Sé qué es un deber.", "Sé que mis acciones tienen consecuencias."],
    explain=[
        "Como estudiante tengo deberes. Llegar a la hora, traer mis útiles, hacer mis tareas, escuchar cuando otra persona habla, seguir las normas de convivencia y cuidar los materiales. Cumplirlos me permite aprender y ayuda a que mi curso trabaje tranquilo.",
        "Cada deber tiene una consecuencia. Si traigo mis útiles, puedo trabajar sin interrupciones. Si no los traigo, pierdo tiempo o dependo de otros. Si cumplo, mi curso avanza. Si falto a un compromiso, puedo reconocerlo y arreglarlo, por ejemplo avisando y entregando después.",
        "Para cumplir ayuda planificar. Anotar las tareas en una agenda, dejar la mochila lista la noche anterior y pedir ayuda cuando algo no se entiende son hábitos de una persona responsable. Pedir ayuda no es una falta: es parte de cumplir.",
    ],
    vocab=[("deber escolar", "tarea o norma que me toca cumplir como estudiante"), ("convivencia", "vivir y trabajar bien con otras personas"), ("agenda", "cuaderno para anotar tareas y fechas"), ("puntualidad", "llegar a la hora"), ("hábito", "algo que se repite hasta hacerse costumbre")],
    worked=[
        W("Un deber y su consecuencia", "Lucas olvidó su cuaderno de Matemática. ¿Qué consecuencia puede tener y cómo puede mejorar?",
          ["Sin el cuaderno no puede trabajar en la clase.", "Puede avisar a su profesora.", "Puede dejar su mochila lista la noche anterior."], "Pierde tiempo de trabajo; mejora preparando su mochila la noche anterior"),
        W("Ordenar los pasos", "Ordena para hacer una tarea: A) pedir ayuda si hay dudas, B) anotar la tarea en la agenda, C) entregarla a tiempo.", ["Primero se anota.", "Luego se pide ayuda si hay dudas.", "Al final se entrega."], "B, A, C"),
    ],
    mistakes=[
        M("Pensar que pedir ayuda es no cumplir.", "Se ve la ayuda como falta de esfuerzo.", "Pedir ayuda es una forma responsable de cumplir."),
        M("Creer que no pasa nada si no cumplo.", "Se ignora la consecuencia en mí y en mi curso.", "Piensa qué pasa si no cumplo y cómo arreglarlo."),
    ],
    tiers=tiers(
        [ex("Hacer mi tarea, ¿es un deber escolar o un juego?", "Un deber escolar", "Es parte de lo que me toca como estudiante."),
         ex("Llegar a la hora, ¿es puntualidad o desorden?", "Puntualidad", "Así se llama llegar a la hora."),
         ex("Anotar la tarea en la agenda, ¿ayuda o dificulta recordarla?", "Ayuda", "Un registro evita olvidar.")],
        [ex("Menciona tres deberes de un estudiante.", "Por ejemplo: llegar a la hora, traer útiles y hacer tareas", "Son deberes escolares."),
         ex("¿Qué consecuencia tiene no traer los útiles?", "Perder tiempo o depender de otros", "Se interrumpe el trabajo."),
         ex("Explica por qué pedir ayuda es parte de ser responsable.", "Porque ayuda a cumplir bien lo que me toca", "No entender algo se resuelve preguntando.")],
        [ex("Horario: lunes y martes hay Matemática, miércoles Artes, jueves Lenguaje. Tengo tarea de Artes. ¿Qué día debo llevar mis materiales de Artes?", "El miércoles", "Artes es el miércoles."),
         ex("Pedro no entendió la tarea. ¿Qué es mejor: pedir ayuda a su profesora o no hacerla?", "Pedir ayuda a su profesora", "Es una forma responsable de cumplir."),
         ex("Lista de útiles de hoy: cuaderno, lápiz, goma, regla. Mía trae cuaderno, lápiz y regla. ¿Qué le falta?", "La goma", "Compara la lista con lo que trajo.")],
        [ex("Rosa dice: «Si se me olvidó, no importa porque nadie se dará cuenta». ¿Qué le responderías?", "Que sí importa y puede avisar y arreglarlo", "Hay una consecuencia aunque nadie lo note."),
         ex("Eli cree que cumplir deberes solo sirve para evitar retos. ¿Qué otra razón hay?", "Aprender y ayudar a que el curso trabaje bien", "Los deberes tienen un propósito.")],
        [ex("Planifica: tienes una tarea para el viernes y hoy es lunes. Escribe dos pasos para entregarla a tiempo.", "Por ejemplo: anotarla en la agenda y hacerla un poco cada día", "Planificar reparte el trabajo."),
         ex("Marta olvidó entregar una tarea. Ordena lo que puede hacer: A) entregarla al día siguiente, B) avisar a su profesora, C) dejar la mochila lista.", "B, A, C", "Avisa, entrega y luego previene.")],
    ),
    context=[ex("En una clase de Artes, cada estudiante debe traer una caja vacía de cartón. Julián la olvidó. Dice: «No importa, otro la traerá». ¿Qué debería hacer y por qué?", "Avisar a su profesora y buscar cómo cumplir", "Es su responsabilidad, no la de otro.")],
    selfcheck=[ex("Nombra dos deberes escolares.", "Por ejemplo: traer útiles y hacer tareas", "Son deberes de estudiante."), ex("¿Qué es la puntualidad?", "Llegar a la hora", "Es cumplir con el horario."), ex("¿Pedir ayuda es una falta o una forma responsable de cumplir?", "Una forma responsable de cumplir", "Ayuda a hacerlo bien.")],
    open_task=task("Crea una mini agenda de tres días. Para cada día escribe un deber escolar que cumplirás. Elige entre: traer mis útiles, hacer la tarea, llegar a la hora, escuchar sin interrumpir, ordenar mi puesto.", "Lunes: traer mis útiles. Martes: hacer la tarea. Miércoles: llegar a la hora.", ["tres días con un deber cada uno", "los deberes son escolares", "son concretos y cumplibles"], ["agenda de tres líneas"], ["escribir deberes que no son escolares", "escribir deseos en lugar de deberes"], "Al final del día marca si cumpliste y piensa qué te ayudó."),
    reinforce="Dibuja tu mochila lista para mañana y marca con una cruz cada útil que debes llevar.",
    extend="Escribe cómo ayuda a tu curso que cada estudiante cumpla sus deberes.",
)

register(
    OA11, 3,
    materials="Este cuaderno y un lápiz. Las situaciones están escritas en los ejercicios.",
    use="Aprenderé a cuidar los espacios que comparto y las pertenencias, mías y de los demás. Sirve para convivir bien en mi casa, mi escuela y mi comunidad.",
    prior=["Sé qué es un deber.", "Sé que hay espacios que comparto con otras personas."],
    explain=[
        "Comparto espacios con otras personas: la sala de clases, el patio, el baño, la plaza y mi casa. Todos usamos esos lugares, así que todos ayudamos a mantenerlos ordenados y limpios. Colaborar es hacer una parte del trabajo entre varias personas.",
        "Hay acciones seguras que puedo hacer: guardar mis cosas, botar la basura en el basurero, dejar ordenados los materiales, no rayar muros ni bancos y ayudar a recoger. En mi casa también ayudo con tareas seguras: poner la mesa, hacer mi cama, guardar mi ropa y ordenar mis juguetes. Las tareas con productos de limpieza fuertes, objetos filosos o cosas pesadas las hacen personas adultas.",
        "También cuido mis pertenencias y las de otros. No tomo algo ajeno sin permiso. Si lo presto, lo cuido y lo devuelvo. Si algo se dañó, aviso y ofrezco arreglarlo. Si encuentro algo perdido, lo entrego a una persona adulta responsable.",
    ],
    vocab=[("espacio compartido", "lugar que usan varias personas"), ("colaborar", "hacer una parte del trabajo entre varios"), ("pertenencia", "objeto que es de alguien"), ("permiso", "aceptación de la persona dueña para usar algo"), ("devolver", "dar de vuelta lo que se prestó")],
    worked=[
        W("Una acción segura", "El patio quedó con papeles después del recreo. ¿Qué puede hacer un estudiante de forma segura?",
          ["Puede recoger papeles con las manos limpias o con guantes, si hay.", "Botarlos en el basurero.", "Si hay vidrios o cosas peligrosas, avisa a una persona adulta."], "Recoger los papeles, botarlos en el basurero y avisar a un adulto si hay algo peligroso"),
        W("Algo prestado", "Gabriela presta su lápiz a Tomás. Tomás lo quiebra sin querer. ¿Qué debe hacer?",
          ["Reconocer lo que pasó.", "Avisar a Gabriela.", "Ofrecer ayuda para repararlo o reponerlo."], "Avisar, reconocerlo y ofrecer repararlo o reponerlo"),
    ],
    mistakes=[
        M("Pensar que botar basura en el piso no daña a nadie.", "Se olvida que otras personas usan ese lugar.", "Usa el basurero y ayuda a mantener limpio."),
        M("Tomar una cosa ajena «solo un rato» sin pedir permiso.", "El dueño no sabe dónde está su cosa.", "Pide permiso y devuélvela."),
    ],
    tiers=tiers(
        [ex("¿La sala de clases es un espacio compartido o un espacio solo mío?", "Un espacio compartido", "La usan muchas personas."),
         ex("¿Los papeles se botan en el piso o en el basurero?", "En el basurero", "Así se mantiene limpio."),
         ex("Hacer mi cama en casa, ¿es una ayuda segura para un niño o una tarea de adultos?", "Una ayuda segura", "Es una tarea simple, sin riesgos.")],
        [ex("Nombra dos espacios que comparto con otras personas.", "Por ejemplo: sala, patio, plaza o mi casa", "Todos son lugares compartidos."),
         ex("Menciona dos formas seguras de ayudar en tu casa.", "Por ejemplo: poner la mesa y guardar mi ropa", "Son tareas simples al alcance de un niño."),
         ex("¿Por qué una persona adulta debe hacer las tareas con productos de limpieza fuertes?", "Porque pueden ser peligrosos", "Un niño no debe manejar productos riesgosos.")],
        [ex("Encuentras un estuche con nombre en el patio. ¿Qué haces: se lo entregas a una persona adulta responsable o te lo quedas?", "Se lo entrego a una persona adulta responsable", "Así el dueño puede recuperarlo."),
         ex("Una banca de la plaza tiene un rayado. Un grupo quiere hacer otro. ¿Qué debería hacer?", "No rayar y avisar a una persona adulta", "Rayar daña un espacio de todos."),
         ex("Hay vidrio roto en el patio. ¿Qué debe hacer un niño: recogerlo o avisar a una persona adulta?", "Avisar a una persona adulta", "El vidrio es peligroso.")],
        [ex("Raúl dice: «El patio no es mío, no me importa si está sucio». ¿Qué argumento le das?", "Es de todos y todos lo usamos", "Un espacio compartido se cuida entre todos."),
         ex("Sofía cree que si presta algo ya no es su responsabilidad cuidarlo. ¿Qué le corresponde a quien lo recibe?", "Cuidarlo y devolverlo", "Quien lo usa se hace cargo.")],
        [ex("Escribe un compromiso concreto para cuidar la sala de clases.", "Por ejemplo: dejar mi puesto ordenado antes de salir", "Es una acción concreta y segura."),
         ex("Ordena para cuidar un préstamo: A) devolverlo, B) pedirlo con permiso, C) usarlo con cuidado.", "B, C, A", "Primero el permiso, luego el uso y al final la devolución.")],
    ),
    context=[ex("Después de un cumpleaños en el curso quedan globos y vasos de plástico en la sala. Un grupo ofrece ayuda. ¿Qué parte pueden hacer los niños con seguridad?", "Juntar los vasos y globos y botarlos en el basurero", "Son tareas seguras si no hay objetos filosos.")],
    selfcheck=[ex("En Historia: ¿Qué significa colaborar?", "Hacer una parte del trabajo entre varias personas", "Cada uno ayuda."), ex("¿Qué haces con algo perdido que encuentras?", "Lo entrego a una persona adulta responsable", "Así puede volver a su dueño."), ex("¿Quién hace las tareas con productos de limpieza fuertes?", "Las personas adultas", "Son tareas riesgosas para niños.")],
    open_task=task("Elige un espacio compartido de esta lista: sala de clases, patio o plaza del barrio. Escribe una lista de tres acciones seguras que ayudan a cuidarlo y una norma que te comprometes a cumplir.", "Elegí el patio. Acciones: botar papeles en el basurero, avisar si hay vidrios y devolver los balones. Me comprometo a dejar el lugar donde jugué sin basura.", ["elige un espacio de la lista", "tres acciones seguras", "una norma o compromiso"], ["lista de tres acciones", "frase de compromiso"], ["incluir tareas peligrosas", "no relacionar las acciones con el espacio"], "Comenta tu lista con una persona de tu casa y pregúntale qué acción agregaría."),
    reinforce="Ordena tu puesto de estudio y deja cada cosa en su lugar.",
    extend="Escribe cómo puede ayudar un curso a mantener limpio el patio sin que nadie haga tareas peligrosas.",
)

register(
    OA11, 4,
    materials="Este cuaderno y un lápiz. Las situaciones están escritas en los ejercicios.",
    use="Aprenderé acciones simples para cuidar mi salud y mi higiene, y cuándo pedir ayuda. Sirve para sentirme bien y avisar a tiempo si algo me pasa.",
    prior=["Sé que cuidarme es una responsabilidad.", "Sé que puedo hablar con una persona adulta de confianza."],
    explain=[
        "Cuidar mi salud es una responsabilidad. Me lavo las manos con agua y jabón antes de comer y después de ir al baño. Me cepillo los dientes. Duermo lo suficiente, como alimentos variados y bebo agua. También me abrigo cuando hace frío y me protejo del sol.",
        "También cuido mi cuerpo y mis emociones. Si me duele algo, tengo mucho sueño, siento miedo o me siento triste, se lo cuento a una persona adulta de confianza. No debo aguantar solo ni esperar a que sea muy grave. Pedir ayuda es una forma de cuidarme.",
        "Hay cosas que no debo hacer solo. No tomo medicamentos si una persona adulta no me los da. No me acerco al fuego. No pruebo productos de limpieza. Si no sé qué hacer, pregunto primero. Mis decisiones de autocuidado se aprenden poco a poco, con apoyo de mi familia y de mi escuela.",
    ],
    vocab=[("higiene", "acciones para mantenerme limpio y sano"), ("autocuidado", "cuidarme a mí mismo"), ("hábito saludable", "costumbre que cuida mi salud"), ("persona adulta de confianza", "adulto con quien me siento seguro y a quien puedo contar lo que me pasa"), ("pedir ayuda", "contar lo que pasa para recibir apoyo")],
    worked=[
        W("Un hábito de higiene", "Mateo viene del recreo y va a almorzar. ¿Qué hábito de higiene debe hacer antes?", ["Antes de comer cuido mis manos.", "Me las lavo con agua y jabón."], "Lavarse las manos con agua y jabón"),
        W("Cuándo pedir ayuda", "A Valentina le duele mucho el estómago en clases. ¿Qué debe hacer?", ["No debe aguantar sola.", "Avisa a su profesora o a una persona adulta de confianza."], "Avisar a su profesora o a una persona adulta de confianza"),
    ],
    mistakes=[
        M("Pensar que pedir ayuda es molestar.", "Se piensa que los adultos no quieren saber.", "Avisar a tiempo ayuda a que todo se resuelva mejor."),
        M("Tomar un remedio que encontré porque «seguro me sirve».", "Un remedio sin indicación puede hacer daño.", "Solo tomo medicamentos que me da una persona adulta responsable."),
    ],
    tiers=tiers(
        [ex("Antes de comer, ¿me lavo las manos o me las seco con la ropa?", "Me lavo las manos", "Se lavan con agua y jabón."),
         ex("El cepillado de dientes, ¿es un hábito saludable o una pérdida de tiempo?", "Un hábito saludable", "Cuida mis dientes."),
         ex("Si me duele algo, ¿lo cuento o lo escondo?", "Lo cuento", "Hay que avisar a una persona adulta de confianza.")],
        [ex("Menciona tres acciones de higiene o autocuidado de la clase.", "Por ejemplo: lavarme las manos, cepillarme los dientes y dormir lo suficiente", "Son hábitos saludables del texto."),
         ex("Explica por qué conviene avisar a tiempo cuando algo me duele.", "Porque así me ayudan antes de que sea más grave", "Pedir ayuda cuida mi salud."),
         ex("¿Quién puede ser una persona adulta de confianza? Da dos ejemplos.", "Por ejemplo: una profesora o una persona de mi familia", "Es alguien con quien me siento seguro.")],
        [ex("Tomás encuentra un frasco con jarabe en un cajón y siente un poco de tos. ¿Se lo toma o avisa a una persona adulta?", "Avisa a una persona adulta", "Solo debe tomar lo que un adulto responsable le da."),
         ex("Después de ir al baño en la escuela, ¿qué hábito de higiene hace Ema?", "Lavarse las manos con agua y jabón", "Es la regla después de ir al baño."),
         ex("Hace mucho sol en el patio. ¿Qué cuidado puede tener Nico?", "Protegerse con sombrero o buscar sombra", "Así se protege del sol.")],
        [ex("Lola dice: «Si me siento triste, es mejor no contárselo a nadie». ¿Qué le recomiendas?", "Contarle a una persona adulta de confianza", "Pedir ayuda también cuida las emociones."),
         ex("Matías cree que solo se cuida la salud cuando se está enfermo. ¿Qué respondes?", "También se cuida con hábitos todos los días", "Los hábitos previenen problemas.")],
        [ex("Escribe dos hábitos que quieres practicar esta semana y por qué.", "Por ejemplo: dormir temprano porque descansa mi cuerpo y lavar mis manos antes de comer", "Une hábito con razón."),
         ex("Ordena según el tiempo: A) almorzar, B) lavarme las manos, C) cepillarme los dientes después de comer.", "B, A, C", "Primero lavo mis manos, luego como y después me cepillo.")],
    ),
    context=[ex("Camila siente miedo porque una situación en el recreo la dejó muy nerviosa. No sabe a quién contarle. ¿Qué puedes recomendarle?", "Contárselo a su profesora o a una persona adulta de confianza", "Pedir ayuda es parte del autocuidado.")],
    selfcheck=[ex("¿Cuándo me lavo las manos? Menciona dos momentos.", "Antes de comer y después de ir al baño", "Son momentos de higiene."), ex("¿Qué es una persona adulta de confianza?", "Una persona adulta con quien me siento seguro y a quien puedo contar lo que me pasa", "Es alguien que me escucha y me ayuda."), ex("¿Puedo tomar remedios sin que me los dé un adulto?", "No", "Pueden hacer daño.")],
    open_task=task("Haz una tarjeta de autocuidado con tres hábitos que cuidan tu salud (por ejemplo: lavar las manos, dormir bien, beber agua) y el nombre de una persona adulta de confianza a quien puedes pedir ayuda (usa su rol, como «mi profesora» o «una persona de mi familia»).", "Hábitos: lavarme las manos, beber agua y dormir. Si necesito ayuda, se lo cuento a mi profesora.", ["tres hábitos saludables", "un rol de persona adulta de confianza", "no incluye datos personales"], ["tarjeta con tres hábitos", "un rol de persona adulta"], ["escribir un nombre completo o dirección", "incluir hábitos peligrosos"], "Pide a una persona de tu casa que lea tu tarjeta y diga qué hábito te cuesta más."),
    reinforce="Cuenta cuántas veces te lavaste las manos hoy y en qué momentos.",
    extend="Escribe cómo ayuda a tu curso que todos se laven las manos antes de comer.",
)

register(
    OA11, 5,
    materials="Este cuaderno y un lápiz. La tabla de registro está escrita en los ejercicios.",
    use="Aprenderé a planificar un compromiso pequeño que se pueda comprobar. Sirve para cumplir lo que prometo y saber si lo logré.",
    prior=["Conozco deberes de estudiante.", "Sé que cumplir tiene consecuencias."],
    explain=[
        "Un compromiso es una promesa de hacer algo. Un buen compromiso es pequeño, concreto y se puede comprobar. «Ser más ordenado» es muy general. «Guardar mis útiles al terminar cada clase» es concreto, porque puedo ver si lo hice.",
        "Para planificar un compromiso respondo cuatro preguntas: qué voy a hacer, cuándo lo haré, qué necesito y cómo comprobaré que lo cumplí. La evidencia puede ser un registro: una tabla donde marco una cruz cada día que cumplo.",
        "Al final reviso. Cuento los días que cumplí y pienso qué me ayudó o qué me dificultó. Si no cumplí, no pasa nada grave: busco una forma de mejorar, por ejemplo poner un recordatorio. Los compromisos que dependen de otras personas se hablan con ellas.",
    ],
    vocab=[("compromiso", "promesa de hacer algo"), ("concreto", "que se puede ver y hacer"), ("evidencia", "señal que prueba que cumplí"), ("registro", "anotación de lo que hice"), ("revisar", "mirar lo que pasó para mejorar")],
    worked=[
        W("Hacer concreto un compromiso", "Un estudiante escribe: «Voy a portarme mejor». ¿Cómo lo hace concreto y comprobable?", ["Pregunto qué acción exacta.", "Por ejemplo: «Levantar la mano antes de hablar en clases».", "Puedo comprobarlo con una cruz cada día."], "Levantar la mano antes de hablar y marcar una cruz cada día"),
        W("Revisar un registro", "Registro de Ana: lunes ✓, martes ✓, miércoles ✗, jueves ✓, viernes ✓. ¿Cuántos días cumplió?", ["Cuento las cruces con ✓: lunes, martes, jueves y viernes.", "Son 4.", "Cumplió 4 de 5 días."], "4 de 5 días"),
    ],
    mistakes=[
        M("Elegir un compromiso enorme, como «nunca más olvidar nada».", "Es difícil de lograr y de comprobar.", "Elige algo pequeño y concreto para unos días."),
        M("Pensar que si fallo un día todo está perdido.", "Se ve la falta como un fracaso total.", "Reconoce lo que pasó y vuelve a intentarlo."),
    ],
    tiers=tiers(
        [ex("«Guardar mis útiles al terminar la clase», ¿es un compromiso concreto o muy general?", "Concreto", "Puedo ver si lo hice."),
         ex("«Ser mejor persona», ¿es un compromiso concreto o muy general?", "Muy general", "No dice qué acción hacer."),
         ex("¿Un registro sirve para anotar lo que hice o para jugar?", "Para anotar lo que hice", "Es la evidencia del compromiso.")],
        [ex("Nombra las cuatro preguntas para planificar un compromiso.", "Qué haré, cuándo, qué necesito y cómo lo comprobaré", "Son las preguntas de la clase."),
         ex("¿Qué evidencia puedo usar para mi compromiso?", "Un registro con cruces", "Muestra qué días cumplí."),
         ex("¿Qué hago si un día no cumplí?", "Reconozco lo que pasó y busco cómo mejorar", "No es un fracaso total.")],
        [ex("Registro de Beto: lunes ✓, martes ✓, miércoles ✓, jueves ✗, viernes ✓. ¿Cuántos días de cinco cumplió?", "4 días", "Cuento solo las marcas ✓."),
         ex("Elige el compromiso más concreto: A) «Estudiar más» B) «Leer 10 minutos después de almuerzo».", "B", "B dice qué, cuándo y cuánto."),
         ex("Para cumplir «traer mi agenda todos los días», Eli pone un recordatorio junto a la puerta. ¿Qué pregunta de planificación responde?", "Qué necesito", "El recordatorio es lo que lo ayuda a cumplir.")],
        [ex("Gabo dice: «Prometo todo, así quedo bien». ¿Qué problema tiene?", "No puede comprobarse ni cumplir todo", "Un compromiso debe ser pequeño y concreto."),
         ex("Pili falló dos días y dice: «Ya no sirve». ¿Qué le recomiendas?", "Revisar qué pasó y seguir intentándolo", "Se puede mejorar.")],
        [ex("Escribe un compromiso con qué, cuándo y evidencia para tu clase de Artes.", "Por ejemplo: traer mis materiales los jueves y marcar una cruz en mi registro", "Incluye las partes."),
         ex("Registro: lunes ✓, martes ✗, miércoles ✗, jueves ✓, viernes ✓. ¿Cuántos días cumplió y cuántos no?", "Cumplió 3 y no cumplió 2", "Hay 3 marcas ✓ y 2 marcas ✗.")],
    ),
    context=[ex("Un curso de 3.º básico decide mantener limpio el patio. Una niña propone: «Cada día, dos personas recogen papeles y se marca una cruz en la lista». ¿Es un compromiso verificable? Explica.", "Sí; es concreto y tiene registro", "Dice qué, quién y cómo comprobarlo.")],
    selfcheck=[ex("¿Qué es un compromiso?", "Una promesa de hacer algo", "Se debe poder cumplir."), ex("Menciona una forma de comprobar que cumplí.", "Un registro con cruces", "Es una evidencia."), ex("¿Los compromisos deben ser pequeños o enormes?", "Pequeños", "Así se pueden cumplir.")],
    open_task=task("Planifica un compromiso de una semana. Elige uno: guardar mis útiles al terminar la clase, ordenar mi puesto antes de salir, o lavarme las manos antes de comer. Escribe qué, cuándo, qué necesitas y dibuja una tabla de cinco días para marcar con una cruz. Al final cuenta cuántos días cumpliste.", "Compromiso: guardar mis útiles al terminar la clase. Cuándo: cada día de clases. Necesito: mi estuche. Registro: L ✓ M ✓ X ✗ J ✓ V ✓; cumplí 4 de 5 días.", ["compromiso concreto", "contesta qué, cuándo y qué necesito", "registro de cinco días y conteo"], ["tabla de cinco días", "frase con el conteo"], ["escribir un compromiso muy general", "no llevar registro"], "Comparte tu registro con una persona de tu casa y cuéntale qué te ayudó a cumplir."),
    reinforce="Marca hoy una cruz en tu registro si cumpliste tu compromiso.",
    extend="Escribe qué cambiarías en tu compromiso si hubiera sido difícil cumplirlo.",
)
