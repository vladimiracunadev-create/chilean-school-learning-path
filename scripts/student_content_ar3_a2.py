"""Cuaderno del estudiante de 3.º básico Artes Visuales: AR03 OA 03 (materiales, herramientas y procedimientos), OA 04 (describir obras) y OA 05 (retroalimentación y mejora)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA3 = "AR03 OA 03"
OA4 = "AR03 OA 04"
OA5 = "AR03 OA 05"


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


def w(title, problem, steps, answer):
    return {"title": title, "problem": problem, "steps": steps, "answer": answer}


def m(wrong, why, fix):
    return {"wrong": wrong, "why": why, "fix": fix}


def lesson(oa, n, materials, use, prior, explain, vocab, worked, mistakes, R, C, A, Z, D, ctx, sc, open_task, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab, worked=worked, mistakes=mistakes,
        tiers={"recovery": R, "understand": C, "apply": A, "reason": Z, "challenge": D},
        context=[ctx], selfcheck=sc, open_task=open_task, reinforce=reinforce, extend=extend,
    )


# ================================================================ OA 03
# ---------------------------------------------------------------- Clase 1
lesson(
    OA3, 1,
    "Plasticina (o masa de sal casera hecha con un adulto: harina, sal y agua; si alguien es alérgico a la harina, usa solo plasticina), un palito de helado, una cuchara plástica, una hoja seca, una tapa de botella y una hoja de papel para anotar tus pruebas. Lávate las manos al terminar y no pruebes la masa.",
    "Aprenderé a modelar un material blando y a dejar una huella con distintos objetos. Sirve para conocer qué puede hacer cada material y cada herramienta antes de crear una obra.",
    ["Sé que las obras se hacen con materiales y herramientas.", "Sé cuidar los útiles que comparto."],
    [
        "Modelar es dar forma con las manos a un material blando, como la plasticina, la masa o la arcilla. Con el modelado se hacen esculturas, que son obras con volumen. Las herramientas de modelar, como un palito o una cuchara, ayudan a cortar, alisar y marcar. Hay herramientas especiales para modelar, como el mirete; tu docente puede mostrártelas. Si no las tienes, usa un palito.",
        "Una huella es la marca que deja un objeto cuando se presiona sobre un material blando. Si presionas una hoja seca sobre la plasticina y la sacas, queda su dibujo en relieve. Hacer huellas sirve para preparar un grabado, que es un procedimiento donde se hace una marca para repetirla o imprimirla. Aquí solo probaremos la huella.",
        "Experimentar significa probar para descubrir. Antes de la obra final, haz una hoja de pruebas: anota qué material y qué herramienta usaste y qué pasó. Experimentar no es usar sin cuidado. Usa poco material, devuélvelo limpio y no pruebes la masa. Elige el material según lo que necesitas, no solo por cómo se ve.",
    ],
    [("modelado", "dar forma con las manos a un material blando"), ("huella", "marca que deja un objeto presionado sobre un material blando"), ("herramienta", "objeto que ayuda a trabajar un material"), ("escultura", "obra con volumen que se puede rodear"), ("hoja de pruebas", "hoja donde anoto qué probé y qué resultó")],
    [
        w("Probar una huella", "Presionas una hoja seca sobre plasticina plana y la sacas. ¿Qué queda y qué anotas en tu hoja de pruebas?", ["Queda la marca de las nervaduras de la hoja en relieve.", "Anoto: «Hoja seca + plasticina: marca clara de las nervaduras»."], "Queda la huella de la hoja; la anoto en la hoja de pruebas"),
        w("Elegir una herramienta", "Quieres hacer una línea fina en la masa. Tienes una cuchara y un palito. ¿Cuál eliges?", ["La cuchara es ancha y deja una marca gruesa.", "El palito tiene punta y deja una línea fina.", "Elijo el palito."], "El palito"),
    ],
    [
        m("Hundir muy fuerte la hoja en la plasticina y romperla.", "No se prueba la presión antes.", "Presiona con suavidad, mira el resultado y ajusta."),
        m("Probar sin anotar nada y después no recordar qué funcionó.", "No se usa la hoja de pruebas.", "Anota material, herramienta y resultado de cada prueba."),
    ],
    [
        ex("Modelar es dar forma con las manos a un material… ¿cómo?", "Blando", "Se modela material blando, como plasticina o arcilla."),
        ex("Presionas una hoja seca sobre plasticina y queda su dibujo. ¿Cómo se llama esa marca?", "Huella", "Una huella es la marca que deja un objeto."),
        ex("Entre un palito de helado y una hoja de papel, ¿cuál sirve como herramienta de modelar en este cuaderno?", "El palito", "La clase dice que un palito ayuda a cortar, alisar y marcar."),
    ],
    [
        ex("¿Qué es una escultura? A: obra con volumen que se puede rodear. B: dibujo plano. C: una foto.", "A", "La escultura tiene volumen."),
        ex("Para dejar una línea fina en la masa, ¿sirve más la punta de un palito o el lado de una cuchara?", "La punta de un palito", "La punta deja una línea delgada."),
        ex("¿Para qué sirve una hoja de pruebas? A: para anotar qué probé y qué resultó. B: para dibujar la obra final.", "A", "Registra material, herramienta y resultado."),
    ],
    [
        ex("Tienes plasticina y una tapa de botella. Presionas la tapa y queda un círculo con bordes marcados. ¿Qué dejaste: una huella o una escultura?", "Una huella", "La marca del objeto en el material es una huella."),
        ex("Quieres una huella muy clara de una hoja. ¿Presionas con suavidad y parejo o con un golpe muy fuerte?", "Con suavidad y parejo", "Así la marca queda nítida y no se rompe."),
        ex("Anotas: «Tenedor plástico + masa: líneas paralelas». ¿Qué herramienta usaste?", "Un tenedor plástico", "La anotación nombra el tenedor."),
    ],
    [
        ex("Pía eligió el material solo porque era brillante, y no sirvió para modelar. ¿Qué debió considerar?", "Si el material sirve para lo que necesita", "El material se elige según lo que se quiere hacer."),
        ex("Javier dice: «Experimentar es usar todo el material sin cuidado». ¿Tiene razón?", "No", "Experimentar es probar con cuidado."),
    ],
    [
        arith("Receta de masa de sal: 2 tazas de harina, 1 taza de sal y 1 taza de agua. Si haces doble receta, ¿cuántas tazas de harina necesitas?", "2 * 2", "Doble receta significa el doble de harina."),
        ex("Pruebas tres herramientas sobre la masa: palito, cuchara y tenedor plástico. Anotas una marca distinta por cada una. ¿Cuántas marcas distintas anotas?", "3", "Hay una marca por cada herramienta."),
    ],
    ex("Van a preparar masa de sal en grupo y alguien es alérgico a la harina. ¿Qué material usan en su lugar: plasticina o harina?", "Plasticina", "La plasticina evita el problema de la alergia."),
    [
        ex("¿Qué se hace con un material blando para darle forma?", "Modelar", "Esa es la acción de modelar."),
        ex("Verdadero o falso: la masa se puede probar con la lengua.", "Falso", "No se prueba la masa; no es comida."),
        ex("¿Qué marca deja una hoja presionada en plasticina?", "Una huella", "La marca de un objeto se llama huella."),
    ],
    task(
        "Haz una hoja de pruebas con TRES pruebas en plasticina o masa: A) una huella de hoja seca; B) una huella de tapa de botella; C) una forma modelada con las manos (una bolita o un rollito). Para cada prueba anota el material, la herramienta y qué resultó. Al final elige la que más te gustó y di por qué.",
        "Prueba 1: plasticina y hoja seca, quedó la huella de las nervaduras. Prueba 2: plasticina y tapa, quedó un círculo con bordes. Prueba 3: plasticina y manos, hice un rollito. Me gustó la 1 porque se ven líneas finas.",
        ["hace tres pruebas distintas", "anota material, herramienta y resultado", "elige una y da una razón", "cuida el material"],
        ["hoja de pruebas con tres anotaciones", "una frase de elección"],
        ["probar y no anotar", "elegir sin una razón"],
        "Reconoce la prueba más clara y pregunta qué ajustó al ver el resultado.",
    ),
    "Con la plasticina o con un trozo de masa, haz una bolita y apriétala con un dedo. Di en voz alta qué marca dejó.",
    "Haz huellas con dos objetos limpios de tu casa en la plasticina y compara cuál dejó una marca más clara.",
)

# ---------------------------------------------------------------- Clase 2
lesson(
    OA3, 2,
    "Distintos papeles (de diario, de revista sin usar, de lustre y kraft) y cartones (cartulina, cartón de caja y cartón corrugado), tijeras de punta redonda, pegamento en barra y pegamento blanco de escolar (cola fría) con un pincel viejo, y una hoja de pruebas. Pide ayuda a un adulto para cortar cartón grueso.",
    "Aprenderé a elegir papel, cartón y pegamento según lo que quiero unir, y a cortar y pegar con cuidado. Sirve para que mis collages queden firmes y limpios.",
    ["Sé usar tijeras con cuidado.", "Sé que cada material tiene distintas características."],
    [
        "Los papeles son delgados y flexibles, como el papel de diario o de lustre. Los cartones son más gruesos y firmes, como la cartulina, el cartón de caja y el cartón corrugado, que tiene ondas por dentro. Un collage es una obra hecha pegando papeles, cartones y otros materiales sobre una base. Las herramientas básicas son la tijera, para cortar, y el pegamento, para unir.",
        "No todos los pegamentos sirven para todo. El pegamento en barra es limpio y sirve para papeles delgados, pero no sujeta bien un cartón grueso. La cola fría, un pegamento blanco, sujeta mejor el cartón, pero si pones mucha en un papel delgado, lo arruga y lo mancha. Por eso conviene poner poca cantidad con un pincel y dejar secar.",
        "También se puede unir sin cortar: rasgar el papel con las manos deja un borde irregular distinto al de la tijera. Antes de pegar, ubica las piezas sobre la base y revisa que te guste. Usa la tijera siempre con la punta hacia abajo, sin caminar con ella, y pide ayuda para cortar cartón grueso.",
    ],
    [("collage", "obra hecha pegando papeles y otros materiales sobre una base"), ("cartón corrugado", "cartón con ondas por dentro"), ("pegamento en barra", "pegamento limpio para papeles delgados"), ("cola fría", "pegamento blanco que sujeta mejor materiales gruesos"), ("rasgar", "cortar un papel con las manos, dejando un borde irregular")],
    [
        w("Elegir pegamento", "Quieres pegar un trozo de cartón de caja sobre otro cartón. ¿Qué pegamento eliges?", ["El cartón es grueso y pesado.", "El pegamento en barra no lo sujeta bien.", "Elijo cola fría, con poca cantidad y dejando secar."], "Cola fría"),
        w("Bordes distintos", "Quieres un borde irregular, como el de una nube. ¿Cortas con tijera o rasgas con las manos?", ["Cortar con tijera deja un borde parejo.", "Rasgar deja un borde irregular.", "Elijo rasgar."], "Rasgar con las manos"),
    ],
    [
        m("Poner mucha cola fría sobre un papel delgado.", "El papel se arruga y se mancha.", "Pon poca cola con un pincel y presiona despacio."),
        m("Cortar el cartón grueso sin ayuda y con la tijera de prisa.", "Es peligroso y se puede cortar un dedo.", "Pide ayuda a un adulto para cortar cartón grueso."),
    ],
    [
        ex("¿Cuál es más grueso y firme: el papel de diario o el cartón de caja?", "El cartón de caja", "Los cartones son más gruesos que los papeles."),
        ex("Un collage se hace pegando papeles y otros materiales sobre… ¿qué?", "Una base", "La clase define collage como pegar materiales sobre una base."),
        ex("¿Para qué se usa la tijera?", "Para cortar", "La tijera es una herramienta para cortar."),
    ],
    [
        ex("¿Qué pegamento sirve para papeles delgados y es limpio? A: pegamento en barra. B: cola fría en mucha cantidad.", "A", "El pegamento en barra es limpio para papeles delgados."),
        ex("El cartón corrugado tiene ondas. ¿Es más parecido a un cartón o a un papel de diario?", "A un cartón", "El corrugado es un cartón con ondas."),
        ex("Rasgar un papel con las manos deja un borde… ¿cómo?", "Irregular", "Rasgar deja un borde irregular."),
    ],
    [
        ex("Quieres unir un cartón corrugado con un cartón de caja. ¿Usas pegamento en barra o cola fría?", "Cola fría", "La cola fría sujeta mejor materiales gruesos."),
        ex("Quieres pegar un papel de lustre muy delgado. ¿Pones mucha cola fría o poca con un pincel?", "Poca con un pincel", "Mucha cola arruga el papel delgado."),
        ex("Tienes que cortar un cartón grueso. ¿Qué haces: cortarlo rápido tú solo o pedir ayuda a un adulto?", "Pedir ayuda a un adulto", "La clase indica pedir ayuda con cartón grueso."),
    ],
    [
        ex("Una niña pegó papel delgado con mucha cola fría y quedó arrugado. ¿Qué cambia la próxima vez?", "Poner menos cola", "Poca cantidad evita que se arrugue."),
        ex("Un niño dice: «Los pegamentos son todos iguales». ¿Tiene razón?", "No", "Cada pegamento sirve mejor para ciertos materiales."),
    ],
    [
        arith("Tienes 3 papeles de diario, 2 de lustre y 4 cartulinas. ¿Cuántas piezas tienes en total para tu collage?", "3 + 2 + 4", "Se suman las piezas de cada material."),
        ex("Tu collage lleva una nube hecha con papel rasgado y un cerro de cartón cortado con tijera. ¿Qué borde es más irregular: el de la nube o el del cerro?", "El de la nube", "El papel rasgado deja un borde irregular."),
    ],
    ex("Quieres pegar una figura de cartón corrugado sobre una base de cartón de caja. ¿Qué pegamento es mejor: la barra o la cola fría?", "La cola fría", "La cola fría sujeta mejor la cartulina."),
    [
        ex("¿Qué material es más firme: el papel de lustre o el cartón?", "El cartón", "Los cartones son firmes."),
        ex("Verdadero o falso: la tijera se camina con la punta hacia arriba.", "Falso", "Se lleva con la punta hacia abajo."),
        ex("¿Qué se hace antes de pegar las piezas?", "Ubicarlas sobre la base", "Se revisa la composición antes de pegar."),
    ],
    task(
        "Haz un collage con un paisaje simple. Usa al menos DOS papeles distintos (por ejemplo diario y lustre) y UN cartón (cartulina o cartón de caja). Une con el pegamento que corresponda. En tu hoja de pruebas anota: qué pegamento usaste para cada material y si algo se arrugó o se despegó. Si tienes que cortar cartón grueso, pide ayuda a un adulto.",
        "Usé papel de diario para el cielo, lustre para el sol y cartulina para el cerro. Pegué el diario y el lustre con barra y el cerro con cola fría. El lustre se arrugó un poco, así que la próxima vez uso menos cola.",
        ["usa dos papeles y un cartón", "elige el pegamento según el material", "anota qué pasó", "corta con cuidado"],
        ["collage", "hoja de pruebas con pegamentos y resultados"],
        ["poner mucha cola en papel delgado", "no anotar qué pegamento usó"],
        "Reconoce la elección del pegamento y pregunta qué cambiaría si algo se despegó.",
    ),
    "Toca un papel y un cartón y di en voz alta cuál es más grueso y cuál se dobla más fácil.",
    "Pega el mismo tipo de papel con barra y con poca cola fría, y anota cuál quedó mejor.",
)

# ---------------------------------------------------------------- Clase 3
lesson(
    OA3, 3,
    "Materiales reutilizables limpios y secos: cajas de cartón, rollos de papel higiénico, tapas plásticas grandes, retazos de tela, botones grandes, lana. Pegamento escolar, cinta adhesiva y tijeras de punta redonda. NO uses latas, vidrio, objetos con bordes cortantes ni piezas muy pequeñas.",
    "Aprenderé a darle una nueva vida a materiales que iban a la basura y a unir piezas para crear una obra. Sirve para cuidar el ambiente y descubrir ideas.",
    ["Sé que los materiales se eligen según lo que necesito.", "Sé usar pegamento y tijeras con cuidado."],
    [
        "El reciclaje es usar de nuevo materiales que ya se usaron, para no botarlos. En arte se usan cajas, rollos de cartón, tapas, retazos de tela y lana. Antes de usarlos deben estar limpios y secos, y no deben tener bordes cortantes ni ser peligrosos. Los textiles son telas e hilos, como la lana y los retazos de tela.",
        "El ensamblaje es una forma de crear uniendo piezas de distintos objetos. Por ejemplo, unir un rollo de cartón y una caja para hacer un robot. Una escultura hecha así tiene volumen. Cuando se combinan materiales distintos, como cartón, tela y lana, se llama técnica mixta. La artesanía es otra forma de crear con las manos, como tejer tiras de tela.",
        "Para transformar un material, mira su forma y piensa en qué se puede convertir. Un rollo puede ser un cuerpo, una torre o un tronco. Para unir, usa cinta adhesiva en las partes que van a quedar escondidas y pegamento en las que se verán. Deja secar antes de seguir. Pide ayuda a un adulto para cortar cartón grueso.",
    ],
    [("reciclaje", "usar de nuevo materiales que ya se usaron"), ("ensamblaje", "crear uniendo piezas de distintos objetos"), ("técnica mixta", "obra hecha con varios materiales o procedimientos"), ("textil", "tela, lana o hilo"), ("artesanía", "objeto hecho a mano con técnicas tradicionales")],
    [
        w("Transformar un rollo", "Tienes un rollo de cartón, una tapa grande y un retazo de tela. Quieres hacer un personaje. ¿Qué parte es cada pieza?", ["El rollo puede ser el cuerpo.", "La tapa grande puede ser la cabeza.", "El retazo de tela puede ser la capa."], "Rollo: cuerpo; tapa: cabeza; tela: capa"),
        w("Elegir cómo unir", "Quieres pegar la cabeza al cuerpo y que no se vea el pegamento. ¿Dónde pones la cinta adhesiva?", ["Busco la parte que queda escondida.", "Pongo la cinta por detrás del cuello.", "Uso pegamento en la parte que sí se ve."], "Cinta por detrás, en la parte escondida"),
    ],
    [
        m("Usar materiales sucios, mojados o con bordes cortantes.", "Pueden ensuciar la obra o lastimar.", "Revisa que estén limpios, secos y seguros."),
        m("Usar tantas cosas en la obra que no se entiende qué es.", "Se piensa que más materiales es mejor.", "Elige pocos materiales y úsalos con una idea clara."),
    ],
    [
        ex("¿Qué es el reciclaje? A: usar de nuevo materiales ya usados. B: botar todo. C: comprar cosas nuevas.", "A", "El reciclaje da un nuevo uso a los materiales."),
        ex("Un rollo de cartón, una caja y una tapa unidos forman un robot. ¿Cómo se llama crear uniendo piezas?", "Ensamblaje", "Esa es la definición de ensamblaje."),
        ex("La lana y los retazos de tela son materiales… ¿de qué tipo?", "Textiles", "Los textiles son telas e hilos."),
    ],
    [
        ex("Una obra mezcla cartón, tela y lana. ¿Es una técnica mixta o de un solo material?", "Técnica mixta", "Usa varios materiales."),
        ex("Un material para reciclar debe estar limpio y seco. ¿Y cómo debe ser en seguridad: sin bordes cortantes o con vidrio?", "Sin bordes cortantes", "Los materiales deben ser seguros."),
        ex("¿Qué es la artesanía? A: un objeto hecho a mano con técnicas tradicionales. B: una foto.", "A", "La artesanía se hace con las manos."),
    ],
    [
        ex("Tienes una caja de leche limpia y seca. ¿Puedes usarla en tu obra, si no tiene bordes cortantes?", "Sí", "Es un material reutilizable seguro."),
        ex("Tienes una lata con el borde abierto. ¿La usas en tu obra?", "No", "Los bordes cortantes son peligrosos."),
        ex("Quieres unir dos cartones y no mostrar la cinta. ¿Pones la cinta por delante o por detrás?", "Por detrás", "Así la cinta queda escondida."),
    ],
    [
        ex("Tomás hizo un robot con 15 piezas y no se entiende qué es. ¿Qué podría hacer: agregar más piezas o usar menos con una idea clara?", "Usar menos piezas con una idea clara", "Pocos materiales bien usados comunican mejor."),
        ex("Valentina dice: «Todo lo que está en la basura sirve para el arte». ¿Es correcto?", "No", "Hay que elegir materiales limpios y seguros."),
    ],
    [
        arith("Para tu obra juntas 4 rollos de cartón, 3 tapas y 2 retazos de tela. ¿Cuántas piezas reutilizadas tienes?", "4 + 3 + 2", "Se suman las piezas de cada tipo."),
        ex("Una obra usa cartón, tela y lana y se hizo uniendo piezas. ¿Es ensamblaje, técnica mixta o ambas?", "Ambas", "Une piezas y mezcla varios materiales."),
    ],
    ex("Van a botar una caja de cartón limpia y tú quieres usarla para una obra. ¿Qué haces: revisarla y usarla o botarla sin pensar?", "Revisarla y usarla", "El reciclaje da un nuevo uso a los materiales."),
    [
        ex("¿Los materiales reciclados deben estar limpios y secos?", "Sí", "La clase lo exige."),
        ex("Verdadero o falso: es seguro usar latas abiertas en una obra.", "Falso", "Tienen bordes cortantes."),
        ex("¿Cómo se llama una obra hecha uniendo piezas de objetos?", "Ensamblaje", "Esa es la definición."),
    ],
    task(
        "Crea un personaje o un objeto con ensamblaje de materiales reutilizables limpios. Elige UNA idea: A) un robot; B) un animal; C) una torre. Usa al menos TRES materiales distintos de la lista (rollo de cartón, caja, tapa grande, retazo de tela, lana). Une con cinta en lo escondido y pegamento en lo visible. Escribe qué material usaste para cada parte.",
        "Hice un robot. El cuerpo es una caja, los brazos son rollos, la cabeza es una tapa grande y la capa es un retazo de tela. Usé cinta atrás y pegamento adelante.",
        ["usa al menos tres materiales reutilizables", "los materiales son limpios y seguros", "dice qué material usó para cada parte", "une con cuidado"],
        ["obra ensamblada", "lista de partes y materiales"],
        ["usar materiales peligrosos", "no explicar qué usó"],
        "Reconoce la transformación de un material y pregunta cómo resolvió una unión.",
    ),
    "Mira un objeto que ibas a botar y di en voz alta en qué lo convertirías.",
    "Cambia solo una pieza de tu obra por otra y anota si cambió la idea.",
)

# ---------------------------------------------------------------- Clase 4
lesson(
    OA3, 4,
    "Materiales naturales que ya estén en el suelo: hojas secas caídas, ramitas caídas, un poco de tierra seca que ya esté suelta en el suelo del patio, arena. Cartón reutilizado como base, pegamento escolar, pincel viejo, agua. Lávate las manos al terminar.",
    "Aprenderé a usar materiales de la naturaleza para crear sin dañar plantas ni lugares. Sirve para crear con respeto por el entorno.",
    ["Sé que los materiales se eligen para un fin.", "Sé que debo cuidar las plantas y animales."],
    [
        "Los materiales naturales vienen de la naturaleza: hojas, ramitas, flores secas, arena, tierra y piedras. En arte se pegan sobre una base, se dibujan o se usan para hacer colores. Por ejemplo, con tierra seca, agua y un poco de pegamento puedes hacer una pintura de color café. Con hojas y ramitas se pueden hacer composiciones sobre cartón.",
        "Para no dañar el entorno, sigue estas reglas. Usa solo lo que ya cayó al suelo: no arranques hojas, ramas ni flores de plantas vivas. No saques piedras ni arena de playas, parques o lugares protegidos. Si no conoces una planta, no la toques, porque algunas irritan la piel. No caves ni saques tierra de jardines, macetas o parques, y no soples la tierra seca. No lleves insectos a casa. Lávate las manos al terminar. Lo que sobre lo devuelves.",
        "Los materiales naturales cambian con el tiempo: las hojas se secan, se doblan y cambian de color. Eso también puede ser parte de tu idea. Escoge pocos materiales y úsalos bien. Un trabajo con materiales naturales puede combinarse con cartón reutilizado y con pintura hecha en casa.",
    ],
    [("material natural", "material que viene de la naturaleza, como hojas o tierra"), ("pigmento", "material que da color a una pintura"), ("composición", "forma en que se ordenan las piezas en una obra"), ("entorno", "lo que nos rodea, como plantas y animales"), ("proteger", "cuidar para que no se dañe")],
    [
        w("Reglas para recolectar", "En un parque ves hojas en el suelo y otras en el árbol. ¿Cuáles usas?", ["Las del árbol son parte de la planta viva.", "Las del suelo ya cayeron.", "Uso solo las del suelo."], "Solo las hojas caídas al suelo"),
        w("Pintura con tierra", "Quieres hacer pintura café con tierra seca de tu patio. ¿Qué mezclas?", ["Tomo un poco de tierra seca.", "Le agrego agua y un poco de pegamento escolar.", "Mezclo con un palito hasta que se pueda pintar."], "Tierra seca, agua y un poco de pegamento"),
    ],
    [
        m("Arrancar hojas y flores de plantas vivas para la obra.", "Se dañan las plantas.", "Usa solo lo que ya cayó al suelo."),
        m("Tocar una planta desconocida sin cuidado.", "Algunas pueden irritar la piel.", "No la toques y pregunta a un adulto."),
    ],
    [
        ex("Una hoja seca que ya cayó al suelo, ¿es un material natural?", "Sí", "Viene de la naturaleza."),
        ex("Entre tierra, plástico y lápiz de cera, ¿cuál es un material natural?", "Tierra", "La tierra viene de la naturaleza."),
        ex("Para pintar café con tierra, hay que mezclarla con agua y un poco de… ¿qué?", "Pegamento", "El pegamento ayuda a que la pintura se adhiera."),
    ],
    [
        ex("¿Puedes arrancar una rama de un árbol vivo para tu obra?", "No", "Solo se usa lo que cayó al suelo."),
        ex("¿Qué es un pigmento? A: material que da color. B: un pincel. C: una tijera.", "A", "El pigmento da color a la pintura."),
        ex("No conoces una planta del parque. ¿La tocas o preguntas a un adulto?", "Preguntas a un adulto", "Algunas plantas irritan la piel."),
    ],
    [
        ex("En la playa ves piedras lindas. ¿Te llevas las de una playa protegida?", "No", "No se sacan piedras de lugares protegidos."),
        ex("Tienes hojas secas y ramitas del suelo. ¿Las pegas sobre cartón reutilizado o las dejas tiradas?", "Las pegas sobre cartón reutilizado", "Se usa una base para la composición."),
        ex("Terminaste tu obra con materiales naturales. ¿Qué haces con las manos: lavarlas o dejarlas sucias?", "Lavarlas", "Se lavan después de tocar tierra y plantas."),
    ],
    [
        ex("Carla arrancó flores de la plaza para su collage. ¿Qué regla no cumplió?", "Usar solo lo que ya cayó", "No se deben arrancar plantas vivas."),
        ex("Diego dice: «Las hojas secas cambian de color y no sirven». ¿Es correcto?", "No", "El cambio de color puede ser parte de la idea."),
    ],
    [
        arith("Pegas 6 hojas, 4 ramitas y 3 flores secas caídas sobre cartón. ¿Cuántas piezas naturales usaste en total?", "6 + 4 + 3", "Se suman las piezas de cada tipo."),
        ex("Quieres hacer una composición con una hoja grande al centro y ramitas alrededor. ¿Cuántos materiales naturales distintos usas?", "2", "Son hojas y ramitas."),
    ],
    ex("Tu curso visita un parque y quiere hacer un collage con lo que encuentren. ¿Qué regla dan: recoger lo que cayó al suelo o arrancar lo más bonito?", "Recoger lo que cayó al suelo", "Así no se daña el entorno."),
    [
        ex("¿Qué se usa como base de una composición de hojas?", "Cartón reutilizado", "La clase propone cartón como base."),
        ex("Verdadero o falso: se pueden arrancar flores de un jardín público.", "Falso", "Hay que cuidar las plantas."),
        ex("¿Qué es proteger el entorno?", "Cuidar para que no se dañe", "Esa es la definición."),
    ],
    task(
        "Crea una composición con materiales naturales ya caídos al suelo. Elige UNA idea: A) un árbol hecho con ramitas y hojas; B) un paisaje con tierra pintada; C) un animal hecho con hojas. Usa cartón reutilizado de base. Escribe: qué materiales usaste, de dónde los sacaste y cómo cuidaste el entorno.",
        "Hice un árbol con ramitas del suelo y hojas secas. Los saqué del patio. Pegué todo sobre cartón de una caja. No arranqué nada y me lavé las manos.",
        ["usa materiales naturales caídos", "usa cartón reutilizado de base", "dice de dónde los sacó", "explica cómo cuidó el entorno"],
        ["composición natural", "tres frases: materiales, origen y cuidado"],
        ["arrancar plantas vivas", "no decir de dónde sacó los materiales"],
        "Reconoce el cuidado del entorno y pregunta cómo eligió la ubicación de las piezas.",
    ),
    "Camina por tu casa o patio y di en voz alta tres materiales naturales que ya estén en el suelo y que podrías usar.",
    "Deja tu obra unos días y anota cómo cambiaron los materiales naturales.",
)

# ---------------------------------------------------------------- Clase 5
lesson(
    OA3, 5,
    "Hojas, lápiz de mina, lápices de colores, témperas o acuarelas, pinceles de distinto grosor, un vaso con agua, un paño y una hoja de pruebas. Cubre la mesa con papel de diario.",
    "Aprenderé a controlar el lápiz y el pincel para lograr líneas, manchas y colores según lo que quiero expresar. Sirve para dibujar y pintar con intención.",
    ["Sé usar lápices y pinceles.", "Sé que los colores se pueden mezclar."],
    [
        "El dibujo se hace con lápices y otras herramientas que dejan una línea. Con el lápiz de mina puedes controlar la presión: si presionas poco, la línea queda clara y suave, y si presionas más, queda oscura y fuerte. El pincel sirve para pintar. Un pincel grueso cubre zonas grandes y uno fino hace detalles.",
        "En la pintura, la cantidad de agua cambia el resultado. Con poca agua, la témpera cubre más y se ve intensa. Con mucha agua, queda transparente y suave. Antes de cambiar de color, lava el pincel y sécalo en el paño. Si pintas sobre algo mojado, los colores se mezclan. Si dejas secar, se mantienen separados.",
        "Controlar el material significa elegir cómo usarlo para lo que quieres. Si quieres un cielo suave, usa mucha agua y presión ligera. Si quieres una línea firme, presiona más y usa un pincel fino. Prueba siempre en tu hoja de pruebas antes de la obra final. Dibujo y pintura son procedimientos distintos que se pueden combinar.",
    ],
    [("presión", "fuerza con que apoyo el lápiz o el pincel"), ("pincel", "herramienta para pintar con cerdas"), ("témpera", "pintura que se mezcla con agua y cubre bien"), ("transparente", "que deja ver lo que hay debajo"), ("procedimiento", "forma de hacer una obra, como dibujo o pintura")],
    [
        w("Controlar la presión", "Quieres dibujar una línea de sombra oscura y una línea de brillo clara con el mismo lápiz. ¿Cómo lo haces?", ["Para la sombra presiono más.", "Para el brillo presiono poco.", "Pruebo en mi hoja antes de la obra."], "Sombra: presión fuerte. Brillo: presión suave"),
        w("Controlar el agua", "Quieres pintar un cielo suave y transparente con témpera. ¿Cuánta agua usas?", ["Para un efecto suave necesito mucha agua.", "Mezclo poca témpera con bastante agua.", "Pruebo en la hoja de pruebas."], "Mucha agua y poca témpera"),
    ],
    [
        m("Pintar sin lavar el pincel entre colores.", "Los colores se ensucian y se mezclan sin querer.", "Lava el pincel y sécalo en el paño antes de cambiar de color."),
        m("Empezar la obra final sin probar nada antes.", "No se sabe cómo se comportará el material.", "Prueba en tu hoja antes de la obra final."),
    ],
    [
        ex("Si presionas poco el lápiz de mina, ¿la línea queda clara u oscura?", "Clara", "Menos presión deja una línea clara."),
        ex("¿Qué pincel usas para detalles: uno grueso o uno fino?", "Uno fino", "El pincel fino hace detalles."),
        ex("La témpera con mucha agua queda… ¿cómo?", "Transparente", "Mucha agua vuelve la pintura transparente."),
    ],
    [
        ex("¿Qué haces antes de cambiar de color? A: lavar el pincel y secarlo. B: seguir sin lavar.", "A", "Así los colores no se ensucian."),
        ex("Pintas sobre una zona mojada. ¿Los colores se mezclan o se mantienen separados?", "Se mezclan", "La humedad permite que se mezclen."),
        ex("¿Qué es un procedimiento en arte? A: forma de hacer una obra, como dibujo o pintura. B: un tipo de papel.", "A", "Dibujo y pintura son procedimientos."),
    ],
    [
        ex("Quieres una línea oscura y firme para el contorno de un árbol. ¿Presionas fuerte o suave?", "Fuerte", "Más presión deja una línea más oscura."),
        ex("Quieres cubrir un fondo grande con color. ¿Usas pincel grueso o fino?", "Grueso", "El pincel grueso cubre zonas grandes."),
        ex("Quieres un color intenso que cubra bien. ¿Usas poca o mucha agua con la témpera?", "Poca agua", "Poca agua da una pintura más intensa."),
    ],
    [
        ex("Camilo quería un cielo suave pero puso casi sin agua la témpera. ¿Qué pasó: quedó muy intenso o muy transparente?", "Muy intenso", "Poca agua deja la pintura intensa y no suave."),
        ex("Rosa dice: «Probar en la hoja es perder tiempo». ¿Tiene razón?", "No", "La prueba evita errores en la obra final."),
    ],
    [
        ex("Para un atardecer quieres un cielo suave arriba y un sol intenso abajo. ¿Dónde usas más agua: en el cielo o en el sol?", "En el cielo", "El cielo suave necesita más agua."),
        ex("Dibujas con lápiz una luna con presión ligera y un contorno de montaña con presión fuerte. ¿Cuál queda más oscuro?", "El contorno de la montaña", "Más presión deja más oscuro."),
    ],
    ex("Vas a pintar una casa con detalles pequeños en las ventanas. ¿Qué pincel eliges para las ventanas: el grueso o el fino?", "El fino", "Los detalles se hacen con pincel fino."),
    [
        ex("¿Con qué se controla el color de la línea del lápiz: la presión o el tamaño de la hoja?", "La presión", "La presión cambia lo claro u oscuro."),
        ex("Verdadero o falso: mucha agua hace una pintura más transparente.", "Verdadero", "Esa es la regla de la témpera."),
        ex("¿Qué se hace después de pintar con el pincel?", "Lavarlo", "Hay que cuidar la herramienta."),
    ],
    task(
        "Elige UNA intención: A) un cielo de atardecer suave; B) un árbol con contorno firme; C) un mar con ondas. Haz primero una hoja de pruebas con tres pruebas (presión del lápiz, cantidad de agua y tipo de pincel). Luego haz tu dibujo o pintura. Escribe qué control usaste y cómo ayudó a tu intención.",
        "Elegí el atardecer suave. En mi hoja probé mucha, media y poca agua. Elegí mucha agua con pincel grueso. El cielo quedó transparente y suave.",
        ["hace tres pruebas en la hoja", "elige según su intención", "usa lo probado en la obra", "explica cómo ayudó"],
        ["hoja de pruebas", "dibujo o pintura", "una frase"],
        ["no probar antes", "no relacionar con la intención"],
        "Reconoce la prueba que más ayudó y pregunta qué cambiaría en la obra.",
    ),
    "Toma un lápiz y haz una línea con poca presión y otra con mucha. Di en voz alta cuál quedó más oscura.",
    "Haz la misma línea con tres presiones y escribe una palabra para cada una: suave, media y fuerte.",
)

# ---------------------------------------------------------------- Clase 6
lesson(
    OA3, 6,
    "Una cámara o un celular de un adulto, o dibujos si no hay equipo; cartón, rollos, tapas, retazos de tela, cinta y pegamento escolar; hoja y lápices para la ficha. Un adulto ayuda con la cámara. No fotografíes personas sin su permiso.",
    "Aprenderé a construir una solución a un problema con materiales y a documentar cómo lo hice con fotos o dibujos. Sirve para explicar mi proceso y repetirlo después.",
    ["Sé elegir materiales y herramientas.", "Sé que registrar lo que hago ayuda a aprender."],
    [
        "Una solución técnica es una obra o un objeto que resuelve un problema usando materiales y procedimientos. Por ejemplo, un soporte de cartón que sostiene un lápiz. Para construirla se elige un material, se prueban uniones y se corrigen los errores. La fotografía es un procedimiento que registra imágenes con una cámara. Las herramientas tecnológicas, como una cámara o un computador, sirven para documentar el trabajo.",
        "Documentar es dejar registro de cómo se hizo algo. Una buena documentación tiene una ficha con los materiales, las herramientas usadas, los pasos, el problema que apareció y cómo se resolvió. Se agregan al menos tres imágenes: una del inicio, una del proceso y una del resultado final. Una imagen digital es una imagen guardada en un computador o celular, como una foto.",
        "Al sacar fotos, pide ayuda a un adulto. No fotografíes a personas sin permiso. Si no hay cámara, haz un dibujo de cada etapa. Al escribir la ficha, usa frases cortas y claras. La autoría es tuya: en la ficha cuenta qué decisiones tomaste.",
    ],
    [("solución técnica", "objeto que resuelve un problema con materiales y procedimientos"), ("documentar", "dejar registro de cómo se hizo algo"), ("fotografía", "procedimiento que registra imágenes con una cámara"), ("imagen digital", "imagen guardada en un computador o celular"), ("autoría", "ser quien creó y decidió la obra")],
    [
        w("Un problema para resolver", "Tu lápiz se cae de la mesa. Quieres un soporte de cartón. ¿Qué materiales y herramientas eliges?", ["Un rollo de cartón para sostener los lápices.", "Una base de cartón firme.", "Cinta, cola fría y tijera de punta redonda."], "Rollo, base de cartón, cinta, cola fría y tijera"),
        w("Tres imágenes", "Quieres documentar tu soporte. ¿Qué tres fotos tomas?", ["Una del inicio, con los materiales.", "Una del proceso, uniendo las piezas.", "Una del resultado final."], "Inicio, proceso y resultado"),
    ],
    [
        m("Hacer la obra y no registrar nada del proceso.", "Después no se puede explicar cómo se hizo.", "Toma fotos o haz dibujos de al menos tres etapas."),
        m("Fotografiar a una persona sin su permiso.", "Se invade su privacidad.", "Pide permiso o fotografía solo la obra."),
    ],
    [
        ex("Un soporte de cartón que sostiene lápices resuelve un problema. ¿Es una solución técnica? Responde sí o no.", "Sí", "Resuelve un problema con materiales."),
        ex("¿Con qué herramienta tecnológica se saca una foto de tu obra?", "Con una cámara", "La cámara registra imágenes."),
        ex("Una foto guardada en un celular, ¿es una imagen digital?", "Sí", "Está guardada digitalmente."),
    ],
    [
        ex("¿Qué es documentar? A: dejar registro de cómo se hizo algo. B: botar los materiales.", "A", "Documentar es registrar el proceso."),
        ex("Las tres imágenes de la documentación son: inicio, proceso y… ¿qué?", "Resultado final", "Son inicio, proceso y resultado."),
        ex("¿Qué debe tener una ficha? A: materiales, herramientas, pasos, problema y solución. B: solo el nombre.", "A", "Esos son los elementos de la ficha."),
    ],
    [
        ex("Quieres sostener cinco lápices en un soporte. ¿Qué material usas para el tubo: un rollo de cartón o una hoja suelta?", "Un rollo de cartón", "El rollo da forma de tubo y es firme."),
        ex("Tu soporte se inclina porque la base es muy delgada. ¿Qué cambias: la base por una más firme o el color?", "La base por una más firme", "Una base firme sostiene el soporte."),
        ex("No tienes cámara para documentar. ¿Qué haces: dibujar cada etapa o no registrar nada?", "Dibujar cada etapa", "Los dibujos también documentan."),
    ],
    [
        ex("Una niña documentó solo el resultado final. ¿Qué le falta?", "Fotos o dibujos del inicio y del proceso", "La documentación necesita tres etapas."),
        ex("Un niño dice: «Si pido ayuda para la cámara ya no es mi trabajo». ¿Es correcto?", "No", "La autoría es tuya: tú decides cómo documentar."),
    ],
    [
        arith("Tu ficha tiene 2 fotos del inicio, 3 del proceso y 1 del resultado. ¿Cuántas fotos hay en total?", "2 + 3 + 1", "Se suman las fotos de cada etapa."),
        ex("En tu ficha anotas: «Problema: el soporte se cae. Solución: base más grande». ¿Qué parte de la ficha es la solución?", "Base más grande", "La solución es lo que cambió para resolver el problema."),
    ],
    ex("Quieres un soporte de cartón para el control remoto de tu casa. Lo construyes y lo documentas. ¿Qué haces: tomar fotos del inicio, proceso y resultado, o solo una foto al final?", "Tomar fotos del inicio, proceso y resultado", "Así documentas bien tu trabajo."),
    [
        ex("¿Una solución técnica resuelve un problema?", "Sí", "Esa es su definición."),
        ex("Verdadero o falso: puedes fotografiar a cualquier persona sin permiso.", "Falso", "Debes pedir permiso."),
        ex("¿Qué procedimiento registra imágenes con una cámara?", "Fotografía", "Esa es la definición."),
    ],
    task(
        "Construye UNA solución técnica con materiales reutilizables limpios. Elige: A) un soporte para lápices; B) un portatarjetas; C) un marco para una foto. Documenta con una ficha: materiales, herramientas, pasos, un problema que apareció y cómo lo resolviste. Agrega tres fotos o tres dibujos: inicio, proceso y resultado. Un adulto ayuda con la cámara.",
        "Hice un soporte para lápices con un rollo y una base de cartón. Herramientas: tijera, cinta, cola fría. Problema: se inclinaba. Solución: base más grande. Tres dibujos: inicio, proceso, resultado.",
        ["construye una solución", "completa la ficha", "incluye tres imágenes", "cuenta un problema y su solución"],
        ["objeto construido", "ficha con tres imágenes"],
        ["no registrar el proceso", "fotografiar personas sin permiso"],
        "Reconoce la solución del problema y pide que explique cómo lo descubrió.",
    ),
    "Cuenta a alguien de tu casa qué problema resolvió tu objeto y cuáles pasos seguiste.",
    "Pide a alguien que intente hacer tu objeto con tu ficha y anota qué no quedó claro.",
)

# ================================================================ OA 04
# ---------------------------------------------------------------- Clase 1
lesson(
    OA4, 1,
    "Hoja y lápiz. Las obras de este cuaderno son descripciones inventadas, rotuladas así. Tu docente puede mostrar obras reales locales, chilenas, latinoamericanas y de otros lugares, con su autor o procedencia, para describirlas.",
    "Aprenderé a describir lo que veo en una obra de arte o artesanía, sin interpretar todavía. Sirve para mirar con atención antes de opinar.",
    ["Sé nombrar líneas, colores, formas y texturas.", "Sé que hay distintos tipos de obras."],
    [
        "Una obra es algo creado por una persona para expresar ideas o sentimientos, como una pintura, una escultura, un mural, un grabado o una fotografía. La artesanía son objetos hechos a mano, como un tejido o una olla de greda. Hay obras locales, de tu comunidad; chilenas; latinoamericanas; y de otros lugares del mundo, llamadas universales.",
        "Describir es decir lo que se ve, sin opinar ni adivinar. Usa el lenguaje visual: qué materiales tiene, qué colores, qué líneas, qué formas, qué texturas. «Hay una casa roja con techo triangular y un camino ondulado» describe. «Es una casa triste» interpreta, porque ya incluye una idea sobre lo que se siente. Primero se describe y después se interpreta.",
        "Una buena descripción se puede comprobar: otra persona mira la obra y ve lo mismo. Las obras de este cuaderno son inventadas. Las reales las aporta tu docente, que dirá quién las hizo o de dónde vienen. Un detalle es una parte pequeña de la obra que ayuda a describirla mejor.",
    ],
    [("obra", "algo creado por una persona para expresar ideas o sentimientos"), ("artesanía", "objeto hecho a mano con técnicas tradicionales"), ("describir", "decir lo que se ve, sin opinar"), ("detalle", "parte pequeña de una obra"), ("lenguaje visual", "línea, color, forma y textura usados en una obra")],
    [
        w("Describir un tejido", "Obra 1 (inventada, artesanía local): un tejido de lana con rombos rojos y negros en filas y flecos en los bordes. ¿Cómo lo describes?", ["Material: lana.", "Colores: rojo y negro.", "Formas: rombos en filas, con flecos en los bordes."], "Tejido de lana con rombos rojos y negros en filas y flecos"),
        w("Separar describir de interpretar", "¿Cuál es una descripción: «Hay tres ojos grandes y una boca ancha» o «Está enojado»?", ["La primera dice lo que se ve.", "La segunda dice una idea sobre lo que siente.", "Describir es decir lo que se ve."], "«Hay tres ojos grandes y una boca ancha»"),
    ],
    [
        m("Decir «es triste» cuando se pide describir.", "Eso ya es una interpretación.", "Di qué colores, formas y líneas hay."),
        m("Decir solo «es linda» o «es fea».", "No nombra nada que se vea.", "Nombra materiales, colores, líneas, formas y texturas."),
    ],
    [
        ex("Obra 1 (inventada): tejido de lana con rombos rojos y negros. ¿De qué material es?", "De lana", "La descripción dice lana."),
        ex("Obra 2 (inventada, olla de greda): una olla redonda de color tierra con aves dibujadas en el cuello. ¿Qué hay dibujado en el cuello?", "Aves", "El texto nombra aves."),
        ex("Obra 3 (inventada, arte universal): una escultura de mármol blanco de una persona sentada. ¿De qué color es el mármol?", "Blanco", "El texto dice mármol blanco."),
    ],
    [
        ex("¿Qué es describir? A: decir lo que se ve. B: decir lo que siente el autor.", "A", "Describir es hablar de lo que se observa."),
        ex("«Hay una casa roja con techo triangular». ¿Es una descripción o una interpretación?", "Una descripción", "Dice lo que se ve."),
        ex("«Es una casa triste». ¿Es una descripción o una interpretación?", "Una interpretación", "Incluye una idea sobre cómo se siente."),
    ],
    [
        ex("Obra 4 (inventada, mural latinoamericano): un mural con figuras grandes de personas, colores fuertes y líneas gruesas. Nombra una línea del lenguaje visual que aparece.", "Líneas gruesas", "El texto dice líneas gruesas."),
        ex("Obra 5 (inventada, pintura chilena): un paisaje con un cerro azul, un río con curvas y un cielo amarillo. ¿Qué forma tiene el río?", "Con curvas", "El texto dice que tiene curvas."),
        ex("¿Qué tipo de obra es una olla de greda hecha a mano: artesanía o fotografía?", "Artesanía", "Está hecha a mano con una técnica tradicional."),
    ],
    [
        ex("Una niña dice «La escultura es bonita, me gusta». ¿Describe lo que se ve?", "No", "No nombra colores, formas ni materiales."),
        ex("Un niño dice «El mural tiene mucho rojo y figuras grandes en el centro». ¿Es una buena descripción?", "Sí", "Dice lo que se ve."),
    ],
    [
        ex("Obra 6 (inventada, tejido andino): una manta con franjas de colores vivos y animales pequeños repetidos. ¿Cuál de estas es una descripción: «hay franjas de colores vivos» o «es muy alegre»?", "Hay franjas de colores vivos", "La primera dice lo que se ve."),
        ex("Obra 7 (inventada, pintura al óleo de otro lugar del mundo): un paisaje de campo con un camino dorado y árboles verdes. ¿Cuántos colores se nombran?", "2", "Se nombran dorado y verde."),
    ],
    ex("Tu docente te muestra una olla de greda de una artesana de tu zona. ¿Qué dices primero: de qué material es y qué formas tiene, o si te parece triste?", "De qué material es y qué formas tiene", "Primero se describe lo que se ve."),
    [
        ex("¿Qué tipo de obra se hace con greda: artesanía o fotografía?", "Artesanía", "La greda se modela a mano."),
        ex("Verdadero o falso: describir es decir lo que se siente.", "Falso", "Describir es decir lo que se ve."),
        ex("En esta clase, ¿qué es una obra universal?", "Una obra de otros lugares del mundo", "La clase llama universales a las obras de otros lugares del mundo."),
    ],
    task(
        "Elige UNA obra inventada de la lista: A) un tejido de lana con rombos rojos y negros; B) un mural con figuras grandes y colores fuertes; C) una escultura de mármol blanco de una persona sentada. Escribe cuatro frases que DESCRIBAN: material, colores, formas y líneas o texturas. No escribas lo que sientes ni lo que pensó el autor. Marca si es obra local o chilena, latinoamericana o universal, según el rótulo.",
        "Elegí el tejido. Es de lana. Tiene rombos rojos y negros en filas. Hay flecos en los bordes. Es una artesanía chilena inventada para este cuaderno.",
        ["usa al menos cuatro frases", "nombra material, colores y formas", "no interpreta ni opina", "dice el tipo de obra"],
        ["cuatro frases de descripción"],
        ["usar palabras como «bonito» o «triste»", "no nombrar el material"],
        "Reconoce la descripción más precisa y pide que cambie una opinión por un detalle visible.",
    ),
    "Mira un objeto de tu casa y descríbelo en voz alta sin decir si te gusta o no.",
    "Con tu docente, describe una obra real de tu comunidad y anota quién la hizo.",
)

# ---------------------------------------------------------------- Clase 2
lesson(
    OA4, 2,
    "Hoja y lápiz. Las obras de este cuaderno son inventadas. Tu docente puede mostrar obras reales de tu comunidad, de Chile, de Latinoamérica y del mundo, con su autor o procedencia.",
    "Aprenderé a relacionar lo que veo en una obra (colores, líneas, formas) con lo que siento al mirarla. Sirve para decir lo que siento con razones.",
    ["Sé describir lo que veo en una obra.", "Sé que las sensaciones se pueden explicar."],
    [
        "Cuando miramos una obra, sentimos algo. Esa sensación viene de lo que vemos: los colores, las líneas, las formas y las texturas. Una obra con líneas quebradas y colores oscuros puede darte inquietud. Una con líneas suaves y colores claros puede darte calma. Eso depende de cada persona.",
        "Para relacionar lo que veo con lo que siento, usa esta frase: «Veo… y me hace sentir… porque…». Por ejemplo: «Veo un cielo con colores cálidos y me hace sentir alegría porque me recuerda el sol». Primero va lo que se ve y luego lo que se siente. Así tu sensación tiene una razón visible en la obra.",
        "No hay una sensación correcta o incorrecta: dos personas pueden sentir cosas distintas ante la misma obra. Lo que importa es poder explicar qué parte de la obra te lo hizo sentir. Esto sirve para obras de cualquier tipo: pinturas, murales, esculturas, tejidos y artesanías.",
    ],
    [("sensación", "lo que siento al mirar algo"), ("emoción", "sentimiento como alegría, miedo o calma"), ("lenguaje visual", "línea, color, forma y textura"), ("razón", "motivo que explica lo que pienso o siento"), ("inquietud", "sensación de estar nervioso o intranquilo")],
    [
        w("Armar la frase", "Obra 1 (inventada, pintura chilena): un mar de azules claros y líneas largas y suaves. ¿Qué frase armas para decir que te da calma?", ["Veo: azules claros y líneas largas y suaves.", "Siento: calma.", "Razón: las líneas suaves me recuerdan olas tranquilas."], "Veo azules claros y líneas suaves y me hace sentir calma porque me recuerdan olas tranquilas"),
        w("Otra sensación", "Obra 2 (inventada, mural latinoamericano): líneas quebradas, rojos intensos y figuras apretadas. ¿Qué podrías sentir?", ["Veo líneas quebradas y rojos intensos.", "Para mí, eso se parece a algo agitado.", "Puedo decir inquietud, con esa razón."], "Inquietud, porque veo líneas quebradas y rojos intensos"),
    ],
    [
        m("Decir «me da miedo» sin decir qué parte de la obra lo produce.", "No hay una razón visible.", "Agrega «porque veo…» y nombra el color, la línea o la forma."),
        m("Pensar que hay una sensación correcta para cada obra.", "Se cree que todos deben sentir lo mismo.", "Cada persona puede sentir algo distinto si lo explica."),
    ],
    [
        ex("Obra 1 (inventada): un mar con azules claros y líneas largas y suaves. ¿Qué colores tiene?", "Azules claros", "El texto lo dice."),
        ex("En la frase «Veo… y me hace sentir… porque…», ¿qué va primero: lo que veo o lo que siento?", "Lo que veo", "Primero va la observación."),
        ex("Una obra con líneas quebradas y rojos intensos puede dar inquietud. ¿Es verdad que dos personas podrían sentir algo distinto? Responde sí o no.", "Sí", "No hay una sola sensación correcta."),
    ],
    [
        ex("¿Qué relaciona la clase? A: lo que veo con lo que siento. B: el precio con el tamaño.", "A", "Se relaciona lo visual con la sensación."),
        ex("«Veo un cielo de colores cálidos y me hace sentir alegría porque me recuerda el sol». ¿Cuál es la razón?", "Me recuerda el sol", "La razón va después de «porque»."),
        ex("Líneas largas y suaves con colores claros pueden dar… ¿qué sensación, según la clase?", "Calma", "La clase lo propone como ejemplo."),
    ],
    [
        ex("Obra 3 (inventada, escultura universal): una figura de piedra con líneas curvas y superficie lisa. Dices «me hace sentir calma porque…». ¿Cuál razón se puede ver en la obra: «porque tiene líneas curvas y superficie lisa» o «porque la hizo alguien famoso»?", "Porque tiene líneas curvas y superficie lisa", "La razón debe ser algo visible en la obra."),
        ex("Obra 4 (inventada, tejido andino): franjas de colores vivos que se repiten. ¿Qué parte de la frase falta si dices «me siento alegre»?", "La razón con «porque veo…»", "Falta explicar qué parte de la obra lo produce."),
        ex("Obra 5 (inventada, olla de greda local): una olla redonda y oscura con líneas gruesas. ¿Qué es lo primero que dices?", "Lo que veo", "Siempre se parte describiendo."),
    ],
    [
        ex("Sofía y Luis ven el mismo mural. Ella siente alegría y él siente nerviosismo. Ambos explican con colores y líneas. ¿Están bien?", "Sí", "Ambos dan razones visibles."),
        ex("Marta dice «siento miedo» y no explica nada. ¿Qué le falta?", "Una razón visible en la obra", "Falta el «porque veo…»."),
    ],
    [
        ex("Una obra tiene rojo, naranja y amarillo. Dices: «Veo colores cálidos y me hace sentir energía porque parecen fuego». ¿Cuál es la razón?", "Parecen fuego", "La razón va después de «porque»."),
        ex("Quieres explicar tu sensación ante una pintura chilena de un mar tranquilo. ¿Mencionas las líneas suaves o el precio de la pintura?", "Las líneas suaves", "Se explica con el lenguaje visual."),
    ],
    ex("Tu docente muestra una artesanía de greda de una comunidad de tu región y pregunta: «¿qué sientes?». ¿Respondes «no sé» o armas: «Veo… y me hace sentir… porque…»?", "Armo la frase con Veo… siento… porque…", "Así se da una razón."),
    [
        ex("¿Qué palabra introduce la razón de lo que sientes?", "Porque", "«Porque» introduce la razón."),
        ex("Verdadero o falso: todas las personas deben sentir lo mismo ante una obra.", "Falso", "Cada una puede sentir algo distinto."),
        ex("¿De qué depende la sensación que da una obra?", "De lo que se ve", "De colores, líneas, formas y texturas."),
    ],
    task(
        "Elige UNA obra inventada: A) mar de azules claros y líneas largas y suaves (chilena); B) mural de líneas quebradas y rojos intensos (latinoamericano); C) escultura de piedra con líneas curvas y superficie lisa (universal). Escribe la frase «Veo… y me hace sentir… porque…» dos veces: una con tu sensación y otra imaginando la de otra persona. Usa el rótulo de procedencia.",
        "Elegí el mar chileno inventado. Veo azules claros y líneas largas y me hace sentir calma porque me recuerda olas tranquilas. Otra persona podría sentir aburrimiento porque ve pocos detalles.",
        ["usa la frase completa", "nombra lo que ve", "da una razón", "imagina otra sensación posible"],
        ["dos frases completas"],
        ["decir solo la sensación", "no usar «porque»"],
        "Reconoce la razón visible y pregunta qué otro detalle cambiaría su sensación.",
    ),
    "Mira un objeto de tu casa y di en voz alta una frase «Veo… y me hace sentir… porque…».",
    "Con tu docente, mira una obra real y escribe tu frase y la de un compañero para compararlas.",
)

# ---------------------------------------------------------------- Clase 3
lesson(
    OA4, 3,
    "Hoja y lápiz. Las obras de este cuaderno son inventadas. Tu docente puede mostrar obras reales con su autor, y puede decir qué se sabe de la obra y qué no.",
    "Aprenderé a decir lo que pienso de una obra y a apoyarlo con detalles que se ven. Sirve para dar una interpretación que otra persona pueda comprobar.",
    ["Sé describir lo que veo.", "Sé decir lo que siento con una razón."],
    [
        "Interpretar es decir qué pienso que significa o cuenta una obra. Una buena interpretación se apoya en evidencia: detalles que se ven en la obra. Usa esta frase: «Pienso que… porque veo…». Por ejemplo: «Pienso que la escena es una fiesta, porque veo personas con las manos unidas y banderines de colores».",
        "Cuidado con adivinar lo que quiso decir el autor. Si el docente no entrega esa información, no puedes saberlo. Mejor di «yo pienso» o «a mí me parece». Una interpretación no es una opinión sin base. Tampoco hay una sola interpretación válida: varias pueden servir si cada una tiene detalles que la apoyan.",
        "Para fundamentar una idea, busca al menos dos detalles de la obra. Si tu idea no tiene detalles que la respalden, revisa si la obra realmente muestra eso. Esto sirve para obras locales, chilenas, latinoamericanas y universales, y también para la artesanía.",
    ],
    [("interpretar", "decir qué pienso que cuenta o significa una obra"), ("evidencia", "detalle que se ve y apoya una idea"), ("fundamentar", "apoyar una idea con razones y evidencia"), ("autor", "persona que creó la obra"), ("suposición", "idea que no se puede comprobar")],
    [
        w("Interpretar con evidencia", "Obra 1 (inventada, mural latinoamericano): personas con las manos unidas y banderines de colores en un patio. ¿Qué interpretas?", ["Veo manos unidas y banderines.", "Los banderines suelen estar en fiestas.", "Pienso que es una fiesta, porque veo manos unidas y banderines de colores."], "Pienso que es una fiesta, porque veo manos unidas y banderines"),
        w("Cuidar con el autor", "Alguien dice: «El autor quiso mostrar que estaba triste». ¿Cómo lo cambias?", ["No sé lo que sintió el autor.", "Puedo decir lo que yo pienso.", "Digo: «Yo pienso que se ve tristeza, porque veo colores grises y una figura sola»."], "Yo pienso que se ve tristeza, porque veo colores grises y una figura sola"),
    ],
    [
        m("Decir «El autor quiso decir…» sin saber nada de él.", "No se puede comprobar lo que no se sabe.", "Di «yo pienso» y apoya con detalles que se ven."),
        m("Dar una interpretación sin ningún detalle.", "No tiene evidencia.", "Agrega al menos dos detalles que se ven en la obra."),
    ],
    [
        ex("Obra 1 (inventada): personas con las manos unidas y banderines. ¿Qué dos detalles hay?", "Manos unidas y banderines", "El texto nombra ambos."),
        ex("En la frase «Pienso que… porque veo…», ¿qué va después de «porque veo»?", "Los detalles", "Después va la evidencia."),
        ex("Una evidencia es un detalle que… ¿qué hace?", "Apoya una idea", "Sirve para respaldar lo que pienso."),
    ],
    [
        ex("¿Qué es interpretar? A: decir qué pienso que cuenta una obra. B: copiar una obra.", "A", "Interpretar es dar una idea sobre el significado."),
        ex("Un niño dice: «El autor quiso mostrar su miedo». Si nadie le dijo nada del autor, ¿qué debería decir?", "Yo pienso…", "No puede saber lo que sintió el autor."),
        ex("¿Hay una sola interpretación válida de una obra?", "No", "Varias pueden servir si tienen evidencia."),
    ],
    [
        ex("Obra 2 (inventada, pintura chilena): un cerro grande, una casa pequeña abajo y un camino que sube. Frase: «Pienso que la casa es pequeña frente al cerro, porque veo…». ¿Qué detalle completa la frase?", "Un cerro grande y una casa pequeña", "Es lo que muestra la obra."),
        ex("Obra 3 (inventada, escultura universal): una figura de piedra con los brazos abiertos. ¿Qué detalle apoya la idea de «recibir»?", "Los brazos abiertos", "Se ven abiertos."),
        ex("Obra 4 (inventada, artesanía local): una canasta con flores tejidas. Si dices «pienso que es para guardar cosas», ¿qué detalle apoya esa idea?", "Que es una canasta", "La forma de canasta sirve para guardar."),
    ],
    [
        ex("Ana dice: «Es una fiesta», pero no da ningún detalle. ¿Qué le falta?", "Evidencia", "Debe nombrar detalles que se ven."),
        ex("Dos niños dan interpretaciones distintas de la misma obra y ambos nombran detalles. ¿Pueden ser ambas válidas?", "Sí", "Ambas están apoyadas en evidencia."),
    ],
    [
        ex("Quieres fundamentar «es una fiesta» con tres detalles: manos unidas, banderines y colores vivos. ¿Cuántos detalles tienes?", "3", "Se nombran tres detalles distintos."),
        ex("Dices: «Pienso que es de noche, porque el cielo es azul oscuro y hay una luna». ¿Cuántas evidencias nombras?", "2", "El cielo oscuro y la luna."),
    ],
    ex("Tu docente muestra una pintura de una escena de campo y dice que el autor es desconocido. Un compañero dice «el autor estaba feliz». ¿Qué le dices: «no lo sabemos» o «sí, seguro»?", "No lo sabemos", "No se puede saber lo que sentía el autor."),
    [
        ex("¿Qué frase usas para fundamentar tu idea?", "Pienso que… porque veo…", "Esa es la frase de la clase."),
        ex("Verdadero o falso: se puede saber siempre lo que quiso decir el autor.", "Falso", "Solo si el docente lo informa."),
        ex("¿Cuántos detalles conviene nombrar al menos?", "Dos", "La clase dice al menos dos detalles."),
    ],
    task(
        "Elige UNA obra inventada: A) mural latinoamericano de personas con manos unidas y banderines; B) pintura chilena de un cerro grande y una casa pequeña; C) canasta tejida con flores (artesanía local). Escribe «Pienso que… porque veo…» con al menos DOS detalles. No digas qué quiso el autor, salvo si tu docente lo informó. Di si la obra es local o chilena, latinoamericana o universal.",
        "Elegí la pintura chilena inventada. Pienso que la casa se ve pequeña frente al cerro, porque veo un cerro grande que ocupa casi toda la hoja y una casa diminuta abajo.",
        ["usa la frase completa", "nombra al menos dos detalles", "no adivina al autor", "dice el tipo de obra"],
        ["una interpretación fundamentada"],
        ["dar una idea sin detalles", "decir lo que quiso el autor sin saberlo"],
        "Reconoce la evidencia más clara y pregunta si otra interpretación podría apoyarse en los mismos detalles.",
    ),
    "Mira un dibujo tuyo y di «Pienso que… porque veo…» sobre lo que cuenta.",
    "Con tu docente, mira una obra real y escribe dos interpretaciones distintas con sus detalles.",
)

# ---------------------------------------------------------------- Clase 4
lesson(
    OA4, 4,
    "Hoja y lápiz. Las obras de este cuaderno son inventadas. Tu docente puede mostrar obras reales locales, chilenas, latinoamericanas y universales con su autor o procedencia, y organizar la actividad de comparar.",
    "Aprenderé a comparar mis respuestas con las de otras personas y a comparar obras de distintos lugares. Sirve para entender que una obra puede provocar ideas distintas y que todas necesitan razones.",
    ["Sé describir, sentir con razón e interpretar con evidencia.", "Sé escuchar a otros."],
    [
        "Cuando varias personas miran la misma obra, sus respuestas pueden ser distintas. Una puede sentir calma y otra energía. Comparar respuestas es escuchar a otros y ver qué se parece y qué es diferente, y si cada una tiene razones. Las respuestas distintas no son errores si se apoyan en lo que se ve.",
        "También se pueden comparar obras de distintos lugares: una artesanía local, una pintura chilena, un mural latinoamericano y una escultura universal. Se comparan sus materiales, colores, formas y la sensación que dan. Por ejemplo: «Ambas usan colores de tierra, pero una es de cerámica y la otra, un mural». Las semejanzas y las diferencias se dicen con el lenguaje visual.",
        "Al comparar, respeta a las demás personas y a las obras. No digas que una obra es mejor solo por venir de un lugar. Cada obra se hizo en un contexto y con materiales distintos. Lo importante es mirar con atención, explicar con razones y escuchar. Cada año se observan varias obras de arte y artesanía local y chilena, latinoamericanas y de arte universal; en tu curso tu docente las irá mostrando.",
    ],
    [("comparar", "mirar qué se parece y qué es diferente"), ("semejanza", "algo que se parece"), ("diferencia", "algo que no se parece"), ("contexto", "lugar y tiempo en que se hizo una obra"), ("respeto", "tratar con cuidado a las personas y a sus ideas")],
    [
        w("Comparar dos respuestas", "Ante el mismo mural (inventado), Rosa dice: «Siento energía, porque veo rojos y líneas gruesas». Pedro dice: «Siento inquietud, porque veo líneas quebradas y figuras apretadas». ¿Qué comparas?", ["Las dos respuestas son distintas.", "Las dos nombran lo que ven.", "Ambas son válidas porque tienen razones."], "Son distintas, pero ambas tienen razones"),
        w("Comparar dos obras", "Obra A (inventada, olla de greda local): color tierra, forma redonda. Obra B (inventada, mural latinoamericano): colores fuertes, figuras grandes. ¿Qué comparas?", ["Colores: tierra frente a fuertes.", "Formas: redonda frente a figuras grandes.", "Tipo: artesanía frente a mural."], "Colores y formas distintas, tipo de obra distinto"),
    ],
    [
        m("Decir que la opinión del compañero está mal solo porque es distinta.", "No se mira si tiene razones.", "Pregunta qué detalle vio y compara."),
        m("Decir que una obra es mejor solo por venir de otro lugar.", "Se compara por origen y no por lo que se ve.", "Compara materiales, colores y formas."),
    ],
    [
        ex("Rosa siente energía por los rojos. Pedro siente inquietud por las líneas quebradas. ¿Sus respuestas son iguales?", "No", "Sienten cosas distintas."),
        ex("Comparar es mirar qué se parece y qué es… ¿qué?", "Diferente", "Se comparan semejanzas y diferencias."),
        ex("Obra A (inventada): olla de greda, color tierra y redonda. ¿Cuál es su color?", "Tierra", "El texto lo dice."),
    ],
    [
        ex("¿Qué es una semejanza? A: algo que se parece. B: algo que no se parece.", "A", "Semejanza es parecido."),
        ex("Dos respuestas distintas ante la misma obra, ambas con razones visibles. ¿Son válidas?", "Sí", "Ambas se apoyan en lo que se ve."),
        ex("Un mural y una olla de greda, ¿son del mismo tipo de obra?", "No", "Uno es mural y la otra, artesanía."),
    ],
    [
        ex("Obra C (inventada, pintura chilena): azul y verde, líneas suaves. Obra D (inventada, escultura universal): piedra gris, líneas rectas. ¿Qué diferencia hay en las líneas?", "Suaves frente a rectas", "El texto da esas líneas."),
        ex("Obra E (inventada, tejido andino) y obra F (inventada, mural latinoamericano) usan colores vivos. ¿Qué tienen en común?", "Colores vivos", "Ambas usan colores vivos."),
        ex("Comparas la olla de greda local con una vasija universal inventada, ambas redondas. ¿Qué semejanza nombras?", "La forma redonda", "Ambas son redondas."),
    ],
    [
        ex("Luis dice: «La obra de mi país es mejor que todas las demás». ¿Compara por lo que se ve?", "No", "Compara por origen, no por la obra."),
        ex("Ema escucha a un compañero que ve algo distinto y le pregunta qué detalle vio. ¿Hace una buena comparación?", "Sí", "Escucha y busca razones."),
    ],
    [
        ex("Comparas tres obras: una local, una latinoamericana y una universal. ¿Cuántas obras comparas?", "3", "Se cuentan tres elementos distintos."),
        ex("Dos niñas hacen cinco frases cada una para comparar. ¿Cuántas frases escriben en total?", "10", "5 + 5 = 10.", "5 + 5"),
    ],
    ex("En tu curso, dos compañeros ven un tejido chileno inventado. Uno siente calma y el otro, energía. Los dos explican con detalles. Tu docente pregunta: «¿cuál tiene razón?». ¿Qué respondes: «ambos, si dan razones» o «solo uno»?", "Ambos, si dan razones", "Cada uno puede sentir distinto si lo explica."),
    [
        ex("¿Qué tipo de diferencias se pueden comparar en dos obras?", "Materiales, colores y formas", "Son elementos del lenguaje visual."),
        ex("Verdadero o falso: comparar obras es decir cuál lugar es mejor.", "Falso", "Se comparan semejanzas y diferencias."),
        ex("¿Qué debes hacer cuando otra persona tiene una opinión distinta?", "Escucharla", "El respeto es parte de comparar."),
    ],
    task(
        "Elige DOS obras inventadas: una de la lista A (local o chilena: tejido de lana con rombos o olla de greda con aves) y una de la lista B (latinoamericana o universal: mural de figuras grandes y colores fuertes o escultura de mármol blanco). Escribe dos semejanzas y dos diferencias usando el lenguaje visual. Agrega una frase: «Una persona podría sentir… y otra…», con una razón para cada una.",
        "Comparé el tejido de lana (chilena inventada) y el mural (latinoamericano inventado). Semejanzas: los dos tienen colores fuertes y formas bien marcadas. Diferencias: uno es de lana, con rombos en filas, y el otro es una pintura en un muro, con figuras de personas. Una persona podría sentir calma por el orden de los rombos, y otra, energía por los rojos.",
        ["compara dos obras", "dos semejanzas y dos diferencias", "usa el lenguaje visual", "da razones para dos respuestas posibles"],
        ["lista de semejanzas y diferencias", "una frase de dos respuestas"],
        ["decir que una obra es mejor por su origen", "no dar razones"],
        "Reconoce la comparación mejor justificada y pregunta qué semejanza no había notado.",
    ),
    "Con alguien de tu casa, mira un objeto de arte o de artesanía y compara qué siente cada uno y por qué.",
    "Con tu docente, compara una obra local con una universal real y registra una semejanza y una diferencia.",
)

# ================================================================ OA 05
# ---------------------------------------------------------------- Clase 1
lesson(
    OA5, 1,
    "Hoja, lápiz y los criterios escritos en este cuaderno. Usa un trabajo tuyo o un trabajo inventado descrito aquí. No uses trabajos de compañeros sin su permiso.",
    "Aprenderé a elegir criterios que se puedan observar para comentar un trabajo de arte. Sirve para dar y recibir comentarios claros y respetuosos.",
    ["Sé describir lo que veo en una obra.", "Sé usar materiales y herramientas de arte."],
    [
        "Un criterio es una pregunta o una característica que usamos para mirar un trabajo. Un criterio observable es algo que se puede ver o comprobar, como «el pegamento está firme» o «hay tres colores». Decir «es lindo» o «tiene talento» no es observable, porque depende del gusto y no habla del trabajo.",
        "Para comentar un trabajo de arte usamos tres tipos de criterios. Primero, el material: cómo se usó el material, por ejemplo si la pintura cubrió bien o si el papel quedó firme. Segundo, el procedimiento técnico: cómo se hizo, por ejemplo si los cortes son parejos o si las uniones aguantan. Tercero, el propósito expresivo: si el trabajo muestra lo que su autor quería expresar.",
        "Los criterios se acuerdan antes de comentar. Así todos miran lo mismo y se evita opinar por gusto personal. Se comenta el trabajo, no a la persona: no se habla de su cuerpo, su personalidad ni su talento. Cada criterio debe ser claro, observable y respetuoso.",
    ],
    [("criterio", "característica que uso para mirar un trabajo"), ("observable", "que se puede ver o comprobar"), ("propósito expresivo", "lo que el autor quiere mostrar o hacer sentir"), ("procedimiento técnico", "cómo se hizo un trabajo"), ("retroalimentación", "comentario para ayudar a mejorar un trabajo")],
    [
        w("Convertir una opinión en criterio", "Alguien dice: «Tu collage es lindo». ¿Cómo lo convertimos en un criterio observable?", ["«Lindo» depende del gusto.", "Puedo mirar algo que se ve, como el pegado.", "Criterio: «Las piezas están pegadas firmes y sin burbujas»."], "Las piezas están pegadas firmes y sin burbujas"),
        w("Tres tipos de criterios", "Para una pintura sobre calma: ¿qué criterio de material, de procedimiento y de propósito escribes?", ["Material: la témpera cubre bien el fondo.", "Procedimiento: los bordes no se pasaron.", "Propósito: los colores y las líneas suaves se relacionan con la calma."], "Cubre el fondo, bordes limpios, colores y líneas de calma"),
    ],
    [
        m("Comentar con «me gusta» o «no me gusta».", "Depende del gusto y no habla del trabajo.", "Usa un criterio que se pueda observar."),
        m("Comentar a la persona («eres buena», «eres malo para dibujar»).", "Se juzga a la persona y no el trabajo.", "Habla del trabajo: qué se ve y cómo se hizo."),
    ],
    [
        ex("«El pegamento está firme y sin burbujas». ¿Es un criterio observable? Responde sí o no.", "Sí", "Se puede mirar y comprobar."),
        ex("«Es muy lindo». ¿Es un criterio observable? Responde sí o no.", "No", "Depende del gusto personal."),
        ex("Un criterio sobre el material es «la témpera cubre bien el fondo». ¿Habla de material, de procedimiento o de propósito?", "Material", "Habla de cómo se usó la pintura."),
    ],
    [
        ex("¿Qué es un criterio observable? A: algo que se puede ver o comprobar. B: algo que me gusta.", "A", "Observable es lo que se puede comprobar."),
        ex("«Los cortes del cartón son parejos». ¿Es un criterio de material o de procedimiento técnico?", "De procedimiento técnico", "Habla de cómo se cortó."),
        ex("«Los colores suaves muestran calma». ¿Es un criterio de propósito?", "Sí", "Relaciona lo visual con lo que se quería expresar."),
    ],
    [
        ex("Quieres un criterio observable para un collage. Entre «tiene talento» y «tiene tres papeles distintos», ¿cuál eliges?", "Tiene tres papeles distintos", "Se puede contar y comprobar."),
        ex("Escribe qué tipo de criterio es: «La pintura no se corrió fuera de los bordes».", "De procedimiento técnico", "Habla de cómo se pintó."),
        ex("Para una escultura de plasticina, ¿cuál es mejor criterio de procedimiento: «las partes están bien unidas» o «es mi favorita»?", "Las partes están bien unidas", "Se puede observar y comprobar."),
    ],
    [
        ex("Mauro dice: «Tu dibujo es feo porque tú no sabes dibujar». ¿Qué está mal?", "Habla de la persona y no del trabajo", "Se debe comentar el trabajo con criterios."),
        ex("Eva dice: «Primero acordemos los criterios y después comentamos». ¿Es buena idea?", "Sí", "Así todos miran lo mismo."),
    ],
    [
        ex("Acuerdas tres criterios: uno de material, uno de procedimiento y uno de propósito. ¿Cuántos criterios son?", "3", "Se cuentan tres elementos distintos."),
        ex("Un criterio dice «tiene como mínimo cuatro colores». Tu trabajo tiene tres. ¿Cumple?", "No", "Tres es menos que cuatro."),
    ],
    ex("Tu curso va a comentar los trabajos de arte de todos. Antes de empezar, ¿qué hacen: acordar los criterios o decir cada uno lo que le gusta?", "Acordar los criterios", "Los criterios se acuerdan antes de comentar."),
    [
        ex("¿Los criterios se acuerdan antes o después de comentar?", "Antes", "Así todos miran lo mismo."),
        ex("Verdadero o falso: «es lindo» es un criterio observable.", "Falso", "Depende del gusto."),
        ex("¿Se comenta el trabajo o a la persona?", "El trabajo", "Se habla de lo que se ve."),
    ],
    task(
        "Escribe TRES criterios observables para comentar este trabajo inventado: «Un collage de un mar con papel de lustre azul, olas de cartulina cortadas con tijera y un sol de papel de diario rasgado; busca expresar calma». Un criterio de material, uno de procedimiento y uno de propósito. Cada uno debe poder comprobarse mirando el trabajo.",
        "Material: el fondo está hecho con papel de lustre azul. Procedimiento: las olas de cartulina están cortadas con tijera. Propósito: los azules se relacionan con la calma.",
        ["escribe tres criterios", "uno de cada tipo", "cada uno es observable", "no habla de la persona"],
        ["tres criterios escritos"],
        ["usar «lindo» o «feo»", "hablar de la persona"],
        "Reconoce el criterio más observable y pide que reescriba uno que dependa del gusto.",
    ),
    "Elige un objeto de tu casa y di en voz alta un criterio observable para comentarlo.",
    "Con tu docente, acuerden tres criterios para un trabajo del curso antes de comentarlo.",
)

# ---------------------------------------------------------------- Clase 2
lesson(
    OA5, 2,
    "Hoja, lápiz y los trabajos inventados descritos en este cuaderno. Puedes usar un trabajo tuyo. No uses trabajos de compañeros sin su permiso.",
    "Aprenderé a reconocer una fortaleza de un trabajo de arte y a explicarla con evidencia. Sirve para decir qué está bien hecho y por qué.",
    ["Sé elegir criterios observables.", "Sé describir lo que veo en un trabajo."],
    [
        "Una fortaleza es algo que está bien logrado en un trabajo. Para reconocerla, usa un criterio: de material, de procedimiento técnico o de propósito expresivo. Luego da la evidencia, es decir, el detalle que se ve y la muestra. Usa esta frase: «Una fortaleza es… porque se ve que…».",
        "Por ejemplo: «Una fortaleza es el uso del pegamento, porque se ve que todas las piezas están firmes y sin burbujas». O: «Una fortaleza es el propósito de calma, porque se ve que los azules claros y las líneas suaves hacen sentir tranquilidad». La fortaleza se dice del trabajo, no de la persona.",
        "Reconocer fortalezas con evidencia ayuda a quien hizo el trabajo a saber qué repetir. También ayuda a aprender para tus propios trabajos. Evita decir solo «está bien» o «es lindo». Busca el detalle concreto. Si no encuentras una fortaleza clara, vuelve a mirar el trabajo con los criterios acordados.",
    ],
    [("fortaleza", "algo que está bien logrado en un trabajo"), ("evidencia", "detalle que se ve y lo demuestra"), ("criterio", "característica que uso para mirar un trabajo"), ("lograr", "conseguir hacer bien algo"), ("repetir", "volver a hacer algo que funcionó")],
    [
        w("Fortaleza de material", "Trabajo inventado: un collage de papel donde todas las piezas están pegadas firmes y sin burbujas. ¿Cuál es la fortaleza y su evidencia?", ["Criterio: uso del pegamento.", "Fortaleza: pegado firme.", "Evidencia: todas las piezas firmes y sin burbujas."], "Una fortaleza es el pegado, porque se ve que todas las piezas están firmes y sin burbujas"),
        w("Fortaleza de propósito", "Trabajo inventado: una pintura con azules claros y líneas suaves que busca expresar calma. ¿Cuál es la fortaleza?", ["Criterio: propósito expresivo.", "Fortaleza: logra calma.", "Evidencia: azules claros y líneas suaves."], "Una fortaleza es el propósito de calma, porque se ven azules claros y líneas suaves"),
    ],
    [
        m("Decir solo «está bien» como fortaleza.", "No nombra qué está bien ni cómo se ve.", "Nombra la fortaleza y el detalle que la muestra."),
        m("Decir «eres muy talentoso».", "Se habla de la persona y no del trabajo.", "Habla de lo que se ve en el trabajo."),
    ],
    [
        ex("Una fortaleza es algo bien… ¿qué?", "Logrado", "Una fortaleza es algo bien logrado en el trabajo."),
        ex("En «una fortaleza es el pegado, porque se ve que las piezas están firmes», ¿cuál es la evidencia?", "Las piezas están firmes", "Es el detalle que se ve."),
        ex("¿Qué frase usas para decir una fortaleza?", "Una fortaleza es… porque se ve que…", "Es la frase de la clase."),
    ],
    [
        ex("¿Qué es la evidencia? A: un detalle que se ve y lo demuestra. B: una opinión.", "A", "La evidencia es observable."),
        ex("«Eres muy talentosa». ¿Es una fortaleza del trabajo o un comentario sobre la persona?", "Sobre la persona", "No habla del trabajo."),
        ex("Una pintura tiene bordes limpios, sin manchas fuera de las líneas. ¿Qué criterio es: de procedimiento técnico o de propósito?", "De procedimiento técnico", "Habla de cómo se pintó."),
    ],
    [
        ex("Trabajo inventado: una escultura de plasticina con las partes bien unidas, sin que se caigan. ¿Cuál es la evidencia de la fortaleza «unión»?", "Las partes están bien unidas", "Es lo que se observa."),
        ex("Trabajo inventado: un dibujo con líneas gruesas y rojos intensos que busca expresar fuerza. Para reconocer esa fortaleza, ¿qué tipo de criterio usas: de material, de procedimiento o de propósito?", "De propósito", "Se habla de si el trabajo muestra lo que quería expresar."),
        ex("Trabajo inventado: un collage con cuatro papeles distintos bien combinados. Fortaleza: variedad de materiales. ¿Cuántos papeles son la evidencia?", "4", "El texto dice cuatro."),
    ],
    [
        ex("Pía dice: «Una fortaleza es tu collage, porque sí». ¿Qué le falta?", "El detalle que lo demuestra", "Una fortaleza necesita evidencia."),
        ex("Ignacio dice: «Una fortaleza puede ser cualquier cosa que me guste». ¿Es correcto?", "No", "Debe basarse en un criterio y una evidencia."),
    ],
    [
        ex("En un trabajo hay dos fortalezas con evidencia: una de material y una de propósito. ¿Cuántas fortalezas reconociste?", "2", "Se cuentan dos fortalezas distintas."),
        ex("Dices: «Una fortaleza es el color, porque se ve que los azules son parejos». ¿Qué nombras como evidencia?", "Que los azules son parejos", "Es lo que se ve."),
    ],
    ex("Una compañera te muestra su dibujo de un sol grande y amarillo que busca expresar alegría. ¿Qué dices: «una fortaleza es el propósito de alegría, porque se ve que el sol es grande y amarillo» o «eres muy buena»?", "Una fortaleza es el propósito de alegría, porque se ve que el sol es grande y amarillo", "Se comenta el trabajo con evidencia."),
    [
        ex("¿Una fortaleza se dice del trabajo o de la persona?", "Del trabajo", "Así se evita juzgar a la persona."),
        ex("Verdadero o falso: «está bien» es una buena fortaleza.", "Falso", "No dice qué está bien ni cómo se ve."),
        ex("¿Qué va después de «porque se ve que…»?", "La evidencia", "Ahí va el detalle que se observa."),
    ],
    task(
        "Lee este trabajo inventado: «Un mural de cartulina con cuatro colores vivos, un cerro de papel rasgado y un sol grande de papel de diario; algunas piezas se despegan, pero los colores vivos y el sol grande transmiten alegría». Escribe DOS fortalezas con la frase «Una fortaleza es… porque se ve que…». Una debe ser de propósito. Usa lo que dice el texto.",
        "Una fortaleza es el uso de cuatro colores, porque se ve que hay variedad. Una fortaleza es el propósito de alegría, porque se ve que los colores son vivos y el sol es grande.",
        ["escribe dos fortalezas", "usa la frase completa", "una es de propósito", "la evidencia sale del texto"],
        ["dos frases de fortaleza"],
        ["decir solo «está bien»", "hablar de la persona"],
        "Reconoce la evidencia más precisa y pide que busque otro detalle que la apoye.",
    ),
    "Mira un trabajo tuyo y di en voz alta una fortaleza con su evidencia.",
    "Con tu docente, busca una fortaleza en el trabajo de un compañero que lo permita y díselo con la frase de la clase.",
)

# ---------------------------------------------------------------- Clase 3
lesson(
    OA5, 3,
    "Hoja, lápiz y los trabajos inventados descritos en este cuaderno. Puedes usar un trabajo tuyo. No uses trabajos de compañeros sin su permiso.",
    "Aprenderé a proponer una mejora clara y relacionada con un criterio y con el propósito del trabajo. Sirve para ayudar con respeto a mejorar un trabajo.",
    ["Sé reconocer una fortaleza con evidencia.", "Sé usar criterios observables."],
    [
        "Un aspecto a mejorar es algo del trabajo que se puede hacer mejor. Una mejora coherente es una propuesta concreta que se relaciona con un criterio y con el propósito del trabajo. Se dice con la frase: «Podrías… para que…». Por ejemplo: «Podrías poner menos pegamento para que el papel no se arrugue».",
        "Una buena propuesta tiene tres partes. Primero, el aspecto: lo que se ve que se puede mejorar, con evidencia. Segundo, la acción: algo concreto que se puede hacer. Tercero, el motivo: para qué ayuda, ligado al propósito. «Mejora tu dibujo» no dice nada. «Podrías hacer más grande el sol para que se note la alegría» sí.",
        "Antes de proponer una mejora, reconoce una fortaleza. Habla con respeto del trabajo, no de la persona, y no hagas el trabajo del otro: tú sugieres y la autora o el autor decide. Una mejora debe ser posible con los materiales que tiene.",
    ],
    [("aspecto a mejorar", "algo del trabajo que se puede hacer mejor"), ("mejora coherente", "propuesta concreta ligada a un criterio y al propósito"), ("propuesta", "idea que ofrezco a otra persona"), ("autor", "persona que hizo el trabajo"), ("concreto", "claro y que se puede hacer")],
    [
        w("Armar una propuesta", "Trabajo inventado: un collage con papel arrugado por exceso de cola fría. Propósito: calma. ¿Qué propones?", ["Aspecto: el papel está arrugado por demasiada cola.", "Acción: usar menos cola o pegamento en barra.", "Motivo: para que se vea parejo, como se necesita para calma."], "Podrías usar menos cola, para que el papel quede parejo y se note la calma"),
        w("Mejora no coherente", "Alguien dice: «Cambia todo el dibujo». ¿Por qué no sirve?", ["No dice qué cambiar.", "No tiene motivo.", "Se parece más a hacer el trabajo del otro."], "No es concreta ni tiene motivo"),
    ],
    [
        m("Decir «mejora tu dibujo» sin explicar cómo.", "No es concreto ni tiene motivo.", "Usa «Podrías… para que…»."),
        m("Proponer una mejora que no tiene que ver con el propósito.", "Puede cambiar lo que el autor quería expresar.", "Liga la mejora con el propósito del trabajo."),
    ],
    [
        ex("En «Podrías… para que…», ¿qué va después de «para que»?", "El motivo", "Explica para qué sirve la mejora."),
        ex("Un collage tiene papel arrugado por demasiada cola. ¿Cuál es el aspecto a mejorar?", "El papel arrugado", "Es lo que se ve que no quedó bien."),
        ex("«Podrías usar menos cola para que el papel quede parejo». ¿Es una propuesta concreta? Responde sí o no.", "Sí", "Dice qué hacer y para qué."),
    ],
    [
        ex("¿Qué tiene una buena propuesta? A: aspecto, acción y motivo. B: solo «mejora».", "A", "Las tres partes la hacen clara."),
        ex("«Cambia todo el dibujo». ¿Es una mejora coherente?", "No", "No es concreta ni tiene motivo."),
        ex("¿Quién decide si se acepta la propuesta: quien propone o el autor del trabajo?", "El autor del trabajo", "La autoría es de quien hizo el trabajo."),
    ],
    [
        ex("Trabajo inventado: un dibujo de un volcán con líneas muy suaves, y el autor quiere expresar fuerza. ¿Qué propones: usar líneas más gruesas y marcadas o usar más colores claros?", "Usar líneas más gruesas y marcadas", "Se relaciona con el propósito de fuerza."),
        ex("Trabajo inventado: un collage con piezas que se despegan. ¿Qué acción propones: usar cola fría en los bordes o cambiar el tema?", "Usar cola fría en los bordes", "Es concreta y resuelve el problema visible."),
        ex("Trabajo inventado: una pintura con colores todos mezclados y sucios. ¿Qué propones: lavar el pincel entre colores o pintar más rápido?", "Lavar el pincel entre colores", "Evita que los colores se ensucien."),
    ],
    [
        ex("Ana dice: «Mejora porque no me gusta». ¿Qué le falta?", "Una acción concreta y un motivo", "Falta «podrías…» y «para que…»."),
        ex("Beto propone pintar de rojo intenso un dibujo hecho para expresar calma. La autora dice que para ella el rojo intenso es agitado. ¿La propuesta ayuda a su propósito?", "No", "Según la autora, el rojo intenso es agitado y no ayuda a la calma."),
    ],
    [
        ex("Una propuesta tiene aspecto, acción y motivo. ¿Cuántas partes tiene?", "3", "Se cuentan tres elementos distintos."),
        ex("Reconoces una fortaleza y propones una mejora. ¿Cuántos comentarios hiciste?", "2", "Una fortaleza y una mejora."),
    ],
    ex("Tu compañero te muestra un dibujo con el sol muy pequeño, y quiere expresar alegría. ¿Dices: «hazlo todo de nuevo» o «podrías hacer el sol más grande para que se note la alegría»?", "Podrías hacer el sol más grande para que se note la alegría", "Es concreta y ligada al propósito."),
    [
        ex("¿Qué frase usas para proponer una mejora?", "Podrías… para que…", "Es la frase de la clase."),
        ex("Verdadero o falso: antes de proponer una mejora conviene reconocer una fortaleza.", "Verdadero", "Eso se recomienda."),
        ex("¿Debe una propuesta ser concreta?", "Sí", "Debe poder hacerse."),
    ],
    task(
        "Lee este trabajo inventado: «Una pintura de un lago con los bordes limpios, que ocupa el centro de la hoja; el propósito es expresar calma; usó colores cálidos muy intensos y las pinceladas se mezclaron, y la pintura quedó sucia». Escribe: una fortaleza con evidencia y UNA propuesta de mejora con «Podrías… para que…». La mejora debe ayudar a la calma y ser posible con pintura y pincel.",
        "Una fortaleza es el contorno del lago, porque se ve que sus bordes están limpios. Podrías lavar el pincel entre colores y usar colores fríos claros para que se note más la calma.",
        ["escribe una fortaleza con evidencia", "propone una mejora concreta", "la mejora se liga al propósito", "no habla de la persona"],
        ["una fortaleza", "una propuesta con aspecto, acción y motivo"],
        ["decir solo «mejora»", "una mejora que no ayuda al propósito"],
        "Reconoce la propuesta más concreta y pide que explique cómo ayuda al propósito.",
    ),
    "Mira un trabajo tuyo y di en voz alta una mejora con «Podrías… para que…».",
    "Con tu docente, propón una mejora a un trabajo inventado distinto y compara con una compañera.",
)

# ---------------------------------------------------------------- Clase 4
lesson(
    OA5, 4,
    "Hoja, lápiz, un trabajo tuyo (o uno inventado descrito aquí) y una hoja para anotar el «antes» y el «después». No uses trabajos de compañeros sin su permiso.",
    "Aprenderé a decidir qué sugerencias aceptar para mejorar mi trabajo, conservando mis ideas. Sirve para aprender de otros sin perder lo que quiero expresar.",
    ["Sé reconocer fortalezas.", "Sé proponer mejoras con «Podrías… para que…»."],
    [
        "Revisar una obra es volver a trabajarla después de recibir comentarios. La autoría es de quien creó el trabajo: tú decides qué cambiar y qué mantener. Escuchar la retroalimentación no significa hacer todo lo que te dicen. Piensa: ¿esta sugerencia ayuda a mi propósito expresivo?",
        "Sigue estos pasos. Primero, escucha sin interrumpir. Segundo, elige las sugerencias que se relacionan con tus criterios y con tu propósito. Tercero, haz los cambios y deja lo que ya era una fortaleza. Cuarto, anota el «antes» y el «después» con una frase que diga qué cambió y por qué. Si no aceptas una sugerencia, explica con respeto por qué.",
        "Conservar la autoría también significa no copiar la idea de otro y decir que es tuya. Si alguien te dio una idea que usaste, puedes decirlo. La revisión no es borrar y empezar de nuevo, sino mejorar con cuidado. Agradece los comentarios aunque no los uses todos.",
    ],
    [("revisar", "volver a trabajar algo para mejorarlo"), ("autoría", "ser quien creó y decide el trabajo"), ("sugerencia", "idea que otra persona me ofrece"), ("antes y después", "registro de cómo era el trabajo y cómo quedó"), ("agradecer", "decir gracias por algo que otro hizo por mí")],
    [
        w("Elegir sugerencias", "Tu dibujo busca expresar calma. Te sugieren: A) «Usa líneas más suaves»; B) «Pinta todo de rojo fuerte». ¿Cuál aceptas?", ["Mi propósito es calma.", "La A ayuda a la calma.", "La B va contra mi propósito."], "Acepto la A y explico con respeto por qué no la B"),
        w("Antes y después", "Antes: colores sucios. Después: lavaste el pincel y quedaron limpios. ¿Qué anotas?", ["Antes: colores mezclados y sucios.", "Después: colores limpios.", "Motivo: lavé el pincel entre colores."], "Antes: colores sucios. Después: limpios porque lavé el pincel"),
    ],
    [
        m("Hacer todo lo que te dicen, aunque no ayude a tu propósito.", "Se pierde la idea propia.", "Elige las sugerencias que ayudan a lo que quieres expresar."),
        m("Rechazar todas las sugerencias sin escucharlas.", "No se aprende de los comentarios.", "Escucha y decide con razones."),
    ],
    [
        ex("¿Quién decide qué sugerencias usar en un trabajo: el autor o quien da el comentario?", "El autor", "La autoría es de quien creó el trabajo."),
        ex("Tu propósito es calma. Te sugieren líneas más suaves. ¿Ayuda a tu propósito?", "Sí", "Las líneas suaves se relacionan con la calma."),
        ex("En el registro, ¿qué dos palabras marcan los momentos antes de cambiar y después de cambiar?", "Antes y después", "Así se anota el cambio."),
    ],
    [
        ex("¿Qué es revisar un trabajo? A: volver a trabajarlo para mejorarlo. B: botarlo y empezar de cero.", "A", "Revisar es mejorar con cuidado."),
        ex("Si no aceptas una sugerencia, ¿qué haces: explicar con respeto por qué o ignorar a la persona?", "Explicar con respeto por qué", "Se agradece y se explica."),
        ex("¿Qué dos cosas dice la frase del registro de cambio?", "Qué cambió y por qué", "Así se justifica."),
    ],
    [
        ex("Tu propósito es mostrar fuerza. Para ti las líneas gruesas son fuertes y los azules muy claros son suaves. Te sugieren: A) «Usa líneas gruesas»; B) «Usa solo azules muy claros». ¿Cuál aceptas?", "A", "Las líneas gruesas ayudan a la fuerza."),
        ex("Tu trabajo tiene una fortaleza: los colores parejos. Al revisarlo, ¿qué haces con esa fortaleza: mantenerla o cambiarla?", "Mantenerla", "Se deja lo que ya era una fortaleza."),
        ex("Un amigo te dio una idea que usaste. ¿Qué haces: decir que fue idea tuya o decir de quién fue?", "Decir de quién fue", "Conservar la autoría incluye ser honesto."),
    ],
    [
        ex("Rita cambió todo su dibujo porque tres personas le dieron ideas distintas y ahora no se parece a lo que quería. ¿Qué no hizo?", "Pensar en su propósito", "Debe elegir según lo que quería expresar."),
        ex("Pablo dice: «No escucho comentarios, mi trabajo ya está perfecto». ¿Aprende de la retroalimentación?", "No", "No escucha ni revisa."),
    ],
    [
        ex("Recibes cuatro sugerencias y aceptas dos. ¿Cuántas no aceptas?", "2", "4 − 2 = 2.", "4 - 2"),
        ex("Tu registro tiene un antes, un después y un motivo. ¿Cuántas partes anotaste?", "3", "Se cuentan tres elementos distintos."),
    ],
    ex("En clase, una compañera te sugiere cambiar el color de tu mar para que se vea más tranquilo. Tu propósito es justamente tranquilidad. ¿Qué haces: considerarlo y probar en una hoja o rechazarlo sin pensar?", "Considerarlo y probar en una hoja", "Ayuda a tu propósito."),
    [
        ex("¿La autoría de tu trabajo es de quien lo creó?", "Sí", "El autor decide."),
        ex("Verdadero o falso: hay que aceptar todas las sugerencias.", "Falso", "Se eligen las que ayudan al propósito."),
        ex("¿Qué anotas para registrar un cambio?", "El antes y el después", "Muestra qué cambió."),
    ],
    task(
        "Lee este trabajo inventado: «Una pintura de un bosque hecha para expresar misterio; los colores oscuros son una fortaleza; las pinceladas están sucias; recibió tres sugerencias: A) lavar el pincel entre colores; B) pintar todo de amarillo intenso; C) dejar más espacio oscuro entre los árboles». Escribe qué sugerencias aceptarías (puedes aceptar más de una), cuáles no y por qué, y completa un registro: «Antes… Después… Cambié… porque…». Mantén la fortaleza.",
        "Acepto A y C porque ayudan al misterio. No acepto B porque el amarillo intenso quita lo misterioso. Antes: pinceladas sucias. Después: limpias. Cambié lavando el pincel porque así los colores oscuros se ven más limpios. Mantuve los colores oscuros.",
        ["elige sugerencias según el propósito", "explica las que no acepta", "completa el registro", "mantiene la fortaleza"],
        ["decisión sobre cada sugerencia", "registro antes y después"],
        ["aceptar todas sin pensar", "borrar la fortaleza"],
        "Reconoce la decisión con razones y pregunta qué dejó igual para conservar su idea.",
    ),
    "Piensa en un comentario que te hayan dado y di en voz alta si ayuda a lo que querías expresar.",
    "Revisa un trabajo tuyo, anota el antes y el después, y cuéntaselo a alguien de tu casa.",
)
