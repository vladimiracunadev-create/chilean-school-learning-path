"""Material del estudiante de 8.º básico, Historia, Geografía y Ciencias Sociales: OA 07 (impactos americanos y debates en Europa)."""
from __future__ import annotations

from hi5_lib import build

OA = "HI08 OA 07"

# ---------------------------------------------------------------- clase 1
F = ("Ficha 1 (hitos simplificados). Antes de 1492, los europeos conocían tres continentes: Europa, Asia y África. "
     "1492: Colón llega a América. 1507: un mapamundi europeo, dibujado por Martin Waldseemüller, usa por primera vez el nombre «América». "
     "1511: el fraile dominico Antonio de Montesinos critica en La Española el trato a los indígenas. 1512: las Leyes de Burgos intentan regular ese trato. "
     "1537: el papa Pablo III declara que los indígenas son seres humanos con derecho a su libertad. 1550-1551: en Valladolid, el fraile Bartolomé de las Casas y el teólogo Juan Ginés de Sepúlveda debaten ante teólogos del rey. "
     "Productos americanos que llegan a Europa: maíz, papa, tomate, cacao, tabaco.")
build(
    OA, 1, F,
    use="Aprenderé a situar los impactos de la conquista de América en Europa, y a nombrar los tres que pide el OA: ampliación del mundo conocido, desafío de representar una nueva realidad y debates morales.",
    prior=["Conozco la conquista de América.", "Sé calcular diferencias entre años.", "Conozco el Renacimiento y la imprenta."],
    explain=[
        "La llegada a América cambió la cultura europea de varias maneras. Primero, ampliar el mundo conocido: antes de 1492 los europeos conocían tres continentes, y después tuvieron que aceptar que existía un cuarto. Un mapamundi de 1507 usó por primera vez el nombre «América». Los mapas, los viajes y los productos nuevos, como el maíz y la papa, cambiaron la idea de cuán grande era el mundo.",
        "Segundo, hubo un desafío: representar una nueva realidad. Había plantas, animales, personas y paisajes que no existían en los libros europeos. Cronistas, pintores y grabadores tuvieron que describirlos con palabras e imágenes conocidas, y a veces se equivocaron. ",
        "Tercero, hubo debates morales sobre la condición humana de los indígenas. Montesinos criticó el trato en 1511; las Leyes de Burgos de 1512 intentaron regularlo; en 1537 el papa declaró que los indígenas son seres humanos, y en 1550-1551 Las Casas y Sepúlveda debatieron en Valladolid. Estos debates no eliminaron la violencia colonial, pero muestran que en Europa hubo posiciones distintas.",
    ],
    vocab=[("mapamundi", "mapa que representa todo el planeta"), ("cronista", "persona que escribe relatos sobre hechos de su tiempo"), ("condición humana", "hecho de ser persona con dignidad y derechos"), ("regular", "poner reglas a una actividad"), ("dominico", "religioso de la orden de Santo Domingo")],
    worked=[
        ("Calcular un periodo", "Según la ficha, ¿cuántos años pasaron entre la llegada de Colón y el mapamundi que nombra «América»?", ["Busco los años: 1492 y 1507.", "Resto: 1507 − 1492 = 15."], "15 años"),
        ("Clasificar un impacto", "El hecho «la papa llega a Europa» ¿es ampliación del mundo conocido, desafío de representar o debate moral?", ["Es un producto nuevo que llega de otro continente.", "Muestra el contacto con un mundo antes desconocido."], "Ampliación del mundo conocido"),
    ],
    mistakes=[("Decir que antes de 1492 los europeos conocían los cuatro continentes.", "Se confunde el mundo conocido por los europeos con todo el planeta.", "Recuerda que conocían Europa, Asia y África."),
              ("Pensar que el debate de Valladolid terminó con la violencia colonial.", "Se supone que una discusión basta para frenar la violencia.", "Distingue debate de práctica: la violencia continuó.")],
    T=[
        ("{F} ¿Cuántos continentes conocían los europeos antes de 1492?", "Tres", "Europa, Asia y África."),
        ("{F} ¿En qué año un mapamundi usó por primera vez el nombre «América»?", "1507", "Lo indica la ficha."),
        ("{F} ¿Quiénes debatieron en Valladolid?", "Bartolomé de las Casas y Juan Ginés de Sepúlveda", "La ficha los nombra."),
        ("=", "{F} ¿Cuántos años pasaron entre el sermón de Montesinos y las Leyes de Burgos?", "1512-1511", "Se resta el primer año al segundo.", " año"),
        ("=", "{F} ¿Cuántos años pasaron entre la declaración del papa Pablo III y el comienzo del debate de Valladolid?", "1550-1537", "Se restan los dos años.", " años"),
        ("{F} ¿A qué siglo pertenecen los hitos de 1507, 1537 y 1550?", "Siglo XVI", "El siglo XVI va de 1501 a 1600."),
        ("{F} Ordena del más antiguo al más reciente: debate de Valladolid, sermón de Montesinos, Leyes de Burgos, declaración del papa.", "Sermón de Montesinos, Leyes de Burgos, declaración del papa, debate de Valladolid", "Los años son 1511, 1512, 1537 y 1550."),
        ("{F} Clasifica cada hecho según el impacto del OA: a) aparece el nombre América en un mapa, b) debate sobre la humanidad de los indígenas, c) llegan maíz y papa. Opciones: ampliación del mundo conocido; debate moral.", "a) ampliación del mundo conocido; b) debate moral; c) ampliación del mundo conocido", "Mapas y productos amplían el mundo; el debate trata de la condición humana."),
        ("=", "{F} Una línea de tiempo usa 1 cm = 10 años y parte en 1500. ¿A cuántos cm queda 1550?", "(1550-1500)//10", "Se divide la diferencia de años por la escala.", " cm"),
        ("{F} ¿Qué declaró el papa Pablo III en 1537? A) Que los indígenas son seres humanos con derecho a su libertad B) Que los indígenas debían ser esclavos", "A) Que los indígenas son seres humanos con derecho a su libertad", "La ficha lo indica."),
        ("{F} Un compañero dice: «Con el debate de Valladolid terminó la violencia contra los indígenas». ¿Qué falla?", "Un debate no frenó por sí solo la violencia colonial", "La ficha habla de un debate y de leyes, no de que la violencia terminara."),
        ("{F} ¿Por qué un mapa de 1507 con el nombre «América» ampliaba el mundo conocido?", "Porque mostraba un continente que los europeos antes no tenían en sus mapas", "Antes solo conocían tres continentes."),
        ("{F} ¿Qué pregunta problema plantea esta clase?", "Cómo cambió la cultura europea con la conquista de América", "Es el problema del OA."),
    ],
    ctx=("Un museo prepara una vitrina sobre 1507. ¿Qué mensaje principal debe tener sobre ese mapamundi? {F}", "Que los europeos empezaron a incluir un cuarto continente en sus mapas", "Muestra la ampliación del mundo conocido."),
    sc=[("¿Qué es un mapamundi?", "Un mapa que representa todo el planeta", "Se definió en el vocabulario."),
        ("¿Quién criticó en 1511 el trato a los indígenas?", "El fraile dominico Antonio de Montesinos", "La ficha lo indica."),
        ("=", "¿Cuántos años pasaron entre 1492 y 1511?", "1511-1492", "Se resta el primer año al segundo.", " años")],
    op=("Dibuja una línea de tiempo con 1 cm = 10 años desde 1490 hasta 1560. Marca siete hitos de la ficha (1492, 1507, 1511, 1512, 1537, 1550 y 1551) con su nombre y píntalos con dos colores: uno para mapas y productos y otro para debates morales. Escribe una frase que explique por qué un debate no elimina la violencia. {F}",
        "1492 a 0,2 cm, 1507 a 1,7 cm, 1511 a 2,1 cm, 1512 a 2,2 cm, 1537 a 4,7 cm, 1550 a 6 cm, 1551 a 6,1 cm. Frase: un debate muestra ideas, pero no cambia por sí solo los hechos.",
        ["respeta la escala", "usa dos colores", "explica el límite de los debates"], ["línea de tiempo", "frase"], ["no usar la escala", "decir que el debate acabó con la violencia"],
        "Pide que explique la diferencia entre ideas y prácticas."),
    reinforce="Nombra los tres impactos del OA y un hecho de la ficha para cada uno.",
    extend="Escribe una pregunta que un historiador haría para saber si los debates cambiaron la vida de algún pueblo.",
)

# ---------------------------------------------------------------- clase 2
F = ("Ficha 2 (fuentes de ejemplo escritas para este cuaderno; no son documentos históricos reales). "
     "Fuente A, carta de un marinero de ejemplo, 1540, a su familia en España: «He visto un árbol que da una fruta con hojas en la punta, parece una piña de pino, pero es dulce y jugosa. También he visto un animal grande de cuello largo que parece un camello pequeño.» "
     "Fuente B, descripción de un grabado de ejemplo, hecho en Europa en 1590 por un artista que nunca viajó a América: muestra a personas americanas con ropas y gestos como los de la antigüedad clásica europea, en un paisaje con palmeras y leones africanos (animales que no viven en América).")
build(
    OA, 2, F,
    use="Aprenderé a analizar cómo los europeos describieron y dibujaron una realidad nueva, y a distinguir lo que las fuentes muestran de lo que imaginan.",
    prior=["Sé contextualizar una fuente.", "Conozco los tres impactos del OA.", "Sé distinguir hecho y opinión."],
    explain=[
        "Representar una nueva realidad fue difícil. Los europeos no tenían palabras ni imágenes para plantas, animales y personas que veían por primera vez. Por eso comparaban lo nuevo con lo conocido: la fruta se parecía a una piña de pino y el animal de cuello largo, a un camello. Estas comparaciones ayudan a entender, pero también pueden deformar.",
        "Los grabados presentan otro problema. Un artista que nunca viajó a América dibujaba a partir de relatos de otros y de su imaginación. Por eso puso a personas americanas con ropas y gestos de la antigüedad europea, y leones africanos en un paisaje con palmeras. El grabado dice más sobre la mirada europea que sobre América.",
        "Para analizar estas fuentes hay que preguntar quién las hizo, si vio lo que describe y para quién. Una carta de un marinero que vio el árbol es una fuente de primera mano; un grabado de un artista que nunca viajó es de segunda mano. Ambas son útiles, pero hay que distinguirlas y no suponer que Europa recibió una imagen única de América.",
    ],
    vocab=[("fuente de primera mano", "fuente de alguien que vio o vivió lo que cuenta"), ("fuente de segunda mano", "fuente de alguien que cuenta lo que otros le contaron"), ("grabado", "imagen impresa a partir de una plancha tallada"), ("comparación", "relación entre algo nuevo y algo conocido"), ("deformar", "cambiar la forma real de algo al representarlo")],
    worked=[
        ("Clasificar una fuente", "La carta del marinero, ¿es de primera o de segunda mano?", ["El marinero dice «he visto».", "Cuenta lo que vivió."], "De primera mano"),
        ("Detectar una deformación", "El grabado pone leones africanos en un paisaje con palmeras de América. ¿Qué error puede tener?", ["Los leones africanos no viven en América.", "El artista usó su imaginación."], "Puso animales que no viven en América"),
    ],
    mistakes=[("Creer que un grabado europeo muestra con exactitud cómo era América.", "Se olvida que el artista no viajó y usó su imaginación.", "Pregunta si el autor vio lo que dibuja."),
              ("Pensar que todos los europeos recibieron la misma imagen de América.", "Se ignora que hubo cartas, grabados y crónicas muy distintos.", "Compara varias fuentes.")],
    T=[
        ("{F} ¿Quién escribió la Fuente A?", "Un marinero", "La ficha lo indica."),
        ("{F} ¿Con qué compara la fruta el marinero?", "Con una piña de pino", "Lo dice en la carta."),
        ("{F} ¿Con qué compara al animal de cuello largo?", "Con un camello pequeño", "La carta lo dice."),
        ("=", "{F} El grabado se hizo en 1590 y la carta es de 1540. ¿Cuántos años separan ambas fuentes?", "1590-1540", "Se resta el año de la carta al del grabado.", " años"),
        ("{F} ¿Qué animal no americano aparece en el grabado?", "Los leones africanos", "La ficha lo indica."),
        ("{F} ¿Cuál de las dos fuentes es de primera mano? A) La carta del marinero B) El grabado del artista que nunca viajó", "A) La carta del marinero", "El marinero vio lo que cuenta."),
        ("{F} Clasifica: a) «parece una piña de pino», b) «personas americanas con ropas como las de la antigüedad clásica europea». ¿Cuál es una comparación del que vio y cuál una deformación de quien imaginó?", "a) comparación del que vio; b) deformación de quien imaginó", "El marinero vio la fruta; el artista no viajó."),
        ("{F} ¿Por qué comparaban lo nuevo con lo conocido? A) Porque no tenían palabras para lo que veían B) Porque preferían no describir lo desconocido", "A) Porque no tenían palabras para lo que veían", "Comparar ayuda a describir lo desconocido."),
        ("{F} Un compañero concluye con el grabado: «En América había leones». ¿Qué falla?", "El artista nunca viajó y usó su imaginación; los leones no son animales americanos", "La fuente deforma la realidad."),
        ("{F} ¿Qué muestra el grabado sobre la mirada europea?", "Que veían América con las ideas y modelos europeos, como la antigüedad clásica", "Vestían a personas americanas como en la antigüedad europea."),
        ("{F} ¿Qué límite tiene la carta del marinero? A) Es la visión de una persona y compara con cosas de España B) Fue hecha por un artista que no viajó", "A) Es la visión de una persona y compara con cosas de España", "Una carta personal no representa toda la realidad."),
        ("{F} ¿Qué conclusión es proporcional? A) Europa recibió imágenes distintas de América, algunas más cercanas y otras más imaginadas B) Todos los europeos tuvieron la misma imagen", "A) Europa recibió imágenes distintas de América, algunas más cercanas y otras más imaginadas", "Las dos fuentes difieren."),
        ("{F} ¿Qué otra fuente ayudaría a conocer cómo era realmente el paisaje? A) Dibujos hechos en el lugar por quien lo vio B) Un grabado hecho por otro artista que no viajó", "A) Dibujos hechos en el lugar por quien lo vio", "Una fuente de primera mano acerca más a la realidad."),
    ],
    ctx=("Una editorial escolar quiere ilustrar un libro con el grabado de 1590. ¿Qué nota aclaratoria debería agregar? {F}", "Que fue hecho por un artista que nunca viajó y que mezcla elementos de la imaginación europea con elementos americanos", "Así se evita presentarlo como retrato fiel."),
    sc=[("¿Qué es una fuente de primera mano?", "Una fuente de alguien que vio o vivió lo que cuenta", "Se definió en el vocabulario."),
        ("¿Qué quiere decir deformar?", "Cambiar la forma real de algo al representarlo", "Se definió en el vocabulario."),
        ("¿Con qué compara el marinero lo que ve? A) Con cosas conocidas de su mundo B) Con cosas que solo existían en América", "A) Con cosas conocidas de su mundo", "Compara con piña de pino y camello.")],
    op=("Escribe una carta de ejemplo de seis líneas, como si fueras un viajero de 1560 que describe a su familia una planta o un animal americano que ves por primera vez, usando una comparación con algo europeo. Incluye una frase que reconozca el límite de tu comparación. {F}",
        "Querida familia: he visto una planta con mazorcas amarillas, parece un trigo muy grande. Aún no la entiendo bien. Límite: mi comparación puede no ser exacta porque no conozco su nombre.",
        ["usa una comparación con algo europeo", "describe algo americano", "reconoce el límite de su comparación"], ["carta"], ["inventar hechos que contradicen la ficha", "no incluir límite"],
        "Pide que explique en qué se parece y en qué se diferencia lo comparado."),
    reinforce="Explica a otra persona por qué los europeos compararon lo nuevo con lo conocido.",
    extend="Escribe una pregunta que le harías a un artista que dibujó América sin viajar.",
)

# ---------------------------------------------------------------- clase 3
F = ("Ficha 3 (productos y territorios, simplificados). Productos americanos que llegaron a Europa en los siglos XVI y XVII: maíz, papa, tomate, cacao, tabaco. Productos europeos que llegaron a América: trigo, caballos, vacas, ovejas y caña de azúcar. "
     "La papa y el maíz se fueron extendiendo por Europa, y el cacao se bebía en la corte española como bebida de lujo. "
     "Continuidades en Europa: el trigo seguía siendo un alimento básico; la mayoría de la población seguía viviendo en el campo; la religión cristiana seguía muy presente.")
build(
    OA, 3, F,
    use="Aprenderé a describir cómo productos americanos cambiaron la alimentación y la cultura europea, y qué continuó igual en Europa.",
    prior=["Conozco las rutas del siglo XVI.", "Sé distinguir cambio y continuidad.", "Conozco los impactos de la conquista."],
    explain=[
        "La conquista de América cambió la alimentación y la vida material de Europa. Llegaron el maíz, la papa, el tomate, el cacao y el tabaco. La papa y el maíz se fueron extendiendo por Europa, y el cacao se bebió en la corte española como producto de lujo. Estos cambios fueron graduales: tardaron décadas e incluso siglos en volverse comunes en la dieta.",
        "El intercambio fue de ida y vuelta. A América llegaron trigo, caballos, vacas, ovejas y caña de azúcar, lo que también transformó ese continente. Pero para la cultura europea el efecto principal estuvo en lo que llegaba: nuevos alimentos, nuevas bebidas, nuevas palabras y una nueva idea del tamaño del mundo.",
        "También hubo continuidades: el trigo siguió siendo el alimento básico, la mayoría de la gente seguía en el campo y la religión cristiana continuaba muy presente. Quien dice que «todo cambió» pasa por alto estas continuidades. Para entender el proceso conviene mirar qué cambió, dónde y con qué ritmo.",
    ],
    vocab=[("intercambio", "paso de productos, ideas o personas de un lugar a otro"), ("dieta", "conjunto de alimentos que come una población"), ("lujo", "algo caro y poco accesible para la mayoría"), ("alimento básico", "alimento que forma la base de la comida diaria"), ("gradual", "que ocurre poco a poco")],
    worked=[
        ("Clasificar un producto", "El tomate, ¿llegó a Europa desde América o desde Asia?", ["Busco en la lista de productos americanos.", "El tomate aparece ahí."], "Desde América"),
        ("Cambio y continuidad", "Una aldea europea de 1600 prueba la papa, pero sigue comiendo pan de trigo. ¿Qué es cambio y qué continuidad?", ["La papa es nueva: cambio.", "El pan de trigo continúa."], "Cambio: la papa; continuidad: el pan de trigo"),
    ],
    mistakes=[("Pensar que los alimentos americanos reemplazaron de inmediato a los europeos.", "Se ignora que el proceso fue gradual.", "Escribe «poco a poco» y menciona el trigo."),
              ("Creer que el intercambio fue solo de América hacia Europa.", "Se olvidan trigo, caballos, vacas y caña de azúcar.", "Nombra productos de ida y de vuelta.")],
    T=[
        ("{F} ¿Qué producto americano se bebía en la corte española como bebida de lujo?", "El cacao", "La ficha lo indica."),
        ("{F} ¿Qué alimento europeo siguió siendo básico?", "El trigo", "La ficha lo señala como continuidad."),
        ("{F} ¿Cuál de estos productos no es americano: maíz, trigo o tomate?", "El trigo", "La ficha lo lista entre los productos europeos."),
        ("{F} ¿Qué productos europeos llegaron a América?", "Trigo, caballos, vacas, ovejas y caña de azúcar", "La ficha los lista."),
        ("{F} Clasifica cada producto según su origen: a) papa, b) trigo, c) cacao. Opciones: América; Europa.", "a) América; b) Europa; c) América", "La ficha separa los productos por origen."),
        ("=", "{F} Una aldea cosecha 120 sacos de trigo y 30 sacos de papa. ¿Cuántas veces mayor es la cosecha de trigo que la de papa?", "120//30", "Se divide la cosecha de trigo entre la de papa.", " veces"),
        ("{F} ¿Por qué el cambio de dieta fue gradual? A) Porque tardó décadas en volverse común B) Porque ocurrió en un solo año", "A) Porque tardó décadas en volverse común", "La explicación habla de un proceso lento."),
        ("{F} Clasifica como cambio o continuidad: a) llega la papa a Europa, b) se sigue comiendo pan de trigo, c) la mayoría vive en el campo.", "a) cambio; b) continuidad; c) continuidad", "Solo la llegada de la papa es nueva."),
        ("{F} ¿Qué se transformó también en América por el intercambio?", "Llegaron trigo, caballos, vacas, ovejas y caña de azúcar", "El intercambio fue de ida y vuelta."),
        ("{F} Un compañero dice: «El cacao era un alimento común para todos los europeos». ¿Qué dato lo contradice?", "El cacao se bebía en la corte como bebida de lujo", "Era caro y poco accesible."),
        ("{F} ¿Qué conclusión es proporcional? A) El contacto con América cambió la alimentación europea poco a poco, con continuidades B) Cambió toda la vida europea de golpe", "A) El contacto con América cambió la alimentación europea poco a poco, con continuidades", "La ficha muestra cambios y continuidades."),
        ("{F} ¿Qué dato necesitarías para saber si una región europea adoptó la papa antes que otra?", "Registros de cultivo o de consumo de cada región", "Muestran dónde y cuándo se usó."),
        ("{F} ¿Qué relación hay entre territorio e intercambio? A) Los productos viajaron por las rutas del Atlántico B) Los productos viajaron solo por tierra", "A) Los productos viajaron por las rutas del Atlántico", "Los barcos conectaban ambos continentes."),
    ],
    ctx=("Un cocinero escolar quiere un menú con productos que muestren el intercambio entre Europa y América. ¿Qué platos incluiría? {F}", "Uno con papa, maíz o tomate y otro con trigo, para mostrar productos de ambos continentes", "Combina productos de origen americano y europeo."),
    sc=[("¿Qué es un intercambio?", "El paso de productos, ideas o personas de un lugar a otro", "Se definió en el vocabulario."),
        ("¿Qué alimento europeo continuó como básico?", "El trigo", "La ficha lo indica."),
        ("¿Qué significa gradual? A) Que ocurre poco a poco B) Que ocurre de golpe", "A) Que ocurre poco a poco", "Así se definió.")],
    op=("Haz una tabla con dos columnas: «Llegó a Europa desde América» y «Llegó a América desde Europa». Escribe tres productos en cada columna usando la ficha y agrega una fila con un producto que continuó igual en Europa. Cierra con una frase sobre el ritmo del cambio. {F}",
        "Europa: maíz, papa, cacao. América: trigo, caballos, vacas. Continuó: pan de trigo. Frase: los cambios fueron graduales y tardaron décadas.",
        ["clasifica bien los productos", "incluye una continuidad", "habla del ritmo"], ["tabla", "frase"], ["mezclar el origen de los productos", "decir que todo cambió de golpe"],
        "Pide que explique qué productos fueron de lujo y cuáles se hicieron comunes."),
    reinforce="Nombra tres productos que viajaron de América a Europa y tres de Europa a América.",
    extend="Escribe una pregunta sobre cómo cambió la comida en tu casa por un producto de origen americano.",
)

# ---------------------------------------------------------------- clase 4
F = ("Ficha 4 (voces de ejemplo que resumen posiciones del siglo XVI; no son citas textuales). "
     "Voz 1, fraile dominico crítico, 1511: «Los indígenas son personas con alma y razón; no se les puede maltratar ni quitar su libertad.» "
     "Voz 2, encomendero español, 1530: «Recibí indígenas a mi cargo para que trabajen; así sostengo mi casa y cumplo con el rey.» "
     "Voz 3, teólogo defensor de la conquista, 1550: «Los indígenas son inferiores y necesitan ser gobernados por los españoles, incluso con la guerra si se resisten.» "
     "Voz 4, fraile defensor de los indígenas, 1550: «Los indígenas tienen razón, leyes y ciudades; son iguales en naturaleza a los europeos y la conquista por la fuerza es injusta.» "
     "Contexto: las posiciones se discutieron ante teólogos del rey, y el rey tuvo que decidir sobre leyes para las Indias.")
build(
    OA, 4, F,
    use="Aprenderé a contrastar las posiciones del debate sobre la condición humana de los indígenas y a explicar las causas y los intereses de cada actor.",
    prior=["Sé contrastar perspectivas.", "Conozco los tres impactos del OA.", "Conozco la conquista y la encomienda."],
    explain=[
        "El debate moral del siglo XVI giró en torno a la condición humana de los indígenas: ¿eran personas con razón y derechos iguales a los de los europeos? Algunos religiosos, como Montesinos y Las Casas, respondieron que sí y criticaron el trato. Otros, como el teólogo Sepúlveda, sostuvieron que eran inferiores y que podían ser gobernados por la fuerza.",
        "Cada actor tenía intereses. El encomendero se beneficiaba del trabajo indígena y defendía el sistema. El teólogo defensor de la conquista justificaba el dominio con argumentos religiosos y de autoridad. Los frailes críticos usaban argumentos morales y su experiencia directa. El rey escuchaba a todos porque necesitaba leyes y también ingresos.",
        "Contrastar estas voces ayuda a no simplificar. Los europeos no pensaban todos lo mismo. Pero tampoco hay que idealizar el debate: aun con leyes y discusiones, la violencia colonial continuó. Un debate de ideas no equivale a un cambio inmediato de las prácticas.",
    ],
    vocab=[("encomienda", "sistema en que un español recibía indígenas a cargo para que trabajaran para él"), ("encomendero", "español que recibía una encomienda"), ("condición humana", "hecho de ser persona con razón y derechos"), ("teólogo", "persona que estudia cuestiones religiosas"), ("justificar", "dar razones para defender una acción")],
    worked=[
        ("Reconocer un interés", "¿Qué interés tiene el encomendero de la voz 2?", ["Leo su voz.", "Recibe indígenas para que trabajen para sostener su casa."], "Un interés económico en el trabajo indígena"),
        ("Contrastar dos posiciones", "¿En qué se oponen las voces 3 y 4?", ["La voz 3 dice que son inferiores.", "La voz 4 dice que son iguales en naturaleza."], "Sobre si los indígenas son iguales o inferiores a los europeos"),
    ],
    mistakes=[("Decir que todos los europeos pensaban lo mismo sobre los indígenas.", "Se ignoran las voces críticas.", "Contrasta posiciones diferentes."),
              ("Creer que el debate cambió de inmediato la vida de los indígenas.", "Se confunde discusión con práctica.", "Recuerda que la violencia colonial continuó.")],
    T=[
        ("{F} ¿Quién dice que los indígenas son personas con alma y razón y no se les puede quitar su libertad?", "El fraile dominico crítico", "Es la voz 1."),
        ("{F} ¿Qué interés económico tiene el encomendero?", "El trabajo de los indígenas para sostener su casa", "La voz 2 lo dice."),
        ("{F} ¿Qué dice el teólogo de la voz 3 sobre los indígenas?", "Que son inferiores y deben ser gobernados por los españoles", "Es su argumento."),
        ("{F} ¿Qué dice el fraile de la voz 4 sobre la conquista por la fuerza?", "Que es injusta", "Es lo que sostiene."),
        ("=", "{F} ¿Cuántos años pasaron entre la voz 1 (1511) y las voces 3 y 4 (1550)?", "1550-1511", "Se resta el primer año al segundo.", " años"),
        ("{F} Clasifica cada voz según defienda o critique el trato a los indígenas: a) voz 1, b) voz 2, c) voz 4.", "a) critica; b) defiende el sistema; c) critica", "Las voces 1 y 4 defienden a los indígenas y la voz 2 defiende la encomienda."),
        ("{F} ¿Qué voz usa un argumento de inferioridad para justificar el dominio? A) La voz 3 B) La voz 4", "A) La voz 3", "El teólogo defensor de la conquista habla de inferioridad."),
        ("{F} ¿Qué voces comparten la idea de que los indígenas son personas con razón?", "Las voces 1 y 4", "Ambas defienden su condición humana."),
        ("{F} Un compañero dice: «Todos los europeos pensaban que los indígenas eran inferiores». ¿Qué voces lo contradicen?", "Las voces 1 y 4", "Ambas defienden su igualdad y critican la conquista por la fuerza."),
        ("{F} ¿Por qué el rey tuvo que escuchar a todas las posiciones?", "Porque debía decidir sobre leyes para las Indias y necesitaba también ingresos", "La ficha habla del contexto de las leyes."),
        ("{F} ¿Qué conclusión es proporcional? A) Hubo posiciones europeas muy distintas sobre los indígenas y el debate no eliminó la violencia colonial B) El debate terminó con todos los abusos", "A) Hubo posiciones europeas muy distintas sobre los indígenas y el debate no eliminó la violencia colonial", "Las voces muestran desacuerdo y la violencia continuó."),
        ("{F} ¿Qué voz falta en el debate de la ficha?", "La de los propios indígenas", "No aparece ninguna voz indígena."),
        ("{F} ¿Qué pregunta ayudaría a entender mejor el impacto del debate? A) ¿Qué leyes se dictaron y se cumplieron? B) ¿Cuántos barcos había en Sevilla?", "A) ¿Qué leyes se dictaron y se cumplieron?", "Conecta el debate con las prácticas."),
    ],
    ctx=("Una profesora propone un juicio simulado entre las voces 3 y 4 de la ficha. ¿Qué pregunta central debe resolver el rey de ejemplo? {F}", "Si los indígenas son iguales o inferiores a los europeos y si la conquista por la fuerza es justa", "Resume el desacuerdo."),
    sc=[("¿Qué es la encomienda?", "Un sistema en que un español recibía indígenas a cargo para que trabajaran para él", "Se definió en el vocabulario."),
        ("¿Quién se beneficia del trabajo indígena?", "El encomendero", "La voz 2 lo dice."),
        ("¿Qué voz falta en el debate? A) La de los indígenas B) La del rey", "A) La de los indígenas", "Ninguna voz indígena aparece.")],
    op=("Escribe un diálogo de seis líneas entre los dos frailes de la ficha (voz 1 y voz 4) y el teólogo de la voz 3. Cada uno debe usar una idea de su voz. Cierra con una frase tuya sobre qué decisión debería tomar el rey y por qué. {F}",
        "Fraile 1: son personas con razón. Teólogo: son inferiores y deben ser gobernados. Fraile 4: tienen leyes y ciudades; la fuerza es injusta. Cierre: el rey debería regular el trato porque son personas.",
        ["usa ideas de la ficha", "respeta las tres posiciones", "justifica la decisión"], ["diálogo", "frase"], ["inventar citas textuales", "hacer que el teólogo cambie sin evidencia"],
        "Pide que explique cómo habría reaccionado un encomendero."),
    reinforce="Explica con tus palabras las dos grandes posiciones del debate moral.",
    extend="Escribe una pregunta que le harías a un indígena de la época sobre este debate.",
)

# ---------------------------------------------------------------- clase 5
F = ("Ficha 5 (pregunta y evidencias de ejemplo). Pregunta: ¿cuánto cambió la cultura europea con la conquista de América? "
     "Evidencia 1: los mapamundis desde 1507 incluyen un cuarto continente. "
     "Evidencia 2: llegan maíz, papa, tomate, cacao y tabaco, pero el cambio de la dieta tarda décadas. "
     "Evidencia 3: grabados y crónicas describen América con comparaciones y también con errores. "
     "Evidencia 4: hubo debates morales (Montesinos, Leyes de Burgos, papa Pablo III y Valladolid) sobre la condición humana de los indígenas. "
     "Evidencia 5: la violencia colonial continuó a pesar de los debates. "
     "Evidencia 6: la mayoría de los campesinos europeos siguió viviendo del campo.")
build(
    OA, 5, F,
    use="Aprenderé a evaluar con un argumento el impacto de la conquista de América en la cultura europea, considerando la ampliación del mundo conocido, la representación y los debates morales.",
    prior=["Sé que un argumento tiene tesis, evidencias y límite.", "Conozco los tres impactos del OA.", "Sé distinguir cambio y continuidad."],
    explain=[
        "Evaluar un impacto significa decidir cuánto cambió algo y con qué pruebas. Para el OA 07, los impactos son tres: la ampliación del mundo conocido (mapas y productos), el desafío de representar una realidad nueva (crónicas y grabados) y los debates morales sobre la condición humana de los indígenas. Una tesis equilibrada puede decir que el impacto fue grande en las ideas y en el mapa, pero más lento en la vida diaria de la mayoría.",
        "Cada parte de la tesis necesita una evidencia. El cambio en los mapas se apoya en la evidencia 1; el desafío de representar, en la 3; los debates morales, en la 4. El límite aparece en las evidencias 5 y 6: la violencia continuó y la vida campesina cambió poco. Estas evidencias impiden decir que «todo cambió».",
        "Un error frecuente es creer que Europa recibió una sola imagen de América, o que el debate moral borró la violencia. Una conclusión sólida reconoce la variedad de imágenes y que las ideas no siempre cambiaron los hechos.",
    ],
    vocab=[("impacto", "efecto fuerte de un hecho sobre algo"), ("evaluar", "decidir cuánto vale algo según evidencias"), ("tesis", "respuesta que se defiende con evidencias"), ("límite", "lo que la evidencia no permite concluir"), ("equilibrada", "que considera aspectos a favor y en contra")],
    worked=[
        ("Asignar evidencia a un impacto", "¿Qué impacto del OA apoya la evidencia 4?", ["Habla de debates sobre la condición humana de los indígenas.", "Eso es un debate moral."], "Los debates morales"),
        ("Usar una evidencia como límite", "¿Qué límite agrega la evidencia 6?", ["Dice que la mayoría de los campesinos siguió viviendo del campo.", "Entonces no todos los aspectos de la vida europea cambiaron."], "Que la vida de la mayoría cambió poco"),
    ],
    mistakes=[("Decir que la conquista cambió toda la vida europea.", "Se ignora la continuidad en el campo.", "Usa la evidencia 6."),
              ("Citar solo los debates morales como si fueran todo el impacto.", "Se olvidan mapas, productos y representaciones.", "Cita evidencias de los tres impactos.")],
    T=[
        ("{F} ¿Qué evidencia muestra la ampliación del mundo conocido?", "La evidencia 1", "Habla de mapas con un cuarto continente."),
        ("{F} ¿Qué evidencia muestra el desafío de representar una realidad nueva?", "La evidencia 3", "Habla de grabados y crónicas con comparaciones y errores."),
        ("{F} ¿Qué evidencia muestra que la violencia continuó?", "La evidencia 5", "La dice con esas palabras."),
        ("{F} ¿Qué evidencias funcionan como límite de la tesis de que «todo cambió»?", "La 5 y la 6", "Muestran que la violencia continuó y la vida campesina cambió poco."),
        ("{F} Clasifica cada evidencia según el impacto: a) 1, b) 3, c) 4. Opciones: ampliación del mundo conocido; representación de una nueva realidad; debate moral.", "a) ampliación del mundo conocido; b) representación de una nueva realidad; c) debate moral", "Cada evidencia corresponde a un impacto."),
        ("{F} ¿Qué tesis se apoya mejor en las evidencias? A) La conquista cambió mucho las ideas y los mapas de Europa, pero más lentamente la vida diaria B) La conquista no cambió nada en Europa", "A) La conquista cambió mucho las ideas y los mapas de Europa, pero más lentamente la vida diaria", "Hay evidencias de cambio y de continuidad."),
        ("{F} Un compañero dice: «Después de Valladolid se acabó la violencia». ¿Qué evidencia lo contradice?", "La evidencia 5", "Dice que la violencia continuó a pesar de los debates."),
        ("{F} ¿Qué evidencia indica que el cambio de dieta fue lento?", "La evidencia 2, que dice que tardó décadas", "Habla de un cambio gradual."),
        ("{F} ¿Por qué sería un error usar solo la evidencia 4?", "Porque deja fuera los mapas, los productos y las representaciones", "No cubre los tres impactos."),
        ("{F} Escribe un límite honesto para la tesis.", "Las evidencias no distinguen entre regiones europeas ni entre grupos sociales", "Un argumento reconoce lo que no prueba."),
        ("{F} ¿Qué respuesta es más sólida? A) «La conquista amplió el mundo conocido, planteó el reto de representarlo y abrió debates morales, aunque la violencia continuó» B) «La conquista fue un hecho sin importancia»", "A) «La conquista amplió el mundo conocido, planteó el reto de representarlo y abrió debates morales, aunque la violencia continuó»", "Cita los tres impactos y reconoce un límite."),
        ("{F} ¿Qué diferencia hay entre decir «hubo debates» y decir «los debates cambiaron la práctica»?", "Lo primero afirma que se discutió; lo segundo afirma un efecto que la ficha no prueba", "La evidencia 5 lo limita."),
        ("{F} ¿Qué evidencia mezcla un cambio y una continuidad en la dieta europea?", "La evidencia 2", "Llegan productos nuevos, pero el cambio tarda décadas."),
    ],
    ctx=("En un foro escolar se pregunta: «¿Cambió Europa con la conquista de América?». Responde en una frase con dos evidencias de la ficha. {F}", "Sí, cambió sus mapas y sus debates morales, pero no toda su vida diaria, porque la violencia continuó y el campo cambió poco", "Usa evidencias de cambio y de límite."),
    sc=[("¿Qué es evaluar un impacto?", "Decidir cuánto cambió algo según evidencias", "Se definió en el vocabulario."),
        ("¿Qué evidencia muestra la continuidad de la vida campesina?", "La evidencia 6", "Dice que siguió viviendo del campo."),
        ("¿Qué es un límite en un argumento? A) Lo que la evidencia no prueba B) Una repetición de la tesis", "A) Lo que la evidencia no prueba", "Así se definió.")],
    op=("Escribe un párrafo de seis líneas que responda la pregunta de la ficha. Incluye tu tesis, tres evidencias numeradas (una de cada impacto del OA), una de las evidencias 5 o 6 como límite y una pregunta que quedaría abierta. {F}",
        "Pienso que la conquista cambió mucho las ideas de Europa. Evidencia 1: mapas con un cuarto continente. Evidencia 3: crónicas y grabados con errores. Evidencia 4: debates morales. Límite: la evidencia 5. Pregunta abierta: ¿qué leyes se cumplieron?",
        ["tiene tesis", "tres evidencias de impactos distintos", "incluye límite y pregunta"], ["párrafo"], ["decir que todo cambió", "citar solo un impacto"],
        "Pide que explique qué otra fuente ayudaría a responder su pregunta abierta."),
    reinforce="Explica oralmente los tres impactos del OA con una evidencia cada uno.",
    extend="Escribe una evidencia que buscarías para saber si el debate de Valladolid cambió alguna ley.",
)
