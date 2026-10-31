"""Material del estudiante de 7.º básico, Historia, Geografía y Ciencias Sociales: OA 02 (revolución agrícola, sedentarización y complejidad social)."""
from __future__ import annotations

from hi5_lib import build

OA = "HI07 OA 02"

# ---------------------------------------------------------------- clase 1
F = ("Ficha 1 (datos de ejemplo, hechos para este cuaderno). "
     "Grupo A, cazadores-recolectores: 30 personas; cambia de campamento 4 veces al año; come frutos, semillas, raíces, peces y animales silvestres; lleva pocas cosas porque debe cargarlas al trasladarse. "
     "Grupo B, agricultores y pastores: 120 personas que viven en una aldea fija; cultivan trigo y cebada, crían ovejas y cabras y guardan los granos en vasijas de barro; si la lluvia falla, la cosecha de ese año se pierde. "
     "Dato general: la agricultura apareció hace unos 10.000 años en Asia occidental y se extendió durante miles de años; muchos grupos siguieron cazando y recolectando, o combinaron ambas formas de vida.")
build(
    OA, 1, F,
    use="Aprenderé a comparar la vida de los grupos que cazan y recolectan con la de los que producen sus alimentos. Sirve para entender qué cambió con la revolución agrícola.",
    prior=["Sé que los primeros grupos humanos vivían de la caza y la recolección.", "Sé qué es una adaptación cultural.", "Sé calcular generaciones de 25 años."],
    explain=[
        "Durante la mayor parte de la historia humana, los grupos obtuvieron su alimento de la naturaleza: cazaban animales, pescaban y recolectaban frutos, semillas y raíces. Para encontrar alimento cambiaban de lugar varias veces al año y llevaban pocas cosas, porque debían cargarlas.",
        "Hace unos 10.000 años, en Asia occidental, algunos grupos empezaron a producir sus alimentos: sembraban cereales y criaban animales. A este cambio se le llama revolución agrícola o neolítica. Quienes producían podían guardar granos y vivir en aldeas fijas, pero dependían de la lluvia y de la cosecha: si fallaban, quedaban sin alimento.",
        "No fue un cambio rápido ni igual en todas partes. Tardó miles de años, apareció en varios lugares del mundo y no todos los grupos lo adoptaron: muchos siguieron cazando y recolectando, o combinaron ambas formas. Por eso no se puede decir que toda la humanidad cambió a la vez ni que el cambio fuera inevitable.",
    ],
    vocab=[("revolución agrícola", "cambio de obtener alimentos de la naturaleza a producirlos con cultivos y crianza"), ("cazador-recolector", "persona que obtiene su alimento cazando, pescando y recolectando"), ("aldea", "pequeño poblado fijo donde viven varias familias"), ("cosecha", "recolección de lo que se sembró"), ("pastor", "persona que cría animales como ovejas o cabras")],
    worked=[
        ("Comparar dos grupos", "{F} ¿Cuál de los dos grupos vive en un lugar fijo?", ["El grupo A cambia de campamento 4 veces al año.", "El grupo B vive en una aldea fija."], "El grupo B"),
        ("Calcular generaciones", "La agricultura apareció hace unos 8.000 años en un lugar de ejemplo. ¿Cuántas generaciones de 25 años son?", ["Una generación dura 25 años.", "Divido: 8.000 ÷ 25 = 320."], "320 generaciones"),
    ],
    mistakes=[("Pensar que todos los grupos dejaron de cazar y recolectar apenas apareció la agricultura.", "Se cree que el cambio fue inmediato y obligatorio.", "Muchos grupos siguieron cazando y recolectando o combinaron ambas formas durante miles de años."),
              ("Creer que producir alimentos siempre fue más seguro que cazar y recolectar.", "No se consideran los riesgos de depender de una cosecha.", "Quien cultiva puede perder todo si falla la lluvia; quien se mueve puede buscar otro lugar.")],
    T=[
        ("{F} ¿Cuántas personas tiene el grupo B?", "120", "La ficha lo indica."),
        ("{F} ¿Cuántas veces al año cambia de campamento el grupo A?", "4 veces", "La ficha lo indica."),
        ("=", "{F} ¿Cuántas personas más viven en el grupo B que en el grupo A?", "120-30", "Se resta la cantidad menor a la mayor.", " personas"),
        ("{F} ¿Por qué el grupo A lleva pocas cosas?", "Porque debe cargarlas cada vez que se traslada", "La ficha dice que cambia de campamento y debe transportar sus pertenencias."),
        ("{F} ¿Dónde guarda el grupo B los granos?", "En vasijas de barro", "La ficha lo dice."),
        ("{F} Clasifica cada actividad como recolección o caza (R) o producción de alimentos (P): 1) sembrar cebada; 2) recoger raíces silvestres; 3) criar cabras; 4) pescar en un río.", "1 P, 2 R, 3 P, 4 R", "Sembrar y criar producen alimento; recoger y pescar lo obtienen de la naturaleza."),
        ("=", "{F} Si cada persona del grupo B necesita 3 vasijas de grano al año, ¿cuántas vasijas necesita la aldea?", "120*3", "Se multiplica la cantidad de personas por las vasijas de cada una.", " vasijas"),
        ("=", "{F} La agricultura apareció hace unos 10.000 años. ¿Cuántas generaciones de 25 años son?", "10000//25", "Se divide el tiempo por la duración de una generación.", " generaciones"),
        ("{F} En un año con poca lluvia, ¿cuál de los dos grupos puede perder el alimento de todo el año? Explica con un dato de la ficha.", "El grupo B, porque si la lluvia falla la cosecha se pierde", "La ficha dice que sus granos dependen de la lluvia."),
        ("{F} Ana dice: «Cuando apareció la agricultura, todos los grupos dejaron de cazar de inmediato». Corrígela con el dato general.", "Fue un cambio gradual y muchos grupos siguieron cazando y recolectando o combinaron ambas formas", "El dato general lo indica."),
        ("{F} ¿Qué ventaja y qué riesgo tiene guardar granos en vasijas, como hace el grupo B?", "Ventaja: tiene comida en meses sin cosecha; riesgo: depende de que la cosecha salga bien", "Guardar alimento da seguridad, pero la cosecha depende de la lluvia."),
        ("{F} Un grupo cría ovejas y además recolecta frutos silvestres. ¿Es solo de caza-recolección, solo de producción o mixto?", "Mixto", "Combina crianza (producción) y recolección."),
        ("{F} Un historiador escribe: «La agricultura fue un progreso que mejoró la vida de todos». Da un argumento a favor y uno en contra con la ficha.", "A favor: se pueden guardar granos y vivir en aldea fija; en contra: se depende de la lluvia y se puede perder la cosecha", "La ficha muestra ventajas y riesgos."),
    ],
    ctx=("Un museo muestra dos maquetas: una con tiendas livianas que se desarman y otra con casas de barro, vasijas y corrales. ¿Cuál corresponde al grupo B y por qué? {F}", "La segunda, porque el grupo B vive en una aldea fija, cultiva y cría animales", "Las casas, vasijas y corrales indican vida fija y producción de alimentos."),
    sc=[("¿Qué es un cazador-recolector?", "Una persona que obtiene su alimento cazando, pescando y recolectando", "Obtiene el alimento de la naturaleza sin producirlo."),
        ("¿Hace cuántos años apareció la agricultura según la ficha, de manera aproximada?", "Hace unos 10.000 años", "La ficha da esa fecha en Asia occidental."),
        ("{F} ¿Qué grupo, el A o el B, vive en una aldea?", "El grupo B", "La ficha lo dice.")],
    op=("Haz una tabla de dos columnas, «Grupo A» y «Grupo B», con cuatro filas: cantidad de personas, dónde viven, cómo consiguen el alimento y un riesgo. Completa la tabla con los datos de la ficha. {F}",
        "Grupo A: 30 personas; campamentos; recolecta y caza; debe moverse. Grupo B: 120 personas; aldea fija; cultiva y cría; la cosecha puede perderse.",
        ["completa las cuatro filas", "usa datos de la ficha", "los riesgos son distintos y razonables"], ["tabla escrita"], ["asignar a B la caza y recolección", "poner el mismo riesgo para ambos"],
        "Pide que explique por qué un grupo puede combinar ambas formas."),
    reinforce="Escribe tres diferencias entre un campamento y una aldea.",
    extend="Escribe una pregunta sobre qué ocurriría con el grupo B si dos años seguidos faltara la lluvia.",
)

# ---------------------------------------------------------------- clase 2
F = ("Ficha 2 (datos de ejemplo, hechos para este cuaderno). "
     "Domesticar es criar o cultivar seres vivos eligiendo a los más útiles para que sus descendientes cambien. "
     "Trigo silvestre: sus espigas se rompen solas y esparcen los granos por el suelo. Trigo domesticado: sus espigas se mantienen enteras y se pueden cosechar. "
     "El perro se domesticó mucho antes que las ovejas y las cabras, que se criaron hace unos 10.000 años. "
     "Calendario de un cultivo de trigo en el hemisferio norte: siembra en noviembre, cuidado de diciembre a abril y cosecha en mayo. "
     "Una aldea de ejemplo tiene 40 casas de adobe (ladrillo de barro y paja), 6 corrales y 12 silos (lugares para guardar granos).")
build(
    OA, 2, F,
    use="Aprenderé a relacionar la domesticación de plantas y animales con la vida en aldeas fijas. Sirve para entender por qué cultivar obliga a quedarse en un lugar.",
    prior=["Sé comparar caza-recolección y producción de alimentos.", "Sé leer un calendario.", "Sé que la agricultura apareció en varios lugares."],
    explain=[
        "Domesticar es criar o cultivar seres vivos, eligiendo los más útiles para que sus descendientes cambien. Así, el trigo silvestre, que esparce sus granos al madurar, fue reemplazado poco a poco por un trigo cuyas espigas se mantienen enteras y se pueden cosechar. En los animales ocurrió algo parecido con las ovejas y las cabras. El cambio se acumuló durante muchas generaciones.",
        "Cultivar exige trabajo en fechas precisas: sembrar, cuidar el campo durante meses, cosechar y guardar los granos. Por eso las familias necesitaban permanecer cerca de sus campos, construir casas más duraderas, corrales para los animales y silos para almacenar. Esta vida estable en un lugar se llama sedentarización.",
        "La relación entre domesticación y sedentarización no es una sola causa ni una sola dirección. En algunos lugares con alimentos abundantes ya había grupos que vivían estables antes de cultivar; en otros, pastores se mueven con sus rebaños durante el año. Por eso las aldeas permanentes fueron una consecuencia muy importante del cultivo, pero no la única forma posible de vida.",
    ],
    vocab=[("domesticar", "criar o cultivar seres vivos eligiendo los más útiles"), ("sedentarización", "paso a vivir de manera estable en un mismo lugar"), ("silo", "lugar para guardar granos"), ("adobe", "ladrillo hecho de barro y paja"), ("pastoreo móvil", "crianza de animales moviéndose con ellos según las estaciones")],
    worked=[
        ("Reconocer domesticación", "{F} ¿Qué diferencia tiene el trigo domesticado con el silvestre?", ["El silvestre esparce los granos por el suelo.", "El domesticado mantiene sus espigas enteras."], "Sus espigas se mantienen enteras y se pueden cosechar"),
        ("Usar el calendario", "{F} ¿Cuántos meses hay entre la cosecha de mayo y la siguiente siembra de noviembre?", ["Cuento desde mayo hasta noviembre.", "Mayo es el mes 5 y noviembre el 11: 11 − 5 = 6."], "6 meses"),
    ],
    mistakes=[("Creer que el trigo se volvió doméstico en una sola cosecha.", "No se considera que el cambio ocurre por selección durante muchas generaciones.", "Imagina cientos de años eligiendo las mejores plantas para sembrar."),
              ("Decir que todos los grupos que criaban animales vivían en aldeas fijas.", "Se ignora el pastoreo móvil.", "Hay pastores que se mueven con sus rebaños según las estaciones.")],
    T=[
        ("{F} ¿Qué mantiene enteras sus espigas: el trigo silvestre o el domesticado?", "El trigo domesticado", "La ficha lo describe así."),
        ("{F} ¿Cuántos corrales tiene la aldea de ejemplo?", "6", "La ficha lo indica."),
        ("{F} ¿Qué animal se domesticó primero: el perro o la oveja?", "El perro", "La ficha dice que se domesticó mucho antes."),
        ("=", "{F} Entre la siembra (mes 11, noviembre) y la cosecha (mayo, mes 17 contando desde el año anterior), ¿cuántos meses pasan?", "17-11", "Se resta el mes de siembra al de cosecha.", " meses"),
        ("{F} ¿Por qué el trigo domesticado es más útil para quien cosecha?", "Porque sus espigas no esparcen los granos y se pueden recolectar", "La ficha dice que se mantienen enteras."),
        ("{F} Ordena las tareas del cultivo: cosecha, siembra, cuidado del campo.", "Siembra, cuidado del campo, cosecha", "El calendario va de noviembre a mayo en ese orden."),
        ("=", "{F} Cada silo guarda 15 sacos de grano. ¿Cuántos sacos caben en los 12 silos?", "12*15", "Se multiplica la cantidad de silos por los sacos de cada uno.", " sacos"),
        ("{F} Clasifica como domesticación (D) o recolección (R): 1) sembrar solo las semillas de las plantas que no esparcen los granos; 2) recoger bayas silvestres; 3) criar cabras eligiendo las que dan más leche; 4) cazar un ciervo.", "1 D, 2 R, 3 D, 4 R", "Elegir plantas o animales útiles para criar es domesticar."),
        ("{F} ¿Por qué un cultivo obliga a una familia a quedarse cerca de su campo de diciembre a abril?", "Porque debe cuidarlo hasta la cosecha de mayo", "La ficha da el calendario de cuidado."),
        ("{F} Pedro dice: «Los pueblos se hicieron sedentarios porque inventaron las casas y después descubrieron la agricultura». Corrígelo con la explicación.", "Cultivar y criar animales exigía permanecer cerca; además hubo grupos que vivían estables por otros motivos, así que no hay una sola causa", "La relación es de varias causas y no tiene una sola dirección."),
        ("{F} ¿Por qué una aldea con silos puede crecer más que un campamento móvil?", "Porque guarda alimento y no necesita trasladar todo cada vez", "Guardar granos da alimento para más personas y más tiempo."),
        ("{F} Unos pastores se trasladan con sus ovejas a las montañas en verano y al valle en invierno. ¿Son sedentarios? Explica.", "No: crían animales pero se mueven con ellos según las estaciones", "El pastoreo móvil es producción de alimentos sin vivir siempre en un lugar."),
        ("Elige la afirmación correcta: A) La domesticación cambió a las plantas y animales y los cambios se acumularon durante muchas generaciones; B) El trigo se volvió domesticado en una sola cosecha.", "A) La domesticación se acumuló durante muchas generaciones", "La selección repetida de lo más útil produce cambios lentos."),
    ],
    ctx=("En un huerto escolar se guardan las semillas de las plantas más grandes para sembrarlas el año siguiente. ¿Con qué idea de la clase se parece y por qué? {F}", "Con la domesticación, porque se eligen los ejemplares más útiles para que los descendientes cambien", "Elegir lo más útil generación tras generación es domesticar."),
    sc=[("¿Qué es un silo?", "Un lugar para guardar granos", "Sirve para almacenar la cosecha."),
        ("¿Qué es la sedentarización?", "Pasar a vivir de manera estable en un mismo lugar", "Ocurre, por ejemplo, al formar aldeas."),
        ("{F} ¿En qué mes se cosecha el trigo del calendario?", "En mayo", "La ficha lo indica.")],
    op=("Dibuja un calendario de un año con un cultivo de la ficha (siembra, cuidado y cosecha). Escribe debajo tres cosas que una familia debía tener cerca de ese campo para poder cultivar y guardar la cosecha. {F}",
        "Calendario con siembra en noviembre, cuidado de diciembre a abril y cosecha en mayo; casas, silos y corrales cerca del campo.",
        ["el calendario respeta los meses de la ficha", "nombra tres elementos de una aldea", "explica por qué se necesitan"], ["calendario dibujado", "tres elementos escritos"], ["mezclar el orden de las tareas", "no relacionar el cultivo con quedarse en el lugar"],
        "Pide que explique qué haría un pastor móvil en esos meses."),
    reinforce="Cuenta en voz alta los meses del calendario del trigo, de la siembra a la cosecha.",
    extend="Escribe una pregunta sobre qué ocurre con un silo si la cosecha fue mala.",
)

# ---------------------------------------------------------------- clase 3
F = ("Ficha 3 (datos de ejemplo, hechos para este cuaderno). "
     "Una aldea cosecha 900 medidas de cebada en un año. Consume 600 medidas, guarda 100 como semilla para sembrar el año siguiente y el resto es excedente. "
     "Con parte del excedente se alimenta a 3 artesanos que no cultivan: una alfarera, un tejedor y un tallador de piedra. "
     "La aldea cambia 2 medidas de cebada por 1 cuenco de barro de otra aldea. También recibe obsidiana, una roca volcánica con filo, de un lugar lejano, a cambio de sal.")
build(
    OA, 3, F,
    use="Aprenderé a explicar cómo un excedente de alimentos permite el intercambio y la especialización. Sirve para entender por qué aparecieron nuevos oficios.",
    prior=["Sé que la agricultura permitió vivir en aldeas.", "Sé restar y multiplicar con números de tres cifras.", "Sé qué es un recurso."],
    explain=[
        "Un excedente es la parte de la cosecha que sobra después de cubrir lo que la comunidad consume y de guardar la semilla para el año siguiente. Si hay excedente, parte de la comunidad puede dedicarse a otras tareas, porque otras personas producen alimento de más para ellas.",
        "Con esas personas liberadas de cultivar aparece la especialización: algunas se dedican solo a fabricar cerámica, tejidos o herramientas. Producen mejor y más rápido lo que saben hacer, pero dependen de que la comunidad les entregue alimento. Si la cosecha es mala, el excedente baja y los oficios se ven en riesgo.",
        "El excedente y la especialización favorecen el intercambio: las comunidades cambian lo que les sobra por lo que no tienen, como la obsidiana, una roca volcánica que sirve para hacer filos y que se intercambiaba entre aldeas muy lejanas. El intercambio crea redes entre aldeas, y la evidencia arqueológica lo muestra cuando se encuentran objetos lejos de donde se fabricaron o extrajeron.",
    ],
    vocab=[("excedente", "parte de la producción que sobra después de cubrir lo que se necesita"), ("especialización", "dedicación de una persona a un solo oficio"), ("intercambio", "entrega de un bien a cambio de otro"), ("artesano", "persona que fabrica objetos con sus manos"), ("obsidiana", "roca volcánica con filo que sirve para fabricar herramientas")],
    worked=[
        ("Calcular un excedente", "Una aldea de ejemplo cosecha 500 medidas, consume 350 y guarda 50 de semilla. ¿Cuál es el excedente?", ["Resto lo consumido: 500 − 350 = 150.", "Resto la semilla: 150 − 50 = 100."], "100 medidas"),
        ("Reconocer intercambio", "Una aldea entrega vasijas y recibe sal. ¿Es intercambio?", ["Hay entrega de un bien a cambio de otro.", "Cada aldea tiene algo que la otra no."], "Sí, es un intercambio"),
    ],
    mistakes=[("Creer que cualquier cosecha produce excedente.", "No se descuenta lo que se consume ni la semilla.", "Excedente = cosecha − consumo − semilla."),
              ("Pensar que los artesanos aparecen porque «nacen» con un talento y no por el alimento disponible.", "Se ignora que dedicarse a un oficio requiere que otros produzcan alimento de más.", "Explica el oficio con el excedente que lo sostiene.")],
    T=[
        ("{F} ¿Cuántas medidas se guardan como semilla?", "100 medidas", "La ficha lo indica."),
        ("=", "{F} ¿Cuántas medidas de excedente tuvo la aldea ese año?", "900-600-100", "Se restan el consumo y la semilla a la cosecha.", " medidas"),
        ("{F} ¿Qué oficios tienen los 3 artesanos?", "Alfarera, tejedor y tallador de piedra", "La ficha los nombra."),
        ("{F} ¿Qué es la obsidiana según la ficha?", "Una roca volcánica con filo", "La ficha la define así."),
        ("=", "{F} Con 200 medidas de cebada, a 2 por cuenco, ¿cuántos cuencos se pueden obtener?", "200//2", "Se divide la cebada por las medidas que vale cada cuenco.", " cuencos"),
        ("{F} ¿Por qué los 3 artesanos pueden dedicarse a su oficio sin cultivar?", "Porque el excedente de la aldea los alimenta", "Otras personas producen alimento de más."),
        ("{F} Clasifica cada situación como intercambio (I) o especialización (E): 1) cambiar cebada por cuencos; 2) dedicarse solo a tejer; 3) recibir obsidiana a cambio de sal; 4) un tallador que solo fabrica herramientas.", "1 I, 2 E, 3 I, 4 E", "El intercambio es dar un bien por otro; la especialización es dedicarse a un solo oficio."),
        ("=", "{F} Otro año la aldea cosecha 750 medidas y consume 600, igual que guarda 100 de semilla. ¿Cuál es el excedente?", "750-600-100", "Se aplica la misma resta.", " medidas"),
        ("{F} En el año de 750 medidas, los 3 artesanos comen 30 medidas cada uno. ¿Alcanza el excedente para alimentarlos? Calcula.", "No: el excedente es 50 y necesitan 90", "50 es menor que 3 × 30 = 90."),
        ("{F} ¿Por qué un año de mala cosecha pone en riesgo los oficios de los artesanos?", "Porque baja el excedente que los alimenta", "Sin excedente no hay con qué sostener a quienes no cultivan."),
        ("{F} Lucía dice: «Las aldeas solo intercambian si todas producen exactamente lo mismo». Corrígela.", "Se intercambia porque cada aldea tiene cosas distintas, como cebada, cuencos u obsidiana", "El intercambio ocurre cuando una comunidad tiene algo que a la otra le falta."),
        ("{F} La obsidiana no existe cerca de la aldea. ¿Qué evidencia arqueológica probaría el intercambio?", "Hallar herramientas de obsidiana en la aldea, lejos de donde se extrae esa roca", "Un objeto lejos de su origen muestra que viajó."),
        ("{F} Un compañero dice que la especialización siempre es mejor para todos. Da una desventaja que se vea en la ficha.", "Los artesanos dependen del excedente: si falla la cosecha, no tienen quien los alimente", "No cultivan, así que su sustento depende de la aldea."),
    ],
    ctx=("En un curso se organiza una feria: unos hacen pan, otros dibujan y otros pintan, y todos cambian lo que hacen por lo que necesitan. ¿Qué dos ideas de la clase aparecen? {F}", "Especialización (cada uno hace una cosa) e intercambio (cambian unos bienes por otros)", "Cada persona se dedica a una tarea y luego intercambia."),
    sc=[("¿Qué es un excedente?", "La parte de la producción que sobra después de cubrir lo que se necesita", "Se calcula descontando consumo y semilla."),
        ("=", "{F} ¿Cuántas medidas de cebada cambió la aldea por 5 cuencos, a 2 medidas por cuenco?", "5*2", "Se multiplica la cantidad de cuencos por su precio.", " medidas"),
        ("¿Qué permite que un grupo de personas se dedique solo a la alfarería?", "Que otras personas produzcan un excedente de alimento", "Las personas liberadas de cultivar pueden especializarse.")],
    op=("Dibuja un esquema de tu aldea de ejemplo con una cosecha de 800 medidas, un consumo de 500 y una semilla de 100. Calcula el excedente y escribe qué oficio sostendrías con él y qué intercambiarías. {F}",
        "Excedente de 200 medidas; sostendría a una alfarera; cambiaría cebada por cuencos de otra aldea.",
        ["el cálculo del excedente es correcto", "nombra un oficio sostenido por el excedente", "describe un intercambio"], ["esquema con cálculo", "oficio e intercambio escritos"], ["no descontar la semilla", "inventar oficios sin relación con el excedente"],
        "Pide que explique qué ocurriría con el oficio si la cosecha bajara a 600."),
    reinforce="Explica con tus palabras la diferencia entre intercambio y especialización.",
    extend="Escribe una pregunta sobre cómo se transportaba la obsidiana a lugares lejanos.",
)

# ---------------------------------------------------------------- clase 4
F = ("Ficha 4 (excavación de ejemplo de una aldea de hace unos 8.000 años, hecha para este cuaderno). "
     "Hay 12 tumbas: 3 contienen collares de piedra y vasijas finas, y 9 solo el cuerpo. "
     "Hay 12 casas: 2 tienen 4 silos grandes cada una, y 10 tienen 1 silo pequeño cada una. Un silo grande guarda 40 medidas y uno pequeño, 10. "
     "Se estudiaron los dientes de 20 personas y 14 tenían caries. "
     "Hay un corral comunal con restos de 60 ovejas y un muro bajo alrededor de los campos.")
build(
    OA, 4, F,
    use="Aprenderé a analizar cambios sociales de las aldeas agrícolas, como la desigualdad, con evidencia. Sirve para entender que el cambio trajo ventajas y problemas.",
    prior=["Sé qué es un excedente.", "Sé distinguir descripción e interpretación.", "Sé que la agricultura permitió aldeas fijas."],
    explain=[
        "La vida en aldeas trajo cambios sociales. Con más alimento almacenado aparecieron la propiedad de la tierra, los silos y los bienes que se podían acumular. Algunas familias lograron acumular más que otras y eso pudo generar desigualdad: diferencias de riqueza, de poder o de prestigio.",
        "La arqueología busca huellas de esa desigualdad: tumbas con muchos objetos y otras casi sin ellos, casas con más espacio de almacenamiento, muros que separan campos. Estas evidencias se deben interpretar con cuidado: un collar en una tumba muestra que alguien recibió objetos al morir, pero no permite asegurar por sí solo que fuera un jefe.",
        "La vida en aldea también trajo costos. Comer más cereales se asocia con más caries, y vivir cerca de los animales y de otras personas favoreció el contagio de enfermedades. Además, defender la tierra pudo producir conflictos. Por eso el cambio no fue solo un progreso: tuvo ventajas y problemas, y afectó de manera distinta a cada grupo.",
    ],
    vocab=[("desigualdad", "diferencia de riqueza, poder o prestigio entre personas"), ("propiedad", "derecho a usar y decidir sobre un bien, como un campo o un silo"), ("acumular", "juntar más de algo, como alimento o bienes"), ("tumba", "lugar donde se entierra a una persona"), ("caries", "daño en los dientes, que se asocia con comer muchos alimentos con almidón")],
    worked=[
        ("Calcular almacenamiento", "{F} ¿Cuántas medidas guarda en total una casa con 4 silos grandes?", ["Un silo grande guarda 40 medidas.", "Multiplico: 4 × 40 = 160."], "160 medidas"),
        ("Separar hecho e interpretación", "{F} El muro bajo alrededor de los campos, ¿es una descripción o una interpretación?", ["El muro es un hecho que se ve en la excavación.", "Para qué servía (defensa, límite de propiedad) sería una interpretación."], "Es una descripción; su función sería interpretación"),
    ],
    mistakes=[("Concluir que quien tenía un collar en su tumba era un jefe.", "Se interpreta más de lo que muestra la evidencia.", "Di solo que recibió más objetos; busca otra evidencia para hablar de poder."),
              ("Pensar que la desigualdad apareció porque algunas personas eran más capaces.", "No hay evidencia de capacidades en las tumbas ni en las casas.", "Explica la desigualdad con el acceso a tierra, excedente y bienes, y no con cualidades personales.")],
    T=[
        ("{F} ¿Cuántas tumbas tienen collares y vasijas finas?", "3", "La ficha lo indica."),
        ("{F} ¿Cuántas casas tienen un silo pequeño?", "10", "La ficha lo indica."),
        ("{F} ¿Qué había en el corral comunal?", "Restos de 60 ovejas", "La ficha lo indica."),
        ("=", "{F} ¿Cuántos silos grandes hay en total entre las 2 casas que los tienen?", "2*4", "Se multiplica por la cantidad de silos de cada casa.", " silos"),
        ("=", "{F} De las 20 personas estudiadas, ¿cuántas no tenían caries?", "20-14", "Se resta la cantidad con caries al total.", " personas"),
        ("{F} La frase «las familias con collares mandaban a las demás», ¿es una descripción o una interpretación?", "Una interpretación", "La excavación muestra collares, pero no muestra quién mandaba."),
        ("=", "{F} ¿Cuántas medidas guardan en total las 2 casas con silos grandes?", "2*4*40", "Se multiplican casas, silos y medidas de cada silo.", " medidas"),
        ("=", "{F} ¿Cuántas medidas guardan en total las 10 casas con un silo pequeño?", "10*10", "Se multiplican casas por medidas del silo.", " medidas"),
        ("{F} ¿Qué dos evidencias de la ficha sugieren desigualdad de riqueza?", "Las 3 tumbas con collares y vasijas finas, y las 2 casas con silos grandes", "Ambas muestran que unas familias tenían más bienes que otras."),
        ("{F} Pablo dice: «Con la agricultura todos fueron iguales, porque todos tenían casa». Corrígelo con datos de la ficha.", "Las 2 casas con silos grandes guardan 320 medidas, y las 10 casas con silo pequeño solo 100 en total", "Los silos muestran diferencias grandes de almacenamiento."),
        ("{F} ¿Se puede afirmar con la ficha que las personas con collares eran jefes? Explica.", "No: solo muestra que recibieron más objetos al ser enterradas; hace falta otra evidencia para hablar de poder", "Un collar no demuestra por sí solo un cargo."),
        ("{F} ¿Qué dato de la ficha podría reflejar un costo para la salud de la vida en aldea, según la explicación de la clase?", "Que 14 de 20 personas tenían caries, algo que se asocia con comer más cereales", "La explicación asocia las caries con una dieta rica en cereales; el dato solo sugiere el costo, no lo prueba."),
        ("{F} Un compañero dice: «Algunos tenían más porque eran más inteligentes». ¿Qué le responderías con la ficha?", "La ficha solo muestra diferencias de objetos y almacenamiento, no de capacidades", "La evidencia no mide inteligencia."),
    ],
    ctx=("Un equipo de arqueólogos halla en una aldea una casa con un silo enorme y diez casas con silos chicos. ¿Qué cambio social de la clase sugiere ese hallazgo? {F}", "Que había desigualdad en la acumulación de alimento", "Las diferencias de almacenamiento sugieren diferencias de riqueza."),
    sc=[("¿Qué es la desigualdad?", "Una diferencia de riqueza, poder o prestigio entre personas", "Es lo que las evidencias de la aldea sugieren."),
        ("¿Un collar en una tumba prueba por sí solo que la persona era un jefe?", "No", "Solo muestra que recibió objetos al ser enterrada."),
        ("=", "{F} ¿Cuántas tumbas hay en total en la aldea?", "3+9", "Se suman las tumbas con y sin objetos.", " tumbas")],
    op=("Escribe una nota de 5 líneas para un museo: dos datos de la ficha 4 que muestran desigualdad, una interpretación prudente y un dato que muestre que la vida en aldea tuvo costos. {F}",
        "Datos: 2 casas con 320 medidas y 10 casas con 100 medidas; interpretación: algunas familias acumulaban más; costo: 14 de 20 personas con caries.",
        ["usa dos datos de la ficha", "la interpretación es prudente", "incluye un costo de la vida en aldea"], ["nota escrita"], ["afirmar que había jefes sin evidencia", "olvidar el costo para la salud"],
        "Pide que explique qué otra evidencia confirmaría su interpretación."),
    reinforce="Explica con tus palabras por qué un excedente puede producir desigualdad.",
    extend="Escribe una pregunta sobre cómo se heredaban los campos y los silos en la aldea de la ficha.",
)

# ---------------------------------------------------------------- clase 5
F = ("Ficha 5 (datos generales y de ejemplo, hechos para este cuaderno). "
     "Posibles causas del origen de la agricultura: 1) clima más cálido y estable tras el fin de la última glaciación, hace unos 11.700 años; 2) cereales silvestres abundantes en algunos lugares; 3) más población en territorios limitados; 4) conocimiento de las plantas y herramientas para cosechar y moler. "
     "Lugares donde surgió por separado: Asia occidental (trigo, cebada), China (arroz, mijo), Mesoamérica (maíz, calabaza), los Andes (papa, quinua) y Nueva Guinea (banano, caña de azúcar). "
     "Otros pueblos, como muchos de Australia, mantuvieron durante miles de años su vida de caza y recolección, manejando el paisaje con cuidado.")
build(
    OA, 5, F,
    use="Aprenderé a construir una explicación con varias causas sobre el origen de la agricultura y sus consecuencias. Sirve para evitar explicaciones de una sola causa.",
    prior=["Sé qué es un excedente y qué es la sedentarización.", "Sé que hubo desigualdad en las aldeas.", "Sé distinguir causa y consecuencia."],
    explain=[
        "Una explicación multicausal combina varias causas para entender un proceso. La agricultura no apareció por una sola razón. Se juntaron el clima más cálido tras la última glaciación, la abundancia de plantas silvestres, el crecimiento de la población y el conocimiento de las plantas.",
        "La agricultura surgió por separado en varios lugares del mundo, con plantas distintas: trigo y cebada en Asia occidental, arroz y mijo en China, maíz en Mesoamérica, papa en los Andes y banano en Nueva Guinea. Por eso no fue un invento de un solo pueblo que luego se copió en todas partes. Las causas tuvieron un peso distinto en cada lugar.",
        "Tampoco fue inevitable ni universal. Algunos pueblos siguieron cazando y recolectando durante miles de años. Y sus consecuencias fueron variadas: más alimento y aldeas fijas, pero también desigualdad y enfermedades. Una buena explicación nombra varias causas y consecuencias, usa evidencia y reconoce lo que aún no se sabe.",
    ],
    vocab=[("multicausal", "que se explica por varias causas combinadas"), ("glaciación", "periodo largo de clima muy frío en que crecen los hielos"), ("causa", "hecho que ayuda a que ocurra otro"), ("consecuencia", "resultado de un hecho"), ("centro independiente", "lugar donde un proceso surgió por separado de otros")],
    worked=[
        ("Contar centros independientes", "{F} ¿En cuántos lugares surgió la agricultura por separado según la ficha?", ["Cuento los lugares nombrados: Asia occidental, China, Mesoamérica, los Andes y Nueva Guinea.", "Son cinco nombres distintos, cada uno con sus propias plantas."], "En 5 lugares"),
        ("Distinguir causa y consecuencia", "Hubo más alimento y también más caries. ¿Cuál es consecuencia de la agricultura?", ["Ambos hechos aparecen después de empezar a cultivar.", "Son consecuencias: unas ventajas y otras problemas."], "Ambos son consecuencias"),
    ],
    mistakes=[("Decir que la agricultura era inevitable y que todos los pueblos terminaron adoptándola.", "Se supone un único camino de progreso.", "Recuerda a los pueblos que siguieron cazando y recolectando durante miles de años."),
              ("Explicar el origen de la agricultura con una sola causa, como el clima.", "Se ignoran otros factores que aparecen en la evidencia.", "Nombra varias causas y di cuáles pudieron pesar más en cada lugar.")],
    T=[
        ("{F} ¿En qué lugar de la ficha surgió el cultivo de la papa?", "En los Andes", "La ficha lo indica."),
        ("{F} ¿Qué plantas se cultivaron por primera vez en Mesoamérica?", "Maíz y calabaza", "La ficha lo indica."),
        ("{F} ¿Cuántos lugares de origen independiente nombra la ficha?", "5", "Asia occidental, China, Mesoamérica, los Andes y Nueva Guinea."),
        ("=", "{F} La última glaciación terminó hace unos 11.700 años y la agricultura empezó hace unos 10.000. ¿Cuántos años pasaron entre ambos hechos?", "11700-10000", "Se restan las dos fechas.", " años"),
        ("{F} ¿Qué pueblos mantuvieron su vida de caza y recolección durante miles de años según la ficha?", "Muchos pueblos de Australia", "La ficha lo dice."),
        ("{F} Clasifica cada causa como ambiental (A) o social y cultural (S): 1) clima más cálido; 2) más población; 3) cereales silvestres abundantes; 4) herramientas para moler.", "1 A, 2 S, 3 A, 4 S", "Clima y plantas son del ambiente; población y herramientas son de la sociedad."),
        ("{F} ¿Por qué cinco lugares de origen muestran que la agricultura no fue un invento de un solo pueblo?", "Porque surgió por separado, con plantas distintas, en lugares lejanos", "Cada lugar desarrolló sus propios cultivos."),
        ("{F} Un historiador dice que la única causa fue el clima. Da dos datos de la ficha que muestren otras causas.", "Más población en territorios limitados y conocimiento de las plantas y herramientas", "La ficha nombra varias causas, no solo el clima."),
        ("{F} ¿Qué hecho ambiental ayuda a explicar que la agricultura apareciera en varios lugares en épocas cercanas?", "El fin de la última glaciación, que cambió el clima en gran parte del mundo", "Un cambio global del clima afectó muchos lugares."),
        ("{F} Camila dice: «La agricultura era inevitable: tarde o temprano todos la adoptaban». Corrígela.", "No: muchos pueblos, como varios de Australia, siguieron cazando y recolectando durante miles de años", "La ficha muestra otros caminos."),
        ("{F} ¿Qué no se puede concluir con la ficha sobre las causas de la agricultura?", "Cuál causa pesó más en cada lugar", "La ficha nombra causas, pero no su peso."),
        ("{F} Ordena de más antiguo a más reciente: aparición de Homo sapiens (hace unos 300.000 años), fin de la última glaciación, origen de la agricultura.", "Aparición de Homo sapiens, fin de la última glaciación, origen de la agricultura", "Las fechas son 300.000, 11.700 y 10.000 años."),
        ("{F} ¿Qué evidencia arqueológica ayudaría a saber si hubo más población antes de los primeros cultivos en un lugar?", "Más casas, campamentos o restos humanos fechados antes de esos cultivos", "Un aumento de huellas humanas apoya la idea de más población."),
    ],
    ctx=("Un panel de museo dice: «La agricultura nació en un solo lugar y de ahí se copió en el resto del mundo». ¿Qué dato de la ficha lo corrige? {F}", "Que surgió por separado en varios lugares (la ficha nombra cinco), con plantas distintas", "Los centros independientes muestran más de un origen."),
    sc=[("¿Qué es una explicación multicausal?", "Una explicación que combina varias causas", "No reduce el hecho a una sola razón."),
        ("¿Fue la agricultura adoptada por todos los pueblos?", "No", "Algunos siguieron cazando y recolectando."),
        ("=", "{F} Si la agricultura empezó hace unos 10.000 años y una generación dura 25 años, ¿cuántas generaciones han pasado?", "10000//25", "Se divide el tiempo por la duración de una generación.", " generaciones")],
    op=("Escribe una explicación de 6 líneas sobre el origen de la agricultura: tres causas de la ficha, dos consecuencias (una ventaja y un problema) y una frase final que reconozca lo que no sabemos. {F}",
        "Causas: clima cálido, cereales silvestres y más población; consecuencias: más alimento y más caries; no sabemos qué causa pesó más en cada lugar.",
        ["nombra tres causas", "nombra una ventaja y un problema", "reconoce un límite del conocimiento"], ["explicación escrita"], ["presentar una sola causa", "contar solo ventajas"],
        "Pide que explique por qué su explicación no sirve igual para Australia."),
    reinforce="Menciona tres plantas cultivadas por primera vez en lugares distintos del mundo.",
    extend="Escribe una pregunta que ayude a comparar el origen de la agricultura en los Andes y en Mesoamérica.",
)
