"""Lenguaje y Comunicación EPJA Nivel 2 (5.º y 6.º), módulo 3: OAD-11, sintetizar ideas construyendo un mapa conceptual.
Los mapas se escriben en texto: [concepto] —palabra de enlace→ [concepto]. Los textos son inventados y se resuelven en papel."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = (
    "Lápiz, goma y cuaderno. Todos los textos y mapas están escritos en cada ejercicio y son inventados para este cuaderno. "
    "Los mapas se escriben así: [concepto] —enlace→ [concepto], y se leen como una frase. Si quieres, dibuja las cajas y las flechas en tu cuaderno. "
    "No necesitas internet. Si algo te cuesta leer, pide apoyo: pedir ayuda es parte de aprender. No escribas datos personales reales."
)

build = make_build(MATERIALS)

O = "EPJA-LECO-NB2-OAD-11"

H1 = ("Mensaje de ejemplo: «Para la comida del sábado necesito tomates, lechugas, pan, queso y jugo. Las verduras se compran en la feria; el resto, en el almacén.» "
      "Mapa de ejemplo: [Compras del sábado] —se divide en→ [Feria] y [Almacén]; [Feria] —vende→ [tomates] y [lechugas]; [Almacén] —vende→ [pan], [queso] y [jugo].")
H2 = "Texto de ejemplo: «El agua llega a cada casa por cañerías. En el hogar se usa para beber, cocinar y limpiar. Después de usarla, el agua sale por el alcantarillado.»"
H3 = ("Texto de ejemplo: «Reciclar es volver a usar materiales para hacer cosas nuevas. Los materiales se separan en vidrio, papel y plástico. "
      "Cada material va a su contenedor. Así se produce menos basura.» Mapa de ejemplo: [Reciclar] —usa→ [Materiales]; [Materiales] —se separan en→ [vidrio], [papel] y [plástico]; "
      "[Materiales] —van a→ [Contenedores]; [Reciclar] —produce→ [Menos basura].")
H4 = ("Fuente 1 (guía de ejemplo del barrio, 2024): «Los mercados de barrio venden productos frescos, como frutas y verduras.» "
      "Fuente 2 (revista vecinal de ejemplo, 2024): «Comprar en el mercado de barrio permite conversar con quien vende y elegir la cantidad que se necesita.» "
      "Mapa parcial: [Mercado de barrio] —vende→ [productos frescos]; [productos frescos] —incluyen→ [frutas] y [verduras]; [Mercado de barrio] —permite→ (completar).")
H5 = ("Texto de ejemplo: «La junta de vecinos es una organización de las personas que viven en un sector. Tiene una directiva, que la dirige y la representa. "
      "La directiva convoca a asambleas, donde los vecinos deciden juntos. La junta también gestiona mejoras para el barrio, como luminarias y plazas.»")
H6 = ("Texto de ejemplo: «Reciclar es volver a usar materiales para hacer cosas nuevas. Los materiales se separan en vidrio, papel y plástico.» "
      "Mapa con problemas: [vidrio] —incluye→ [Materiales]; [Reciclar es volver a usar materiales para hacer cosas nuevas]; [Materiales] [papel]; [Materiales] —se separan en→ [plástico].")

# ============================================================ clase 1
build(
    O, 1, H1,
    use="Hoy reconozco las partes de un mapa conceptual a partir de algo que ya hago: ordenar ideas, como una lista de compras.",
    prior=["Sé hacer listas y agrupar cosas parecidas.", "Puedo escribir un mensaje corto.", "Leo textos breves."],
    explain=[
        "Ordenar ideas es algo que ya haces: cuando preparas una lista de compras, juntas lo que se compra en la feria y lo que se compra en el almacén. Un mapa conceptual es una forma de dibujar ese orden: muestra las ideas importantes y cómo se relacionan.",
        "Tiene tres partes. Los conceptos son las ideas clave, escritas en pocas palabras y dentro de cajas. Las palabras de enlace son las que unen dos conceptos, como «se divide en» o «vende». Las flechas muestran hacia dónde se lee.",
        "Dos conceptos unidos por una palabra de enlace forman una proposición: una frase completa, por ejemplo «Feria vende tomates». El concepto más general va arriba y los más específicos, abajo. Sintetizar es quedarse con lo esencial, no copiar el texto entero.",
    ],
    vocab=[("mapa conceptual", "dibujo que muestra ideas clave y cómo se relacionan"), ("concepto", "idea clave, en pocas palabras"), ("palabra de enlace", "palabra que une dos conceptos"), ("proposición", "dos conceptos y su enlace, que se leen como una frase"), ("sintetizar", "quedarse con lo esencial")],
    worked=[
        ("Leer un mapa", "Mapa de ejemplo: [Talleres de la sede] —incluyen→ [Costura] y [Computación]; [Costura] —es los→ [martes]; [Computación] —es los→ [jueves].", ["El concepto más general es «Talleres de la sede».", "Con «incluyen» se une a «Costura» y «Computación».", "Las proposiciones se leen: «Talleres incluyen costura», «Costura es los martes»."], "El mapa se lee de arriba abajo, como frases"),
        ("Agrupar una lista", "Lista de ejemplo: «lavar, barrer, trapear, comprar pan».", ["Lavar, barrer y trapear son limpieza.", "Comprar pan es otra cosa: es una compra.", "Se pueden hacer dos grupos."], "Dos grupos: «Limpieza de la casa» y «Compras»"),
    ],
    mistakes=[("Copiar frases enteras dentro de las cajas.", "Un mapa sintetiza: los conceptos son palabras clave, no oraciones.", "Resume cada idea en una o pocas palabras."),
              ("Unir cajas sin palabras de enlace.", "Sin enlace no se sabe cómo se relacionan los conceptos.", "Escribe sobre cada flecha una palabra que permita leer una frase.")],
    T=[
        ("abc", "{F} ¿Cuál es el concepto más general del mapa?", "Compras del sábado", "Jugo", "Lechugas", "Es el tema que contiene a todos los demás conceptos."),
        ("ab", "{F} ¿Qué palabra de enlace une «Compras del sábado» con «Feria» y «Almacén»?", "se divide en", "vende", "Esa conexión expresa que las compras se reparten en dos lugares."),
        ("{F} ¿Cuántos conceptos hay en el mapa en total? Responde con un número.", "8", "Son Compras del sábado, Feria, Almacén, tomates, lechugas, pan, queso y jugo."),
        ("abc", "{F} ¿Qué se compra en el almacén según el mapa?", "Pan, queso y jugo", "Tomates y lechugas", "Solo pan", "Del concepto «Almacén» salen esos tres conceptos."),
        ("ab", "{F} ¿Qué proposición se puede leer del mapa?", "Feria vende lechugas", "Almacén vende lechugas", "Las lechugas están bajo «Feria», no bajo «Almacén»."),
        ("=", "{F} Cuenta las proposiciones: 2 salen de «Compras del sábado», 2 de «Feria» y 3 de «Almacén». ¿Cuántas son en total?", "2+2+3", "Cada concepto unido con su enlace es una proposición; se suman.", "proposiciones"),
        ("abc", "Una lista dice «cortar, hervir, freír, lavar platos». ¿Qué concepto general agrupa «cortar, hervir, freír»?", "Cocinar", "Limpieza", "Descanso", "Los tres son pasos de preparar comida."),
        ("ab", "¿Por qué conviene hacer un mapa en vez de copiar el texto?", "Porque muestra las ideas clave y sus relaciones de un vistazo", "Porque así se escribe más", "Un mapa sintetiza: ordena lo esencial y lo hace visible."),
        ("abc", "Un mapa tiene cajas, pero ninguna palabra de enlace. ¿Qué falta?", "No se sabe cómo se relacionan los conceptos", "Los conceptos están mal escritos", "Sobran las flechas", "Las palabras de enlace son las que dan sentido a la relación."),
        ("abc", "Mapa de ejemplo: [Compras] —vende→ [Feria]. ¿Qué error tiene?", "El enlace no corresponde: la feria vende, las compras no venden", "Le faltan colores", "No tiene conceptos", "La relación debe poder leerse como una frase verdadera."),
        ("ab", "El texto dice «el resto, en el almacén». ¿Dónde se ubica «jugo»?", "Bajo «Almacén»", "Bajo «Feria»", "«El resto» se refiere a lo que no es verdura, como el jugo."),
        ("abc", "Se agrega «Panadería» como lugar donde se compra el pan. ¿Cómo se modifica el mapa?", "«Pan» pasa bajo «Panadería», que se une a «Compras del sábado» con «se divide en»", "Se borra el pan", "Panadería va dentro de «jugo»", "Un nuevo lugar es otro concepto del mismo nivel que Feria y Almacén."),
        ("abc", "¿Cuál de estas es una buena palabra de enlace entre «Almacén» y «pan»?", "vende", "pan", "grande", "Con «vende» se lee «Almacén vende pan», una frase completa."),
    ],
    ctx=("abc", "Una persona quiere organizar los datos de un mensaje: «El domingo hay reunión en la sede, con agua y galletas. El lunes, limpieza de la plaza.» ¿Qué concepto general sirve?", "Actividades del fin de semana y del lunes", "Galletas", "Plaza", "Reúne las dos actividades que el mensaje menciona."),
    sc=[("En Lenguaje: ¿qué es un concepto en un mapa conceptual?", "Una idea clave, en pocas palabras", "Se escribe dentro de una caja."),
        ("¿Para qué sirve la palabra de enlace?", "Para unir dos conceptos y leer una frase", "Sin ella no se entiende la relación."),
        ("¿Dónde va el concepto más general?", "Arriba", "De él salen los más específicos.")],
    op=("Haz un mapa con este mensaje de ejemplo: «Para el cumpleaños necesito comprar globos y servilletas en la tienda, y preparar sándwiches y ensalada en casa.» Escribe un concepto general, dos grupos, los conceptos de cada grupo y las palabras de enlace.",
        "[Cumpleaños] —se divide en→ [Comprar] y [Preparar]; [Comprar] —incluye→ [globos] y [servilletas]; [Preparar] —incluye→ [sándwiches] y [ensalada].",
        ["tiene un concepto general arriba", "usa palabras de enlace en cada unión", "agrupa lo que corresponde"],
        ["un mapa dibujado o escrito en el cuaderno"],
        ["copiar frases completas", "olvidar las palabras de enlace"],
        "Pregunta: «¿Se puede leer cada unión como una frase?»."),
    reinforce="Haz un mapa de tu lista de tareas de mañana con un concepto general y dos grupos.",
    extend="Explica a otra persona con tus palabras qué diferencia hay entre una lista y un mapa conceptual.",
)

# ============================================================ clase 2
build(
    O, 2, H2,
    use="Hoy reconozco los conceptos de un texto, ordeno lo general y lo específico y aprendo vocabulario para sintetizar.",
    prior=["Sé qué son conceptos y palabras de enlace.", "Puedo leer un mapa sencillo.", "Conozco sinónimos y antónimos."],
    explain=[
        "Para armar un mapa, primero hay que encontrar los conceptos del texto. Suelen ser sustantivos importantes: aquello de lo que habla el texto. En «La plaza tiene juegos y bancas», los conceptos son «plaza», «juegos» y «bancas», y la palabra de enlace puede ser «tiene».",
        "Luego se ordenan en una jerarquía, de lo más general a lo más específico. «Elementos de la plaza» es general; «juegos» y «bancas» son específicos y van debajo. Una pregunta útil es: ¿cuál de estos conceptos incluye a los otros?",
        "El vocabulario también ayuda. Un sinónimo permite escribir una idea con otras palabras sin cambiar su sentido: «hogar» y «casa». Un antónimo muestra lo contrario: «llega» y «sale». Escribe con cuidado: «cañerías» lleva ñ y «alcantarillado», ll.",
    ],
    vocab=[("jerarquía", "orden de lo más general a lo más específico"), ("general", "que incluye a otros conceptos"), ("específico", "que es una parte de uno más general"), ("sinónimo", "palabra de significado parecido"), ("antónimo", "palabra de significado contrario"), ("alcantarillado", "red de tubos que lleva el agua usada")],
    worked=[
        ("Encontrar los conceptos", "Texto de ejemplo: «El consultorio tiene un mesón de atención y una sala de espera. En el mesón se piden las horas».", ["Subrayo los sustantivos clave: consultorio, mesón, sala de espera, horas.", "Descarto lo que no es esencial: «un», «en el».", "Elijo «Consultorio» como el concepto general."], "Conceptos: consultorio, mesón, sala de espera y horas"),
        ("Ordenar y enlazar", "Con los conceptos del consultorio: [Consultorio] —tiene→ [mesón] y [sala de espera]; [mesón] —entrega→ [horas].", ["«Consultorio» es el concepto general.", "Mesón y sala de espera son específicos.", "«Tiene» y «entrega» permiten leer cada frase."], "Consultorio tiene mesón y sala de espera; el mesón entrega horas"),
    ],
    mistakes=[("Elegir verbos o conectores como conceptos.", "Los conceptos suelen ser sustantivos importantes; los verbos y conectores sirven de enlace.", "Pregunta: ¿esto es de lo que habla el texto o la relación entre dos ideas?"),
              ("Poner lo específico arriba y lo general abajo.", "La jerarquía va de lo general a lo específico.", "Pregunta cuál concepto incluye a los demás.")],
    T=[
        ("abc", "{F} ¿Cuál es un concepto importante del texto?", "Alcantarillado", "Después", "Cada", "Es un sustantivo clave: nombra la red que lleva el agua usada."),
        ("ab", "{F} ¿Por dónde llega el agua a la casa?", "Por cañerías", "Por el alcantarillado", "El texto dice «llega a cada casa por cañerías»; el alcantarillado es por donde sale."),
        ("{F} ¿Con qué letra se escribe «cañerías»: con ñ o con n? Responde con una letra: ñ o n.", "ñ", "La palabra caña lleva ñ, igual que cañería."),
        ("abc", "{F} ¿Qué concepto es más general?", "Usos del agua", "Beber", "Limpiar", "Incluye a beber, cocinar y limpiar."),
        ("ab", "{F} ¿Cuál es un concepto específico del agua en el hogar?", "Cocinar", "Usos del agua", "Cocinar es uno de los usos concretos del agua."),
        ("abc", "{F} ¿Qué enlace sirve entre «Agua» y «Cañerías»?", "llega por", "sin", "muy", "Con «llega por» se lee «Agua llega por cañerías»."),
        ("abc", "Un sinónimo de «hogar» es:", "casa", "calle", "plaza", "Hogar y casa nombran el lugar donde se vive."),
        ("ab", "Un antónimo de «llega» es:", "sale", "viene", "Llegar y salir expresan movimientos contrarios en el texto."),
        ("ab", "En el mapa, ¿qué debería ir debajo de «Usos del agua»?", "beber, cocinar y limpiar", "agua y cañerías", "Son los usos que el texto menciona."),
        ("abc", "Un compañero pone «beber» arriba y «Usos del agua» debajo. ¿Cuál es el error?", "Invirtió la jerarquía: lo general va arriba", "Escribió mal «beber»", "No usó colores", "«Usos del agua» incluye a «beber»."),
        ("abc", "{F} ¿Cuál proposición está bien formada?", "[Alcantarillado] —lleva→ [agua usada]", "[agua usada] —→ [lleva]", "[Alcantarillado] [agua]", "Tiene dos conceptos y un enlace que permite leer una frase."),
        ("ab", "¿Cuál palabra se escribe con ll?", "alcantarillado", "alcantarilado", "Viene de alcantarilla, que lleva ll."),
        ("abc", "Se quiere sintetizar «Después de usarla, el agua sale por el alcantarillado». ¿Qué opción sintetiza mejor?", "[Agua usada] —sale por→ [Alcantarillado]", "[Después de usarla, el agua sale por el alcantarillado]", "[Agua]", "La primera conserva lo esencial en dos conceptos y un enlace."),
    ],
    ctx=("abc", "Un folleto de ejemplo del barrio dice: «La feria vende frutas y verduras, y también hay un puesto de flores.» ¿Qué concepto general sirve para el mapa?", "Feria", "Flores", "Verduras", "«Feria» incluye a los demás conceptos."),
    sc=[("En Lenguaje: ¿qué es una jerarquía en un mapa conceptual?", "Un orden de lo general a lo específico", "En una jerarquía lo más general va arriba y lo específico, debajo."),
        ("En Lenguaje: al armar un mapa, ¿qué es un sinónimo?", "Una palabra de significado parecido", "Los sinónimos ayudan a no repetir palabras en el mapa."),
        ("¿Qué suelen ser los conceptos?", "Sustantivos importantes", "Nombran de lo que habla el texto.")],
    op=("Lee el texto de ejemplo: «El pan se hace con harina, agua y sal. La masa se deja reposar y luego se hornea.» Escribe una lista de conceptos, elige el más general y arma tres proposiciones con palabras de enlace.",
        "Conceptos: pan, harina, agua, sal, masa, horno. General: pan. Proposiciones: [Pan] —se hace con→ [harina]; [Pan] —se hace con→ [agua]; [Masa] —se hornea en→ [horno].",
        ["elige sustantivos como conceptos", "ubica el más general arriba", "forma proposiciones que se lean bien"],
        ["lista de conceptos y tres proposiciones"],
        ["usar verbos como conceptos", "olvidar el enlace"],
        "Pregunta: «¿Cuál concepto incluye a los demás?»."),
    reinforce="Elige un aviso corto y subraya sus conceptos y su concepto más general.",
    extend="Escribe dos sinónimos y un antónimo de palabras de un texto que hayas leído hoy.",
)

# ============================================================ clase 3
build(
    O, 3, H3,
    use="Hoy sigo cinco pasos para construir un mapa conceptual y reviso la concordancia de los verbos de enlace.",
    prior=["Sé encontrar conceptos y ordenar lo general y lo específico.", "Escribo palabras de enlace.", "Conozco el presente de los verbos."],
    explain=[
        "Construir un mapa se hace paso a paso. Paso 1: lee el texto completo. Paso 2: subraya los conceptos importantes. Paso 3: ordénalos de lo más general a lo más específico. Paso 4: une los conceptos con palabras de enlace. Paso 5: revisa que cada proposición se lea bien.",
        "Las palabras de enlace suelen ser verbos: «usa», «produce», «incluyen». Deben concordar con el concepto del que parten. Si el concepto está en singular, el verbo va en singular: «Puestos venden» (plural) pero «Feria vende» (singular).",
        "Cuida la ortografía de los conceptos: «plástico» lleva tilde por ser esdrújula, y «contenedor» se escribe con c y con d. Al sintetizar, evita copiar frases completas: reduce cada idea a una palabra o dos.",
    ],
    vocab=[("concordancia", "acuerdo entre el verbo y su sujeto en número"), ("singular", "una sola cosa"), ("plural", "más de una cosa"), ("contenedor", "recipiente grande para guardar o juntar cosas"), ("esdrújula", "palabra con la fuerza en la antepenúltima sílaba")],
    worked=[
        ("Los cinco pasos", "Texto de ejemplo: «La biblioteca vecinal presta libros y ofrece una sala de estudio. Los libros se organizan por temas».", ["Paso 1: leo todo el texto sobre la biblioteca.", "Paso 2: subrayo biblioteca, libros, sala de estudio y temas.", "Paso 3: «Biblioteca» es el más general.", "Paso 4: uno con enlaces: presta, ofrece, se organizan por.", "Paso 5: leo cada proposición: todas tienen sentido."], "El mapa tiene 4 conceptos y 3 proposiciones"),
        ("Concordancia", "Enlaces de ejemplo: «Vecinos eligen directiva» y «Directiva convoca asamblea».", ["«Vecinos» es plural: el verbo también, «eligen».", "«Directiva» es singular: el verbo también, «convoca»."], "Verbos que concuerdan: eligen (plural) y convoca (singular)"),
    ],
    mistakes=[("Escribir enlaces que no concuerdan: «Materiales va a contenedores».", "El sujeto es plural y el verbo está en singular.", "Fíjate si el concepto es uno o varios y ajusta el verbo."),
              ("Saltarse el paso 5.", "Sin revisar, quedan frases sin sentido.", "Lee cada unión en voz alta y comprueba que sea una frase.")],
    T=[
        ("abc", "{F} ¿Cuál es el concepto más general del mapa?", "Reciclar", "Plástico", "Contenedores", "Todo el texto trata de reciclar."),
        ("=", "{F} ¿Cuántos conceptos hay en el mapa? Cuenta: 1 (Reciclar) + 1 (Materiales) + 3 (vidrio, papel, plástico) + 1 (Contenedores) + 1 (Menos basura).", "1+1+3+1+1", "Se suman los conceptos de cada grupo.", "conceptos"),
        ("{F} ¿Cuántas proposiciones tiene el mapa? Responde con un número.", "6", "Reciclar usa Materiales (1); se separan en tres conceptos (3); van a Contenedores (1); Reciclar produce Menos basura (1)."),
        ("abc", "{F} ¿Qué enlace une «Reciclar» con «Menos basura»?", "produce", "usa", "van a", "«Reciclar produce menos basura» recoge la última idea del texto."),
        ("ab", "{F} ¿Qué conceptos salen de «Materiales»?", "vidrio, papel, plástico y Contenedores", "Reciclar y Menos basura", "Son los materiales y el lugar al que van."),
        ("abc", "¿Qué se hace en el paso 3?", "Ordenar los conceptos de general a específico", "Copiar el texto", "Dibujar flechas de colores", "Ordenar de lo general a lo específico es lo que organiza el mapa."),
        ("ab", "¿Cuál enlace concuerda con «Materiales»?", "van a", "va a", "«Materiales» es plural, así que el verbo es «van»."),
        ("abc", "¿Cuál enlace concuerda con «Reciclar»?", "produce", "producen", "producimos", "«Reciclar» es una sola idea, así que va en singular."),
        ("ab", "¿Cuál palabra lleva tilde?", "plástico", "plastico", "Es esdrújula: la fuerza está en la antepenúltima sílaba."),
        ("abc", "Un mapa pone: [Reciclar] —produce→ [Materiales]. ¿Qué error tiene?", "El enlace no coincide con el texto: reciclar usa materiales", "Faltan colores", "Está bien", "El texto dice que reciclar usa materiales; no los produce."),
        ("ab", "Se quiere sintetizar «Cada material va a su contenedor». ¿Qué sintetiza mejor?", "[Materiales] —van a→ [Contenedores]", "[Cada material va a su contenedor]", "La primera usa dos conceptos y un enlace en lugar de copiar la frase."),
        ("abc", "{F} Si el texto agregara «El vidrio se lleva limpio», ¿dónde iría?", "Como proposición entre [vidrio] y [limpio]", "Reemplazando «Reciclar»", "No se podría agregar nada", "Se agrega un nuevo concepto bajo «vidrio»."),
        ("abc", "{F} ¿Cuál es el error de este mapa: [Menos basura] —usa→ [Reciclar]?", "Invierte la relación del texto: reciclar produce menos basura", "No tiene error", "Le faltan tildes", "La dirección de la relación debe respetar lo que dice el texto."),
    ],
    ctx=("abc", "Una vecina arma un mapa para explicar la separación de basura en un condominio de ejemplo y escribe: [Residuos] —se separan en→ [orgánicos] y [reciclables]. ¿Cuál es una mejora?", "Agregar proposiciones: [reciclables] —incluyen→ [vidrio], [papel] y [plástico]", "Copiar un párrafo completo", "Quitar el enlace", "Agrega detalle sin perder la síntesis."),
    sc=[("En Lenguaje: ¿qué es concordar el verbo?", "Que coincida en número con su sujeto", "Singular con singular y plural con plural."),
        ("¿Qué se revisa en el paso 5?", "Que cada proposición se lea bien", "Cada unión debe ser una frase."),
        ("¿Qué tipo de palabra suele ser el enlace?", "Un verbo", "Expresa la relación entre los conceptos.")],
    op=("Haz un mapa con este texto de ejemplo: «El compost se hace con restos de frutas y verduras. Los restos se mezclan con tierra y se dejan reposar. Después, el compost sirve para abonar las plantas.» Sigue los cinco pasos y revisa la concordancia.",
        "[Compost] —se hace con→ [Restos de frutas y verduras]; [Restos] —se mezclan con→ [tierra]; [Compost] —sirve para→ [Abonar plantas].",
        ["sigue los cinco pasos", "usa enlaces que concuerdan", "sintetiza sin copiar frases completas"],
        ["un mapa con al menos cuatro proposiciones"],
        ["copiar frases completas", "usar enlaces que no concuerdan"],
        "Pregunta: «¿El verbo concuerda con su concepto?»."),
    reinforce="Elige un párrafo corto y sigue los cinco pasos para armar su mapa.",
    extend="Escribe tres enlaces con verbos en plural y tres en singular para distintos conceptos.",
)

# ============================================================ clase 4
build(
    O, 4, H4,
    use="Hoy practico con apoyo: completo un mapa que reúne dos fuentes y escribo su cita.",
    prior=["Sé construir un mapa de un texto.", "Distingo concepto y enlace.", "Sé citar una fuente de forma sencilla."],
    explain=[
        "Practicar con apoyo significa completar un mapa que ya está empezado. Puedes seguir las pistas del mapa parcial y buscar en el texto lo que falta. Así se aprende el procedimiento antes de hacerlo solo.",
        "A veces el mapa reúne información de más de una fuente. Sintetizar ideas de varias fuentes es unirlas en un solo mapa sin repetir lo que dicen igual y sin mezclar datos que no corresponden. Al pie del mapa se anotan las fuentes.",
        "Una cita sencilla lleva quién, título o tipo de texto y año. Así, quien lea tu mapa puede ir a la fuente. Cuida la ortografía: «información» y «también» llevan tilde porque son agudas terminadas en n; «fuente» no lleva.",
    ],
    vocab=[("fuente", "texto o persona de donde sale un dato"), ("síntesis", "resumen de lo esencial"), ("repetir", "decir lo mismo otra vez"), ("pie del mapa", "lugar donde se anotan las fuentes")],
    worked=[
        ("Completar el mapa parcial", "Fuente A (ejemplo): «El centro comunitario ofrece talleres de costura.» Fuente B (ejemplo): «El centro comunitario tiene una sala de reuniones.» Mapa parcial: [Centro comunitario] —ofrece→ [talleres de costura]; [Centro comunitario] —tiene→ (completar).", ["La Fuente B dice que el centro tiene una sala de reuniones.", "Agrego: [Centro comunitario] —tiene→ [sala de reuniones].", "La Fuente A ya aportó ofrece y talleres de costura."], "El mapa completo reúne las dos fuentes en dos proposiciones"),
        ("Cita al pie", "Al pie del mapa del centro comunitario se escribe: «Fuente A: folleto de ejemplo del centro, 2024. Fuente B: boletín de ejemplo del centro, 2024.»", ["Se nombra cada fuente.", "Se indica el tipo de texto y el año.", "Así se sabe de dónde viene cada parte."], "Las dos fuentes quedan citadas al pie del mapa"),
    ],
    mistakes=[("Mezclar información de las dos fuentes sin indicar de cuál viene.", "Si hay un dato dudoso, no se sabe dónde buscar.", "Anota las fuentes al pie y marca cuál aportó cada parte."),
              ("Repetir el mismo concepto dos veces con distinto nombre.", "Un mapa claro usa un solo nombre por concepto.", "Elige la palabra más precisa y úsala siempre.")],
    T=[
        ("abc", "{F} ¿Qué vende el mercado de barrio según la Fuente 1?", "Productos frescos", "Ropa", "Electrodomésticos", "La Fuente 1 lo dice expresamente."),
        ("ab", "{F} ¿Qué incluyen los productos frescos en el mapa?", "Frutas y verduras", "Conversar y elegir la cantidad", "Eso lo dice la Fuente 1; lo otro viene de la Fuente 2."),
        ("{F} ¿De cuál fuente sale «elegir la cantidad que se necesita»? Responde: Fuente 1 o Fuente 2.", "Fuente 2", "La Fuente 2 afirma que se puede elegir la cantidad."),
        ("abc", "{F} ¿Qué enlace completa «Mercado de barrio _____ conversar con quien vende»?", "permite", "vende", "incluyen", "La Fuente 2 usa «permite» para esa idea."),
        ("=", "{F} El mapa completo tiene 5 proposiciones: 1 (vende) + 2 (incluyen frutas y verduras) + ... ¿cuántas son de «permite»?", "5-1-2", "Se resta del total las proposiciones que ya conocemos.", "proposiciones"),
        ("abc", "{F} ¿Qué concepto es el más general?", "Mercado de barrio", "frutas", "elegir la cantidad", "Es el tema que ordena todos los demás."),
        ("ab", "¿Qué conviene escribir al pie del mapa?", "Las fuentes con tipo de texto y año", "Un chiste", "Así se puede comprobar de dónde sale cada dato."),
        ("abc", "¿Cuál es una buena cita de la Fuente 1?", "Guía de ejemplo del barrio, 2024", "Una guía", "2024", "Dice quién y el año, lo que permite encontrar la fuente."),
        ("ab", "¿Cuál palabra lleva tilde?", "información", "fuente", "Información es aguda y termina en n; fuente es grave y termina en vocal."),
        ("abc", "{F} Un mapa dice [Mercado de barrio] —vende→ [frutas] y también [verduras] y además [frutas frescas]. ¿Qué problema tiene?", "Repite el concepto de frutas con otro nombre", "Está perfecto", "Le faltan fuentes", "Un concepto debe tener un solo nombre."),
        ("abc", "{F} ¿Qué haces si las dos fuentes dicen cosas opuestas sobre un dato?", "Lo anoto, busco una tercera fuente confiable y lo indico en el mapa", "Elijo la que me gusta", "Borro los dos datos sin avisar", "Cuando hay desacuerdo se verifica con otra fuente."),
        ("ab", "¿Cuál es un sinónimo de «fresco» en «productos frescos»?", "recién cosechado", "viejo", "Fresco indica que no ha pasado mucho tiempo desde su obtención."),
        ("abc", "{F} ¿Cuál es la mejor síntesis de las dos fuentes?", "El mercado de barrio vende productos frescos y permite conversar y elegir la cantidad", "El mercado es bueno", "Las frutas son ricas", "Reúne lo esencial de las dos fuentes."),
    ],
    ctx=("abc", "Una persona prepara un mapa para una charla en la junta de vecinos con dos folletos de ejemplo. ¿Cómo indica sus fuentes?", "Al pie: «Folleto 1: junta de ejemplo, 2024. Folleto 2: centro de salud de ejemplo, 2024»", "No las indica", "Escribe «los folletos»", "Con tipo, institución y año se pueden encontrar."),
    sc=[("En Lenguaje: ¿qué datos tiene la cita sencilla de un mapa?", "Quién, título o tipo de texto y año", "Con esos datos quien lee puede volver a la fuente."),
        ("En Lenguaje: ¿qué es sintetizar varias fuentes?", "Unir lo esencial en un solo mapa sin repetir", "Se evita mezclar y duplicar datos."),
        ("¿Dónde se anotan las fuentes?", "Al pie del mapa", "Así queda claro de dónde viene cada dato.")],
    op=("Completa un mapa con estas dos fuentes de ejemplo. Fuente 1: «La biblioteca de barrio presta libros.» Fuente 2: «La biblioteca de barrio también ofrece un espacio para estudiar.» Escribe el mapa con un concepto general, dos proposiciones y las dos fuentes al pie (invéntales título y año).",
        "[Biblioteca de barrio] —presta→ [libros]; [Biblioteca de barrio] —ofrece→ [espacio para estudiar]. Fuente 1: guía de ejemplo, 2024. Fuente 2: boletín de ejemplo, 2024.",
        ["incluye datos de las dos fuentes", "usa enlaces que concuerdan", "cita las fuentes al pie"],
        ["un mapa de tres conceptos y dos citas"],
        ["no citar", "mezclar los datos sin orden"],
        "Pregunta: «¿De qué fuente sale cada dato?»."),
    reinforce="Elige dos avisos sobre un mismo tema y reúne sus datos en un mapa.",
    extend="Explica cómo cambia un mapa cuando se agrega una tercera fuente con un dato nuevo.",
)

# ============================================================ clase 5
build(
    O, 5, H5,
    use="Hoy aplico lo aprendido: construyo un mapa sobre cómo funciona una junta de vecinos.",
    prior=["Sé armar un mapa con enlaces que concuerdan.", "Sé citar una fuente.", "Conozco las reglas básicas de tildes."],
    explain=[
        "Los mapas conceptuales sirven en la vida diaria y en la comunidad: para preparar una charla, explicar cómo funciona una organización o estudiar un trámite. Un mapa bien hecho deja ver en un vistazo quién hace qué y cómo se relacionan las partes.",
        "Al aplicar, ten presente tu público. Si el mapa lo verá otra persona, usa conceptos claros y pocas palabras. También revisa que tenga una jerarquía comprensible y que los verbos de enlace concuerden con sus conceptos.",
        "Cuida la ortografía y la puntuación: «directiva» y «asamblea» son palabras graves terminadas en vocal y no llevan tilde; «luminarias» tampoco. Al explicar el mapa en voz alta, ayúdate de las proposiciones: cada una es una frase completa.",
    ],
    vocab=[("directiva", "grupo que dirige una organización"), ("asamblea", "reunión de las personas de una organización para decidir"), ("gestionar", "hacer trámites o acciones para lograr algo"), ("luminaria", "lámpara del alumbrado público")],
    worked=[
        ("Armar un mapa", "Texto de ejemplo: «El comedor comunitario recibe alimentos y los prepara. Tiene un equipo de voluntarios, que cocina y sirve las comidas».", ["Concepto general: «Comedor comunitario».", "Subordinados: Alimentos, Equipo de voluntarios, Comidas.", "Enlaces: recibe, tiene, cocina y sirve."], "[Comedor comunitario] —recibe→ [Alimentos]; [Comedor comunitario] —tiene→ [Equipo de voluntarios]; [Equipo de voluntarios] —cocina y sirve→ [Comidas]"),
        ("Explicar el mapa en voz alta", "Con el mapa anterior: «El comedor comunitario recibe alimentos. Tiene un equipo de voluntarios. El equipo cocina y sirve las comidas».", ["Leo cada proposición como una frase.", "Mantengo el orden de arriba hacia abajo."], "Explicar un mapa es leer sus proposiciones en orden"),
    ],
    mistakes=[("Escribir en las cajas oraciones largas.", "El mapa pierde claridad.", "Reduce cada caja a una palabra clave."),
              ("Olvidar quién hace cada acción.", "Sin ello la relación queda confusa.", "Escribe enlaces con verbos que muestren quién hace qué.")],
    T=[
        ("abc", "{F} ¿Qué es la junta de vecinos?", "Una organización de las personas que viven en un sector", "Un partido político", "Una empresa", "El texto lo define en su primera oración."),
        ("ab", "{F} ¿Quién dirige y representa a la junta?", "La directiva", "Las plazas", "El texto dice que la directiva la dirige y la representa."),
        ("{F} ¿A qué convoca la directiva? Responde con una palabra.", "asambleas", "El texto dice «convoca a asambleas»."),
        ("abc", "{F} ¿Qué se hace en las asambleas?", "Los vecinos deciden juntos", "Se venden productos", "Se cambian las luminarias", "El texto lo indica con «donde los vecinos deciden juntos»."),
        ("ab", "{F} ¿Qué incluyen las mejoras?", "Luminarias y plazas", "Directiva y asambleas", "El texto cita luminarias y plazas como ejemplos de mejoras."),
        ("=", "{F} Un mapa tiene proposiciones: tiene (1), convoca a (1), permiten (1), gestiona (1) e incluyen (2). ¿Cuántas son en total?", "1+1+1+1+2", "Se suman las proposiciones de cada enlace.", "proposiciones"),
        ("abc", "{F} ¿Cuál es el concepto general del mapa?", "Junta de vecinos", "Plazas", "Asambleas", "Todos los demás conceptos dependen de él."),
        ("ab", "¿Cuál enlace concuerda con «Asambleas»?", "permiten", "permite", "«Asambleas» es plural, así que el verbo va en plural."),
        ("abc", "Un mapa pone [Mejoras] —gestiona→ [Junta de vecinos]. ¿Qué error tiene?", "Invierte quién gestiona: la junta gestiona las mejoras", "Está bien", "Falta una tilde", "El texto dice que la junta gestiona mejoras, no al revés."),
        ("ab", "¿Cuál palabra lleva tilde?", "gestión", "gestionar", "Gestión es aguda y termina en n; gestionar es aguda pero termina en r."),
        ("abc", "{F} Se quiere sintetizar «La directiva convoca a asambleas, donde los vecinos deciden juntos». ¿Cuál es mejor?", "[Directiva] —convoca a→ [Asambleas]; [Asambleas] —permiten→ [Decidir juntos]", "[La directiva convoca a asambleas donde los vecinos deciden juntos]", "[Directiva] [Asambleas]", "La primera usa conceptos breves y enlaces."),
        ("abc", "{F} Otra persona dice que una junta «solo es una reunión». ¿Qué parte del mapa lo corrige?", "Muestra que además tiene directiva y gestiona mejoras", "Muestra que las plazas son verdes", "No lo corrige", "El mapa incluye más funciones que reunirse."),
        ("ab", "Al explicar el mapa a otra persona, ¿qué conviene?", "Leer cada proposición como una frase, de arriba hacia abajo", "Leer solo las cajas", "Las proposiciones dan el hilo de la explicación."),
    ],
    ctx=("abc", "Una persona prepara una charla breve de ejemplo para vecinos sobre cómo funciona una biblioteca vecinal. ¿Qué le conviene llevar?", "Un mapa con pocos conceptos y enlaces claros", "Un texto largo para leer entero", "Nada", "Un mapa claro ayuda a que el público siga la explicación."),
    sc=[("En Lenguaje: ¿qué es una asamblea?", "Una reunión donde las personas deciden juntas", "Es el espacio de decisión de una organización."),
        ("¿Qué debe tener cada caja de un mapa?", "Un concepto breve", "Las oraciones largas lo vuelven confuso."),
        ("¿Cómo se explica un mapa en voz alta?", "Leyendo sus proposiciones", "Cada una es una frase completa.")],
    op=("Haz un mapa conceptual con este texto de ejemplo: «Un centro de salud familiar atiende a las personas de su sector. Tiene un equipo de profesionales, que realizan controles y consultas. El centro entrega horas por teléfono o en el mesón.» Agrega al pie una fuente de ejemplo con título y año. Prepara una explicación de dos frases.",
        "[Centro de salud] —atiende a→ [Personas del sector]; [Centro de salud] —tiene→ [Equipo]; [Equipo] —realiza→ [controles] y [consultas]; [Centro de salud] —entrega→ [horas].",
        ["incluye un concepto general y cinco conceptos o más", "usa enlaces con verbos que concuerdan", "cita la fuente y explica en dos frases"],
        ["un mapa con cuatro proposiciones y una cita"],
        ["escribir oraciones largas en las cajas", "no citar la fuente"],
        "Pregunta: «¿Quién hace qué en tu mapa?»."),
    reinforce="Haz un mapa de cómo funciona un servicio que usas: la feria, el consultorio o la biblioteca.",
    extend="Explica un mapa tuyo a otra persona en menos de un minuto y pregúntale qué entendió.",
)

# ============================================================ clase 6
build(
    O, 6, H6,
    use="Hoy reviso mapas, corrijo errores y decido qué quiero repasar.",
    prior=["Sé armar un mapa con enlaces y jerarquía.", "Sé citar fuentes.", "Cuido tildes y concordancia."],
    explain=[
        "Revisar un mapa es leerlo como lo haría otra persona. Preguntas útiles: ¿el concepto general está arriba?, ¿cada unión tiene palabra de enlace?, ¿cada proposición se lee como una frase verdadera según el texto?, ¿las cajas tienen palabras clave y no oraciones?",
        "Los errores más comunes son: invertir la jerarquía, olvidar los enlaces, copiar frases enteras y usar verbos que no concuerdan. Corregirlos mejora la comprensión, no solo la apariencia.",
        "Para cerrar, anota qué ya dominas y qué quieres repasar: encontrar conceptos, ordenar la jerarquía, elegir enlaces, concordar los verbos, citar las fuentes o cuidar tildes. Elige uno o dos y practica con un texto nuevo.",
    ],
    vocab=[("revisar", "volver a mirar para corregir"), ("invertir", "poner al revés"), ("clave", "que es esencial"), ("repasar", "volver a practicar")],
    worked=[
        ("Corregir un mapa", "Texto de ejemplo: «El consultorio tiene un mesón y una sala de espera». Mapa con problemas: [mesón] —tiene→ [Consultorio]; [Consultorio] [sala de espera]; [El consultorio atiende a las personas del sector].", ["Error 1: [mesón] —tiene→ [Consultorio] invierte la jerarquía; correcto: [Consultorio] —tiene→ [mesón].", "Error 2: la caja larga copia una oración; correcto: [Consultorio].", "Error 3: [Consultorio] [sala de espera] no tiene enlace; correcto: [Consultorio] —tiene→ [sala de espera]."], "Se corrigen la jerarquía, la caja larga y el enlace faltante"),
        ("Concordancia", "Enlace de ejemplo: «Puestos vende frutas».", ["«Puestos» es plural.", "El verbo debe ser «venden»."], "Puestos venden frutas"),
    ],
    mistakes=[("Dar por bueno un mapa solo porque se ve ordenado.", "El orden visual no asegura que las proposiciones sean verdaderas.", "Lee cada proposición y compárala con el texto."),
              ("Querer repasar todo.", "Es más eficaz repasar lo que más cuesta.", "Elige uno o dos puntos y practícalos.")],
    T=[
        ("abc", "{F} ¿Cuál es el error de «[vidrio] —incluye→ [Materiales]»?", "Invierte la jerarquía: materiales incluyen vidrio", "Le falta una tilde", "No tiene conceptos", "El vidrio es una parte de los materiales y no al revés."),
        ("ab", "{F} ¿Qué problema tiene la caja «Reciclar es volver a usar materiales para hacer cosas nuevas»?", "Es una oración, no un concepto breve", "Está escrita en colores", "Un concepto debe ser una palabra clave, no una frase copiada."),
        ("{F} ¿Qué falta en «[Materiales] [papel]»? Responde con una palabra.", "enlace", "Sin palabra de enlace no se lee como una frase."),
        ("abc", "{F} ¿Qué se concluye de la proposición «[Materiales] —se separan en→ [plástico]»?", "Es correcta: concuerda con el texto y el verbo está en plural", "Está al revés y hay que invertirla", "Hay que borrarla", "El texto dice que los materiales se separan en vidrio, papel y plástico."),
        ("ab", "{F} ¿Qué conceptos incluyen los materiales según el texto?", "vidrio, papel y plástico", "Reciclar y cosas nuevas", "El texto enumera esos tres materiales."),
        ("abc", "¿Qué verbo concuerda con «Materiales»?", "incluyen", "incluye", "incluí", "«Materiales» es plural, así que el verbo también va en plural."),
        ("abc", "¿Qué error es el más grave: invertir una relación o poner una caja larga?", "Invertir una relación, porque cambia el sentido", "Poner la caja larga, porque nadie la lee", "Ninguno es un error", "Una relación invertida da información falsa; la caja larga solo resta claridad."),
        ("ab", "¿Cuál palabra lleva tilde?", "plástico", "papel", "Plástico es esdrújula; papel es aguda terminada en l."),
        ("abc", "{F} Quien lee el mapa con problemas pregunta «¿cómo se unen vidrio y papel?». ¿Qué falta?", "Un concepto general y enlaces", "Más color", "Un título largo", "Falta la jerarquía y las palabras de enlace."),
        ("ab", "¿Cuál es un antónimo de «general»?", "específico", "amplio", "General incluye a otros; específico es una parte concreta."),
        ("abc", "{F} Se corrige el mapa y queda: [Reciclar] —usa→ [Materiales]; [Materiales] —se separan en→ [vidrio], [papel] y [plástico]. ¿Cuántas proposiciones tiene?", "4", "5", "3", "Reciclar usa Materiales (1) y se separan en tres conceptos (3): son 4."),
        ("ab", "¿Qué es lo más útil para decidir qué repasar?", "Revisar mis puntos débiles", "Repetir todo sin orden", "Elegir lo que cuesta permite practicar con intención."),
        ("abc", "Si dos personas leen el mismo mapa y entienden lo mismo, ¿qué indica?", "Que el mapa es claro", "Que el mapa tiene muchos colores", "Que el texto es corto", "Un buen mapa comunica de manera parecida a distintas personas."),
    ],
    ctx=("abc", "Una persona revisa el mapa que hizo para una charla en su organización y descubre que una caja dice una oración entera. ¿Qué hace?", "La reduce a una palabra clave y deja el detalle para la explicación oral", "La deja igual", "Borra todo", "El mapa debe sintetizar; el detalle se dice en voz alta."),
    sc=[("En Lenguaje: ¿qué errores comunes tiene un mapa?", "Jerarquía invertida, enlaces olvidados y cajas con oraciones", "Revisar y corregir esos errores mejora la claridad del mapa."),
        ("¿Cómo se comprueba una proposición?", "Se lee como frase y se compara con el texto", "Debe ser verdadera según la fuente."),
        ("¿Cómo elijo qué repasar?", "Según mis puntos más débiles", "Practicar lo que más cuesta hace que el repaso rinda más.")],
    op=("Revisa y corrige este mapa de ejemplo sobre el texto: «El supermercado de barrio vende alimentos y productos de limpieza. Tiene cajas para pagar.» Mapa con problemas: [alimentos] —vende→ [Supermercado]; [Supermercado] [productos de limpieza]; [Cajas para pagar]. Escribe el mapa corregido y una lista de dos puntos que quieres repasar.",
        "[Supermercado] —vende→ [alimentos] y [productos de limpieza]; [Supermercado] —tiene→ [cajas]. Repasar: jerarquía y enlaces.",
        ["corrige la jerarquía", "agrega los enlaces que faltan", "elige dos puntos para repasar"],
        ["un mapa corregido y dos puntos escritos"],
        ["mantener el error de jerarquía", "no elegir qué repasar"],
        "Pregunta: «¿Qué relación estaba invertida?»."),
    reinforce="Pide a otra persona que lea tu mapa y diga qué entendió.",
    extend="Escribe una lista de tres preguntas para revisar cualquier mapa antes de mostrarlo.",
)
