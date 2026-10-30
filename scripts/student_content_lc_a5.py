"""Student material for 1.º básico Lengua y Cultura de los Pueblos Originarios Ancestrales, OA 15 (patrimonio), OA 16 (ser humano, naturaleza y cosmos) y OA 17 (arte)."""
from __future__ import annotations

from student_content_lc_a1 import F_AYM, F_DIA, F_RN, L, M, T, W
from student_lessons import ex

OA15, OA16, OA17 = "LC01 OA 15", "LC01 OA 16", "LC01 OA 17"

# ============================================================ OA 15 · Patrimonio cultural
L(
    OA15, 1,
    materials="Lápiz y hojas. La lista de elementos de ejemplo está escrita en el cuaderno.",
    use="Aprenderé qué es el patrimonio cultural y por qué una comunidad valora ciertas cosas, siempre escuchando su voz.",
    prior=["Sé qué es un objeto antiguo.", "Sé que hay cosas que valoramos mucho."],
    explain=[
        "El patrimonio cultural es todo lo que una comunidad, un territorio o un pueblo recibe de quienes vivieron antes y quiere cuidar y pasar a quienes vienen después. Puede ser un objeto, un lugar, una fiesta, un cuento o una forma de hacer algo.",
        "Algo es patrimonio no porque lo diga una persona de afuera, sino porque la comunidad lo valora. Por eso escuchamos su voz. Por ejemplo, para el pueblo rapa nui los moai son parte de su patrimonio, y el Parque Nacional Rapa Nui fue declarado Patrimonio de la Humanidad por la UNESCO.",
        "Al hablar de patrimonio respondemos tres preguntas: ¿qué es?, ¿por qué lo valora la comunidad? y ¿quién lo dice? Si no sabemos por qué algo es importante, preguntamos y no suponemos.",
    ],
    vocab=[("patrimonio", "lo que una comunidad recibe y quiere cuidar para el futuro"), ("valorar", "considerar importante"), ("comunidad", "grupo de personas que comparten un lugar y una cultura"), ("heredar", "recibir de quienes vivieron antes"), ("voz comunitaria", "lo que dice la propia comunidad")],
    worked=[
        W("Reconocer patrimonio", "Ficha: «" + F_RN + "» ¿Qué elemento de la ficha es patrimonio de ese pueblo?", ["Busco algo que la comunidad valora.", "Los moai son figuras de piedra del pueblo rapa nui.", "La comunidad los valora."], "Los moai."),
        W("Quién lo dice", "Una persona de afuera dice que un lugar es patrimonio, pero la comunidad no lo dijo. ¿Qué haces?", ["Pregunto a la comunidad.", "No supongo.", "Escucho su voz."], "Pregunto a la comunidad."),
    ],
    mistakes=[
        M("Pensar que patrimonio es solo lo muy antiguo.", "También puede ser una fiesta o un saber que se practica hoy.", "Pregunta qué valora la comunidad."),
        M("Decidir por la comunidad qué es su patrimonio.", "Le toca a ella decirlo.", "Escucha su voz."),
    ],
    R=[
        ex("Patrimonio es lo que una comunidad recibe y quiere cuidar. ¿Verdadero o falso?", "Verdadero", "Esa es la definición."),
        ex("Los moai son figuras de piedra del pueblo rapa nui. ¿Son patrimonio de ese pueblo? Sí o No.", "Sí", "La comunidad los valora."),
        ex("Valorar es considerar algo importante. ¿Verdadero o falso?", "Verdadero", "Eso significa valorar."),
    ],
    C=[
        ex("¿Quién dice qué es su patrimonio? A) la comunidad B) cualquier persona de afuera", "A", "Es su voz."),
        ex("Verdadero o falso: el patrimonio puede ser una fiesta o un saber.", "Verdadero", "No solo objetos."),
        ex("¿Qué haces si no sabes por qué algo es importante?", "Pregunto", "No se supone."),
    ],
    A=[
        ex("Marca lo que puede ser patrimonio: un cuento que cuenta la comunidad, una bolsa de plástico, una fiesta, un lugar que cuida.", "un cuento, una fiesta y un lugar que cuida", "La bolsa de plástico no es valorada por la comunidad."),
        ex("Une cada ejemplo con su tipo. 1) moai 2) un cuento antiguo 3) una fiesta. a) objeto b) relato c) celebración", "1-a, 2-b, 3-c", "Cada uno es un tipo distinto."),
        ex("Ordena: 1) pregunto por qué es importante 2) escucho a la comunidad 3) escribo lo que me dijeron.", "1, 2, 3", "Se pregunta, se escucha y se anota."),
    ],
    Z=[
        ex("Ana dice que todo lo viejo es patrimonio. ¿Qué error comete?", "No todo lo viejo es valorado por una comunidad", "Lo valora la comunidad."),
        ex("¿Por qué escuchamos la voz de la comunidad?", "Porque ella decide qué valora", "Es su patrimonio."),
    ],
    D=[
        ex("Una escuela tiene 5 objetos que la comunidad valora y 3 que no. ¿Cuántos son patrimonio?", "5", "Solo los valorados."),
        ex("Un libro dice que algo es patrimonio, pero no dice por qué. ¿Qué haces?", "Pregunto a la comunidad o al educador", "No basta con la afirmación."),
    ],
    context=[ex("En tu escuela se valoran 2 cuentos, 1 canción y 1 objeto de la comunidad. ¿Cuántos elementos patrimoniales hay?", "4", "2 + 1 + 1 = 4.")],
    selfcheck=[ex("¿Qué es patrimonio?", "Lo que una comunidad recibe y quiere cuidar", "Pasa a otras generaciones."), ex("¿Quién dice qué es patrimonio?", "La comunidad", "Es su voz."), ex("¿Es patrimonio solo lo antiguo?", "No", "También lo que se practica hoy.")],
    task=T("Mira esta lista: los moai, un cuento que cuentan las abuelas, una fiesta de la comunidad, una bolsa de plástico. Escribe cuáles pueden ser patrimonio y por qué la comunidad podría valorarlos. Escribe una pregunta para el educador tradicional: ¿qué cosas de nuestra comunidad son patrimonio?",
           "Pueden ser patrimonio: los moai, el cuento y la fiesta. La bolsa no. Pregunta: ¿qué cosas de nuestra comunidad son patrimonio?",
           ["identifica ejemplos", "da razones", "formula una pregunta"], ["lista", "pregunta"], ["decidir por la comunidad"],
           "Valora la pregunta; no corregir qué considera una comunidad como patrimonio."),
    reinforce="Nombra tres cosas que tu familia o escuela valora y quiere cuidar.",
    extend="Pregunta a una persona mayor qué quiere que se cuide para el futuro.",
)

L(
    OA15, 2,
    materials="Lápiz y hojas. Una tabla de ejemplos materiales e inmateriales está escrita en el cuaderno.",
    use="Aprenderé a distinguir entre patrimonio material (se puede tocar) e inmaterial (se vive y se practica).",
    prior=["Sé qué es un objeto.", "Sé que hay cosas que no se tocan, como una canción."],
    explain=[
        "El patrimonio material son cosas que se pueden tocar: objetos, construcciones y lugares. Por ejemplo, una vasija de cerámica, un tejido o los moai. Se guardan y se cuidan para que no se rompan.",
        "El patrimonio inmaterial son cosas que no se tocan, pero se viven y se practican: cuentos, canciones, fiestas, saberes y la lengua. Pasan de personas mayores a jóvenes y existen mientras se practican.",
        "A veces un objeto y una práctica van juntos. Por ejemplo, un tejido es un objeto material, pero el saber para hacerlo es inmaterial. Cuando cuidamos el objeto y también el saber, cuidamos todo el patrimonio.",
    ],
    vocab=[("material", "que se puede tocar"), ("inmaterial", "que no se toca, pero se vive y se practica"), ("objeto", "cosa que se puede tomar con las manos"), ("saber", "lo que alguien sabe hacer"), ("práctica", "algo que se hace con frecuencia")],
    worked=[
        W("Material o inmaterial", "¿Una vasija de cerámica es material o inmaterial?", ["La puedo tocar.", "Es un objeto.", "Es material."], "Material."),
        W("Un objeto y su saber", "Un tejido es material. ¿Qué es el saber para hacerlo?", ["No se toca.", "Se aprende y se practica.", "Es inmaterial."], "Inmaterial."),
    ],
    mistakes=[
        M("Pensar que solo los objetos son patrimonio.", "Los saberes y las fiestas también.", "Piensa en lo material y lo inmaterial."),
        M("Cuidar el objeto y olvidar el saber.", "Sin el saber, se pierde el objeto del futuro.", "Cuida ambos."),
    ],
    R=[
        ex("Una vasija se puede tocar. ¿Es material o inmaterial?", "Material", "Se puede tocar."),
        ex("Una canción que se canta, ¿es material o inmaterial?", "Inmaterial", "No se toca, se vive."),
        ex("La lengua de un pueblo, ¿es material o inmaterial?", "Inmaterial", "Se practica al hablar."),
    ],
    C=[
        ex("¿Cuál es patrimonio inmaterial? A) una fiesta B) una piedra", "A", "La fiesta se vive y se practica."),
        ex("Verdadero o falso: el saber de hacer un tejido es inmaterial.", "Verdadero", "Se aprende y se practica."),
        ex("¿Qué se debe cuidar de un tejido?", "El objeto y el saber de hacerlo", "Ambos son patrimonio."),
    ],
    A=[
        ex("Clasifica como MATERIAL o INMATERIAL: a) un moai b) un cuento c) un telar.", "a) material, b) inmaterial, c) material", "El cuento no se toca."),
        ex("Une cada ejemplo con su tipo. 1) una fiesta 2) un tejido 3) una canción. a) material b) inmaterial", "1-b, 2-a, 3-b", "El tejido se toca; la fiesta y la canción no."),
        ex("En una lista hay 3 objetos y 2 saberes. ¿Cuántos elementos son inmateriales?", "2", "Solo los saberes."),
    ],
    Z=[
        ex("Luz dice que si guarda un tejido ya cuidó todo. ¿Qué falta?", "Cuidar el saber de hacerlo", "El saber es inmaterial y también es patrimonio."),
        ex("¿Por qué los saberes existen mientras se practican?", "Porque se pasan al practicarlos", "Si nadie los practica, se olvidan."),
    ],
    D=[
        ex("Una comunidad tiene 4 tejidos y 6 personas que saben tejer. ¿Cuántos elementos son materiales?", "4", "Los tejidos se tocan."),
        ex("Un museo guarda objetos, pero nadie enseña a hacerlos. ¿Se cuida todo el patrimonio? Sí o No.", "No", "Falta el saber."),
    ],
    context=[ex("En la feria de la comunidad hay 2 telares (objetos) y 1 abuela que enseña a tejer. ¿Qué parte es inmaterial?", "La enseñanza de la abuela", "Es un saber.")],
    selfcheck=[ex("¿Qué es material?", "Lo que se puede tocar", "Es algo físico que se toca."), ex("¿Qué es inmaterial?", "Lo que se vive y se practica", "No se toca."), ex("¿Una canción es material?", "No", "Es un saber inmaterial.")],
    task=T("Dibuja dos columnas: MATERIAL e INMATERIAL. Pon en cada una tres ejemplos de esta lista: moai, cuento, telar, fiesta, vasija de cerámica, lengua. Escribe una frase que diga por qué es importante cuidar los dos.",
           "Material: moai, telar, vasija. Inmaterial: cuento, fiesta, lengua. Hay que cuidar los dos para que el patrimonio no se pierda.",
           ["clasifica bien", "usa los ejemplos dados", "explica por qué cuidar ambos"], ["dos columnas", "frase"], ["olvidar el saber"],
           "Valora la clasificación; si hay dudas sobre lo cultural, preguntar al educador tradicional."),
    reinforce="Toca tres objetos de tu casa y di si son material o inmaterial.",
    extend="Escribe una pregunta sobre un saber que se pasa de abuelos a nietos.",
)

L(
    OA15, 3,
    materials="Lápiz y hojas. Los casos de amenazas están escritos en el cuaderno.",
    use="Aprenderé qué cosas pueden dañar el patrimonio y qué cuidados son respetuosos y posibles.",
    prior=["Sé qué es patrimonio.", "Sé que hay cosas que se pueden perder."],
    explain=[
        "El patrimonio puede estar en peligro. Una amenaza es algo que puede dañarlo o hacerlo desaparecer. Por ejemplo, la basura en un lugar importante, el robo de piezas antiguas, el olvido de un cuento o que nadie hable una lengua.",
        "En Chile, los sitios arqueológicos y las piezas antiguas están protegidos por la ley. Por eso no debemos llevarnos ni mover piedras, cerámicas u otros objetos antiguos que encontremos. Si vemos algo así, avisamos a un adulto.",
        "También hay cuidados para lo inmaterial: escuchar a los mayores, aprender de ellos, practicar con respeto y no usar un saber de una comunidad sin permiso. Cada comunidad decide cómo proteger su patrimonio. Nosotros podemos ayudar con acciones simples.",
    ],
    vocab=[("amenaza", "algo que puede dañar o hacer desaparecer"), ("cuidado", "acción para proteger algo"), ("sitio arqueológico", "lugar con restos de personas que vivieron hace mucho"), ("proteger", "evitar que se dañe"), ("olvido", "cuando algo ya no se recuerda ni se practica")],
    worked=[
        W("Amenaza y cuidado", "Hay basura cerca de un lugar importante. ¿Qué amenaza hay y qué cuidado ayuda?", ["Amenaza: la basura daña el lugar.", "Cuidado: recoger la basura con un adulto.", "Así se protege."], "Amenaza: basura; cuidado: recogerla con un adulto."),
        W("Una pieza antigua", "Encuentras una cerámica antigua en un campo. ¿La guardas?", ["Puede ser patrimonio protegido por la ley.", "No la muevo ni me la llevo.", "Aviso a un adulto."], "No; aviso a un adulto."),
    ],
    mistakes=[
        M("Llevarse una pieza antigua porque es linda.", "Es patrimonio protegido.", "No la toques y avisa."),
        M("Pensar que solo se pierden los objetos.", "También se pierden cuentos y lenguas si no se practican.", "Cuida lo inmaterial."),
    ],
    R=[
        ex("Una amenaza es algo que puede dañar. ¿Verdadero o falso?", "Verdadero", "Esa es la definición."),
        ex("¿Qué cuida el patrimonio? A) recoger basura B) llevarse piezas antiguas", "A", "Recoger basura protege."),
        ex("Si encuentras una pieza antigua, ¿qué haces? A) aviso a un adulto B) me la llevo", "A", "Está protegida por la ley."),
    ],
    C=[
        ex("¿Cuál es una amenaza? A) el olvido de un cuento B) una fiesta", "A", "Si nadie lo cuenta, se pierde."),
        ex("Verdadero o falso: las piezas arqueológicas están protegidas por la ley.", "Verdadero", "No se pueden llevar."),
        ex("¿Qué cuidado ayuda al patrimonio inmaterial?", "Escuchar y practicar con respeto", "Así sigue vivo."),
    ],
    A=[
        ex("Une la amenaza con el cuidado. 1) basura 2) olvido de un cuento 3) robo de piezas. a) escuchar y contar b) recoger y avisar c) no llevarse piezas y avisar", "1-b, 2-a, 3-c", "Cada cuidado responde a una amenaza."),
        ex("Clasifica como AMENAZA o CUIDADO: a) llevarse una cerámica b) aprender un cuento c) tirar basura.", "a) amenaza, b) cuidado, c) amenaza", "Aprender cuida el patrimonio."),
        ex("Ordena qué haces si ves una pieza antigua: 1) aviso a un adulto 2) no la toco 3) miro sin moverla.", "3, 2, 1", "Miro, no toco y aviso."),
    ],
    Z=[
        ex("Tomás dice que una piedra pintada es linda y se la lleva. ¿Qué error comete?", "Puede ser patrimonio protegido", "Debió dejarla y avisar."),
        ex("¿Por qué cuidar los saberes ayuda al futuro?", "Porque los jóvenes podrán practicarlos", "Así se transmiten a otros."),
    ],
    D=[
        ex("Una comunidad tenía 9 cuentistas y hoy quedan 4. ¿Cuántos menos hay?", "5", "9 − 4 = 5."),
        ex("Un cartel dice «no tocar». ¿Qué haces aunque nadie mire? A) respeto el cartel B) toco", "A", "El cuidado no depende de que nos miren."),
    ],
    context=[ex("En una visita a un sitio con restos antiguos, el guía pide no mover nada. Si 20 niños obedecen y 0 desobedecen, ¿cuántos cuidan el lugar?", "20", "Todos obedecen el pedido.")],
    selfcheck=[ex("En Lengua y Cultura de los Pueblos Originarios, ¿qué es una amenaza?", "Algo que puede dañar el patrimonio", "Lo pone en peligro."), ex("¿Qué haces si ves una pieza antigua?", "No la toco y aviso a un adulto", "Está protegida por la ley."), ex("¿Cómo cuidas un cuento?", "Lo escucho y lo cuento con respeto", "Así sigue vivo.")],
    task=T("Dibuja un cartel con tres cuidados para el patrimonio (por ejemplo: no tirar basura, no llevarse piezas antiguas, escuchar a los mayores). Escribe una amenaza al lado de cada cuidado. Escribe una pregunta para la comunidad: ¿qué cuidados quieren que hagamos?",
           "Cartel: no tirar basura (amenaza: basura), no llevarme piezas (amenaza: robo), escuchar a los mayores (amenaza: olvido). Pregunta: ¿cómo podemos ayudar?",
           ["une amenaza y cuidado", "propone acciones posibles", "pregunta a la comunidad"], ["cartel", "pregunta"], ["proponer acciones peligrosas"],
           "Valora las acciones simples; recordar que la comunidad decide cómo protege su patrimonio."),
    reinforce="Recoge basura de tu patio con un adulto y cuéntalo.",
    extend="Pregunta a la comunidad qué cuidados necesita un lugar importante para ellos.",
)

L(
    OA15, 4,
    materials="Lápiz y hojas. Un modelo de ficha con espacios está escrito en el cuaderno.",
    use="Aprenderé a escribir una ficha de patrimonio que cuente lo permitido sin exponer información delicada.",
    prior=["Sé qué es patrimonio material e inmaterial.", "Sé qué es información privada."],
    explain=[
        "Una ficha patrimonial es un papel breve que presenta un elemento valioso. Debe decir su nombre, de qué comunidad es, de qué tipo es (material o inmaterial), por qué es importante y quién nos lo contó.",
        "Una ficha responsable no incluye información delicada: no dice dónde están exactamente los lugares sagrados, ni muestra objetos reservados, ni cuenta secretos. Tampoco usa datos personales de las personas, como direcciones.",
        "Antes de compartir una ficha, la mostramos a quien nos enseñó y a la comunidad para que la corrija si hace falta. Así aprendemos y devolvemos lo que recibimos. Si algo no se puede mostrar, dejamos un espacio vacío.",
    ],
    vocab=[("ficha", "papel breve con datos de algo"), ("procedencia", "de dónde y de quién viene"), ("sensible", "que puede dañar si se muestra"), ("autorizar", "dar permiso"), ("corregir", "cambiar lo que está mal")],
    worked=[
        W("Llenar una ficha", "Elemento: los moai. ¿Qué datos pones? ", ["Nombre: moai.", "Pueblo: rapa nui.", "Tipo: material. Importancia: figuras de piedra valoradas por la comunidad."], "Nombre, pueblo, tipo, importancia y fuente."),
        W("Dato delicado", "Alguien quiere escribir el lugar exacto de un sitio ceremonial. ¿Qué haces?", ["Es información sensible.", "No lo escribo.", "Dejo el espacio vacío."], "No lo escribo."),
    ],
    mistakes=[
        M("Escribir la ubicación exacta de un lugar sagrado.", "Puede dañarse si se difunde.", "Deja ese dato vacío."),
        M("Compartir la ficha sin mostrarla a quien enseñó.", "Puede tener errores o mostrar algo no permitido.", "Muéstrala primero."),
    ],
    R=[
        ex("Una ficha lleva nombre, pueblo, tipo, importancia y fuente. ¿Cuántos datos son?", "5", "Se cuentan cinco."),
        ex("¿Se escribe el lugar exacto de un sitio sagrado? Sí o No.", "No", "Es información sensible."),
        ex("La fuente dice quién nos contó. ¿Verdadero o falso?", "Verdadero", "Esa es la fuente."),
    ],
    C=[
        ex("¿Qué haces antes de compartir la ficha? A) la muestro a quien enseñó B) la publico", "A", "Así puede corregirla."),
        ex("Verdadero o falso: una ficha responsable cuenta secretos.", "Falso", "No incluye información delicada."),
        ex("Si un dato no se puede mostrar, ¿qué haces?", "Dejo el espacio vacío", "Así se protege el lugar."),
    ],
    A=[
        ex("Completa la ficha con los datos: Nombre: moai. Pueblo: ______. Tipo: material.", "rapa nui", "Los moai son del pueblo rapa nui."),
        ex("Marca lo que puede ir en la ficha: nombre, lugar exacto de un sitio sagrado, tipo, dirección de una casa.", "nombre y tipo", "Lo demás es sensible o privado."),
        ex("Ordena para hacer la ficha: 1) la muestro a quien enseñó 2) escribo los datos permitidos 3) la comparto.", "2, 1, 3", "Se escribe, se muestra y luego se comparte."),
    ],
    Z=[
        ex("Camila publicó una ficha con el lugar exacto de un sitio sagrado. ¿Qué error cometió?", "Expuso información sensible", "Debió dejar ese dato vacío."),
        ex("¿Por qué mostramos la ficha a quien nos enseñó?", "Para que la corrija y autorice", "Así se respeta su voz."),
    ],
    D=[
        ex("Una ficha tiene 5 espacios y 1 se deja vacío por ser sensible. ¿Cuántos se llenan?", "4", "5 − 1 = 4."),
        ex("Dos fichas del mismo elemento tienen datos distintos. ¿Qué haces?", "Pregunto a la comunidad", "Puede haber distintas voces."),
    ],
    context=[ex("Tu curso hace 3 fichas con 5 datos cada una. ¿Cuántos datos escriben en total?", "15", "Se suma 5 + 5 + 5 = 15.")],
    selfcheck=[ex("¿Qué datos lleva una ficha?", "Nombre, pueblo, tipo, importancia y fuente", "Son los básicos."), ex("¿Qué no se escribe?", "Información sensible o privada", "Así se protege el lugar."), ex("¿A quién muestro la ficha?", "A quien me enseñó", "Para que la corrija.")],
    task=T("Completa una ficha para uno de estos elementos, usando solo la ficha que lo describe. Moai: «" + F_RN + "» Cerámica diaguita: «" + F_DIA + "» Escribe: nombre, pueblo, tipo (material o inmaterial), por qué es valioso (según la ficha de la clase) y fuente («ficha del cuaderno»). Deja un espacio vacío con la frase «Lo que la comunidad decide no mostrar».",
           "Nombre: cerámica diaguita. Pueblo: diaguita. Tipo: material. Valor: hace cerámica con dibujos geométricos. Fuente: ficha del cuaderno. Lo que la comunidad decide no mostrar: (vacío).",
           ["completa los datos", "no incluye información delicada", "deja el espacio vacío"], ["ficha completa"], ["incluir ubicaciones exactas"],
           "Valora el espacio vacío; invitar a mostrar la ficha a la comunidad antes de compartirla."),
    reinforce="Completa una ficha con tres datos de un objeto de tu casa.",
    extend="Escribe una pregunta para que la comunidad te diga qué parte no se puede mostrar.",
)

# ============================================================ OA 16 · Ser humano, naturaleza y cosmos desde la ciencia indígena
L(
    OA16, 1,
    materials="Lápiz y hojas. Los datos para observar están escritos en el cuaderno. No mires directamente al Sol.",
    use="Aprenderé a observar patrones del cielo y de las estaciones, como lo han hecho las personas durante muchísimo tiempo.",
    prior=["Sé que hay día y noche.", "Sé que la Luna cambia de forma."],
    explain=[
        "Las personas han observado el cielo y la naturaleza durante muchísimo tiempo. Notaron patrones: cosas que se repiten. El Sol sale y se pone cada día, la Luna cambia de forma y vuelve a empezar en cerca de un mes, y las estaciones se repiten cada año.",
        "Los pueblos originarios han acumulado observaciones durante generaciones. Esas observaciones se guardan en relatos, en prácticas y en la memoria de los mayores. A este saber se le llama ciencia indígena o conocimiento indígena. Cada pueblo tiene el suyo.",
        "Para observar un patrón, anotamos lo que vemos, cuándo y cuántas veces se repite. Una regla de seguridad es no mirar nunca directamente el Sol, porque daña los ojos. Con la Luna y las estrellas podemos observar de noche, con un adulto.",
    ],
    vocab=[("patrón", "algo que se repite siempre igual"), ("observación", "mirar con atención y anotar"), ("evidencia acumulada", "muchas observaciones guardadas durante mucho tiempo"), ("estación", "tiempo del año: verano, otoño, invierno o primavera"), ("fase de la Luna", "forma que vemos de la Luna")],
    worked=[
        W("Reconocer un patrón", "El Sol sale por la mañana y se pone por la tarde, cada día. ¿Es un patrón?", ["Se repite siempre.", "Podemos anotarlo.", "Sí es un patrón."], "Sí."),
        W("Orden de la Luna", "Tabla de práctica: semana 1, Luna nueva; semana 2, cuarto creciente; semana 3, Luna llena; semana 4, cuarto menguante. ¿Qué viene después de la semana 4?", ["Se completa un ciclo.", "Vuelve a empezar.", "Sigue la Luna nueva."], "Luna nueva."),
    ],
    mistakes=[
        M("Mirar directamente al Sol para observarlo.", "Daña los ojos.", "Observa la sombra o el cielo sin mirar el Sol."),
        M("Decir un patrón sin haber mirado varias veces.", "Con una vez no se ve si se repite.", "Anota varios días."),
    ],
    R=[
        ex("Un patrón es algo que se repite. ¿Verdadero o falso?", "Verdadero", "Esa es la definición."),
        ex("¿Se puede mirar directamente al Sol? Sí o No.", "No", "Daña los ojos."),
        ex("Las estaciones son 4. ¿Verdadero o falso?", "Verdadero", "Verano, otoño, invierno y primavera."),
    ],
    C=[
        ex("¿Qué es una observación? A) mirar con atención y anotar B) adivinar", "A", "Observar es anotar lo que se ve."),
        ex("Verdadero o falso: la Luna tiene siempre la misma forma.", "Falso", "Cambia a lo largo del mes."),
        ex("¿Dónde se guardan las observaciones de los pueblos?", "En relatos, prácticas y la memoria de los mayores", "Se transmiten por generaciones."),
    ],
    A=[
        ex("Ordena las fases de práctica: 1) cuarto creciente 2) Luna nueva 3) Luna llena 4) cuarto menguante.", "2, 1, 3, 4", "Nueva, cuarto creciente, llena y cuarto menguante."),
        ex("Tabla de práctica: lunes sale el Sol, martes sale el Sol, miércoles sale el Sol. ¿Qué patrón ves?", "El Sol sale todos los días", "Se repite cada día."),
        ex("Tabla de práctica de días en junio: el día 1 dura 10 horas de luz y el día 30 dura 10 horas de luz. ¿Cambió mucho la luz en el mes?", "No", "Las duraciones son iguales."),
    ],
    Z=[
        ex("Pedro vio la Luna llena una noche y dice «siempre está llena». ¿Qué error comete?", "Observó solo una vez", "Debe observar varias noches."),
        ex("¿Por qué anotamos las observaciones?", "Para comparar y ver si algo se repite", "Sin anotar se olvida."),
    ],
    D=[
        ex("Tabla de práctica: en una semana contaste 5 noches con Luna visible y 2 sin Luna visible. ¿Cuántas noches fueron?", "7", "5 + 2 = 7."),
        ex("Una niña dice que su observación vale igual que la de un pueblo que observó durante generaciones. ¿Qué le dices?", "Que ambas valen, pero la acumulada tiene mucha más evidencia", "Muchas observaciones dan más seguridad."),
    ],
    context=[ex("Un niño anota que durante 2 semanas el Sol salió cada día. Si cada semana tiene 7 días, ¿cuántos días anotó?", "14", "Se suma 7 + 7 = 14 días.")],
    selfcheck=[ex("En la observación del cielo, ¿qué es un patrón?", "Algo que se repite", "Se repite siempre igual."), ex("¿Mirar al Sol está permitido?", "No", "Es muy peligroso."), ex("¿Qué es la evidencia acumulada?", "Muchas observaciones durante mucho tiempo", "Da mayor seguridad.")],
    task=T("Observa el cielo del día (sin mirar el Sol) durante 3 días y anota: hora, si hay nubes y cómo está la Luna si se ve. Si no puedes salir, usa estos datos de práctica: lunes, nubes; martes, sin nubes; miércoles, nubes. Escribe qué se repite y qué cambia. Escribe una pregunta para el educador tradicional sobre qué observa su comunidad.",
           "Lunes nubes, martes sin nubes, miércoles nubes. Se repite que hay cielo cada día. Cambia si hay nubes. Pregunta: ¿qué observan los mayores en el cielo?",
           ["anota lo que ve", "identifica qué se repite y qué cambia", "respeta la seguridad"], ["tabla de 3 días", "pregunta"], ["mirar el Sol directo"],
           "Valora la seguridad y la tabla; no completar con interpretaciones culturales sin fuente."),
    reinforce="Anota cómo está el cielo hoy y mañana.",
    extend="Pregunta a una persona mayor qué observa del cielo y cuándo.",
)

L(
    OA16, 2,
    materials="Lápiz y hojas. Casos de práctica sobre observación y decisión están escritos en el cuaderno.",
    use="Aprenderé cómo las observaciones de la naturaleza ayudan a tomar decisiones, como cuándo sembrar o cuándo guardar alimentos.",
    prior=["Sé qué es un patrón.", "Sé qué es sembrar."],
    explain=[
        "El conocimiento indígena no es solo una idea: se usa en la vida diaria. Cuando una comunidad observa la naturaleza, aprende cuándo sembrar, cuándo cosechar, cuándo moverse con los animales y cómo cuidar el agua. Este saber se prueba con la experiencia año tras año.",
        "Para decidir usan lo observado: el clima, las plantas, los animales y el cielo. Después de decidir, miran el resultado y aprenden: si salió bien, repiten; si salió mal, ajustan. Así el conocimiento mejora con el tiempo.",
        "Es importante recordar que cada pueblo tiene su territorio y su clima, y por eso sus decisiones son distintas. Lo que sirve en el altiplano puede no servir en la costa. Por eso preguntamos qué se hace en cada lugar y no generalizamos.",
    ],
    vocab=[("decisión", "elegir qué hacer"), ("experiencia", "lo aprendido de hacer algo muchas veces"), ("clima", "cómo suele estar el tiempo en un lugar"), ("ajustar", "cambiar un poco para mejorar"), ("cosechar", "recoger lo que se sembró")],
    worked=[
        W("Observar y decidir", "Caso de práctica: Ana nota que hace más frío cada mañana de otoño y decide guardar leña. ¿Qué observó y qué decidió?", ["Observó: más frío cada mañana.", "Decidió: guardar leña.", "Usó lo observado para decidir."], "Observó el frío y decidió guardar leña."),
        W("Aprender del resultado", "Caso de práctica: una familia sembró más temprano y las plantas se helaron. ¿Qué hará la próxima vez?", ["Mira el resultado.", "Ajusta la fecha.", "Siembra más tarde."], "Sembrará más tarde."),
    ],
    mistakes=[
        M("Pensar que lo que sirve en un lugar sirve en todos.", "Los climas son distintos.", "Pregunta qué se hace en cada lugar."),
        M("Decidir sin mirar los resultados anteriores.", "Se repiten errores.", "Aprende de la experiencia."),
    ],
    R=[
        ex("Caso de práctica: Ana nota frío y guarda leña. ¿Qué decidió?", "Guardar leña", "Fue su decisión."),
        ex("Cosechar es recoger lo que se sembró. ¿Verdadero o falso?", "Verdadero", "Esa es la definición."),
        ex("La experiencia es lo aprendido de hacer algo muchas veces. ¿Verdadero o falso?", "Verdadero", "Eso es experiencia."),
    ],
    C=[
        ex("¿Para qué se usa lo observado? A) para tomar decisiones B) para nada", "A", "Orienta qué hacer."),
        ex("Verdadero o falso: lo que sirve en el altiplano sirve igual en la costa.", "Falso", "Los lugares son distintos."),
        ex("¿Qué haces si una decisión salió mal?", "Ajusto la próxima vez", "Así se aprende."),
    ],
    A=[
        ex("Une la observación con la decisión (caso de práctica). 1) llueve mucho 2) hace mucho calor 3) hay heladas. a) regar más b) proteger las plantas del frío c) regar menos", "1-c, 2-a, 3-b", "Cada observación orienta una decisión."),
        ex("Ordena: 1) miro el resultado 2) observo 3) decido.", "2, 3, 1", "Observo, decido y reviso."),
        ex("Una familia sembró 12 semillas y brotaron 9. ¿Cuántas no brotaron?", "3", "12 − 9 = 3."),
    ],
    Z=[
        ex("Luz sembró igual que su vecino de otro lugar y no le resultó. ¿Qué pudo faltar?", "Mirar su propio clima", "Cada lugar es distinto."),
        ex("¿Por qué el conocimiento mejora con el tiempo?", "Porque se aprende de los resultados", "Cada intento enseña algo."),
    ],
    D=[
        ex("En 5 años, una familia anotó heladas en 3. ¿En cuántos años no hubo heladas?", "2", "5 − 3 = 2."),
        ex("Un libro dice que todos los pueblos siembran en septiembre. ¿Qué dudas tienes?", "Cada lugar y pueblo tiene sus tiempos", "No hay una fecha única."),
    ],
    context=[ex("Caso de práctica: una comunidad anota la lluvia de 4 semanas: 2, 0, 3 y 1 días con lluvia. ¿Cuántos días llovió en total?", "6", "2 + 0 + 3 + 1 = 6.")],
    selfcheck=[ex("¿Qué es la experiencia?", "Lo aprendido de hacer algo muchas veces", "Nos enseña a decidir."), ex("¿Una decisión depende del lugar?", "Sí", "El clima cambia."), ex("¿Qué haces con un resultado malo?", "Ajusto", "Así aprendo de los errores.")],
    task=T("Lee este caso de práctica: «Una familia observa que las lluvias llegan más tarde este año.» Escribe dos decisiones posibles, una observación que haría para decidir y a quién le preguntarías. No digas cuál es «la correcta».",
           "Decisiones: esperar más para sembrar o regar con cuidado. Observaría las nubes y la humedad. Preguntaría a los mayores.",
           ["relaciona observación y decisión", "no dice cuál es la única correcta", "pregunta a los mayores"], ["dos decisiones", "una observación", "una pregunta"], ["decir que hay una única respuesta"],
           "Valora el razonamiento; conversar con humildad sobre que cada comunidad decide con su experiencia."),
    reinforce="Observa el cielo antes de salir y decide qué ropa usar.",
    extend="Pregunta a un adulto qué observa antes de decidir algo en el huerto o en la casa.",
)

L(
    OA16, 3,
    materials="Lápiz y hojas. Casos de práctica están escritos en el cuaderno.",
    use="Aprenderé a distinguir un saber cultural de una indicación médica y a reconocer quién tiene la autoridad para cada cosa.",
    prior=["Sé que los médicos cuidan la salud.", "Sé que las comunidades tienen saberes."],
    explain=[
        "Los pueblos originarios tienen saberes sobre la naturaleza y también sobre cuidarse. Personas de la comunidad conocen y enseñan esos saberes. Pero un saber cultural no reemplaza a un médico ni a un adulto responsable cuando alguien está enfermo.",
        "Si alguien se siente mal, avisamos a un adulto y buscamos ayuda de salud. Nunca probamos plantas, remedios o preparados por nuestra cuenta. Algunas plantas son peligrosas, y solo personas que conocen y tienen permiso saben cómo usarlas.",
        "En la escuela aprendemos sobre estos saberes con respeto. Quien los enseña tiene la autoridad para hacerlo, y nosotros no los practicamos ni hacemos recomendaciones de salud. Aprendemos que existe un saber, quién lo guarda y por qué se valora.",
    ],
    vocab=[("autoridad", "persona que puede enseñar o decidir algo"), ("saber cultural", "conocimiento que guarda una comunidad"), ("indicación médica", "instrucción de un profesional de la salud"), ("peligroso", "que puede hacer daño"), ("adulto responsable", "persona mayor que cuida de un niño")],
    worked=[
        W("Si me siento mal", "Caso de práctica: Camila tiene dolor de guata. ¿Qué hace primero?", ["Avisa a un adulto.", "Busca ayuda de salud.", "No prueba plantas por su cuenta."], "Avisar a un adulto."),
        W("Quién enseña un saber", "Un compañero quiere enseñarte cómo preparar una planta que vio en un video. ¿Qué haces?", ["No sé si es seguro.", "Quien enseña debe ser una persona autorizada.", "No la pruebo."], "No la pruebo y aviso a un adulto."),
    ],
    mistakes=[
        M("Probar una planta o preparado por cuenta propia.", "Puede ser peligroso.", "Avisa a un adulto."),
        M("Creer que un saber cultural reemplaza a un médico.", "Cuando alguien está enfermo se busca ayuda de salud.", "Avisa a un adulto y busca ayuda."),
    ],
    R=[
        ex("Si te sientes mal, ¿qué haces? A) aviso a un adulto B) pruebo una planta", "A", "Los adultos buscan ayuda."),
        ex("¿Es seguro probar plantas por mi cuenta? Sí o No.", "No", "Pueden ser peligrosas."),
        ex("Un médico cuida la salud. ¿Verdadero o falso?", "Verdadero", "Es su tarea."),
    ],
    C=[
        ex("Verdadero o falso: un saber cultural reemplaza a un médico.", "Falso", "Cuando hay enfermedad se busca ayuda de salud."),
        ex("¿Quién puede enseñar un saber de una comunidad? A) quien tiene autoridad en la comunidad B) cualquiera que vio un video", "A", "Debe ser la persona autorizada."),
        ex("¿Qué aprendemos en la escuela sobre estos saberes?", "Que existen, quién los guarda y por qué se valoran", "No los practicamos."),
    ],
    A=[
        ex("Clasifica como SEGURO o NO SEGURO: a) avisar a un adulto si me duele algo b) probar una planta que no conozco c) lavarme las manos.", "a) seguro, b) no seguro, c) seguro", "Probar plantas desconocidas es peligroso."),
        ex("Une la situación con lo que haces. 1) tengo fiebre 2) un amigo me ofrece una planta 3) quiero saber un saber cultural. a) aviso a un adulto b) digo que no y aviso c) pregunto al educador tradicional", "1-a, 2-b, 3-c", "Cada situación pide una acción."),
        ex("Ordena si te sientes mal: 1) busco ayuda de salud 2) aviso a un adulto 3) espero indicaciones.", "2, 1, 3", "Primero aviso, luego se busca ayuda y se espera."),
    ],
    Z=[
        ex("Luis dice que una planta de su patio le sirve de remedio y se la ofrece a un compañero. ¿Qué error cometió?", "Dio una planta sin ser una persona autorizada", "No sabía si era seguro."),
        ex("¿Por qué no hacemos recomendaciones de salud en la escuela?", "Porque no somos profesionales de la salud", "Podríamos hacer daño."),
    ],
    D=[
        ex("Una persona mayor cuenta que en su comunidad usan ciertas plantas. ¿Debes probarlas? Sí o No.", "No", "Solo quien tiene autoridad sabe cómo."),
        ex("Un cartel dice «esta planta cura todo». ¿Qué haces?", "Dudo y pregunto a un adulto", "Es una afirmación peligrosa."),
    ],
    context=[ex("En un taller, un adulto explica que su comunidad cuida plantas medicinales. 12 niños escuchan y ninguno las prueba. ¿Cuántos niños probaron plantas?", "0", "Se aprende, no se prueba.")],
    selfcheck=[ex("¿Qué haces si te sientes mal?", "Aviso a un adulto", "Se busca ayuda."), ex("¿Pruebas plantas por tu cuenta?", "No", "Puede ser peligroso."), ex("¿Quién enseña un saber de su comunidad?", "Quien tiene autoridad", "Es la persona autorizada.")],
    task=T("Dibuja una tarjeta con tres reglas de seguridad: 1) avisar a un adulto si me siento mal, 2) no probar plantas ni preparados, 3) preguntar al educador tradicional qué saber se puede compartir en la escuela. Escribe una pregunta para el educador: ¿cómo cuida su comunidad la salud de las personas?",
           "Reglas: aviso a un adulto, no pruebo plantas, pregunto al educador. Pregunta: ¿cómo cuidan la salud en su comunidad?",
           ["distingue saber cultural e indicación médica", "incluye reglas de seguridad", "formula una pregunta"], ["tarjeta", "pregunta"], ["recomendar plantas"],
           "Revisa que no haya recomendaciones de salud; recordar que la autoridad es la comunidad y los profesionales de salud."),
    reinforce="Practica en voz alta qué dirías a un adulto si te sientes mal.",
    extend="Escribe una pregunta sobre quién guarda los saberes de salud en una comunidad.",
)

L(
    OA16, 4,
    materials="Lápiz, hojas y colores. Un esquema de tres círculos está dibujado en el cuaderno.",
    use="Aprenderé a explicar con respeto cómo se relacionan las personas, la naturaleza y el cosmos para algunos pueblos, diciendo la fuente.",
    prior=["Sé que el Sol, la Luna y las estrellas están en el cielo.", "Sé que las personas son parte de la naturaleza."],
    explain=[
        "Para muchos pueblos originarios, las personas, la naturaleza y el cosmos están relacionados. El cosmos es todo lo que existe: la Tierra, el Sol, la Luna y las estrellas. Una persona no vive separada, sino parte de un gran conjunto.",
        "Podemos dibujar tres círculos: uno para las personas, otro para la naturaleza y otro para el cosmos. Se tocan y se cruzan. Así mostramos la idea de relación. Pero esta es una forma simple de explicarlo y cada pueblo tiene su propia manera de contarlo.",
        "Al explicar, decimos «según…», nombramos al pueblo o la fuente y evitamos decir que todos piensan igual. Si no sabemos cómo lo explica un pueblo, preguntamos. Una explicación respetuosa es honesta sobre lo que sabe y lo que falta.",
    ],
    vocab=[("cosmos", "todo lo que existe: Tierra, Sol, Luna y estrellas"), ("relación", "conexión entre dos cosas"), ("persona", "ser humano"), ("conjunto", "todo formado por partes"), ("honesto", "que dice lo que sabe y lo que no")],
    worked=[
        W("Relacionar", "Las personas necesitan el Sol para tener luz y calor. ¿Qué relación hay entre persona y cosmos?", ["El Sol es parte del cosmos.", "Nos da luz y calor.", "Las personas dependen de él."], "Las personas dependen de la luz y el calor del Sol."),
        W("Citar la fuente", "Quieres decir que un pueblo ve a la Tierra como madre. ¿Qué escribes?", ["No digo «todos».", "Cito al pueblo o a la fuente.", "Escribo «Según la fuente, en los pueblos andinos se habla de la Pachamama»."], "«Según la fuente, en los pueblos andinos se habla de la Pachamama.»"),
    ],
    mistakes=[
        M("Decir «todos los pueblos creen lo mismo del cosmos».", "Cada pueblo tiene su manera.", "Di de qué pueblo o fuente hablas."),
        M("Explicar como si lo supiera todo.", "Hay mucho que no sabemos.", "Di lo que falta."),
    ],
    R=[
        ex("El cosmos es todo lo que existe: Tierra, Sol, Luna y estrellas. ¿Verdadero o falso?", "Verdadero", "Esa es la idea."),
        ex("¿El Sol da luz? Sí o No.", "Sí", "Da luz y calor."),
        ex("Persona, naturaleza y cosmos forman tres círculos. ¿Cuántos círculos son?", "3", "Se cuentan tres."),
    ],
    C=[
        ex("¿Qué se dice al explicar con respeto? A) «según la fuente…» B) «todos creen…»", "A", "Cita la fuente."),
        ex("Verdadero o falso: las personas viven separadas del cosmos.", "Falso", "Son parte de un conjunto."),
        ex("¿Qué haces si no sabes cómo lo explica un pueblo?", "Pregunto", "No se inventa."),
    ],
    A=[
        ex("Une cada elemento con su círculo. 1) el río 2) una niña 3) el Sol. a) persona b) naturaleza c) cosmos", "1-b, 2-a, 3-c", "Cada elemento va con su grupo."),
        ex("Marca las frases respetuosas: a) «Según la fuente, el pueblo ve…» b) «Todos los pueblos creen lo mismo» c) «No sé cómo lo explica ese pueblo; lo preguntaré».", "a y c", "La b generaliza."),
        ex("Ordena para explicar: 1) digo la fuente 2) dibujo los círculos 3) explico la relación.", "2, 3, 1", "Se dibuja, se explica y se cita."),
    ],
    Z=[
        ex("Beto dice que su dibujo de tres círculos es la única forma de entender el cosmos. ¿Qué error comete?", "Cada pueblo tiene su manera", "El dibujo es una forma simple."),
        ex("¿Por qué es mejor decir «según la fuente» que «es así»?", "Porque muestra de dónde viene el dato", "Eso es ser honesto."),
    ],
    D=[
        ex("Tres niños dibujan los círculos: dos con círculos que se cruzan y uno con círculos separados. ¿Cuántos mostraron relación?", "2", "Los que se cruzan."),
        ex("Un video dice «los indígenas adoran el Sol». ¿Qué cuidado tienes?", "Dudar y pedir una fuente de la comunidad", "Puede ser una generalización."),
    ],
    context=[ex("En tu esquema pones 2 elementos de persona, 3 de naturaleza y 2 de cosmos. ¿Cuántos elementos hay?", "7", "2 + 3 + 2 = 7.")],
    selfcheck=[ex("¿Qué es el cosmos?", "Todo lo que existe: Tierra, Sol, Luna y estrellas", "Es el conjunto."), ex("¿Se separan persona y naturaleza?", "No", "Ambas están relacionadas."), ex("¿Qué haces para explicar con respeto?", "Cito la fuente y no generalizo", "Eso es ser honesto.")],
    task=T("Dibuja tres círculos que se cruzan: personas, naturaleza y cosmos. Pon dentro de cada uno dos ejemplos (por ejemplo: niña y mayor; río y llama; Sol y Luna). Escribe una frase que explique la relación y empiece con «Según…». Escribe lo que no sabes.",
           "Personas: niña y mayor. Naturaleza: río y llama. Cosmos: Sol y Luna. Según lo que aprendimos en clase, las personas dependen de la luz del Sol y del agua. No sé cómo lo explica cada pueblo.",
           ["dibuja la relación", "cita la fuente", "dice lo que no sabe"], ["esquema", "frase"], ["generalizar a todos los pueblos"],
           "Valora la honestidad; invitar a preguntar a la comunidad cómo lo explica su pueblo."),
    reinforce="Nombra una cosa de persona, una de naturaleza y una del cosmos.",
    extend="Escribe una pregunta para el educador tradicional sobre cómo se cuenta en su pueblo la relación con el cielo.",
)

# ============================================================ OA 17 · Expresiones de arte del pueblo originario
L(
    OA17, 1,
    materials="Lápiz y hojas. Las fichas de obras de práctica están escritas en el cuaderno.",
    use="Aprenderé a reconocer quién hizo una obra de arte de un pueblo originario, de qué contexto viene y para qué sirve.",
    prior=["Sé qué es una obra de arte.", "Sé que las personas hacen objetos con las manos."],
    explain=[
        "Una obra puede ser un tejido, una cerámica, una escultura, un canto, un baile o un dibujo. Cada obra tiene una autoría: la persona, el grupo o la comunidad que la hizo. Reconocer la autoría es una forma de respeto.",
        "También tiene un contexto: dónde, cuándo y para qué se hizo. Por ejemplo, la cerámica del pueblo diaguita tiene dibujos geométricos y se hizo en los valles del Norte Chico. Un tejido puede servir para abrigar, para una fiesta o para ambas cosas.",
        "La función de una obra es para qué sirve: utilidad, belleza, memoria o ceremonia. Algunas obras tienen un sentido que solo la comunidad conoce. Por eso, antes de decir qué significa una obra, preguntamos a quien sabe, y no inventamos.",
    ],
    vocab=[("obra", "algo que una persona crea con arte"), ("autoría", "quién hizo la obra"), ("contexto", "dónde, cuándo y para qué se hizo"), ("función", "para qué sirve"), ("comunidad", "grupo que comparte un lugar y una cultura")],
    worked=[
        W("Reconocer autoría y función", "Ficha de práctica: «Una cerámica de los valles del Norte Chico, con dibujos geométricos, hecha por una artesana diaguita para guardar alimentos.» ¿Quién la hizo y para qué sirve?", ["Quién: una artesana diaguita.", "Contexto: valles del Norte Chico.", "Función: guardar alimentos."], "Una artesana diaguita; sirve para guardar alimentos."),
        W("No inventar el significado", "Ves un dibujo en un tejido y no sabes qué significa. ¿Qué haces?", ["No invento.", "Pregunto a la comunidad o al educador.", "Anoto la fuente."], "Pregunto a quien sabe."),
    ],
    mistakes=[
        M("Decir «eso lo hacen los indígenas» sin nombrar al pueblo ni a la persona.", "Se pierde la autoría.", "Nombra al pueblo y, si se sabe, a la persona."),
        M("Inventar el significado de un diseño.", "Puede ser falso o faltar al respeto.", "Pregunta a quien lo conoce."),
    ],
    R=[
        ex("La autoría dice quién hizo la obra. ¿Verdadero o falso?", "Verdadero", "Esa es la definición."),
        ex("Ficha de práctica: una cerámica para guardar alimentos. ¿Cuál es su función?", "Guardar alimentos", "Para eso sirve."),
        ex("El contexto dice dónde, cuándo y para qué se hizo. ¿Verdadero o falso?", "Verdadero", "Eso significa contexto."),
    ],
    C=[
        ex("¿Qué es una obra? A) algo que alguien crea con arte B) una piedra del camino", "A", "Es una creación."),
        ex("Verdadero o falso: puedo inventar el significado de un diseño.", "Falso", "Siempre debo preguntar."),
        ex("¿Por qué reconocer la autoría?", "Para respetar a quien la hizo", "Cada obra tiene su autor o autora."),
    ],
    A=[
        ex("Une la obra con su función. 1) un tejido de lana 2) una cerámica 3) un canto. a) abrigar b) guardar alimentos c) contar historias", "1-a, 2-b, 3-c", "Cada obra sirve para algo."),
        ex("Ficha de práctica: «Cerámica con dibujos geométricos de los valles del Norte Chico.» ¿De qué pueblo es, según el cuaderno?", "Del pueblo diaguita", "La ficha diaguita lo dice."),
        ex("Ordena para presentar una obra: 1) la función 2) quién la hizo 3) el contexto.", "2, 3, 1", "Quién, dónde y para qué."),
    ],
    Z=[
        ex("Ana dice «esta obra es de los indígenas». ¿Qué le falta?", "Nombrar el pueblo y la persona", "Sin autoría no se respeta."),
        ex("¿Por qué preguntamos antes de decir qué significa una obra?", "Porque el sentido lo sabe la comunidad", "No se inventa."),
    ],
    D=[
        ex("Una niña ve dos tejidos con los mismos dibujos pero de lugares distintos. ¿Significan lo mismo? Sí o No.", "No necesariamente", "Cada comunidad tiene su sentido."),
        ex("En un museo hay 6 cerámicas y 4 tejidos. ¿Cuántas obras hay?", "10", "6 + 4 = 10."),
    ],
    context=[ex("Ficha de práctica: «Un telar de una familia mapuche». Escribe qué dato de autoría tiene la ficha.", "Una familia mapuche", "Nombra a quién lo hizo.")],
    selfcheck=[ex("¿Qué es la autoría?", "Quién hizo la obra", "Respeta a su creador."), ex("¿Qué es la función?", "Para qué sirve", "Es su uso."), ex("¿Se inventa el significado?", "No", "Se pregunta a quien sabe.")],
    task=T("Elige una ficha de práctica: a) cerámica con dibujos geométricos de los valles del Norte Chico (pueblo diaguita); b) tejido de lana del altiplano (pueblo aymara); c) escultura de piedra de una isla del Pacífico (pueblo rapa nui). Completa: autoría (pueblo), contexto (lugar), función (para qué sirve) y una pregunta para la comunidad sobre su sentido.",
           "Elegí a). Autoría: pueblo diaguita. Contexto: valles del Norte Chico. Función: guardar o servir alimentos. Pregunta: ¿qué cuentan los dibujos?",
           ["nombra el pueblo", "dice contexto y función", "no inventa el sentido"], ["ficha completa", "pregunta"], ["inventar el sentido"],
           "Valora la pregunta; no dar significados que no vengan de la comunidad."),
    reinforce="Mira un objeto de tu casa y di quién lo hizo y para qué sirve.",
    extend="Escribe una pregunta para un artesano sobre quién le enseñó a hacer su obra.",
)

L(
    OA17, 2,
    materials="Hojas, lápices y colores. Los materiales y permisos están escritos en el cuaderno.",
    use="Aprenderé qué materiales y técnicas usan algunas obras y qué parte puedo explorar yo con respeto.",
    prior=["Sé dibujar líneas y figuras.", "Sé qué es un material."],
    explain=[
        "Las obras se hacen con materiales: lana, arcilla, piedra, madera, fibras o metales. Y con técnicas: hilar, tejer, modelar, tallar. La técnica es la manera de trabajar el material.",
        "Algunas técnicas son muy especiales y las enseña la comunidad. Otras, más simples, las podemos explorar nosotros sin tocar lo reservado. Por ejemplo, podemos hacer un dibujo de líneas y triángulos inspirado en una cerámica, pero sin copiar diseños que no nos corresponde copiar.",
        "Antes de trabajar, preguntamos: ¿qué se puede explorar?, ¿qué no? Y siempre decimos que es una obra «inspirada en» y no «del pueblo». Así aprendemos y cuidamos la autoría.",
    ],
    vocab=[("material", "lo que se usa para hacer algo"), ("técnica", "manera de trabajar un material"), ("tallar", "darle forma a la piedra o la madera quitando partes"), ("inspirado en", "que toma una idea, pero no copia"), ("explorar", "probar para aprender")],
    worked=[
        W("Material y técnica", "Un tejido de lana. ¿Cuál es el material y cuál la técnica?", ["Material: lana.", "Técnica: tejer.", "La técnica es cómo se trabaja."], "Material: lana; técnica: tejer."),
        W("Explorar con permiso", "Quieres hacer una cerámica de arcilla como la diaguita. ¿Qué haces primero?", ["Pregunto qué puedo explorar.", "Hago un diseño propio con líneas y triángulos.", "Digo «inspirado en»."], "Pregunto y hago un diseño propio, inspirado en."),
    ],
    mistakes=[
        M("Copiar un diseño de una comunidad sin permiso.", "Puede tener un sentido que no nos corresponde.", "Crea un diseño propio, inspirado en."),
        M("Decir «este es un diseño del pueblo» de lo que hiciste tú.", "No lo es.", "Di «inspirado en»."),
    ],
    R=[
        ex("La técnica es la manera de trabajar un material. ¿Verdadero o falso?", "Verdadero", "Eso significa técnica."),
        ex("¿La lana es un material? Sí o No.", "Sí", "Se usa para tejer."),
        ex("Tallar es darle forma a la piedra o la madera. ¿Verdadero o falso?", "Verdadero", "Esa es la técnica."),
    ],
    C=[
        ex("¿Qué dices de tu obra? A) «inspirada en…» B) «es del pueblo»", "A", "No es del pueblo."),
        ex("Verdadero o falso: puedo copiar cualquier diseño que vea.", "Falso", "Algunos tienen un sentido reservado."),
        ex("¿Qué haces antes de explorar una técnica?", "Pregunto qué se puede explorar", "Se pide orientación."),
    ],
    A=[
        ex("Une material y técnica. 1) arcilla 2) lana 3) piedra. a) tejer b) modelar c) tallar", "1-b, 2-a, 3-c", "Cada material tiene su técnica."),
        ex("Marca lo que puedes explorar con respeto: a) hacer un diseño propio de líneas b) copiar un diseño reservado c) modelar plastilina.", "a y c", "La b no corresponde."),
        ex("Ordena: 1) hago mi obra 2) pregunto qué puedo explorar 3) escribo «inspirado en».", "2, 1, 3", "Pregunto, hago y escribo."),
    ],
    Z=[
        ex("Luis copió un diseño de un tejido y dice que es del pueblo. ¿Qué dos errores cometió?", "Copió sin permiso y le puso mal la autoría", "Debió crear algo propio y decir «inspirado en»."),
        ex("¿Por qué la técnica especial la enseña la comunidad?", "Porque es un saber que ella cuida", "Tiene un valor cultural."),
    ],
    D=[
        ex("Una niña hace 3 dibujos con triángulos y 2 con líneas. ¿Cuántos dibujos hace?", "5", "3 + 2 = 5."),
        ex("Un compañero quiere usar un símbolo que vio en un tejido sin saber qué significa. ¿Qué le dices?", "Que pregunte antes y use algo propio", "No sabemos su sentido."),
    ],
    context=[ex("Para un taller, cada niño recibe 3 plastilinas. Si hay 2 niños, ¿cuántas plastilinas se necesitan?", "6", "Se suma 3 + 3 = 6.")],
    selfcheck=[ex("¿Qué es la técnica?", "La manera de trabajar un material", "Es el cómo."), ex("¿Qué escribo en mi obra?", "Inspirada en…", "No es del pueblo."), ex("¿Copio diseños reservados?", "No", "Así se respeta.")],
    task=T("Con lápiz y colores, crea un diseño propio de líneas, triángulos y puntos. Escribe: material (lápiz y papel), técnica (dibujar) y la frase «Obra inspirada en la cerámica de los valles del Norte Chico; no es una obra del pueblo». Escribe una pregunta para la comunidad: ¿qué puedo explorar con respeto?",
           "Material: lápiz y papel. Técnica: dibujar. Obra inspirada en la cerámica de los valles del Norte Chico; no es una obra del pueblo. Pregunta: ¿qué diseños no debo copiar?",
           ["crea un diseño propio", "dice material y técnica", "escribe «inspirada en»"], ["dibujo", "frase", "pregunta"], ["copiar un diseño reservado"],
           "Valora lo propio de su diseño; recordar que no se imitan diseños reservados y que la comunidad enseña los que sí."),
    reinforce="Dibuja un diseño con tres triángulos y dos líneas.",
    extend="Pregunta a un artesano o artesana qué le gustaría que los niños aprendieran de su trabajo.",
)

L(
    OA17, 3,
    materials="Hojas y lápices. Casos de práctica están escritos en el cuaderno.",
    use="Aprenderé a distinguir qué decisiones de una obra son culturales y cuáles personales, y qué es aprender y qué es apropiarse.",
    prior=["Sé que cada persona elige colores y formas.", "Sé qué es una obra."],
    explain=[
        "En una obra de un pueblo hay decisiones culturales y decisiones personales. Las culturales vienen de la comunidad: ciertos diseños, técnicas o sentidos. Las personales son las elecciones de quien crea: un color, una forma, un tamaño.",
        "Aprender de una obra es mirarla, preguntar, entender su contexto y crear algo propio inspirado en ella. Apropiarse es copiar un diseño o símbolo y usarlo como si fuera nuestro, o venderlo, sin permiso de la comunidad.",
        "Para cuidar lo ajeno, nos preguntamos: ¿pedí permiso?, ¿copié o me inspiré?, ¿dije quién es el autor o la autora? Si respondemos con respeto a estas preguntas, estamos aprendiendo y no apropiándonos.",
    ],
    vocab=[("decisión cultural", "elección que viene de la comunidad"), ("decisión personal", "elección de quien crea"), ("apropiación", "usar algo ajeno como propio sin permiso"), ("inspirarse", "tomar una idea para crear algo propio"), ("permiso", "autorización de quien corresponde")],
    worked=[
        W("Cultural o personal", "Eliges rojo para tu dibujo porque te gusta. ¿Es una decisión cultural o personal?", ["La elegí yo por gusto.", "No viene de una comunidad.", "Es personal."], "Personal."),
        W("Aprender o apropiarse", "Copias un símbolo de un tejido y lo pones en una polera para vender. ¿Aprendes o te apropias?", ["Copié.", "No pedí permiso.", "Vendo sin ser mi obra."], "Me apropio."),
    ],
    mistakes=[
        M("Pensar que copiar es una forma de respetar.", "Copiar sin permiso es apropiarse.", "Inspírate y crea algo propio."),
        M("Vender algo con un símbolo de un pueblo sin permiso.", "No es nuestro.", "Pregunta y no lo uses."),
    ],
    R=[
        ex("Elegir mi color favorito, ¿es decisión cultural o personal?", "Personal", "La elijo yo."),
        ex("Apropiarse es usar algo ajeno como propio sin permiso. ¿Verdadero o falso?", "Verdadero", "Esa es la definición."),
        ex("Inspirarse es tomar una idea y crear algo propio. ¿Verdadero o falso?", "Verdadero", "Eso es inspirarse."),
    ],
    C=[
        ex("¿Qué es aprender? A) mirar, preguntar y crear algo propio B) copiar y vender", "A", "Así se respeta."),
        ex("Verdadero o falso: copiar un símbolo sin permiso es respeto.", "Falso", "Eso es apropiación."),
        ex("¿Qué preguntas haces para no apropiarte?", "¿Pedí permiso? ¿Copié o me inspiré? ¿Dije quién es el autor?", "Cuidan la autoría."),
    ],
    A=[
        ex("Clasifica como APRENDER o APROPIARSE: a) pedir permiso b) copiar y vender c) crear algo propio.", "a) aprender, b) apropiarse, c) aprender", "Copiar y vender es apropiación."),
        ex("Une la decisión con su tipo. 1) forma de un diseño ancestral de una comunidad 2) tamaño de mi dibujo. a) cultural b) personal", "1-a, 2-b", "Una viene de la comunidad y la otra la decido yo."),
        ex("Ordena para crear con respeto: 1) pido permiso 2) me inspiro 3) escribo quién es el autor.", "1, 2, 3", "Permiso, inspiración y autoría."),
    ],
    Z=[
        ex("Camila imprimió un símbolo de un tejido en sus cuadernos para vender. ¿Qué cuidado le faltó?", "Pedir permiso a la comunidad", "Eso es apropiación."),
        ex("¿Por qué las decisiones culturales no se cambian a gusto?", "Porque tienen sentido para la comunidad", "No son personales."),
    ],
    D=[
        ex("Un niño dibuja 4 diseños propios y copia 1 de un tejido. ¿Cuántos son propios?", "4", "Solo los que creó."),
        ex("Una persona de la comunidad te autoriza a usar un diseño en tu escuela, pero no para vender. ¿Puedes venderlo? Sí o No.", "No", "El permiso fue limitado."),
    ],
    context=[ex("En una exposición escolar hay 5 obras inspiradas en la cerámica y 1 copia con el sello de una comunidad. ¿Cuántas son inspiradas?", "5", "La copia no lo es.")],
    selfcheck=[ex("¿Qué es la apropiación?", "Usar algo ajeno como propio sin permiso", "No respeta a nadie."), ex("¿Qué es inspirarse?", "Tomar una idea y crear algo propio", "Así se aprende."), ex("¿Qué pido antes de usar un diseño?", "Permiso", "A la comunidad.")],
    task=T("Lee los tres casos y escribe APRENDER o APROPIARSE con una razón: a) una niña dibuja un diseño propio inspirado en una cerámica y dice quién la inspiró; b) un niño copia un símbolo de un tejido y lo vende; c) una niña pregunta qué puede dibujar y crea algo suyo. Escribe una pregunta para la comunidad sobre qué puedes usar.",
           "a) aprender, porque crea algo propio y cita. b) apropiarse, porque copia y vende sin permiso. c) aprender, porque pregunta y crea algo suyo.",
           ["clasifica bien", "da razones", "formula una pregunta"], ["tres respuestas", "pregunta"], ["decir que copiar es respeto"],
           "Valora las razones; la pregunta sobre qué puede usar debe ir a la comunidad."),
    reinforce="Inventa un diseño tuyo y escribe «inspirado en».",
    extend="Escribe una frase para agradecer a quien te enseñó algo de su arte.",
)

L(
    OA17, 4,
    materials="Hojas, lápices y colores. Un modelo de ficha de obra está escrito en el cuaderno.",
    use="Aprenderé a crear una obra propia inspirada en lo que aprendí y a explicarla sin imitar lo reservado.",
    prior=["Sé dibujar y explicar mi dibujo.", "Sé qué es inspirarse."],
    explain=[
        "Una respuesta artística cuidada es una obra que tú creas después de aprender de una expresión de arte de un pueblo. No es una copia. Usa tus propias ideas, y puede usar formas simples como líneas, puntos y triángulos.",
        "Para cuidar lo ajeno, evitamos los símbolos y diseños que pertenecen a una comunidad o que tienen un sentido reservado. Preguntamos al educador tradicional qué podemos usar. Si no lo sabemos, elegimos formas generales y propias.",
        "Al terminar, escribimos una ficha: título, materiales, técnica, qué nos inspiró y de quién aprendimos. Decimos «obra inspirada en…» y agradecemos a quien nos enseñó. Así mostramos respeto y aprendizaje.",
    ],
    vocab=[("respuesta artística", "obra que creo después de aprender"), ("título", "nombre de una obra"), ("inspiración", "idea de la que parte una obra"), ("agradecimiento", "decir gracias por lo recibido"), ("ficha de obra", "papel breve que explica la obra")],
    worked=[
        W("Escribir una ficha", "Hiciste un dibujo de líneas y triángulos con lápices. ¿Qué datos pones en la ficha?", ["Título: «Valles de colores».", "Materiales y técnica: lápices, dibujar.", "Inspiración y agradecimiento."], "Título, materiales, técnica, inspiración y agradecimiento."),
        W("Elegir formas propias", "No sabes si un símbolo se puede usar. ¿Qué haces?", ["No lo uso.", "Pregunto al educador tradicional.", "Uso formas simples y propias."], "No lo uso y pregunto."),
    ],
    mistakes=[
        M("Usar un símbolo reservado para que se vea «auténtico».", "No te corresponde y puede ser irrespetuoso.", "Crea con formas propias."),
        M("No decir quién te inspiró.", "Se pierde el reconocimiento.", "Escribe «inspirado en» y agradece."),
    ],
    R=[
        ex("Una ficha de obra lleva título, materiales, técnica, inspiración y agradecimiento. ¿Cuántos datos son?", "5", "Se cuentan cinco."),
        ex("¿Una obra inspirada es una copia? Sí o No.", "No", "Es algo propio."),
        ex("Agradecer es decir gracias. ¿Verdadero o falso?", "Verdadero", "Eso es agradecimiento."),
    ],
    C=[
        ex("¿Qué usas para crear con respeto? A) formas propias y simples B) símbolos reservados", "A", "No te corresponden los reservados."),
        ex("Verdadero o falso: la ficha dice de quién aprendiste.", "Verdadero", "Reconoce la inspiración."),
        ex("¿Qué haces si no sabes si puedes usar un símbolo?", "Pregunto y no lo uso", "Se evita el riesgo."),
    ],
    A=[
        ex("Escribe un título posible para un dibujo de montañas con triángulos y colores.", "Respuesta aceptable: «Montañas de colores»", "El título nombra lo que se ve."),
        ex("Marca lo que va en la ficha: título, símbolo reservado copiado, técnica, agradecimiento.", "título, técnica y agradecimiento", "No se copia lo reservado."),
        ex("Ordena para terminar tu obra: 1) escribo la ficha 2) hago mi dibujo 3) agradezco.", "2, 1, 3", "Dibujo, ficha y agradecimiento."),
    ],
    Z=[
        ex("Pedro dice que su obra se ve más real si usa un símbolo copiado. ¿Qué le dices?", "Que cree con formas propias y pregunte antes", "Lo reservado no se usa."),
        ex("¿Por qué agradecemos a quien nos enseñó?", "Porque nos compartió su saber", "Es una forma de respeto."),
    ],
    D=[
        ex("En una muestra hay 8 obras propias y 2 con símbolos reservados que se retiran. ¿Cuántas quedan?", "8", "Se retiran las 2 con símbolos reservados."),
        ex("Una niña usa solo líneas y puntos y escribe «inspirada en un tejido que vimos». ¿Es una respuesta cuidada? Sí o No.", "Sí", "Es propia y reconoce la inspiración."),
    ],
    context=[ex("Tu curso hará una muestra con 10 dibujos. Si 6 están terminados, ¿cuántos faltan?", "4", "10 − 6 = 4.")],
    selfcheck=[ex("¿Qué es una respuesta artística cuidada?", "Una obra propia inspirada en lo aprendido", "Es propia y no copia."), ex("¿Qué escribo en la ficha?", "Título, materiales, técnica, inspiración y agradecimiento", "Son los datos."), ex("¿Uso símbolos reservados?", "No", "No me corresponden.")],
    task=T("Crea un dibujo o un collage con papeles de colores, usando solo líneas, puntos y triángulos. Escribe su ficha: título, materiales, técnica, «obra inspirada en…» (por ejemplo, la cerámica de los valles del Norte Chico, el tejido de lana del altiplano o las figuras de piedra de una isla del Pacífico) y una frase de agradecimiento a quien te enseñó. Pregunta al educador tradicional si hay algo que no deberías copiar.",
           "Título: «Valles de colores». Materiales: papel de colores. Técnica: collage. Obra inspirada en la cerámica de los valles del Norte Chico. Gracias a mi profesora por enseñarme.",
           ["crea algo propio", "escribe la ficha completa", "agradece"], ["obra", "ficha"], ["copiar símbolos reservados"],
           "Valora lo propio de la obra y la ficha; revisa que no haya símbolos reservados; invitar a mostrar la obra a la comunidad."),
    reinforce="Pon un título a un dibujo tuyo y escribe de qué te inspiraste.",
    extend="Prepara una frase de agradecimiento para una persona de la comunidad que te enseñó algo.",
)
