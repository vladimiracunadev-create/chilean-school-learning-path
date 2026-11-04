"""Cuaderno del estudiante de 1.º medio Artes Visuales: AR1M OA 02 (imaginarios personales, grabado y pintura mural con materiales sustentables)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA2 = "AR1M OA 02"


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


# ---------------------------------------------------------------- Clase 1
lesson(
    OA2, 1,
    "Hojas, lápiz de mina y lápices de colores. Las dos fichas (un grabado y un mural de ejemplo) están escritas en esta clase; no necesitas buscar imágenes.",
    "Aprenderé qué son el grabado y el mural, para qué se usan y cómo mi imaginario personal puede ser el punto de partida. Sirve para elegir una técnica según lo que quiero decir y a quién.",
    ["Sé que una obra se lee por su contexto, su lenguaje visual y su propósito.", "Sé separar un dato observable de una inferencia."],
    [
        "El grabado es un procedimiento para hacer una imagen en una matriz, que es una placa (de cartón, madera u otro material) que se entinta y se presiona sobre papel. De una misma matriz salen varias copias casi iguales, llamadas edición. Un número como 5/20 indica que esa copia es la quinta de una edición de veinte. La pintura mural, en cambio, se hace sobre un muro y se ve en el lugar donde está, muchas veces en la calle.",
        "Cada técnica tiene un propósito distinto. El grabado multiplica una imagen para regalarla, venderla o repartirla, y se mira de cerca, en las manos. El mural llega a mucha gente que pasa y no entra a ningún lugar, y se mira a distancia, por eso usa figuras grandes y planos de color. Mi imaginario personal es el conjunto de imágenes, recuerdos y símbolos con que veo el mundo, como una escalera de mi casa o el cerro que veo cada mañana. Es el punto de partida de mi obra.",
        "Al leer una ficha separo datos de inferencias. «Impreso en negro sobre papel claro» es un dato. «La artista siente que su casa la vigila» es una inferencia: la ficha no lo dice. Cuando trabajo con mi imaginario cuido mi privacidad: uso símbolos y no muestro datos personales ni rostros de otras personas. Elegir entre grabado y mural es una decisión: pregunto quién va a verlo, desde dónde y cuántas veces.",
    ],
    [("matriz", "placa que se entinta para imprimir una imagen en papel"), ("edición", "serie de copias hechas con la misma matriz"), ("mural", "pintura hecha sobre un muro, visible en el lugar donde está"), ("imaginario personal", "conjunto de imágenes, recuerdos y símbolos propios con que alguien ve el mundo"), ("plano de color", "zona de color uniforme y sin degradado")],
    [
        w("Leer dos fichas", "Ficha de ejemplo del grabado: huella en negro sobre papel claro de 15 cm de lado, una casa pequeña dentro de un ojo enorme, matriz de cartón, copia 5/20. Ficha de ejemplo del mural: 6 m de largo por 3 m de alto, en un muro exterior, pintura para exteriores, cuatro colores en planos grandes. ¿Dónde se ve cada uno?", ["El grabado mide poco y se sostiene en la mano, se ve de cerca.", "El mural mide 6 m por 3 m en un muro exterior, se ve a distancia y desde la calle.", "Por eso el mural usa planos de color grandes."], "El grabado se ve de cerca y el mural a distancia desde la calle"),
        w("Dato o inferencia", "De la ficha del grabado, una compañera escribe: «Fue hecho por alguien que tiene miedo». ¿Qué es su frase?", ["La ficha solo dice qué se ve y cómo se hizo.", "No menciona ninguna emoción de la artista."], "Es una inferencia sin respaldo en la ficha"),
    ],
    [
        m("Pensar que un grabado es una copia exacta de una pintura.", "El grabado es un procedimiento propio: la imagen nace en la matriz.", "Piensa en la matriz primero y en la copia como resultado de imprimirla."),
        m("Elegir la técnica sin pensar en quién va a ver la obra.", "Un mural sirve a distancia y un grabado de cerca; si no se piensa, el mensaje no se lee.", "Pregunta quién lo verá, desde dónde y cuántas veces."),
    ],
    [
        ex("En el grabado, ¿qué es la matriz? A. La placa que se entinta para imprimir B. El papel donde queda la imagen.", "A", "La matriz es la placa; el papel recibe la imagen impresa."),
        ex("Un grabado dice «7/15». ¿Qué significa? A. Es la copia número 7 de una edición de 15 B. Se hicieron 7 copias de 15 colores.", "A", "El primer número es el de la copia y el segundo el total de la edición."),
        ex("Un mural de 8 m por 4 m está en un muro exterior frente a una calle ancha. ¿Desde dónde se ve mejor, de cerca o a distancia?", "A distancia", "Es muy grande y se hace para quien pasa por la calle."),
    ],
    [
        ex("¿Qué es un imaginario personal? A. Imágenes, recuerdos y símbolos propios con que alguien ve el mundo B. Una técnica de pintura sobre muros.", "A", "Es un conjunto de referencias de la propia vida; no es una técnica."),
        ex("Quieres que lo vea mucha gente que pasa por la calle sin entrar a ningún lugar. ¿Qué eliges: un mural o un grabado guardado en una carpeta?", "Un mural", "El mural está en el lugar donde pasa la gente; la carpeta solo la ve quien la abre."),
        ex("Ficha: «Escalera que sube hacia una ventana, tinta azul sobre papel kraft». ¿Cuál es una inferencia? A. La artista quiere escapar de su casa B. La tinta es azul.", "A", "La ficha no habla de lo que quiere la artista; el color de la tinta sí lo dice."),
    ],
    [
        arith("Otro mural de ejemplo mide 7 m de largo por 3 m de alto. ¿Cuántos metros cuadrados tiene?", "7 * 3", "El área de un rectángulo es largo por alto.", " m²"),
        arith("De una edición planeada de 20 copias, 3 salieron manchadas y se descartan. ¿Cuántas copias buenas quedan?", "20 - 3", "Se restan las copias descartadas del total.", " copias"),
        ex("Un mural de ejemplo usa tres colores en planos grandes y está en un muro exterior. ¿Cuál es un rasgo de lenguaje visual? A. Tres colores en planos grandes B. Está en un muro exterior.", "A", "Los planos de color son parte de cómo se ve; el muro exterior es el contexto."),
    ],
    [
        ex("Una artista quiere que su imagen se lea desde la vereda de enfrente, a 20 m de distancia. ¿Qué decisión sirve? A. Figuras grandes en planos de color B. Líneas muy finas de 1 mm.", "A", "A esa distancia solo se distinguen formas grandes; las líneas de 1 mm desaparecen."),
        ex("¿Qué ventaja tiene el grabado que no tiene el mural? A. Permite hacer varias copias iguales para repartir B. Se ve desde lejos.", "A", "La matriz se imprime muchas veces; el mural es una sola obra y se ve a distancia."),
    ],
    [
        arith("Un mural de 18 m² lo pintan 3 personas y cada una avanza 2 m² por hora. ¿Cuántas horas tardan?", "18 // (3 * 2)", "Primero se calcula cuánto pintan las tres juntas por hora y luego se divide el área.", " horas"),
        ex("Una estudiante dibuja una escalera de su casa en todos sus bocetos. En su obra esa escalera es... A. un símbolo recurrente de su imaginario personal B. un error de composición.", "A", "Repetir una imagen propia con sentido es parte de un imaginario, no un error."),
    ],
    ex("Tu liceo ofrece un muro exterior de 5 m por 3 m y una prensa casera de cuchara para grabado. Tu imaginario es una casa dentro de un ojo; quieres que lo vea el barrio y que cada vecino pueda llevarse una copia. ¿Qué haces? A. Pinto el mural en el muro y hago un grabado en serie para repartir B. Solo pinto una hoja pequeña y la guardo.", "A", "El mural llega al barrio y el grabado en serie se puede repartir; guardar la hoja no cumple ninguno de los dos propósitos."),
    [
        ex("¿Cómo se llama el conjunto de copias hechas con la misma matriz?", "Edición", "Todas salen de la misma placa."),
        ex("Verdadero o falso: un grabado se hace directamente sobre un muro.", "Falso", "El grabado se hace con una matriz que se imprime sobre papel; el mural se pinta en el muro."),
        ex("¿Qué se pregunta para elegir entre grabado y mural?", "Quién lo verá, desde dónde y cuántas veces", "Así la técnica sirve al mensaje."),
    ],
    task(
        "Elige UN imaginario de ejemplo. A) Una escalera de casa que siempre sube hacia una ventana. B) El cerro que se ve desde tu patio en distintas horas. C) Un mercado de barrio con toldos de colores. Haz dos bocetos pequeños del mismo imaginario: uno pensado como grabado de 10 cm y otro como mural de 6 m por 3 m. Anota en cada uno quién lo vería, desde dónde y por qué cambiaste la imagen. Usa solo símbolos, sin personas reconocibles ni datos personales.",
        "Elegí la A. Grabado: escalera pequeña en negro con muchos detalles, para mirar de cerca. Mural: escalera enorme en dos colores planos, para verse desde la calle. Cambié los detalles por planos grandes porque se ve a distancia y no entrega ningún dato personal.",
        ["hace dos bocetos del mismo imaginario", "adapta la imagen a cada técnica", "anota quién ve cada obra y desde dónde", "usa símbolos sin datos personales"],
        ["dos bocetos", "nota de público y distancia"],
        ["repetir el mismo dibujo sin adaptarlo", "mostrar datos personales o rostros"],
        "Pregunta qué cambió entre ambos bocetos y por qué ese cambio ayuda a quien mira.",
    ),
    "Cuenta a una persona de tu casa en qué se diferencian un grabado y un mural y cuál elegirías para tu barrio.",
    "Anota tres símbolos de tu imaginario que podrías usar sin mostrar datos personales y di cuál se vería mejor en un mural.",
)

# ---------------------------------------------------------------- Clase 2
lesson(
    OA2, 2,
    "Hojas, lápiz de mina, cartón y papel limpios, y un envase limpio de plástico. Las fichas de materiales de ejemplo están escritas en esta clase; no necesitas comprar nada.",
    "Aprenderé a investigar el origen, el uso y el descarte de los materiales de grabado y pintura mural y a decidir cuáles son más sustentables. Sirve para crear sin dañar el ambiente ni gastar de más.",
    ["Sé que el grabado usa una matriz y que el mural se pinta en un muro.", "Sé comparar materiales por durabilidad y mantención."],
    [
        "Un material sustentable se puede usar sin agotar recursos ni dañar el ambiente. Para decidir investigo tres cosas en una ficha: su origen (de dónde viene y si es nuevo o reutilizado), su uso (qué tan bien sirve para mi técnica) y su descarte (qué pasa cuando lo dejo de usar). Reutilizar es darle otro uso a algo sin transformarlo, como un cartón de caja como matriz. Reciclar es transformar un material en otro nuevo.",
        "En grabado sirven el cartón de caja usado, el papel de diario y las pinturas o tintas a base de agua. Los restos de papel se separan para reciclar y los pinceles se lavan en un recipiente, no se vacían restos de pintura por el desagüe. En pintura mural conviene una pintura al agua, que se limpia con agua, y pigmentos de tierra de color. Una unión reversible, como cinta de papel o un engrudo de harina y agua, se puede despegar sin dañar; una unión permanente, como un pegamento fuerte, no.",
        "Cuando una ficha no dice un dato, no lo invento: lo marco como pendiente y lo investigo. Tampoco confundo «sustentable» con «feo» o «barato»: puedo lograr buenas imágenes con cartón y tinta al agua. Y evito los materiales que no sé si son seguros: uso solo lo que se puede manipular sin riesgo en casa, sin solventes, sin vidrio y sin herramientas filudas.",
    ],
    [("sustentable", "que se puede usar sin agotar recursos ni dañar el ambiente"), ("reutilizar", "dar otro uso a algo sin transformarlo"), ("reciclar", "transformar un material usado en un material nuevo"), ("unión reversible", "forma de unir piezas que se puede deshacer sin dañarlas"), ("pigmento", "sustancia que da color a una pintura")],
    [
        w("Ficha de origen, uso y descarte", "Material de ejemplo: cartón de una caja de embalaje ya usada. Origen: reutilizado; uso: matriz de grabado en relieve; descarte: se recicla si queda limpio y sin tinta. ¿Es una buena opción sustentable?", ["Origen: reutilizado, no se compra nada nuevo.", "Uso: sirve para recortar formas y entintar.", "Descarte: se puede reciclar si se limpia."], "Sí: es reutilizado, sirve para la técnica y se puede reciclar"),
        w("Unión reversible o permanente", "Para fijar un cartón sobre una base de prueba, ¿qué eliges: engrudo de harina y agua o pegamento fuerte?", ["Quiero reutilizar la base después de la prueba.", "El engrudo de harina y agua se despega con humedad sin dañar el cartón.", "El pegamento fuerte no se despega."], "Engrudo de harina y agua, porque es reversible"),
    ],
    [
        m("Creer que un material es sustentable solo porque es barato.", "El precio no dice nada sobre su origen ni su descarte.", "Revisa la ficha de origen, uso y descarte antes de decidir."),
        m("Lavar los pinceles y vaciar los restos de pintura por el desagüe.", "Los restos de pintura contaminan el agua.", "Limpia lo que puedas con papel, lava los pinceles en un recipiente y guarda los restos para reutilizar."),
    ],
    [
        ex("Un material de ejemplo es papel de diario guardado de la semana pasada. ¿Cuál es su origen? A. Reutilizado B. Recién fabricado.", "A", "El diario ya tuvo un uso antes; no se fabricó para esta obra."),
        ex("En materiales sustentables, ¿qué diferencia hay entre reutilizar y reciclar?", "Reutilizar es dar otro uso sin transformar y reciclar es transformar el material en otro", "En el primero el objeto sigue siendo el mismo; en el segundo cambia."),
        ex("Un engrudo de harina y agua es una unión que se deshace con humedad. ¿Es reversible o permanente?", "Reversible", "Se puede despegar sin dañar las piezas."),
    ],
    [
        ex("Para lavar un pincel con pintura al agua, ¿qué es lo adecuado? A. Limpiarlo con papel y luego lavarlo en un recipiente B. Vaciar la pintura por el desagüe.", "A", "El recipiente evita que la pintura vaya directo al agua; el desagüe la contamina."),
        ex("Ficha de ejemplo de un envase de plástico limpio: origen reutilizado, uso como paleta, descarte reciclable si queda limpio. ¿Cuál es su uso?", "Servir de paleta", "El uso es lo que la ficha dice que se hace con el material."),
        ex("Una ficha no dice cuánto dura una pintura de ejemplo sobre un muro. ¿Qué haces? A. Marco el dato como pendiente y lo investigo B. Escribo una duración que me parece posible.", "A", "Un dato que falta se investiga; no se inventa."),
    ],
    [
        arith("Una ficha de ejemplo puntúa cada material con 1 punto por origen reutilizado, 1 por buen uso y 1 por descarte reciclable. El cartón tiene los tres y un envase tiene origen y uso. ¿Cuántos puntos suman entre los dos?", "3 + 2", "El cartón suma 3 y el envase suma 2.", " puntos"),
        ex("Dos matrices de ejemplo: A) cartón de caja usada, B) una placa nueva comprada para una sola prueba. Con origen y descarte, ¿cuál es más sustentable?", "La A", "La caja ya existía y se puede reciclar; la placa nueva gasta un recurso nuevo."),
        ex("Quieres un pigmento sustentable y a mano. ¿Cuál sirve? A. Tierra de color molida con agua y engrudo B. Un solvente fuerte con pintura sintética.", "A", "La tierra de color y el engrudo son seguros y se manipulan en casa; un solvente no es seguro ni sustentable."),
    ],
    [
        ex("Un compañero dice: «Mi obra es sustentable porque usé cartón, aunque pegué todo con un pegamento permanente y boté los restos de pintura al desagüe». ¿Qué parte de su afirmación falla?", "El descarte y la unión, porque contaminó y no se puede reutilizar", "Sustentable se juzga por origen, uso y descarte, no solo por el cartón."),
        ex("Ficha de ejemplo: «Pintura al agua para exteriores, sin solventes, se limpia con agua. Para ser reciclable su envase debe quedar limpio». ¿Qué dato de la ficha apoya su carácter sustentable? A. Se limpia con agua B. Es para exteriores.", "A", "Limpiarse con agua evita solventes; ser para exteriores habla de su uso, no de su impacto."),
    ],
    [
        ex("Para tu obra tienes una ficha de ejemplo: tierra de color (origen natural, uso como pigmento, descarte se devuelve a la tierra) y un colorante en spray (origen sintético, uso fácil, descarte difícil). Quieres decidir con origen y descarte. ¿Cuál eliges?", "La tierra de color", "Su origen es natural y su descarte es simple; el spray tiene descarte difícil."),
        arith("Una matriz de 15 cm de lado se recorta de una hoja de cartón de 45 cm de lado. ¿Cuántas matrices cuadradas caben en una fila de la hoja?", "45 // 15", "Se divide el lado de la hoja entre el lado de la matriz.", " matrices"),
    ],
    ex("Tu curso tiene una caja de cartón, restos de papel de diario, un envase de plástico limpio y tierra de color. Debes hacer una prueba de grabado y una de mural con lo que hay, sin comprar nada. ¿Qué haces con cada uno? A. Matriz con el cartón, papel de diario para probar la impresión, el envase para mezclar el pigmento B. Compro placas y pintura nuevas para empezar de cero y boto lo que hay.", "A", "Usa solo lo disponible y reutilizable; comprar y botar no es sustentable."),
    [
        ex("¿Qué tres datos tiene la ficha de un material en esta clase?", "Origen, uso y descarte", "Con ellos se decide si el material es sustentable."),
        ex("Verdadero o falso: un material barato siempre es sustentable.", "Falso", "El precio no dice nada de su origen ni de su descarte."),
        ex("¿Cuál es una unión reversible? A. Cinta de papel B. Pegamento fuerte.", "A", "La cinta de papel se despega sin dañar las piezas."),
    ],
    task(
        "Elige UN material de ejemplo. A) Cartón de caja usada. B) Papel de diario. C) Un envase de plástico limpio. Completa una ficha con origen, uso y descarte (si falta un dato, márcalo pendiente). Luego haz dos pruebas pequeñas con él: una de textura para grabado (frotar con lápiz sobre el cartón o el papel) y otra de color (mezclar harina, agua y un poco de témpera en el envase). Decide si lo usarías en tu obra y justifica.",
        "Elegí A, cartón de caja usada. Origen: reutilizado. Uso: matriz de grabado en relieve. Descarte: reciclable si queda limpio. Prueba de textura: al frotar con lápiz se marca bien la superficie corrugada. Prueba de color: la mezcla de témpera con harina cubre bien. Lo usaría porque es reutilizado y se puede reciclar.",
        ["completa origen, uso y descarte", "marca como pendiente un dato que falta", "hace dos pruebas distintas", "decide con las pruebas y la ficha"],
        ["ficha de material", "dos pruebas pequeñas", "decisión justificada"],
        ["inventar datos de la ficha", "juzgar solo por el precio"],
        "Pregunta qué dato de la ficha pesó más en su decisión y cuál dejó pendiente.",
    ),
    "Busca en tu casa un envase limpio y di su origen, un posible uso en tu obra y su descarte.",
    "Compara dos materiales que conozcas con origen, uso y descarte y decide cuál usarías para un mural y por qué.",
)

# ---------------------------------------------------------------- Clase 3
lesson(
    OA2, 3,
    "Hojas, lápiz de mina, lápices de colores, regla, cartón y papel limpios. Los casos de prueba están escritos en esta clase; no necesitas buscar nada.",
    "Aprenderé a probar decisiones en grabado y en mural: imagen invertida, entintado, presión y ampliación de un boceto. Sirve para anticipar errores antes de hacer la obra final.",
    ["Sé que una matriz permite una edición.", "Sé elegir materiales con origen, uso y descarte."],
    [
        "Al imprimir una matriz la imagen sale invertida, como en un espejo. Si armo la palabra SOL en la matriz con tiras de cartón pegadas, debo ponerla al revés para que se lea bien en el papel. Lo mismo pasa con una flecha que apunta a la derecha en la matriz: en la copia apunta a la izquierda. En un grabado en relieve lo que queda en alto se entinta y se imprime; lo que recorto queda sin tinta y deja el color del papel.",
        "El entintado y la presión también deciden el resultado. Con poca tinta la imagen sale pálida y con huecos; con demasiada se empasta y se pierden los detalles. Una presión pareja, hecha con el dorso de una cuchara de madera o con la mano plana, da una copia limpia. Por eso hago pruebas de estado: copias de ensayo, que se numeran o se marcan como prueba y se guardan para comparar antes de la edición.",
        "Para pasar un boceto pequeño a un muro grande uso una cuadrícula. Divido el boceto en cuadros iguales y el muro en la misma cantidad de cuadros, más grandes. El factor de ampliación es la medida del muro dividida entre la medida del boceto. Si el boceto mide 20 cm de largo y el muro 400 cm, el factor es 400 ÷ 20 = 20: cada centímetro del boceto se vuelve 20 cm en el muro.",
    ],
    [("imagen invertida", "imagen que sale al revés, como en un espejo, al imprimir una matriz"), ("relieve", "parte de la matriz que queda en alto y recibe la tinta"), ("prueba de estado", "copia de ensayo que se hace antes de la edición para revisar el resultado"), ("cuadrícula", "red de cuadros iguales para trasladar una imagen a otro tamaño"), ("factor de ampliación", "número por el que se multiplica el boceto para llegar al tamaño del muro")],
    [
        w("Escribir al revés", "Quieres que en la copia impresa se lea la letra R de «RÍO». ¿Cómo debe quedar la R en la matriz?", ["Al imprimir, la imagen se invierte como en un espejo.", "Para que se lea bien en el papel, debo armarla invertida en la matriz.", "La R debe quedar invertida en la matriz."], "La R debe ir invertida (en espejo) en la matriz"),
        w("Ampliar con cuadrícula", "Boceto de 25 cm de largo y muro de 500 cm de largo. ¿Cuál es el factor de ampliación y cuánto medirá en el muro una casa que en el boceto mide 4 cm?", ["Factor: 500 ÷ 25 = 20.", "La casa: 4 × 20 = 80 cm."], "Factor 20; la casa mide 80 cm"),
    ],
    [
        m("Armar la palabra al derecho en la matriz.", "Al imprimir sale invertida y no se puede leer.", "Arma la palabra invertida en la matriz y comprueba con un espejo."),
        m("Ampliar un boceto a ojo, sin cuadrícula.", "Las proporciones cambian y el dibujo se deforma.", "Usa una cuadrícula y multiplica cada medida por el factor de ampliación."),
    ],
    [
        ex("Al imprimir una matriz, ¿cómo sale la imagen respecto a lo que hay en la matriz? A. Invertida, como en un espejo B. Igual.", "A", "La impresión da vuelta la imagen; por eso se talla invertida lo que debe leerse."),
        ex("En un grabado en relieve, ¿qué parte de la matriz recibe la tinta?", "La parte que queda en alto", "La tinta solo toca lo que sobresale."),
        ex("Una copia sale pálida y con huecos. ¿Qué pudo faltar? A. Tinta o presión B. Un papel más grande.", "A", "Poca tinta o poca presión dejan la imagen incompleta."),
    ],
    [
        ex("Una flecha apunta a la derecha en tu matriz. ¿Hacia dónde apunta en la copia impresa?", "Hacia la izquierda", "La impresión invierte la imagen como un espejo."),
        arith("Un boceto mide 30 cm de largo y tu muro mide 450 cm. ¿Cuál es el factor de ampliación?", "450 // 30", "Se divide el largo del muro entre el del boceto.", ""),
        ex("¿Para qué sirve una prueba de estado? A. Para revisar la imagen antes de hacer la edición B. Para vender la copia.", "A", "Permite corregir entintado y presión antes de las copias finales."),
    ],
    [
        arith("En el boceto, una ventana mide 3 cm de ancho y el factor de ampliación es 15. ¿Cuántos centímetros medirá en el muro?", "3 * 15", "Cada medida del boceto se multiplica por el factor.", " cm"),
        ex("Quieres que en la copia impresa se lea «LUZ». ¿Qué haces en la matriz? A. Pego las letras invertidas, en espejo B. Las pego igual que se leen.", "A", "Al imprimir se invierten; si se tallan invertidas, salen al derecho."),
        ex("Con demasiada tinta, la copia queda con las líneas finas tapadas. ¿Qué haces en la prueba siguiente? A. Entintar con una capa más delgada B. Presionar más fuerte con la cuchara.", "A", "El exceso de tinta empasta los detalles; reducirla los recupera."),
    ],
    [
        ex("Una compañera amplía un boceto de 20 cm a un muro de 340 cm, pero dibuja en el muro una puerta de 4 cm de ancho, la misma medida del boceto. Con el factor correcto, ¿cuánto debe medir la puerta en el muro?", "68 cm", "El factor es 340 ÷ 20 = 17 y 4 × 17 = 68 cm; 4 cm no cambia de tamaño."),
        ex("Dos pruebas de estado del mismo grabado: P1 con poca tinta, P2 con tinta pareja y presión firme. ¿Cuál usas como modelo para la edición y por qué?", "La P2, porque muestra la imagen completa y limpia", "La P1 tiene huecos; la P2 muestra el resultado buscado."),
    ],
    [
        arith("Tu muro mide 600 cm de largo y 300 cm de alto, y tu boceto mide 30 cm de largo. ¿Cuántos centímetros de alto debe medir el boceto para mantener la proporción?", "300 // (600 // 30)", "Primero se calcula el factor, 600 ÷ 30 = 20, y luego se divide la altura del muro entre 20.", " cm"),
        ex("Pegas en la matriz una casa con la puerta en el lado izquierdo. ¿En qué lado queda la puerta en la copia impresa?", "En el lado derecho", "La impresión invierte la imagen como un espejo, así que izquierda y derecha se cambian."),
    ],
    ex("Para el mural de tu curso debes ampliar un boceto de 30 cm de largo a un muro de 540 cm. Una persona dibuja la puerta de 6 cm del boceto como de 80 cm en el muro. ¿Es correcto? A. No, porque 540 ÷ 30 = 18 y 6 × 18 = 108 cm B. Sí, porque 80 es un número redondo.", "A", "El factor es 18 y la puerta debe medir 108 cm para mantener la proporción."),
    [
        ex("¿Qué número se usa para ampliar un boceto a un muro?", "El factor de ampliación", "Es la medida del muro dividida entre la del boceto."),
        ex("Verdadero o falso: en un grabado en relieve, lo que recorto de la matriz deja el color del papel.", "Verdadero", "Sin tinta, queda el color del papel."),
        ex("¿Cómo debes escribir una palabra en la matriz para que se lea bien en la copia?", "Invertida, como en un espejo", "La impresión la devuelve al derecho."),
    ],
    task(
        "Elige UNA prueba. A) Palabra «PUENTE»: arma en un cartón de 15 cm de lado la palabra invertida con tiras de cartón pegadas, recortadas con tijera de punta roma (usa un espejo para comprobar), entinta con témpera o tinta al agua y haz dos copias con presión distinta. B) Cuadrícula: dibuja un boceto de 20 cm de largo con una casa y un árbol, divídelo en cuadros de 2 cm y calcula el factor de ampliación para un muro de 400 cm. C) Entintado: haz tres copias del mismo recorte de cartón con poca, media y mucha tinta. Registra lo que ves y decide qué usarías para la obra final.",
        "Elegí C. Copia 1 con poca tinta: pálida y con huecos. Copia 2 con tinta media: líneas limpias. Copia 3 con mucha tinta: se empastó y tapó los detalles. Para la obra final usaré la tinta media con presión pareja.",
        ["realiza las pruebas con materiales disponibles", "registra lo que observa en cada una", "decide con evidencia de las pruebas", "cuida los materiales y limpia el espacio"],
        ["dos o tres pruebas", "registro escrito de lo observado", "decisión justificada"],
        ["armar la palabra al derecho", "ampliar a ojo"],
        "Pregunta qué diferencia vio entre las pruebas y cuál eligió para la obra final.",
    ),
    "Escribe tu nombre al revés en un papel y míralo en un espejo para comprobar que se lee bien.",
    "Calcula el factor de ampliación para pasar un boceto de 24 cm a un muro de 480 cm y ubica tres elementos de tu boceto en el muro.",
)

# ---------------------------------------------------------------- Clase 4
lesson(
    OA2, 4,
    "Hojas, lápiz de mina, regla, lápices de colores, cartón y papel limpios. Los datos de los dos encargos de ejemplo están escritos en esta clase; no necesitas buscar nada.",
    "Aprenderé a desarrollar una propuesta propia de grabado o mural basada en mi imaginario personal, con materiales sustentables y un plan de trabajo. Sirve para pasar de una idea a una obra que se pueda hacer.",
    ["Sé que una imagen impresa sale invertida y que un boceto se amplía con cuadrícula.", "Sé decidir un material con origen, uso y descarte."],
    [
        "Una propuesta de grabado o mural parte de mi imaginario, pasa por una técnica y se concreta en un plan. El plan responde cuatro preguntas: qué imagen hago, con qué técnica, con qué materiales sustentables y cuánto necesito. Calcular lo que necesito evita comprar de más. Para una edición cuento las copias finales más las pruebas de estado. Para un mural calculo el área del muro y cuánta pintura cubre cada litro; ese dato se llama rendimiento.",
        "Un ejemplo de cálculo (con datos de ejemplo): un muro de 4 m por 3 m tiene 12 m². Si cada litro de pintura rinde 6 m² por mano y planeo dos manos, necesito 12 × 2 ÷ 6 = 4 litros. Para un mural preparo primero el muro: se limpia, se repara y se prepara con la base que indique quien conoce el muro, para que la pintura se pegue. Todo mural exige permiso de quien administra el muro y se deja el lugar limpio al terminar.",
        "Una buena propuesta es coherente: la técnica sirve al imaginario y los materiales sirven a la técnica. Si mi imagen es de detalles finos, el grabado en cartón se adapta mejor; si es de planos grandes, el mural. Anoto qué cambiaría en una versión siguiente. Y cuido mi autoría: si tomo un recurso de un referente, lo declaro y lo transformo, no lo copio.",
    ],
    [("rendimiento", "cuántos metros cuadrados cubre un litro de pintura"), ("mano de pintura", "cada capa de pintura que se aplica sobre una superficie"), ("coherencia", "relación lógica entre la idea, la técnica y los materiales"), ("plan de trabajo", "lista ordenada de pasos, materiales y cantidades para hacer una obra"), ("permiso", "autorización de quien administra un lugar para intervenirlo")],
    [
        w("Calcular pintura", "Datos de ejemplo: muro de 4 m por 3 m, pintura que rinde 6 m² por litro en cada mano, dos manos. ¿Cuántos litros necesitas?", ["Área: 4 × 3 = 12 m².", "Dos manos: 12 × 2 = 24 m² de pintado.", "Litros: 24 ÷ 6 = 4."], "4 litros"),
        w("Plan de edición", "Quieres una edición de 8 copias buenas y calculas 3 pruebas de estado. ¿Cuántas hojas de papel necesitas si cada copia usa una hoja?", ["Copias finales: 8.", "Pruebas: 3.", "Total: 8 + 3 = 11 hojas."], "11 hojas"),
    ],
    [
        m("Calcular la pintura sin multiplicar por el número de manos.", "Una sola mano rara vez cubre bien un muro.", "Multiplica el área por las manos y luego divide entre el rendimiento."),
        m("Empezar a pintar el muro sin limpiarlo ni pedir permiso.", "La pintura se despega y se interviene un lugar ajeno.", "Pide permiso, limpia y repara el muro antes de pintar."),
    ],
    [
        ex("En una propuesta, ¿qué es el rendimiento de una pintura? A. Cuántos metros cuadrados cubre un litro B. Cuánto cuesta un litro.", "A", "El rendimiento mide la superficie cubierta, no el precio."),
        ex("¿Qué se hace primero con un muro antes de pintarlo? A. Limpiarlo y repararlo B. Dibujar con pintura.", "A", "Un muro sucio o dañado no deja que la pintura se pegue bien."),
        ex("¿Quién debe autorizar que pintes un mural en un muro exterior?", "Quien administra el muro", "Un lugar no se interviene sin autorización de su responsable."),
    ],
    [
        arith("Datos de ejemplo: un muro de 5 m por 2 m. ¿Cuántos metros cuadrados hay que pintar en una mano?", "5 * 2", "El área es largo por alto.", " m²"),
        arith("Una edición de 10 copias buenas requiere 2 pruebas de estado. ¿Cuántas hojas se necesitan si cada copia usa una hoja?", "10 + 2", "Se suman las copias finales y las pruebas.", " hojas"),
        ex("Tu imagen tiene detalles muy finos. ¿Qué técnica se adapta mejor a ella? A. Grabado pequeño en cartón B. Mural de 6 m por 3 m.", "A", "Los detalles finos se ven de cerca; en un mural enorme se perderían de lejos."),
    ],
    [
        arith("Con datos de ejemplo: muro de 6 m² por mano, dos manos y una pintura que rinde 4 m² por litro. ¿Cuántos litros necesitas?", "6 * 2 // 4", "Se multiplica el área por las manos y se divide por el rendimiento.", " litros"),
        ex("Para el imaginario «el cerro de mi patio», que se ve de lejos y en planos de color, ¿qué propuesta es más coherente? A. Un mural en planos de color grandes B. Un grabado de 5 cm con líneas muy finas.", "A", "Los planos grandes se leen a distancia, como el cerro; el grabado diminuto perdería el efecto."),
        ex("Un compañero tomó el recurso del color plano de un mural de ejemplo y lo aplicó a su propio cerro. ¿Lo reinterpretó o lo copió?", "Lo reinterpretó", "Tomó un recurso y lo cambió de tema y de lugar."),
    ],
    [
        ex("El plan de un compañero dice: «Muro de 15 m², pintura de rendimiento 5 m² por litro, una mano: necesito 3 litros». Pero piensa dar dos manos. ¿Cuántos litros necesita realmente?", "6 litros", "15 × 2 = 30 m² de pintado y 30 ÷ 5 = 6 litros."),
        ex("Un plan dice que el mural será «sustentable» porque usará pintura nueva sin ficha de materiales ni plan de limpieza. ¿Qué le falta? A. Ficha de origen, uso y descarte y un plan para limpiar y reutilizar B. Un color más vivo.", "A", "Sustentable se justifica con origen, uso y descarte; el color no cambia eso."),
    ],
    [
        arith("Un grupo pinta un mural de 24 m² con pintura de rendimiento 8 m² por litro y dos manos. ¿Cuántos litros necesita?", "24 * 2 // 8", "Se multiplica por las manos y se divide por el rendimiento.", " litros"),
        ex("Un grupo calcula que necesita 6 litros de pintura en total y ya tiene 3 litros sobrantes de otra obra. ¿Cuántos litros más debe conseguir? A. 3 B. 6.", "A", "Necesita 6 litros y ya tiene 3, entonces le faltan 6 − 3 = 3."),
    ],
    ex("Tu liceo te da un muro de 5 m por 3 m y una caja de cartón. Quieres una propuesta del tema «mi barrio de noche»: o un mural de planos grandes en dos colores o un grabado de 12 cm con trazos finos. Con los datos de ejemplo (pintura que rinde 6 m² por litro, dos manos), ¿cuántos litros necesitas para el mural? A. 5 litros B. 15 litros.", "A", "El área es 15 m², con dos manos son 30 m² y 30 ÷ 6 = 5 litros; 15 litros ignora el rendimiento."),
    [
        ex("¿Qué se suma a las copias finales al calcular el papel de una edición?", "Las pruebas de estado", "También usan papel."),
        ex("Verdadero o falso: puedo calcular la pintura con el área sin considerar las manos.", "Falso", "Cada mano cubre el muro y gasta pintura."),
        ex("¿Qué cuatro preguntas responde un plan de trabajo?", "Qué imagen, con qué técnica, con qué materiales y cuánto se necesita", "Así la propuesta se puede realizar."),
    ],
    task(
        "Elige UN encargo de ejemplo. A) Mural de 4 m por 3 m en el muro de un patio, con pintura que rinde 6 m² por litro y dos manos. B) Edición de 8 copias de un grabado de 12 cm en cartón, con 3 pruebas de estado. C) Un mural de 5 m por 2 m y un grabado de 10 copias sobre el mismo imaginario. Define tu imaginario, la técnica y los materiales sustentables (con origen, uso y descarte), calcula lo que necesitas y escribe un plan de cinco pasos con una nota de qué cambiarías en una versión siguiente. Pide el permiso por escrito si el muro no es tuyo.",
        "Elegí el encargo A. Imaginario: el cerro de mi patio. Técnica: mural en planos de dos colores. Materiales: pintura al agua y brocha reutilizada. Cálculo: 12 m² × 2 manos ÷ 6 = 4 litros. Plan: 1) pedir permiso, 2) limpiar el muro, 3) pasar el boceto con cuadrícula, 4) pintar dos manos, 5) limpiar y guardar los restos. En una versión siguiente probaría tres colores.",
        ["define imaginario, técnica y materiales con ficha", "calcula las cantidades con datos del encargo", "escribe un plan de pasos ordenados", "incluye permiso, limpieza y autoría"],
        ["propuesta escrita", "cálculos de materiales", "plan de cinco pasos"],
        ["olvidar las manos de pintura", "no pedir permiso"],
        "Pregunta cómo hizo cada cálculo y de qué manera su técnica sirve a su imaginario.",
    ),
    "Cuenta a una persona de tu casa cómo calcularías la pintura de un muro que mide 3 m por 2 m si cada litro rinde 6 m² y das dos manos.",
    "Cambia un dato del encargo (por ejemplo, el rendimiento) y recalcula cuántos litros necesitas.",
)

# ---------------------------------------------------------------- Clase 5
lesson(
    OA2, 5,
    "Hojas y lápiz. Las dos propuestas y la pauta están escritas en esta clase; no necesitas buscar nada.",
    "Aprenderé a contrastar propuestas de grabado y mural con criterios: coherencia con el imaginario, calidad de la técnica, sustentabilidad y cuidado del lugar. Sirve para elegir y mejorar mi propia propuesta con argumentos.",
    ["Sé calcular materiales para una edición o un mural.", "Sé que un mural exige permiso y cuidado del muro."],
    [
        "Contrastar es comparar dos propuestas con los mismos criterios. Uso cuatro. Coherencia: la técnica y los materiales sirven al imaginario. Calidad de la técnica: la impresión o la pintura se ve limpia y se entiende desde donde se mira. Sustentabilidad: los materiales tienen origen, uso y descarte adecuados. Cuidado del lugar: hay permiso, el muro queda limpio y se respeta a quienes lo habitan. A cada criterio le pongo de 0 a 3 puntos y justifico con un dato.",
        "La justificación sigue el esquema «dato, criterio, conclusión». Por ejemplo: «La propuesta B usa cartón reutilizado (dato); cumple sustentabilidad (criterio); por eso le doy 3 (conclusión)». No sirve decir «me gustó más». Tampoco comparo propuestas con medidas distintas: si una se hace a escala 1:20 y otra a 1:50, primero las llevo a la misma. La comparación es sobre las obras, no sobre las personas que las hicieron.",
        "Después de contrastar reviso mi propia propuesta con la misma pauta. Escribo la parte más fuerte, la más débil y un cambio concreto para mejorarla. Al exponer el trabajo cuido la privacidad, doy crédito a quien me ayudó y a mis referentes, y no difundo fotos de personas sin su permiso. Si la propuesta es para un lugar real, pido autorización antes de intervenirlo.",
    ],
    [("contrastar", "comparar propuestas con los mismos criterios"), ("coherencia", "relación lógica entre idea, técnica y materiales"), ("sustentabilidad", "uso de materiales que no agotan recursos ni dañan el ambiente"), ("cuidado del lugar", "obtener permiso, dejar limpio y respetar a quienes habitan el sitio"), ("justificar", "explicar una decisión con un dato y un criterio")],
    [
        w("Puntuar una propuesta", "Propuesta 1: grabado de 12 cm hecho con cartón de caja, tinta al agua y 3 pruebas de estado; el imaginario es una escalera con muchos detalles finos; se imprimirá en el liceo sin intervenir ningún muro. Puntúa de 0 a 3 los cuatro criterios.", ["Coherencia: los detalles finos calzan con el grabado, 3.", "Calidad de la técnica: tiene pruebas de estado, 3.", "Sustentabilidad: cartón reutilizado y tinta al agua, 3.", "Cuidado del lugar: no interviene muros, 3."], "Total 3 + 3 + 3 + 3 = 12 puntos"),
        w("Cuidado del lugar", "Propuesta 2: mural de planos grandes sobre el muro de una escuela, con pintura nueva, sin permiso aún y sin plan de limpieza. Puntúa de 0 a 3 sustentabilidad y cuidado del lugar.", ["Sustentabilidad: pintura nueva sin ficha ni limpieza, 1.", "Cuidado del lugar: no tiene permiso y no hay plan de limpieza, 0."], "Sustentabilidad 1 y cuidado del lugar 0"),
    ],
    [
        m("Elegir la propuesta ganadora porque «se ve más bonita».", "No hay datos que otra persona pueda comprobar.", "Usa los cuatro criterios y justifica cada puntaje con dato, criterio y conclusión."),
        m("Comparar una propuesta con otra que usa una escala distinta sin ajustarla.", "Las medidas no son comparables.", "Lleva ambas a la misma escala antes de comparar."),
    ],
    [
        ex("¿Cuál criterio se refiere a que la técnica y los materiales sirvan al imaginario? A. Coherencia B. Sustentabilidad.", "A", "La coherencia relaciona idea, técnica y materiales; la sustentabilidad se refiere al ambiente."),
        ex("Un mural no tiene permiso de la escuela y dejará pintura sobrante en el patio. ¿Qué criterio falla?", "Cuidado del lugar", "El permiso y la limpieza son parte del cuidado del lugar."),
        ex("¿Qué esquema se usa para justificar un puntaje?", "Dato, criterio y conclusión", "Une lo observable con el criterio y con la decisión."),
    ],
    [
        arith("Una propuesta recibe coherencia 3, calidad de la técnica 2, sustentabilidad 3 y cuidado del lugar 1. ¿Cuánto suma?", "3 + 2 + 3 + 1", "Se suman los cuatro puntajes.", " puntos"),
        ex("Propuesta: grabado en cartón de caja usada con tinta al agua. ¿Qué criterio sostiene ese dato? A. Sustentabilidad B. Cuidado del lugar.", "A", "El origen reutilizado y la tinta al agua hablan de sustentabilidad."),
        ex("Una compañera dice: «Mi mural es mejor que el tuyo porque lo hice yo». ¿Qué le falta a su argumento?", "Un criterio y un dato comprobable", "Quién lo hizo no es un criterio de comparación."),
    ],
    [
        ex("Propuesta 1: coherencia 3, calidad 2, sustentabilidad 3, cuidado 3. Propuesta 2: coherencia 3, calidad 2, sustentabilidad 1, cuidado 0. ¿Cuántos puntos de diferencia hay a favor de la propuesta 1?", "5", "La 1 suma 11 y la 2 suma 6, entonces la diferencia es 11 − 6 = 5."),
        ex("La propuesta 2 podría mejorar su cuidado del lugar. ¿Qué cambio concreto? A. Pedir permiso por escrito y planear la limpieza B. Pintar los bordes de otro color.", "A", "El permiso y la limpieza son el cuidado del lugar; el color de los bordes no."),
        ex("Un boceto de mural está a escala 1:20 y mide 15 cm de largo. Otro boceto, de otro grupo, está a escala 1:50 y mide 6 cm. Para comparar sus tamaños reales, ¿qué haces primero?", "Llevarlas a la misma escala", "Con escalas distintas, las medidas no se pueden comparar directamente."),
    ],
    [
        ex("Al exponer tu grabado en el pasillo, quieres mostrar una foto donde aparece un compañero sosteniendo la copia. ¿Qué haces? A. Pido su permiso o muestro solo la obra B. La publico sin avisar porque no se le ve mal.", "A", "El consentimiento se pide siempre; que se vea bien no lo reemplaza."),
        ex("Tu propuesta usó una técnica de un referente de ejemplo que conociste en una ficha. En la exposición, ¿qué debes poner? A. El crédito del referente y qué recurso tomaste B. Nada, porque la obra es tuya.", "A", "Aunque la obra sea tuya, el recurso viene de otra persona y debe declararse."),
    ],
    [
        arith("Un grupo reúne 4 grabados de 12 cm y quiere exponerlos en una tira de cartulina con 3 cm de espacio entre cada uno y 3 cm en cada extremo. ¿Cuántos centímetros debe medir la tira?", "4 * 12 + 3 * 3 + 2 * 3", "Son 4 grabados, 3 espacios entre ellos y 2 extremos de 3 cm.", " cm"),
        ex("Dos propuestas empatan en 11 puntos. La A tiene cuidado del lugar 1 y la B tiene cuidado del lugar 3. El muro pertenece a una escuela que aún no autoriza. ¿Cuál conviene defender?", "La B", "Con el mismo total, el criterio que depende del permiso del lugar pesa más para poder realizarla."),
    ],
    ex("Tu curso decide cuál de dos propuestas para el patio se hará. La propuesta del grupo A suma coherencia 3, calidad 3, sustentabilidad 2 y cuidado 3. La del grupo B suma 3, 2, 3 y 3. ¿Cuál tiene más puntos o empatan? Di el total de cada una.", "Empatan en 11", "A suma 3 + 3 + 2 + 3 = 11 y B suma 3 + 2 + 3 + 3 = 11."),
    [
        ex("¿Qué cuatro criterios se usan para contrastar propuestas en esta clase?", "Coherencia, calidad de la técnica, sustentabilidad y cuidado del lugar", "Juntos revisan la obra, el ambiente y el lugar."),
        ex("Verdadero o falso: se puede comparar propuestas con escalas distintas sin ajustarlas.", "Falso", "Las medidas no coinciden si las escalas son distintas."),
        ex("Después de contrastar, ¿qué se escribe sobre la propia propuesta?", "La parte más fuerte, la más débil y un cambio concreto", "Eso permite mejorarla."),
    ],
    task(
        "Compara estas dos propuestas de ejemplo para el patio de un liceo. Propuesta 1: grabado de 12 cm en cartón de caja, tinta al agua, edición de 10 copias con 2 pruebas de estado; imaginario: una escalera con mucho detalle; se repartirá en el liceo. Propuesta 2: mural de 4 m por 3 m, planos en dos colores, pintura nueva, 4 litros calculados con dos manos; imaginario: el cerro del patio; aún no tiene permiso ni plan de limpieza. Puntúa de 0 a 3 coherencia, calidad de la técnica, sustentabilidad y cuidado del lugar para cada una, con «dato, criterio, conclusión». Elige una, propón un cambio concreto para la más débil y escribe una frase de crédito y consentimiento para exponerlas.",
        "Propuesta 1: coherencia 3, calidad 3, sustentabilidad 3, cuidado 3: total 12. Propuesta 2: coherencia 3, calidad 2, sustentabilidad 1, cuidado 0: total 6. Elijo la 1 y a la 2 le agregaría permiso por escrito y plan de limpieza. Frase de exposición: «Grabados de estudiantes del curso, con permiso; referente de ejemplo de esta clase».",
        ["puntúa los cuatro criterios en ambas propuestas", "justifica con dato, criterio y conclusión", "propone un cambio concreto", "incluye consentimiento y crédito"],
        ["tabla de puntajes", "justificaciones", "frase de crédito y consentimiento"],
        ["decidir por gusto", "olvidar el permiso del muro"],
        "Pregunta qué dato respalda su puntaje más bajo y qué cambio concreto haría.",
    ),
    "Cuenta a una persona de tu casa cuáles son los cuatro criterios para contrastar propuestas de grabado y mural.",
    "Redacta dos frases con «dato, criterio, conclusión» sobre un mural o grabado que conozcas.",
)
