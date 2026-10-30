"""Material del estudiante de 2.º básico, Historia, Geografía y Ciencias Sociales: OA 03 (aportes y sociedad mestiza) y OA 04 (aportes de inmigrantes)."""
from __future__ import annotations

from student_lessons import ex, register


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


OA3, OA4 = "HI02 OA 03", "HI02 OA 04"

# ================================================================ OA 03
PAL = ("Ficha de palabras (dada por la clase): cancha, choclo, palta, poroto y guagua vienen del quechua, una lengua andina. Copihue y pehuén vienen del mapuzugun, el idioma mapuche. "
       "Ventana y mesa vienen del castellano, el idioma que llegó con los españoles. Charquicán: la ficha no dice su origen, así que no lo inventamos.")
register(
    OA3, 1,
    materials="Lápiz y papel. La ficha de palabras está escrita en cada ejercicio.",
    use="Aprenderé que muchas palabras que usamos vienen de lenguas indígenas y del castellano. Sirve para ver qué aportó cada pueblo a nuestra forma de hablar.",
    prior=["Sé que Chile tiene pueblos originarios.", "Sé que los españoles llegaron a Chile."],
    explain=[
        "En Chile hablamos castellano, un idioma que llegó con los españoles. Pero usamos también muchas palabras que vienen de lenguas de los pueblos originarios. Así, nuestro modo de hablar es una mezcla.",
        "Cancha, choclo, palta, poroto y guagua vienen del quechua. Copihue y pehuén vienen del mapuzugun. Copihue es una flor y pehuén es el nombre de un árbol, la araucaria. Cuando hablas de una palta o un choclo, usas palabras que vienen de pueblos originarios.",
        "Para saber el origen de una palabra necesitamos una fuente. No debemos inventar su historia. Si una ficha no dice de dónde viene una palabra, como charquicán, escribimos «aún no sabemos» y buscamos más información.",
    ],
    vocab=[("aporte", "algo que una persona o un pueblo entrega a la sociedad"), ("quechua", "lengua de los pueblos andinos"), ("mapuzugun", "idioma del pueblo mapuche"), ("castellano", "idioma que llegó con los españoles"), ("origen", "lugar o pueblo de donde viene algo")],
    worked=[
        {"title": "Buscar un origen", "problem": f"{PAL} ¿De qué lengua viene la palabra palta?", "steps": ["Busco palta en la ficha.", "Aparece junto a cancha, choclo, poroto y guagua: del quechua."], "answer": "Del quechua"},
        {"title": "No inventar", "problem": f"{PAL} ¿Qué escribimos sobre el origen de charquicán?", "steps": ["Reviso la ficha.", "La ficha dice que no da su origen."], "answer": "Que aún no sabemos y buscamos una fuente"},
    ],
    mistakes=[
        {"wrong": "Decir que todas las palabras de Chile vienen del castellano.", "why": "Se olvida que usamos palabras de lenguas indígenas.", "fix": "Revisa la ficha: hay palabras del quechua y del mapuzugun."},
        {"wrong": "Inventar de dónde viene una palabra.", "why": "Parece fácil adivinar un origen.", "fix": "Si la ficha no lo dice, escribe «aún no sabemos»."},
    ],
    tiers={
        "recovery": [
            ex(f"{PAL} ¿De qué lengua viene la palabra choclo?", "del quechua", "La ficha lo indica."),
            ex(f"{PAL} ¿De qué idioma viene la palabra copihue?", "del mapuzugun", "La ficha lo indica."),
            ex(f"{PAL} ¿Qué es el pehuén: una flor o un árbol?", "un árbol, la araucaria", "La ficha lo explica."),
        ],
        "understand": [
            ex("¿Qué idioma llegó con los españoles?", "el castellano", "Así lo explica la clase."),
            ex(f"{PAL} Nombra tres palabras que vienen del quechua.", "cancha, choclo y palta (o poroto, guagua)", "Son palabras de la ficha."),
            ex("¿Por qué decimos que nuestro modo de hablar es una mezcla?", "Porque usamos palabras de lenguas indígenas y del castellano", "Se juntan varios orígenes."),
        ],
        "apply": [
            ex(f"{PAL} Clasifica la palabra poroto: ¿quechua, mapuzugun o castellano?", "quechua", "La ficha la nombra entre las del quechua."),
            ex(f"{PAL} Clasifica la palabra ventana: ¿quechua, mapuzugun o castellano?", "castellano", "La ficha dice que viene del castellano."),
            ex(f"{PAL} Une: 1) guagua, 2) copihue, 3) mesa. A) castellano, B) quechua, C) mapuzugun.", "1 con B; 2 con C; 3 con A", "Cada palabra se une con su lengua según la ficha."),
        ],
        "reason": [
            ex("Un compañero dice: «Charquicán viene del mapuzugun». ¿Qué le preguntas?", "¿En qué fuente lo viste?", "La ficha no dice su origen, así que necesita una fuente."),
            ex("Valentina dice: «Si una palabra viene del quechua, no es chilena». ¿Qué respondes?", "Es chilena porque la usamos aquí, aunque tenga ese origen", "Muchas palabras de origen indígena son parte del español de Chile."),
        ],
        "challenge": [
            ex(f"{PAL} Escribe una oración con una palabra del quechua y otra del mapuzugun.", "Mi abuela me regaló un copihue y comimos choclo", "Debe incluir una palabra de cada lengua."),
            ex("¿Por qué conviene decir «aún no sabemos» antes que adivinar un origen?", "Porque una idea sin fuente puede ser falsa", "Una fuente da seguridad."),
        ],
    },
    context=[ex("Un niño pide palta para el pan, otro pide pan con choclo cocido y su abuela le dice que mire el copihue. ¿Cuántas palabras de la ficha de origen indígena usaron?", "3", "Palta, choclo y copihue son tres palabras de origen indígena.")],
    selfcheck=[
        ex(f"{PAL} ¿De qué lengua viene guagua?", "del quechua", "La ficha lo indica."),
        ex("¿Qué es el mapuzugun?", "el idioma del pueblo mapuche", "Así se llama su lengua."),
        ex(f"{PAL} ¿Qué decimos del origen de charquicán?", "aún no sabemos", "La ficha no lo dice."),
    ],
    open_task=task(
        f"Haz una tabla con tres columnas: quechua, mapuzugun, castellano. Escribe en cada columna las palabras de la ficha que corresponden. {PAL} Agrega una frase con una palabra de cada columna.",
        "Quechua: cancha, choclo, palta, poroto, guagua. Mapuzugun: copihue, pehuén. Castellano: ventana, mesa. Frase: En la cancha hay un copihue junto a la ventana.",
        ["tres columnas", "palabras bien ubicadas", "una frase con tres palabras"], ["tabla escrita"], ["poner charquicán con un origen inventado", "mezclar columnas"],
        "Pide que explique cómo supo cada origen. Debe decir que lo tomó de la ficha."),
    reinforce="Escribe tres alimentos de tu casa cuyos nombres sean palabras de la ficha.",
    extend="Averigua con un adulto una palabra que use tu familia y pregunta si saben de dónde viene.",
)

ALI = ("Ficha de alimentos (dada por la clase): de América vienen la papa, el maíz, los porotos y el zapallo. De Europa llegaron con los españoles el trigo, la cebolla, el ajo, la gallina y la vaca. "
       "El pan amasado se hace con trigo, que llegó de Europa, en hornos de barro. Las humitas se hacen con choclo, un alimento de América.")
register(
    OA3, 2,
    materials="Lápiz y papel. La ficha de alimentos está escrita en cada ejercicio.",
    use="Aprenderé que algunos alimentos vienen de América y otros llegaron de Europa, y que hoy los cocinamos juntos. Sirve para entender nuestra comida como una mezcla.",
    prior=["Sé qué es un aporte.", "Sé que los españoles llegaron a Chile."],
    explain=[
        "Un alimento tiene tres partes que podemos mirar: el producto, que es el ingrediente; la preparación, que es la forma de cocinarlo; y el intercambio cultural, que es cuando dos pueblos comparten algo. Esto nos ayuda a entender de dónde viene nuestra comida.",
        "De América vienen la papa, el maíz, los porotos y el zapallo. De Europa llegaron con los españoles el trigo, la cebolla, el ajo, la gallina y la vaca. Por eso el pan amasado usa trigo, que llegó de Europa, y se hace en hornos de barro. Las humitas usan choclo, un alimento de América.",
        "Un plato completo casi nunca tiene un solo origen. Por ejemplo, un plato con papa y cebolla junta un producto de América con uno de Europa. Por eso no decimos «este plato es solo indígena» ni «este plato es solo español». Hablamos de productos y de formas de preparar.",
    ],
    vocab=[("producto", "ingrediente o alimento"), ("preparación", "forma de cocinar un alimento"), ("intercambio", "cuando dos grupos comparten algo"), ("origen", "lugar de donde viene algo"), ("ingrediente", "alimento que se usa para hacer una comida")],
    worked=[
        {"title": "Origen de un producto", "problem": f"{ALI} ¿De dónde viene la papa?", "steps": ["Busco papa en la ficha.", "Está en la lista de lo que viene de América."], "answer": "De América"},
        {"title": "Producto y preparación", "problem": f"{ALI} En el pan amasado, ¿cuál es el producto y cuál la preparación?", "steps": ["El producto es el trigo, que llegó de Europa.", "La preparación es hacerlo y cocerlo en horno de barro."], "answer": "Producto: trigo; preparación: horno de barro"},
    ],
    mistakes=[
        {"wrong": "Decir que un plato completo tiene un solo origen.", "why": "Se mira solo un ingrediente.", "fix": "Mira cada ingrediente y cada forma de cocinar por separado."},
        {"wrong": "Pensar que el trigo siempre estuvo en América.", "why": "Se olvida que llegó con los españoles.", "fix": "La ficha dice que el trigo llegó de Europa."},
    ],
    tiers={
        "recovery": [
            ex(f"{ALI} ¿De dónde vienen los porotos?", "de América", "La ficha lo indica."),
            ex(f"{ALI} ¿De dónde llegó el trigo?", "de Europa", "La ficha lo indica."),
            ex("Un producto, ¿es un ingrediente o una forma de cocinar?", "un ingrediente", "Producto es lo que se cocina."),
        ],
        "understand": [
            ex(f"{ALI} ¿Con qué se hacen las humitas?", "con choclo", "La ficha lo dice."),
            ex("¿Qué es una preparación?", "la forma de cocinar un alimento", "Es el modo de hacer la comida."),
            ex(f"{ALI} ¿En qué se hace el pan amasado?", "en hornos de barro", "La ficha lo explica."),
        ],
        "apply": [
            ex(f"{ALI} Clasifica en América o Europa: el zapallo.", "América", "La ficha lo pone entre los de América."),
            ex(f"{ALI} Clasifica en América o Europa: la cebolla.", "Europa", "La ficha dice que llegó con los españoles."),
            ex(f"{ALI} Une: 1) gallina, 2) maíz. A) de América, B) de Europa.", "1 con B; 2 con A", "La gallina llegó con los españoles y el maíz es de América."),
        ],
        "reason": [
            ex(f"{ALI} Un plato lleva papa y cebolla. ¿Tiene un solo origen? Explica.", "No; la papa es de América y la cebolla es de Europa", "Cada producto tiene su origen."),
            ex(f"{ALI} Sofía dice: «Las humitas son un plato español». Usa la ficha para responder.", "No; se hacen con choclo, un alimento de América", "El producto principal de las humitas viene de América."),
        ],
        "challenge": [
            ex(f"{ALI} Escribe un plato con un producto de América y otro de Europa.", "papa con cebolla", "Cada ingrediente viene de un lugar distinto."),
            ex("¿Por qué no decimos que un plato completo es «solo indígena» ni «solo español»?", "Porque mezcla productos y formas de cocinar de varios orígenes", "La comida chilena es una mezcla."),
        ],
    },
    context=[ex("En una feria venden humitas, pan amasado y papas cocidas. ¿Cuántos de esos tres alimentos usan un producto que viene de América según la ficha (choclo, trigo, papa)?", "2", "Humitas usan choclo y las papas son de América; el pan amasado usa trigo, que llegó de Europa.")],
    selfcheck=[
        ex(f"{ALI} ¿De dónde viene el maíz?", "de América", "La ficha lo indica."),
        ex(f"{ALI} ¿Qué llegó con los españoles: la gallina o la papa?", "la gallina", "La papa es de América."),
        ex("¿Qué es un intercambio cultural?", "cuando dos grupos comparten algo", "Se comparte comida, palabras o costumbres."),
    ],
    open_task=task(
        f"Elige uno de estos platos y haz una tabla con tres filas: producto, preparación y origen de cada producto. Platos: humitas, pan amasado, papas con cebolla. {ALI}",
        "Plato: humitas. Producto: choclo (América). Preparación: se hacen con choclo. No pongo un solo origen para todo el plato.",
        ["un plato elegido", "producto y preparación", "origen de cada producto"], ["tabla escrita"], ["decir que el plato completo es solo de un origen", "inventar un origen"],
        "Pregunta qué otro ingrediente podría agregar y de dónde vendría."),
    reinforce="Nombra tres alimentos de tu casa y di si el ingrediente principal viene de América o de Europa, usando la ficha.",
    extend="Escribe una pregunta para saber de dónde viene otro alimento que comes seguido.",
)

FIE = ("Ficha de fiestas (dada por la clase): en La Tirana, en el norte de Chile, cada julio se celebra una fiesta religiosa con bailes, trajes y música. "
       "Mezcla tradiciones de los pueblos andinos con la fe católica que trajeron los españoles. El domingo de Cuasimodo, en el centro del país, personas a caballo acompañan al sacerdote que visita a enfermos; es una tradición de origen español. "
       "Fuentes de ejemplo creadas para esta clase: descripción de hace 150 años, fotografía de hace 40 años y video de hace 3 años.")
register(
    OA3, 3,
    materials="Lápiz y papel. La ficha de fiestas está escrita en cada ejercicio.",
    use="Aprenderé que algunas fiestas mezclan costumbres de pueblos distintos y que cambian con el tiempo. Sirve para entender que las tradiciones están vivas.",
    prior=["Sé qué es un aporte.", "Sé qué es una continuidad y un cambio."],
    explain=[
        "Una tradición es una costumbre que pasa de padres a hijos. Muchas fiestas de Chile mezclan aportes de pueblos originarios y de los españoles. Con el tiempo, las tradiciones cambian, pero siguen vivas.",
        "En la fiesta de La Tirana, en el norte, se baila con trajes y música, y se mezclan tradiciones andinas con la fe católica. El domingo de Cuasimodo, en el centro, personas a caballo acompañan al sacerdote en su visita a los enfermos. Es una tradición de origen español que sigue practicándose.",
        "Para ver cómo cambia una tradición, comparamos fuentes de fechas distintas. Una descripción de hace 150 años, una fotografía de hace 40 años y un video de hace 3 años pueden mostrar cosas distintas de la misma fiesta. Lo que se parece muestra continuidad. Lo que es distinto muestra cambio.",
    ],
    vocab=[("tradición", "costumbre que pasa de generación en generación"), ("fiesta religiosa", "fiesta que celebra una creencia"), ("mezcla", "unión de cosas distintas"), ("continuidad", "lo que se mantiene en el tiempo"), ("cambio", "lo que ya no es igual que antes")],
    worked=[
        {"title": "Detectar una mezcla", "problem": f"{FIE} ¿Qué mezcla la fiesta de La Tirana?", "steps": ["Leo La Tirana en la ficha.", "Dice: tradiciones andinas y fe católica."], "answer": "Tradiciones de los pueblos andinos y la fe católica"},
        {"title": "Ordenar fuentes", "problem": f"{FIE} ¿Qué fuente de la ficha es la más reciente?", "steps": ["Miro los años: 150, 40 y 3.", "Hace 3 años es lo menos tiempo."], "answer": "El video de hace 3 años"},
    ],
    mistakes=[
        {"wrong": "Decir que una fiesta no ha cambiado nada.", "why": "No se comparan fuentes de distintas fechas.", "fix": "Compara qué se parece y qué es distinto."},
        {"wrong": "Decir que una fiesta tiene un solo origen.", "why": "Se piensa que solo vino de un pueblo.", "fix": "Mira si mezcla aportes de más de una cultura."},
    ],
    tiers={
        "recovery": [
            ex(f"{FIE} ¿En qué zona de Chile está La Tirana?", "en el norte", "La ficha lo indica."),
            ex(f"{FIE} ¿Cuándo se celebra La Tirana?", "cada julio", "La ficha lo dice."),
            ex(f"{FIE} ¿Quién acompaña al sacerdote en el domingo de Cuasimodo?", "personas a caballo", "La ficha lo dice."),
        ],
        "understand": [
            ex(f"{FIE} ¿Qué tradiciones mezcla La Tirana?", "andinas y la fe católica", "La ficha lo explica."),
            ex(f"{FIE} ¿De qué origen es la tradición de Cuasimodo?", "español", "La ficha lo dice."),
            ex("¿Para qué sirve comparar fuentes de fechas distintas?", "Para ver qué se mantiene y qué cambia", "Así se ve la continuidad y el cambio."),
        ],
        "apply": [
            ex(f"{FIE} Ordena de más antigua a más reciente: video de hace 3 años, descripción de hace 150 años, fotografía de hace 40 años.", "descripción de hace 150 años, fotografía de hace 40 años, video de hace 3 años", "Se ordenan de mayor a menor número de años."),
            ex(f"{FIE} Clasifica como continuidad o cambio: la fiesta de La Tirana se sigue celebrando cada julio.", "continuidad", "Se mantiene hasta hoy."),
            ex("Clasifica como continuidad o cambio: hace 150 años no existían los videos y hoy se graba la fiesta con celulares.", "cambio", "Es un cambio en cómo se registra la fiesta."),
        ],
        "reason": [
            ex("Carla dice: «Como hoy se usan celulares para grabar la fiesta, ya no es una tradición». ¿Qué respondes?", "Puede seguir siendo tradición aunque cambie cómo se registra", "Cambiar la forma de registrar no cambia la tradición."),
            ex(f"{FIE} ¿Por qué no podemos decir que Cuasimodo es «solo indígena»?", "Porque la ficha dice que es de origen español", "La ficha da el origen."),
        ],
        "challenge": [
            ex(f"{FIE} Escribe una frase con «mezcla» sobre La Tirana.", "La Tirana mezcla tradiciones andinas y fe católica", "Usa los datos de la ficha."),
            ex("Una tradición cambia con los años. ¿Deja por eso de ser parte de la cultura?", "no", "Las tradiciones cambian y siguen vivas."),
        ],
    },
    context=[ex("En tu curso comparan una fotografía de hace 40 años de una fiesta de La Tirana y un video de hace 3 años. Ven bailes y trajes en ambos. ¿Qué muestra eso: continuidad o cambio?", "continuidad", "Lo que se parece en ambos muestra que se mantiene.")],
    selfcheck=[
        ex(f"{FIE} ¿Qué se celebra en el norte cada julio?", "La Tirana", "La ficha lo dice."),
        ex("¿Qué es una tradición?", "una costumbre que pasa de generación en generación", "Se transmite entre generaciones."),
        ex("¿Las tradiciones cambian con el tiempo?", "sí", "Pueden cambiar y seguir vivas."),
    ],
    open_task=task(
        f"Elige La Tirana o Cuasimodo. Dibuja una escena de la fiesta y escribe tres frases: qué es, qué aportes mezcla y qué podría cambiar con el tiempo. {FIE}",
        "La Tirana. Es una fiesta religiosa en el norte con bailes y trajes. Mezcla tradiciones andinas con fe católica. Con el tiempo puede cambiar cómo se registra, pero sigue celebrándose.",
        ["fiesta elegida", "aportes mezclados", "una idea sobre cambio"], ["dibujo", "tres frases"], ["decir que no ha cambiado nada", "inventar datos que no están en la ficha"],
        "Pide que cite de la ficha cada dato. Si agrega algo, pide una fuente."),
    reinforce="Cuenta a alguien en casa qué mezcla tiene La Tirana y qué es Cuasimodo.",
    extend="Pregunta a un adulto de tu casa por una tradición que se haya mantenido y otra que haya cambiado.",
)

MES = ("Ficha de mestizaje (dada por la clase): de los pueblos originarios vienen palabras como palta y choclo, alimentos como la papa y el maíz, y fiestas como el We Tripantu. "
       "De los españoles vienen el castellano, el trigo y la fe católica. Muchas familias chilenas tienen antepasados de ambos orígenes. "
       "La historia del encuentro tuvo momentos difíciles, que estudiarás más adelante.")
register(
    OA3, 4,
    materials="Lápiz y papel. La ficha de mestizaje está escrita en cada ejercicio.",
    use="Aprenderé qué significa que Chile sea una sociedad mestiza y daré ejemplos. Sirve para reconocer que nuestra cultura tiene raíces diversas.",
    prior=["Sé qué aportó cada pueblo en palabras y alimentos.", "Sé qué es una tradición."],
    explain=[
        "Mestizaje es la mezcla de personas y culturas de pueblos distintos. Chile es una sociedad mestiza porque mezcla aportes de los pueblos originarios y de los españoles. Esa mezcla se ve en las palabras, los alimentos, las fiestas y las familias.",
        "De los pueblos originarios vienen palabras como palta y choclo, alimentos como la papa y el maíz, y fiestas como el We Tripantu. De los españoles vienen el castellano, el trigo y la fe católica. Muchas familias chilenas tienen antepasados de ambos orígenes.",
        "El mestizaje es complejo. La historia del encuentro entre los pueblos tuvo momentos difíciles, y todavía hay muchas preguntas por responder. Además, a esta mezcla se sumaron después personas de muchos otros países. Por eso Chile es diverso: tiene muchas raíces.",
    ],
    vocab=[("mestizaje", "mezcla de personas y culturas de pueblos distintos"), ("sociedad", "grupo grande de personas que vive junta"), ("diverso", "con muchas formas distintas"), ("raíz", "origen de una cultura o familia"), ("antepasado", "persona de la familia que vivió hace mucho")],
    worked=[
        {"title": "Dos aportes", "problem": f"{MES} Escribe un aporte indígena y uno español.", "steps": ["Indígena: busco palta, choclo, papa o maíz.", "Español: busco castellano, trigo o fe católica."], "answer": "Indígena: la papa. Español: el trigo"},
        {"title": "Una combinación", "problem": f"{MES} Nombra una combinación de aportes en un mismo plato.", "steps": ["Un plato con papa, de América, y cebolla, de Europa.", "Es una mezcla de ambos orígenes."], "answer": "Papa de América con cebolla de Europa"},
    ],
    mistakes=[
        {"wrong": "Decir que todas las personas en Chile son iguales porque hay mestizaje.", "why": "Se pierde la diversidad.", "fix": "Hay muchas raíces y muchas formas de vida en Chile."},
        {"wrong": "Decir que el encuentro entre pueblos fue solo bueno.", "why": "Se olvida que hubo momentos difíciles.", "fix": "Recuerda que la historia tuvo momentos difíciles y que hay más por aprender."},
    ],
    tiers={
        "recovery": [
            ex("Mestizaje, ¿es la mezcla de culturas o una sola cultura?", "la mezcla de culturas", "Esa es su definición."),
            ex(f"{MES} ¿Qué idioma vino con los españoles?", "el castellano", "La ficha lo dice."),
            ex(f"{MES} ¿Qué fiesta indígena nombra la ficha?", "el We Tripantu", "La ficha la nombra."),
        ],
        "understand": [
            ex(f"{MES} Nombra dos aportes de los pueblos originarios.", "palta y choclo, o papa y maíz (cualquiera de la ficha)", "Son aportes que la ficha nombra."),
            ex(f"{MES} Nombra dos aportes de los españoles.", "castellano, trigo o fe católica (dos de ellos)", "La ficha cita tres."),
            ex("¿Por qué decimos que Chile tiene muchas raíces?", "Porque junta aportes de muchos pueblos", "La mezcla viene de varios orígenes."),
        ],
        "apply": [
            ex(f"{MES} Une: 1) trigo, 2) papa. A) aporte español, B) aporte de pueblos originarios.", "1 con A; 2 con B", "El trigo llegó con los españoles y la papa es de América."),
            ex(f"{MES} Escribe una frase con «mestizaje» y dos aportes.", "El mestizaje mezcla la papa y el trigo", "Usa dos aportes de la ficha."),
            ex(f"{MES} Clasifica como aporte indígena o español: la palabra choclo.", "indígena", "Viene del quechua."),
        ],
        "reason": [
            ex("Mateo dice: «El mestizaje significa que todos son iguales». ¿Por qué no es correcto?", "Porque Chile tiene muchas raíces y mucha diversidad", "Mezclar no es igualar."),
            ex(f"{MES} ¿Por qué la ficha dice que hubo momentos difíciles?", "Porque la historia del encuentro no fue solo amable", "Una descripción honesta lo reconoce."),
        ],
        "challenge": [
            ex(f"{MES} Escribe una explicación corta con dos aportes, una combinación y una pregunta pendiente.", "Aportes: palta y trigo. Combinación: papa con cebolla. Pregunta: ¿qué más aportaron los pueblos?", "Debe tener los cuatro elementos."),
            ex("Además de pueblos originarios y españoles, ¿qué otros grupos se sumaron a la mezcla de Chile?", "personas de muchos otros países", "La diversidad creció con la llegada de inmigrantes."),
        ],
    },
    context=[ex("En una fiesta familiar hay empanadas con trigo, papas cocidas y se cantan canciones. Un niño dice: «Mi mesa mezcla cosas de América y de Europa». ¿Tiene razón?", "sí", "Las papas son de América y el trigo llegó de Europa.")],
    selfcheck=[
        ex("¿Qué es el mestizaje?", "la mezcla de personas y culturas", "Es unir raíces distintas."),
        ex(f"{MES} ¿De dónde viene el castellano?", "de los españoles", "Llegó con ellos."),
        ex("¿Chile tiene una sola raíz?", "no", "Tiene muchas raíces."),
    ],
    open_task=task(
        f"Haz un cartel que diga «Chile, una sociedad mestiza». Dibuja dos aportes de pueblos originarios y dos de los españoles, y escribe una pregunta que aún tengas. {MES}",
        "Pueblos originarios: palta y papa. Españoles: trigo y castellano. Pregunta: ¿qué otras comidas mezclan aportes?",
        ["dos aportes de cada grupo", "una pregunta pendiente", "título del cartel"], ["cartel dibujado"], ["decir que todos son iguales", "no incluir una pregunta"],
        "Pregunta por qué su cartel muestra mezcla. Debe mencionar aportes de ambos grupos."),
    reinforce="Explica a alguien qué es el mestizaje con un ejemplo de comida y otro de palabra.",
    extend="Escribe una pregunta sobre otro grupo que haya llegado a Chile y ayude a su diversidad.",
)

# ================================================================ OA 04
BIO = ("Biografías inventadas, basadas en historias reales de épocas distintas: Anna, niña alemana, viajó con su familia en barco a Valdivia, en el sur de Chile, hace unos 170 años, porque el gobierno ofrecía tierras para cultivar. "
       "Samir, joven árabe, llegó a Chile hace más de 100 años buscando trabajo y empezó vendiendo telas. Carolina, de Venezuela, llegó a Chile hace pocos años con su familia para estudiar y trabajar. "
       "Min-jun, joven coreano, llegó a Chile con su familia hace unos 50 años para abrir un negocio de ropa en Santiago.")
register(
    OA4, 1,
    materials="Lápiz y papel. Las biografías inventadas están escritas en cada ejercicio.",
    use="Aprenderé qué es migrar y a decir de dónde llegó una persona, adónde y por qué. Sirve para entender que cada persona migrante tiene su propia historia.",
    prior=["Sé que Chile tiene mucha diversidad.", "Sé ubicar norte y sur."],
    explain=[
        "Migrar es cambiar de lugar para vivir en otra parte. Un inmigrante es una persona que llega a vivir a un país distinto del suyo. Cada migración tiene un origen, que es el lugar de salida, y un destino, que es el lugar de llegada.",
        "Las razones para migrar son distintas. Algunas personas buscan trabajo, otras tierras para cultivar, otras estudiar o vivir con su familia. En la ficha, Anna salió de Alemania hacia Valdivia por tierras. Samir llegó desde el mundo árabe por trabajo. Carolina salió de Venezuela para estudiar y trabajar. Min-jun salió de Corea para abrir un negocio de ropa.",
        "No hay una sola historia de inmigrantes. Las personas llegaron en épocas distintas y por razones distintas, desde distintas naciones europeas, orientales, árabes y latinoamericanas. Por eso no debemos generalizar. Cada historia se mira con sus datos.",
    ],
    vocab=[("migrar", "cambiar de lugar para vivir en otro sitio"), ("inmigrante", "persona que llega a vivir a otro país"), ("origen", "lugar de donde sale una persona"), ("destino", "lugar adonde llega una persona"), ("razón", "motivo por el que se hace algo")],
    worked=[
        {"title": "Origen, destino y razón", "problem": f"{BIO} Escribe origen, destino y razón de Anna.", "steps": ["Origen: Alemania.", "Destino: Valdivia, en el sur de Chile.", "Razón: el gobierno ofrecía tierras para cultivar."], "answer": "Origen: Alemania. Destino: Valdivia. Razón: tierras para cultivar"},
        {"title": "No generalizar", "problem": f"{BIO} ¿Todas las personas migraron por la misma razón?", "steps": ["Anna vino por tierras.", "Samir por trabajo, Carolina por estudiar y trabajar, y Min-jun para abrir un negocio."], "answer": "No; cada persona tuvo su razón"},
    ],
    mistakes=[
        {"wrong": "Decir que todos los inmigrantes llegaron por la misma razón.", "why": "Se generaliza una sola historia.", "fix": "Cada persona tiene su propio origen, destino y razón."},
        {"wrong": "Confundir origen con destino.", "why": "Se mezclan los dos lugares del viaje.", "fix": "Origen es de donde sale; destino es adonde llega."},
    ],
    tiers={
        "recovery": [
            ex(f"{BIO} ¿Adónde llegó Anna?", "a Valdivia, en el sur de Chile", "La ficha lo indica."),
            ex(f"{BIO} ¿Qué vendía Samir al empezar?", "telas", "La ficha lo indica."),
            ex("Inmigrante, ¿es quien llega a vivir a otro país o quien sale de su casa a pasear?", "quien llega a vivir a otro país", "Esa es su definición."),
        ],
        "understand": [
            ex(f"{BIO} ¿De qué país salió Min-jun?", "de Corea", "La ficha lo indica."),
            ex("Explica con tus palabras qué es el origen en una migración.", "el lugar del que sale la persona", "Origen es el lugar de salida."),
            ex(f"{BIO} ¿Por qué llegó Anna a Valdivia?", "porque ofrecían tierras para cultivar", "Esa es su razón."),
        ],
        "apply": [
            ex(f"{BIO} Une cada persona con su razón: 1) Samir, 2) Carolina, 3) Min-jun. A) estudiar y trabajar, B) buscar trabajo, C) abrir un negocio de ropa.", "1 con B; 2 con A; 3 con C", "Cada persona tuvo su propia razón."),
            ex(f"{BIO} Ordena de más antigua a más reciente la llegada: Carolina, Min-jun, Anna, Samir.", "Anna, Samir, Min-jun, Carolina", "Hace 170, más de 100, unos 50 y pocos años."),
            ex(f"{BIO} Escribe origen y destino de Samir si solo sabes que llegó a Chile y vino del mundo árabe.", "origen: mundo árabe; destino: Chile", "La ficha da esos dos datos."),
        ],
        "reason": [
            ex("Un compañero dice: «Todos los inmigrantes llegaron para trabajar en el campo». Usa la ficha: ¿tiene razón?", "No; Samir vendía telas y Carolina quería estudiar", "Hay distintas razones."),
            ex(f"{BIO} ¿Por qué es mejor decir «algunos inmigrantes» que «todos»?", "Porque cada historia es distinta", "Así se evita generalizar."),
        ],
        "challenge": [
            ex(f"{BIO} Escribe una frase con origen, destino y razón de Carolina.", "Carolina salió de Venezuela y llegó a Chile para estudiar y trabajar", "Incluye los tres datos."),
            ex("Imagina una niña que sale de Italia y llega a Chile buscando trabajo para su familia. ¿Cuál es su destino?", "Chile", "El destino es adonde llega."),
        ],
    },
    context=[ex("En una exposición del colegio, tres carteles dicen: «Anna, de Alemania a Valdivia», «Samir, del mundo árabe a Chile» y «Carolina, de Venezuela a Chile». ¿Qué dato muestra el cartel de Anna que los otros dos no nombran?", "una ciudad de destino, Valdivia", "Solo Anna tiene una ciudad como destino.")],
    selfcheck=[
        ex("¿Qué es el destino?", "el lugar adonde llega la persona", "Es el lugar de llegada."),
        ex(f"{BIO} ¿Quién llegó hace pocos años?", "Carolina", "La ficha lo indica."),
        ex("¿Todas las historias de inmigrantes son iguales?", "no", "Cada una tiene su origen, destino y razón."),
    ],
    open_task=task(
        f"Elige a Anna, Samir, Carolina o Min-jun y haz una ficha con: nombre, origen, destino, razón y época. {BIO}",
        "Nombre: Samir. Origen: mundo árabe. Destino: Chile. Razón: buscar trabajo. Época: hace más de 100 años. Empezó vendiendo telas.",
        ["nombre", "origen y destino", "razón", "época"], ["ficha escrita"], ["mezclar origen con destino", "generalizar a todos los inmigrantes"],
        "Pregunta qué parte de la ficha cambiaría si fuera otra persona. Debe decir que todo."),
    reinforce="Explica a alguien qué es migrar usando el ejemplo de una persona de la ficha.",
    extend="Pregunta a un adulto si en tu familia alguien cambió de ciudad o de país y escribe una frase sin datos personales.",
)

APO = ("Ficha de aportes (dada por la clase): Ignacio Domeyko, polaco, llegó a Chile hace casi 200 años; estudió los minerales y fue rector de la Universidad de Chile. "
       "Rodulfo Philippi, alemán, llegó hace más de 170 años; estudió plantas y animales y dirigió el Museo Nacional de Historia Natural. "
       "Familias alemanas del sur fundaron colegios y negocios. La comunidad palestina fundó hace más de 100 años el Club Deportivo Palestino. "
       "Fuente 1: libro de historia. Fuente 2: placa en un museo.")
register(
    OA4, 2,
    materials="Lápiz y papel. La ficha de aportes está escrita en cada ejercicio.",
    use="Aprenderé qué aportaron personas inmigrantes en ciencias, trabajo, comercio, deporte y artes. Sirve para reconocer su contribución con nombres y fuentes.",
    prior=["Sé qué es migrar.", "Sé qué es una fuente."],
    explain=[
        "Las personas inmigrantes aportaron a Chile en oficios, ciencias, comercio, artes y deportes. Un aporte es algo que una persona o un grupo entrega a la sociedad. Para reconocerlo, necesitamos saber quién lo hizo y en qué fuente aparece.",
        "Ignacio Domeyko, polaco, estudió los minerales y fue rector de la Universidad de Chile. Rodulfo Philippi, alemán, estudió plantas y animales y dirigió el Museo Nacional de Historia Natural. Las familias alemanas del sur fundaron colegios y negocios. La comunidad palestina fundó el Club Deportivo Palestino.",
        "No todo aporte lo hizo una sola persona. Muchas veces participaron comunidades completas. Por eso, cuando uses una fuente, anota quiénes participaron: una persona, una familia o una comunidad. Así tu descripción es más clara y justa.",
    ],
    vocab=[("aporte", "algo que una persona o grupo entrega a la sociedad"), ("científico", "persona que estudia para conocer mejor la naturaleza"), ("comunidad", "grupo de personas con algo en común"), ("fundar", "crear algo nuevo, como un colegio o un club"), ("rector", "persona que dirige una universidad")],
    worked=[
        {"title": "Un aporte en ciencias", "problem": f"{APO} ¿Qué aportó Rodulfo Philippi?", "steps": ["Busco su nombre en la ficha.", "Dice que estudió plantas y animales y dirigió el Museo Nacional de Historia Natural."], "answer": "Estudió plantas y animales y dirigió el museo"},
        {"title": "Quiénes participaron", "problem": f"{APO} ¿Quiénes fundaron el Club Deportivo Palestino?", "steps": ["Busco club en la ficha.", "Dice: la comunidad palestina."], "answer": "La comunidad palestina"},
    ],
    mistakes=[
        {"wrong": "Decir que todos los inmigrantes de un país hicieron el mismo aporte.", "why": "Se generaliza desde un ejemplo.", "fix": "Nombra a la persona o comunidad de la fuente."},
        {"wrong": "Decir que un aporte lo hizo una sola persona cuando fue una comunidad.", "why": "No se lee quiénes participaron.", "fix": "Anota quiénes participaron según la fuente."},
    ],
    tiers={
        "recovery": [
            ex(f"{APO} ¿De qué país venía Domeyko?", "de Polonia (era polaco)", "La ficha dice que era polaco."),
            ex(f"{APO} ¿Qué estudiaba Domeyko?", "los minerales", "La ficha lo dice."),
            ex("Fundar, ¿es crear algo nuevo o destruirlo?", "crear algo nuevo", "Fundar es crear."),
        ],
        "understand": [
            ex(f"{APO} ¿Qué cargo tuvo Domeyko en la Universidad de Chile?", "rector", "La ficha lo dice."),
            ex(f"{APO} ¿Qué fundaron familias alemanas del sur?", "colegios y negocios", "La ficha lo dice."),
            ex("¿Por qué es importante anotar quiénes participaron en un aporte?", "Para ser claros y justos", "Así reconocemos a todos."),
        ],
        "apply": [
            ex(f"{APO} Une: 1) Philippi, 2) Domeyko. A) plantas y animales, B) minerales.", "1 con A; 2 con B", "Cada científico estudió algo distinto."),
            ex(f"{APO} Escribe una institución que se menciona en la ficha.", "Universidad de Chile, Museo Nacional de Historia Natural o Club Deportivo Palestino", "La ficha nombra las tres."),
            ex(f"{APO} ¿Qué fuente de la ficha es una placa en un museo?", "la fuente 2", "La ficha la nombra así."),
        ],
        "reason": [
            ex("Un niño dice: «Todos los alemanes fueron científicos». Usa la ficha: ¿tiene razón?", "No; algunos fundaron colegios y negocios", "La ficha muestra distintos aportes."),
            ex(f"{APO} ¿Qué diferencia hay entre el aporte de Domeyko y el de la comunidad palestina?", "Domeyko fue una persona y la comunidad fue un grupo", "Uno fue individual y el otro colectivo."),
        ],
        "challenge": [
            ex(f"{APO} Escribe una frase con un aporte, quién lo hizo y la fuente que lo respalda.", "Rodulfo Philippi dirigió el Museo Nacional de Historia Natural, según el libro de historia", "Incluye aporte, persona y fuente."),
            ex(f"{APO} ¿Fue Domeyko chileno de nacimiento?", "No; era polaco", "La ficha lo dice."),
        ],
    },
    context=[ex("En un museo, una placa dice: «Esta sala recuerda a la comunidad palestina, que fundó un club deportivo». ¿Quién participó en este aporte?", "la comunidad palestina", "La placa nombra a la comunidad.")],
    selfcheck=[
        ex(f"{APO} ¿Qué dirigió Philippi?", "el Museo Nacional de Historia Natural", "La ficha lo dice."),
        ex("¿Qué es un aporte?", "algo que una persona o grupo entrega a la sociedad", "Es una contribución."),
        ex("¿Una comunidad puede hacer un aporte?", "sí", "Un aporte puede ser de un grupo."),
    ],
    open_task=task(
        f"Haz una tabla con cuatro filas: persona o comunidad, aporte, fuente y lugar o institución que se menciona. Llénala con Domeyko, Philippi, familias alemanas del sur o la comunidad palestina. {APO}",
        "Persona: Domeyko. Aporte: estudió minerales y fue rector de la Universidad de Chile. Fuente: libro de historia. Lugar o institución: Universidad de Chile.",
        ["una persona o comunidad", "aporte correcto", "una fuente"], ["tabla escrita"], ["decir que todos hicieron lo mismo", "inventar un aporte"],
        "Pide que lea su fuente y diga quién participó."),
    reinforce="Nombra dos aportes de personas inmigrantes de esta clase.",
    extend="Escribe una pregunta sobre otro aporte de inmigrantes que te gustaría investigar.",
)

ENC = ("Ficha de encuentros (dada por la clase): el kuchen es un pastel de origen alemán que en Chile se hace con frutas de la zona. En el sur hay casas de madera de estilo alemán, construidas por familias alemanas. "
       "Las arepas son de Venezuela y hoy se venden en ciudades de Chile. Las hojas de parra rellenas son una comida árabe que hoy se prepara en Chile. El ceviche es una comida peruana que también se prepara en Chile. "
       "La pizza es una comida de origen italiano y hoy se prepara en Chile. En Santiago hay restaurantes de comida coreana.")
register(
    OA4, 3,
    materials="Lápiz y papel. La ficha de encuentros está escrita en cada ejercicio.",
    use="Aprenderé cómo comidas, casas y costumbres de otros países se adaptan en Chile. Sirve para entender que los encuentros culturales cambian a las dos partes.",
    prior=["Sé qué es un aporte.", "Sé qué es un origen y un destino."],
    explain=[
        "Un encuentro cultural ocurre cuando personas de países distintos comparten costumbres. Una práctica puede adaptarse en Chile: conserva algo de su origen y también toma algo del lugar nuevo.",
        "El kuchen es un pastel de origen alemán. En Chile se hace con frutas de la zona. Las casas de madera de estilo alemán del sur fueron construidas por familias alemanas. Las arepas son de Venezuela, las hojas de parra rellenas son una comida árabe y el ceviche es una comida peruana y la pizza es de origen italiano. Hoy todos se preparan en Chile. También hay restaurantes de comida coreana en Santiago.",
        "Para estudiar un encuentro hay que separar dos cosas: el origen, que es de dónde viene la práctica, y la transformación, que es cómo cambió en Chile. Por ejemplo, el kuchen alemán usa frutas chilenas. Eso es una adaptación.",
    ],
    vocab=[("encuentro cultural", "cuando personas de países distintos comparten costumbres"), ("adaptarse", "cambiar un poco para encajar en un lugar nuevo"), ("transformación", "cambio de forma de algo"), ("arquitectura", "forma de construir casas y edificios"), ("origen", "lugar de donde viene algo")],
    worked=[
        {"title": "Origen y transformación", "problem": f"{ENC} Escribe el origen y la transformación del kuchen.", "steps": ["Origen: es un pastel alemán.", "Transformación: en Chile se hace con frutas de la zona."], "answer": "Origen alemán; en Chile usa frutas de la zona"},
        {"title": "Reconocer una adaptación", "problem": f"{ENC} Nombra una comida de otro país que hoy se prepara en Chile.", "steps": ["Reviso la ficha.", "Las arepas, el ceviche y las hojas de parra rellenas se preparan en Chile."], "answer": "Arepas"},
    ],
    mistakes=[
        {"wrong": "Decir que una comida de otro país es igual en todas partes.", "why": "Se olvida que se adapta a ingredientes del lugar.", "fix": "Mira qué cambió en Chile."},
        {"wrong": "Decir que la comida «extranjera» no es parte de Chile.", "why": "Se piensa que solo importa lo que se hacía antes.", "fix": "Hoy es parte de la vida chilena y de su diversidad."},
    ],
    tiers={
        "recovery": [
            ex(f"{ENC} ¿De qué país es el origen de las arepas?", "Venezuela", "La ficha lo dice."),
            ex(f"{ENC} ¿De qué origen es el kuchen?", "alemán", "La ficha lo dice."),
            ex(f"{ENC} ¿Qué comida de otro país hay en los restaurantes de Santiago, según la ficha?", "comida coreana", "La ficha lo dice."),
        ],
        "understand": [
            ex(f"{ENC} ¿De qué país es el origen de la pizza?", "Italia", "La ficha lo dice."),
            ex(f"{ENC} ¿Qué comida es árabe?", "las hojas de parra rellenas", "La ficha lo dice."),
            ex("¿Qué es adaptarse?", "cambiar un poco para encajar en un lugar nuevo", "Eso describe el cambio."),
        ],
        "apply": [
            ex(f"{ENC} Une: 1) arepas, 2) kuchen. A) Alemania, B) Venezuela.", "1 con B; 2 con A", "Cada comida tiene su origen."),
            ex(f"{ENC} Escribe la transformación del kuchen en Chile.", "se hace con frutas de la zona", "La ficha lo indica."),
            ex(f"{ENC} Clasifica: casas de madera de estilo alemán, ¿comida o arquitectura?", "arquitectura", "Es una forma de construir."),
        ],
        "reason": [
            ex("Pablo dice: «El kuchen que comemos en Chile es igual al de Alemania». ¿Qué dato de la ficha lo contradice?", "Que en Chile se hace con frutas de la zona", "Por eso es una adaptación."),
            ex("Una niña dice: «Las arepas son chilenas porque se venden aquí». Explica si es correcto el origen.", "Su origen es Venezuela, aunque hoy también se preparan en Chile", "Origen y presencia actual son cosas distintas."),
        ],
        "challenge": [
            ex(f"{ENC} Escribe una frase que separe origen y transformación del ceviche.", "El ceviche es de origen peruano y en Chile también se prepara", "Separa de dónde viene y cómo es hoy."),
            ex(f"{ENC} Une cada comida con su país de origen: 1) pizza, 2) ceviche, 3) kuchen. A) Alemania, B) Italia, C) Perú.", "1 con B; 2 con C; 3 con A", "Cada comida tiene su origen."),
        ],
    },
    context=[ex("Un restaurante de tu barrio sirve arepas, ceviche y kuchen. ¿De cuántos países distintos viene esa comida (Venezuela, Perú, Alemania)?", "3", "Cada comida tiene un país de origen distinto.")],
    selfcheck=[
        ex(f"{ENC} ¿De qué país es el ceviche?", "Perú", "La ficha lo dice."),
        ex("¿Qué es un encuentro cultural?", "cuando personas de países distintos comparten costumbres", "Se comparte y se adapta."),
        ex(f"{ENC} ¿Dónde hay casas de madera de estilo alemán?", "en el sur", "La ficha lo dice."),
    ],
    open_task=task(
        f"Elige una comida de la ficha y haz una tabla con dos filas: origen y transformación en Chile. Dibuja el plato. {ENC}",
        "Comida: kuchen. Origen: pastel alemán. Transformación en Chile: se hace con frutas de la zona.",
        ["comida elegida", "origen correcto", "transformación"], ["dibujo", "tabla escrita"], ["decir que es igual en todos lados", "mezclar origen con transformación"],
        "Pregunta qué ingrediente de Chile le agregarías. Debe separar origen de transformación."),
    reinforce="Cuenta en voz alta de qué país viene una comida que se prepara en tu barrio.",
    extend="Pregunta a un adulto de tu casa por una comida de otro país que se coma cerca de ti y anota su origen.",
)

DIV = ("Ficha de diversidad (dada por la clase): Ignacio Domeyko, polaco, hace casi 200 años; aporte: estudió minerales y fue rector de la Universidad de Chile; fuente: libro de historia; límite: no dice cómo vivía su familia. "
       "Comunidad palestina, hace más de 100 años; aporte: fundó el Club Deportivo Palestino; fuente: placa en un club; límite: no cuenta todas las historias de la comunidad. "
       "Familias alemanas del sur, hace unos 170 años; aporte: colegios y negocios; fuente: relato de un museo; límite: no habla de todas las familias.")
register(
    OA4, 4,
    materials="Lápiz y papel. La ficha de diversidad está escrita en cada ejercicio.",
    use="Aprenderé a presentar un aporte de inmigrantes con nombres, época, fuente y límite, sin estereotipos. Sirve para hablar de la diversidad con precisión y respeto.",
    prior=["Sé qué es un aporte.", "Sé qué es una fuente."],
    explain=[
        "Una ficha de diversidad tiene cinco partes: la persona o comunidad, la época, la evidencia o fuente, el aporte y el límite de la fuente. Con esas partes podemos presentar un aporte de forma clara y respetuosa.",
        "El límite de la fuente es lo que ella no nos cuenta. Por ejemplo, el libro de historia dice lo que estudió Domeyko, pero no cuenta cómo vivía su familia. La placa del club habla del club, pero no de todas las historias de la comunidad palestina.",
        "Evitamos los estereotipos cuando no decimos que todas las personas de un país son iguales. No escribimos «los alemanes siempre...» ni «los árabes siempre...». Escribimos con nombres y datos: «según la fuente, esta comunidad fundó este club».",
    ],
    vocab=[("estereotipo", "idea fija y simple sobre un grupo"), ("evidencia", "lo que muestra una fuente"), ("límite de la fuente", "lo que la fuente no cuenta"), ("época", "tiempo en que ocurrió algo"), ("ficha", "hoja con datos organizados")],
    worked=[
        {"title": "Completar una ficha", "problem": f"{DIV} Completa la ficha de la comunidad palestina: persona o comunidad, época, aporte, fuente y límite.", "steps": ["Comunidad: palestina.", "Época: hace más de 100 años.", "Aporte: fundó el Club Deportivo Palestino. Fuente: placa en un club. Límite: no cuenta todas las historias."], "answer": "Comunidad palestina; hace más de 100 años; fundó un club; placa; no cuenta todas las historias"},
        {"title": "Evitar un estereotipo", "problem": "¿Qué frase evita un estereotipo: «Los alemanes son todos agricultores» o «Según un relato de un museo, algunas familias alemanas del sur fundaron colegios»?", "steps": ["La primera dice «todos».", "La segunda cita una fuente y dice «algunas»."], "answer": "La segunda"},
    ],
    mistakes=[
        {"wrong": "Escribir una ficha sin decir el límite de la fuente.", "why": "Se piensa que una fuente lo cuenta todo.", "fix": "Pregunta siempre qué no nos cuenta la fuente."},
        {"wrong": "Usar «todos» para hablar de un grupo.", "why": "Se generaliza desde un ejemplo.", "fix": "Escribe «algunas personas» o nombra a la persona o comunidad."},
    ],
    tiers={
        "recovery": [
            ex(f"{DIV} ¿Cuál es la fuente de Domeyko?", "un libro de historia", "La ficha lo dice."),
            ex(f"{DIV} ¿De qué época es la comunidad palestina de la ficha?", "hace más de 100 años", "La ficha lo dice."),
            ex("El límite de una fuente, ¿es lo que cuenta o lo que no cuenta?", "lo que no cuenta", "Límite es lo que queda fuera."),
        ],
        "understand": [
            ex(f"{DIV} ¿Cuál es el aporte de las familias alemanas del sur?", "colegios y negocios", "La ficha lo dice."),
            ex(f"{DIV} ¿Qué no dice la fuente de Domeyko?", "cómo vivía su familia", "Ese es su límite."),
            ex("¿Por qué evitamos decir «todos los alemanes»?", "Porque no todas las personas son iguales", "Evita el estereotipo."),
        ],
        "apply": [
            ex(f"{DIV} Une: 1) Domeyko, 2) familias alemanas del sur. A) relato de un museo, B) libro de historia.", "1 con B; 2 con A", "Cada ficha tiene su fuente."),
            ex(f"{DIV} Ordena de más antigua a más reciente según la época: comunidad palestina, Domeyko, familias alemanas.", "Domeyko, familias alemanas, comunidad palestina", "Casi 200, unos 170 y más de 100 años."),
            ex(f"{DIV} Escribe el límite de la fuente de las familias alemanas.", "no habla de todas las familias", "Ese es el límite que dice la ficha."),
        ],
        "reason": [
            ex("Marta dice: «Si una fuente cuenta un aporte, ya sabemos todo del grupo». ¿Qué respondes?", "Una fuente solo cuenta una parte; hay un límite", "Siempre queda algo fuera."),
            ex("Dani escribe: «Los árabes siempre venden telas». Corrige la frase para que no sea un estereotipo.", "Algunas personas árabes comenzaron vendiendo telas, según una fuente", "Se usa «algunas» y una fuente."),
        ],
        "challenge": [
            ex(f"{DIV} Redacta una frase de presentación de Domeyko con aporte, época y fuente.", "Hace casi 200 años, Domeyko estudió minerales y fue rector, según un libro de historia", "Incluye los tres datos."),
            ex("Escribe una pregunta que ayude a completar el límite de una de las fuentes.", "¿Cómo vivía la comunidad palestina?", "La pregunta busca lo que la fuente no cuenta."),
        ],
    },
    context=[ex("Una compañera lee una placa de un club fundado por inmigrantes. La placa dice el nombre del club y el año, pero no cuenta cómo vivían sus fundadores. ¿Qué parte de la ficha es esto?", "el límite de la fuente", "Es lo que la placa no cuenta.")],
    selfcheck=[
        ex("¿Cuántas partes tiene la ficha de diversidad de la clase?", "5", "Persona o comunidad, época, evidencia, aporte y límite."),
        ex("¿Qué es un estereotipo?", "una idea fija y simple sobre un grupo", "Simplifica a las personas."),
        ex(f"{DIV} ¿Qué aportaron las familias alemanas del sur?", "colegios y negocios", "La ficha lo dice."),
    ],
    open_task=task(
        f"Elige una persona o comunidad de la ficha y completa una ficha de cinco partes: persona o comunidad, época, aporte, fuente y límite. {DIV} Escribe además una frase sin «todos».",
        "Comunidad palestina. Hace más de 100 años. Aporte: fundó un club deportivo. Fuente: placa. Límite: no cuenta todas las historias. Frase: Según la placa, la comunidad palestina fundó un club.",
        ["cinco partes", "fuente identificada", "frase sin todos"], ["ficha escrita"], ["olvidar el límite", "usar la palabra todos"],
        "Pide que lea su límite y diga qué otra fuente ayudaría."),
    reinforce="Explica a alguien por qué no decimos «todos» cuando hablamos de un grupo de personas.",
    extend="Haz una pregunta para encontrar otra fuente que complete el límite de una de las fichas.",
)
